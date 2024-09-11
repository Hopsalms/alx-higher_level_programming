#include "lists.h"

/**
 * check_cycle - function that checks if a linked list contains a cycle in it
 *
 * @list: list of linked list parameters
 * Return: 1 if there is no cycle, 0 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || !list->next)
		return (0);
	fast = list;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
