#include <stdio.h>
unsigned int factorial_non_recursive(int n) {
    unsigned int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}
unsigned int factorial_recursive(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial_recursive(n - 1);
}
int main() {
    int number = 5;
    unsigned int result_non_recursive = factorial_non_recursive(number);
    printf("Non-Recursive Factorial of %d: %u\n", number, result_non_recursive);
    unsigned int result_recursive = factorial_recursive(number);
    printf("Recursive Factorial of %d: %u\n", number, result_recursive);
    return 0;
}
