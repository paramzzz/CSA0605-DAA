def fullJustify(words, maxWidth):
    result = []
    current_line = []
    current_width = 0

    for word in words:
        if current_width + len(word) + len(current_line) > maxWidth:
            # Distribute spaces evenly
            gaps = len(current_line) - 1
            if gaps == 0:
                result.append(current_line[0] + ' ' * (maxWidth - len(current_line[0])))
            else:
                total_spaces = maxWidth - sum(len(w) for w in current_line)
                base_spaces, extra_spaces = divmod(total_spaces, gaps)
                result.append(''.join(w + ' ' * base_spaces + (' ' if i < extra_spaces else '') for i, w in enumerate(current_line[:-1])) + current_line[-1])
            current_line = []
            current_width = 0
        current_line.append(word)
        current_width += len(word)

    # Handle the last line
    last_line = ' '.join(current_line)
    result.append(last_line + ' ' * (maxWidth - len(last_line)))

    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(fullJustify(words, maxWidth))
# Output:
# [
#   "This    is    an",
#   "example  of text",
#   "justification.  "
# ]


