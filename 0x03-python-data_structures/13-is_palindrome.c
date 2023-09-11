#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: double pointer to the head of the linked list
 *
 * Return: 1, if palindrome
 * else, 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int arr[1024];
	int i = 0, j;

	if (*head == NULL)
		return (1);
	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	i--;
	for (j = 0; j <= i / 2; j++)
	{
		if (arr[j] != arr[i - j])
			return (0);
	}
	return (1);
}
