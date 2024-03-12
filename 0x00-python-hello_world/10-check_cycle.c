#include "list.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *rabbit, *turtle;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list;
	rabbit = list->next;

	while (rabbit != NULL && rabbit->next != NULL)
	{
		if (rabbit == turtle)
			return (1);
		turtle = turtle->next;
		rabbit = rabbit->next->next;
	}
	return (0);
}
