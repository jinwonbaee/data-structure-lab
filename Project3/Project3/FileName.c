#include <stdio.h>

void main() {
	int i, j, k;
	char student[2][3][20];
	for (i = 0; i < 2; i++) {
		print("\n 학생 %d의 이름 : ", i + 1);
		gets(student[i][0]);
		print("\n 학생 %d의 학과 : ", i + 1);
		gets(student[i][1]);
		print("\n 학생 %d의 학번 : ", i + 1);
		gets(student[i][2]);


	}

	for (i = 0; i < 2; i++) {
		print("\n\n 학생 %d", i + 1);
		for (j = 0; j < 3; i++) {
			print("\n\t");
			for (k = 0; student[i][j][k] != '\0'; k++) {
				print("%c", student[i][j][k]);
			}
		}
	}
	getchar();
}