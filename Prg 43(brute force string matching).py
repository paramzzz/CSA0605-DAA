def strStr(haystack, needle):
    if needle == "":
        return 0
    try:
        return haystack.index(needle)
    except ValueError:
        return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))  # Output: 2

