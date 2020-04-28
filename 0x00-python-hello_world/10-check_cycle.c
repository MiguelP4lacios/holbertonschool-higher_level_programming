#include "lists.h"
/**
 * check_cycle - check if a linked list is cycle or no
 * @list: linked list
 * Return: O or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}
