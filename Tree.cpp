// Tree.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctime>
#include <iostream>
#include <cstdlib>
#include <conio.h>
#include <conio.h>
#define CMP_EQ(a, b) ((a) == (b))
#define CMP_LT(a, b) ((a) < (b))
#define CMP_GT(a, b) ((a) > (b))

size_t n = 0;
long *mas = NULL;

void Read() //функция генерации массива случайных чисел
{
	size_t i;
	printf("Array size: ");
	scanf("%u", &n);

	mas = (long*)calloc(n, sizeof(long));

	srand(time(NULL));

	int A = 1;
	int B = 100;

	for (int i = 0; i < n; i++) {
		mas[i] = A + rand() % ((B + 1) - A);
	}
}
typedef struct tagTREE
{
	int inf;
	tagTREE *left;
	tagTREE *right;
}TREE;


TREE* Insert(TREE *root, int x)
{
	if (root == NULL)
	{
		root = new TREE;
		root->inf = x;
		root->left = root->right = NULL;
	}
	else
	{
		if (x <= root->inf)
			root->left = Insert(root->left, x);
		else
			root->right = Insert(root->right, x);
	}
	return root;
}
//функция удаления элемента из дерева
TREE* Remove(TREE *root, int x)
{
	TREE *t;
	if (root == NULL) return 0;
	if (x == root->inf)
	{
		if (root->left == NULL)
		{
			t = root->right;
			delete root;
			return t;
		}
		t = root->left;
		while (t->right) t = t->right;
		t->right = root->right;
		return root->left;
	}
	if (x <= root->inf)
		root->left = Remove(root->left, x);
	else
		root->right = Remove(root->right, x);
	return root;
}

TREE* WriteTree(TREE *root)
{
	if (root != NULL)
	{
		WriteTree(root->left);
		printf("%d, ", root->inf);
		WriteTree(root->right);
	}
	return NULL;
}
TREE* Find(TREE *root, int x) {
	while (root) {
		if (CMP_GT(root->inf, x)) {
			root = root->left;
			continue;
		}
		else if (CMP_LT(root->inf, x)) {
			root = root->right;
			continue;
		}
		else {
			return root;
		}
	}
	return NULL;
}

//главная функция
void main(void)
{
	setlocale(LC_ALL, "RUS");
	TREE *mytree = NULL; 
	int i;
	Read();
	double start1 = clock();
	for (i = 0; i < n; i++){
		mytree = Insert(mytree, mas[i]);
	}
	printf("Spent time on insert: %.6lf\n", (clock() - start1) / CLOCKS_PER_SEC);


	/*double start2 = clock();
	for (i = 0; i < n; i++){
		Find(mytree, mas[i]);
	}
	printf("Spent time on find: %.6lf\n", (clock() - start2) / CLOCKS_PER_SEC);
	
	
	double start3 = clock();
	for (i = 0; i < n; i++){
		mytree=Remove(mytree, mas[i]);
	}
	printf("Spent time on remove: %.6lf\n", (clock() - start3) / CLOCKS_PER_SEC);
	*/
	WriteTree(mytree);
	getch();
}