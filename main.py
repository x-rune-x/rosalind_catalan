def catalan_numbers(n):
    if n == 1 or n == 0:
        return 1

    output = 0
    for k in range(1, n + 1):
        output += catalan_numbers(k - 1) * catalan_numbers(n - k)

    return output


def matching_pairs(rna_seq):
    print(rna_seq)
    n = int(len(rna_seq)/2)
    rna_pairs = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}

    if (n == 1 and rna_seq[1] == rna_pairs[rna_seq[0]]) or n == 0:
        return 1

    output = 0
    for k in range(1, n + 1):
        if rna_seq[2*k - 1] == rna_pairs[rna_seq[0]]:
            # print(rna_seq, rna_seq[2*k - 1], 2*k - 1, rna_seq[1:2*k - 1], rna_seq[2*k:], output)
            output += matching_pairs(rna_seq[1:2*k - 1]) * matching_pairs(rna_seq[2*k:])

    return output


def get_rna_seq_from_file(file_path):
    with open(file_path) as read_file:
        return read_file.readlines()


rna = get_rna_seq_from_file('rosalind_cat.txt')[1]
perfect_noncrossing_matchings = matching_pairs(rna)
print(perfect_noncrossing_matchings)

with open('solution.txt', 'w') as write_file:
    write_file.write(str(perfect_noncrossing_matchings))
