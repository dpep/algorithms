#include "c_utils.h"


#define N(A) (A - '0')

int main() {
	char *num1, *num2, *res;

	num1 = "101";
	num2 = "10101";

	char *ptr1, *ptr2, *rptr;
	int size = MAX(strlen(num1), strlen(num2)) + 1;
	res = malloc(sizeof(char)*size + 1);
	memset(res, '0', size);
	rptr = res + size;
	*rptr = '\0'; // terminate string
	rptr--;

	ptr1 = num1 + strlen(num1) - 1;
	ptr2 = num2 + strlen(num2) - 1;

	int sum, carry = 0;
	for (; ptr1 >= num1 && ptr2 >= num2; ptr1--, ptr2--, rptr--) {
		sum = N(*ptr1) + N(*ptr2) + carry;
		*rptr = sum % 2 + '0';
		carry = sum / 2;
	}

	for (; ptr1 >= num1; ptr1--, rptr--) {
		sum = N(*ptr1) + carry;
		*rptr = sum % 2 + '0';
		carry = sum / 2;
	}

	for (; ptr2 >= num2; ptr2--, rptr--) {
		sum = N(*ptr2) + carry;
		*rptr = sum % 2 + '0';
		carry = sum / 2;
	}
	*rptr = carry + '0';
	while (*res == '0') {
		res++;
	}

	printf("%s + %s = %s\n", num1, num2, res);

	return EXIT_SUCCESS;
}