def catalan_numbers(n):
    if n == 1 or n == 0:
        return 1

    output = 0
    for k in range(1, n + 1):
        output += catalan_numbers(k - 1) * catalan_numbers(n - k)

    return output


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


def number_of_noncrossing_matchings(rna_seq):
    rna_pairs = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}

    known_matchings = {
        "AU": 1,
        "UA": 1,
        "GC": 1,
        "CG": 1
    }

    def matching_pairs_dynamic(seq):
        print(seq)
        n = int(len(seq) / 2)

        if len(seq) == 0:
            print('returning 1')
            return 1

        if seq in known_matchings:
            print('Seq found!')
            return known_matchings[seq]

        output = 0
        for k in range(1, n + 1):
            if seq[2 * k - 1] == rna_pairs[seq[0]]:
                print(f'First part is {seq[1:2 * k - 1]}, second part is {seq[2 * k:]}')
                output += matching_pairs_dynamic(seq[1:2 * k - 1]) * matching_pairs_dynamic(seq[2 * k:])

        known_matchings.update({seq: output})

        return output

    return matching_pairs_dynamic(rna_seq)


def get_rna_seq_from_file(file_path):
    with open(file_path) as read_file:
        return read_file.readlines()


rna = get_rna_seq_from_file('sample.txt')[1]
perfect_noncrossing_matchings = number_of_noncrossing_matchings('AUAU')
print(perfect_noncrossing_matchings)

with open('solution.txt', 'w') as write_file:
    write_file.write(str(perfect_noncrossing_matchings))

