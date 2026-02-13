MASS_TABLE = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]



def is_consistent(peptide, experimental_spectrum):
    theoretical = get_circular_spectrum(peptide)
    temp_experimental = experimental_spectrum[:]
    for mass in theoretical:
        if mass not in temp_experimental:
            return False
        temp_experimental.remove(mass)
    return True


def get_circular_spectrum(peptide):
    prefix_mass = [0]
    for mass in peptide:
        prefix_mass.append(prefix_mass[-1] + mass)

    parent_mass = prefix_mass[-1]
    spectrum = [0]
    for i in range(len(prefix_mass)):
        for j in range(i + 1, len(prefix_mass)):
            mass = prefix_mass[j] - prefix_mass[i]
            spectrum.append(mass)
            if i > 0 and j < len(prefix_mass) - 1:
                spectrum.append(parent_mass - mass)
    return sorted(spectrum)



def Branch_and_Bound(spectrum):
    candidates = [[]]
    final_peptides = []
    parent_mass = max(spectrum)

    while candidates:
        new_candidates = []
        for peptide in candidates:
            for mass in MASS_TABLE:
                new_candidates.append(peptide + [mass])

        candidates = []
        for peptide in new_candidates:
            current_mass = sum(peptide)
            if current_mass == parent_mass:
                if get_circular_spectrum(peptide) == spectrum:
                    final_peptides.append(peptide)
            elif is_consistent(peptide, spectrum):
                candidates.append(peptide)
    return final_peptides


test_spectrum = [0, 57, 71, 99, 128, 156, 170, 227]

results = Branch_and_Bound(test_spectrum)

unique_results = set(tuple(p) for p in results)
print(f"Found {len(unique_results)} valid sequences:")
for seq in unique_results:
    print(list(seq))