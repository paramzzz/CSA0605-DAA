
def solve(s: str) -> str:
    letters = set('abcdefghijklmnopqrstuvwxyz')
    result = s
    
    prev_result = ""
    

    while result:
        
        to_remove = set()
        for letter in letters:
            if letter in result:
                to_remove.add(letter)
        prev_result = result
        
        for char in to_remove:
            result = result.replace(char, '', 1)
    
    return prev_result


print(solve("aabcbbca"))  # Output: "ba"
