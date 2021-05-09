def brackets_check(line):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    first_bracket_pos = 0

    for i, char in enumerate(line, 1):
        if char in brackets.values():
            stack.append(char)
            if first_bracket_pos == 0:
                first_bracket_pos = i

        elif char in brackets:
            if not stack or brackets[char] != stack.pop():
                return i
            if not stack:
                first_bracket_pos = 0

    return first_bracket_pos if stack else 'Success'


def main():
    print(brackets_check(line=input()))


if __name__ == '__main__':
    main()
