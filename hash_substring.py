def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_choice = input().rstrip()
    if input_choice == "F":
        with open("input.txt") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    if input_choice == "I":
        pattern = input().rstrip()
        text = input().rstrip()

    # return both lines in one return
    return pattern, text


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)

    # calculate the hash value of the pattern
    p_hash = sum(ord(pattern[i]) * pow(10, p_len - i - 1) for i in range(p_len)) 

    # calculate the hash value of the first window in the text
    t_hash = sum(ord(text[i]) * pow(10, p_len - i - 1) for i in range(p_len))

    # check if pattern matches with the first window
    if p_hash == t_hash and pattern == text[:p_len]:
        occurrences.append(0)

    # calculate the hash value of each subsequent window and check if it matches with the pattern
    for i in range(1, t_len - p_len + 1):
        t_hash = t_hash - ord(text[i - 1]) * pow(10, p_len - 1)
        t_hash = t_hash * 10 + ord(text[i + p_len - 1])
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            occurrences.append(i)

    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

