def get_catalan_num(num):
    # Make function dynamic by storing previously found catalan numbers to be quickly accessed
    # instead of going through whole recursion process when the answer has already been computed.

    catalan_nums = {
        0: 1,
        1: 1
    }

    def catalan_dynamic(n):
        if n in catalan_nums:
            return catalan_nums[n]

        output = 0
        for k in range(1, n + 1):
            output += catalan_dynamic(k - 1) * catalan_dynamic(n - k)

        catalan_nums.update({n: output})

        return output

    return catalan_dynamic(num)


def number_of_noncrossing_matchings(rna_seq):
    rna_pairs = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}

    # Most basic pairings we use for base cases.
    known_matchings = {
        "AU": 1,
        "UA": 1,
        "GC": 1,
        "CG": 1
    }

    def matching_pairs_dynamic(seq):
        # Rosalind specifies conditions that the length of the RNA sequence is even and has the same number of
        # A's as U's and G's as C's.
        n = int(len(seq) / 2)

        if len(seq) == 0:
            return 1

        if seq in known_matchings:
            return known_matchings[seq]

        output = 0
        for k in range(1, n + 1):
            if seq[2 * k - 1] == rna_pairs[seq[0]]:
                # Added condition of working with RNA is that a
                # pair can only be formed between complementary nucleotides.

                output += matching_pairs_dynamic(seq[1:2 * k - 1]) * matching_pairs_dynamic(seq[2 * k:])
                known_matchings.update({seq: output})

        return output

    answer = matching_pairs_dynamic(rna_seq)
    print(known_matchings)

    return answer % 1000000


def get_rna_seq_from_file(file_path):
    with open(file_path) as read_file:
        return read_file.readlines()


rna = get_rna_seq_from_file('rosalind_cat.txt')[1]
perfect_noncrossing_matchings = number_of_noncrossing_matchings(rna)
print(perfect_noncrossing_matchings)

with open('solution.txt', 'w') as write_file:
    write_file.write(str(perfect_noncrossing_matchings))

