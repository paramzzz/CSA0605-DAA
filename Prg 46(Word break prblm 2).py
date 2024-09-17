def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]

wordDict = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
s = "ilike"
print(wordBreak(s, wordDict))  # Output: True

s = "ilikesamsung"
print(wordBreak(s, wordDict))  # Output: True

s = "ilikesamsungmango"
print(wordBreak(s, wordDict))  # Output: True

s = "ilikesamsungmangogogo"
print(wordBreak(s, wordDict))  # Output: False
