#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_list - reverses a linked list
 *
 * @head: double pointer to the head of the linked list
 *
 * Return: pointer to the new head of the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: double pointer to the head of the linked list
 *
 * Return: 1, if palidrome
 * else, 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *prev, *midl;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	prev = reverse_list(&temp);
	midl = prev;
	temp = *head;
	while (prev)
	{
		if (temp->n != prev->n)
			return (0);
		temp = temp->next;
		prev = prev->next;
	}
	reverse_list(&midl);
	return (1);
}
