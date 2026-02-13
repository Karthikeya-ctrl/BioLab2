import collections

AA_MASSES = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def get_linear_spectrum(peptide):
    n = len(peptide)
    spectrum = [0]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            spectrum.append(sum(peptide[i:i + length]))
    return sorted(spectrum)


def get_score(peptide, experimental_spectrum):
    theoretical = get_linear_spectrum(peptide)
    theo_counts = collections.Counter(theoretical)
    exp_counts = collections.Counter(experimental_spectrum)

    score = 0
    for mass in theo_counts:
        score += min(theo_counts[mass], exp_counts.get(mass, 0))
    return score


def trim_leaderboard(leaderboard, spectrum, n):
    if not leaderboard:
        return []

    scores = [(get_score(p, spectrum), p) for p in leaderboard]
    scores.sort(key=lambda x: x[0], reverse=True)

    trimmed = [scores[i][1] for i in range(min(len(scores), n))]

    if len(scores) > n:
        threshold = scores[n - 1][0]
        for i in range(n, len(scores)):
            if scores[i][0] == threshold:
                trimmed.append(scores[i][1])
            else:
                break
    return trimmed


def leaderboard_cyclopeptide_sequencing(spectrum, n):
    leaderboard = [[]]
    leader_peptide = []
    parent_mass = max(spectrum)  #

    while leaderboard:
        new_candidates = []
        for peptide in leaderboard:
            for mass in AA_MASSES:
                new_candidates.append(peptide + [mass])

        leaderboard = []
        for peptide in new_candidates:
            p_mass = sum(peptide)


            if p_mass == parent_mass:
                if get_score(peptide, spectrum) > get_score(leader_peptide, spectrum):
                    leader_peptide = peptide

            elif p_mass < parent_mass:
                leaderboard.append(peptide)

        leaderboard = trim_leaderboard(leaderboard, spectrum, n)

    return leader_peptide


noisy_spectrum = [0, 113, 114, 128, 129, 227, 242, 257, 355, 370, 371, 484]
n_value = 10
result = leaderboard_cyclopeptide_sequencing(noisy_spectrum, n_value)
print(f"Top Scoring Peptide Sequence (Masses): {result}")