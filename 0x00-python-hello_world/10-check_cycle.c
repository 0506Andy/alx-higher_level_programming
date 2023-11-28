#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *relaxed = list;
	listint_t *quick = list;

	if (!list)
	{
		return (0);
	}
	while (relaxed && quick && quick->next)
	{
		relaxed = relaxed->next;
		quick = quick->next->next;
		if (relaxed == quick)
		{
			return (1);
		}
	}

	return (0);
}
