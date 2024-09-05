#include <stdio.h>
void constantTime() {
    printf("This function runs in O(1) time complexity.\n");
}
void linearTime(int n) {
    for (int i = 0; i < n; i++) {
        printf("This function runs in O(n) time complexity, iteration %d.\n", i);
    }
}
void quadraticTime(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("This function runs in O(n^2) time complexity, iteration (%d, %d).\n", i, j);
        }
    }
}
int main() {
    int n = 5;
    printf("Analyzing time complexities:\n");
    constantTime();
    linearTime(n);
    quadraticTime(n);
    return 0;
}
