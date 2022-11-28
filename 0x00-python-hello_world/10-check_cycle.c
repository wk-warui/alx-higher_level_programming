#include "lists.h"

/**
 * check_cylce - a function that checks if a singly linked list has a
 * cycle in it
 * @list: the list to check
 *
 * Return: 1, if a cycle is present or 0, if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *bear = list;
	listint_t *tort = list;

	while (tort && bear && bear->next)
	{
		tort = tort->next;
		bear = bear->next->next;

		if (bear == tort)
			return (1);
	}

	return (0);
}
