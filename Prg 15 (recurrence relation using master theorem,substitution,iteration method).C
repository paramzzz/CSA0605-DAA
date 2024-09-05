#include <stdio.h>
#include <math.h>
void masterTheorem(int n) {
    if (n <= 1) {
        return;
    }
    masterTheorem(n / 2);
    masterTheorem(n / 2);
    printf("Processing at n = %d\n", n);
}
int substitutionMethod(int n) {
    if (n <= 1) {
        return 1;
    }
    return 2 * substitutionMethod(n / 2) + n;
}
int iterationMethod(int n) {
    if (n <= 1) {
        return 1;
    }
    return iterationMethod(n - 1) + n;
}
int main() {
    int n = 8;
    printf("Master Theorem:\n");
    masterTheorem(n);
    printf("\nSubstitution Method Result: %d\n", substitutionMethod(n));
    printf("\nIteration Method Result: %d\n", iterationMethod(n));
    return 0;
}
