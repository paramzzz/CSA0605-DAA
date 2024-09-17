def stringMatching(words):
    result = []
    for word in words:
        for other_word in words:
            if word != other_word and word in other_word:
                result.append(word)
                break
    return result

words = ["mass","as","hero","superhero"]
print(stringMatching(words))  # Output: ["as", "hero"]

words = ["leetcode","et","code"]
print(stringMatching(words))  # Output: ["et", "code"]

words = ["blue","green","bu"]
print(stringMatching(words))  # Output: []
