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
	listint_t *prev = NULL, *next = NULL;
	listint_t *current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
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
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *prev_slow_ptr = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL)
		return (1);
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev_slow_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	if (fast_ptr != NULL)
		slow_ptr = slow_ptr->next;
	second_half = reverse_list(&slow_ptr);
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	prev_slow_ptr->next = reverse_list(&slow_ptr);
	return (is_palindrome);
}
