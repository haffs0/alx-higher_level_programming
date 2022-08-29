#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - check if a lists is a palindrome
 * @head: the lists
 * Return: 0 if is palindrome else 1
 */

int is_palindrome(listint_t **head)
{
	int first;
	listint_t *current, *prev;

	current = *head;

	if (current == NULL)
		return (1);

	first = current->n;

	while (current && current->next && current->next->next != NULL)
	{
		prev = current->next->next;
		current = current->next;
	}

	if (first == prev->n)
		return (1);

	return (0);
}
