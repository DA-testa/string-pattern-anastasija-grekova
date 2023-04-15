import os

def read_input():
    check = input().rstrip()

    if check == "F":
        path = os.getcwd() + '/tests'
        os.chdir(path)
        file_name = '06'
    
        file_path = f"{path}/{file_name}"
        print(input())
        quit()
        with open(file_path, "r", encoding="utf-8-sig") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()    

    if check == "I":
        pattern = input().rstrip()
        text = input().rstrip()

    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    count = []
    patternLength = len(pattern)

    patternHashVal = sum(ord(pattern[i]) * pow(10, patternLength - i - 1) for i in range(patternLength)) 

    textHashVal = sum(ord(text[i]) * pow(10, patternLength - i - 1) for i in range(patternLength))

    if patternHashVal == textHashVal and pattern == text[:patternLength]:
        count.append(0)

    for i in range(1, len(text) - patternLength + 1):
        textHashVal = textHashVal - ord(text[i - 1]) * pow(10, patternLength - 1)
        textHashVal = textHashVal * 10 + ord(text[i + patternLength - 1])
        if patternHashVal == textHashVal and pattern == text[i:i+patternLength]:
            count.append(i)

    return count


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
