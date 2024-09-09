def min_value(s: str) -> str:
    """
    Replace all occurrences of '?' in s with lowercase English letters to minimize the value of s.
    """
    seen = set()  # keep track of seen characters
    result = []  # resulting string

    for c in s:
        if c == '?':
            # find a character that has not been seen before
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char not in seen:
                    result.append(char)
                    seen.add(char)
                    break
        else:
            result.append(c)
            seen.add(c)

    return ''.join(result)

# Test the function
s = "a?b?c"
print("Input:", s)
print("Output:", min_value(s))
