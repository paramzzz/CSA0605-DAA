def is_perfect_number(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num
def find_perfect_numbers(limit):
    perfect_numbers = []
    for number in range(1, limit + 1):
        if is_perfect_number(number):
            perfect_numbers.append(number)
    return perfect_numbers
limit = 10000
perfect_numbers = find_perfect_numbers(limit)
print("Perfect numbers up to", limit, ":", perfect_numbers)
