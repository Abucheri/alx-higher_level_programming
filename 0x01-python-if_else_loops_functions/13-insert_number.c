#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - puts a no. into a sorted singly linked list
 *
 * @head: pointer to head of linked list
 * @number: no. to add
 *
 * Return: NULL, for failure
 * else, pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}
	new->next = node->next;
	node->next = new;
	return (new);
}
