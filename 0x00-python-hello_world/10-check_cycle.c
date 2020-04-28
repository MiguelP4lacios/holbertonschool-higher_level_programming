#include "lists.h"
/**
 * check_cycle - check if a linked list is cycle or no
 * @list: linked list
 * Return: O or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *listaux = current;

	while (current && listaux && current->next)
	{
		listaux = listaux->next;
		current = current->next->next;
		if (current == listaux)
			return (1);
	}
	return (0);
}
