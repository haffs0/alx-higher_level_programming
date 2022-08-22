#include "lists.h"
#include <signal.h>
#include <stdio.h>
/**
 * check_cycle - check if a lists have a cycle
 * @list: the lists to check
 * Return: 1 on success or 0 on failure
 */

int check_cycle(listint_t *list)
{
	listint_t *list1, *list2;

	if (list == NULL || list->next == NULL)
		return (0);

	list1 = list->next;
	list2 = list->next->next;

	while (list1 && list2 && list2->next)
	{
		if (list1 == list2)
			return (1);

		list1 = list1->next;
		list2 = list2->next->next;
	}
	return (0);
}
