def combination_sum2(candidates, target):
    def backtrack(remain, comb, start):
        if remain == 0:
            result.append(list(comb))
            return
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i + 1)
            comb.pop()

    candidates.sort()
    result = []
    backtrack(target, [], 0)
    return result

# Test case 1:
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combination_sum2(candidates, target))  # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
