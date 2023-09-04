#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - determines if a singly-linked list includes a cycle
 *
 * @list: singly-linked list to evaluate
 *
 * Return: 0, for no cycle
 * else, 1 for prescence of a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t = *tr;
	listint_t = *hr;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	tr = list->next;
	hr = list->next->next;
	while (tr && hr && hr->next)
	{
		if (tr == hr)
		{
			return (1);
		}
		tr = tr->next;
		hr = hr->next->next;
	}
	return (0);
}
