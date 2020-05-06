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
	size_t size, j, flag = 1;
	int *palindro_array;

	if (*head == NULL)
		return (1);
	corrent = *head;
	for (size = 0; corrent; size++)
		corrent = corrent->next;
	palindro_array = malloc(sizeof(int) * size);
	if (!palindro_array)
		return (1);
	corrent = *head;
	for (j = 0; j < size; j++)
	{
		palindro_array[j] = corrent->n;
		corrent = corrent->next;
	}
	for (j = 0; j < size; j++, size--)
	{
		if (palindro_array[j] != palindro_array[size - 1])
			flag = 0;
	}
	free (palindro_array);
	if (flag == 0)
		return(0);
	return (1);
}
