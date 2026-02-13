MASS_TABLE = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def get_circular_spectrum(peptide):
    n = len(peptide)
    extended_peptide = peptide + peptide
    spectrum = [0, sum(peptide)]

    for length in range(1, n):
        for start in range(n):
            sub_fragment = extended_peptide[start: start + length]
            spectrum.append(sum(sub_fragment))

    return sorted(spectrum)


def brute_force_sequencing(experimental_spectrum):
    parent_mass = max(experimental_spectrum)
    valid_sequences = []

    def find_combinations(current_peptide, current_sum):
        if current_sum == parent_mass:
            if get_circular_spectrum(current_peptide) == experimental_spectrum:
                valid_sequences.append(current_peptide)
            return

        if current_sum > parent_mass:
            return

        for mass in MASS_TABLE:
            find_combinations(current_peptide + [mass], current_sum + mass)

    find_combinations([], 0)
    return valid_sequences



test_spectrum = [0, 57, 71, 99, 128, 156, 170, 227]

results = brute_force_sequencing(test_spectrum)

unique_results = set(tuple(sorted(res)) for res in results)
print(f"Found {len(results)} permutations.")
print(f"Unique amino acid sets: {[list(r) for r in unique_results]}")