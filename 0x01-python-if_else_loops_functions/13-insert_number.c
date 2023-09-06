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
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current->next != NULL && number > current->next->n)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
