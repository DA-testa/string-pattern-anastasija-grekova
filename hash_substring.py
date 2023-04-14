# python3

PRIME = 10**9 + 7
MULTIPLIER = 263

def read_input():
    # acquire input from keyboard or file
    input_type = input().strip().lower()
    if input_type == 'i':
        return input().strip(), input().strip()
    elif input_type == 'f':
        with open(input().strip()) as f:
            return f.readline().strip(), f.readline().strip()

def print_occurrences(output):
    # output the positions of occurrences
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # find the positions of occurrences of pattern in text using Rabin Karp algorithm
    n, m = len(text), len(pattern)
    pattern_hash = sum(ord(pattern[i]) * MULTIPLIER**i for i in range(m)) % PRIME
    hashes = [0] * (n-m+1)
    s = text[n-m:]
    hashes[n-m] = sum(ord(s[i]) * MULTIPLIER**i for i in range(m)) % PRIME
    y = pow(MULTIPLIER, m-1, PRIME)
    for i in range(n-m-1, -1, -1):
        hashes[i] = (MULTIPLIER*hashes[i+1] + ord(text[i]) - y*ord(text[i+m])) % PRIME
    return [i for i in range(n-m+1) if hashes[i] == pattern_hash and text[i:i+m] == pattern]

# launch the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
