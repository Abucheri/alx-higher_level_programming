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
	listint_t *new_node;
	listint_t *current;
	listint_t *prev;

	new_node = malloc(sizeof(listint_t));
	current = *head;
	prev = NULL;
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	prev->next = new_node;
	new_node->next = current;
	return (new_node);
}
