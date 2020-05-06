#include "lists.h"
/**
 * 
 * 
 * 
 * 
*/
int is_palindrome(listint_t **head)
{
	listint_t * corrent;
	size_t size, j;
	int palindro_array[2000];

	if (*head == NULL)
		return (1);
	corrent = *head;
	for (size = 0; corrent; size++)
	{
		palindro_array[size] = corrent->n;
		corrent = corrent->next;
	}
	corrent = *head;
	for (j = 0; j < size; j++, size--)
	{
		if (palindro_array[j] != palindro_array[size - 1])
			return (0);
	}
	return (1);
}
