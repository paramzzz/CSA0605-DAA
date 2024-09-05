def armstrong_number(n, power=None):
    if power is None:
        power = len(str(n))
    if n == 0:
        return 0
    else:
        last_digit = n % 10
        return last_digit ** power + armstrong_number(n // 10, power)
def is_armstrong(num):
    return num == armstrong_number(num)
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
