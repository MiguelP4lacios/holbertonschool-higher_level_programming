#include "lists.h"
/**
 * create_node - creates a new node
 * @n: int
 * Return: address memory node
 */
listint_t *create_node(const int n)
{
	listint_t *n_node;

	n_node = malloc(sizeof(listint_t));
	if (n_node == NULL)
		return (NULL);
	n_node->n =  n;
	n_node->next = NULL;
	return (n_node);
}

/**
 * insert_node - thisinserts a number into a
 * sorted singly linked list.
 * @head: dkdk
 * @number: djdjd
 * Return: djdjdjd
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *isrt_node, *tmp;

	if (!head)
		return (NULL);
	isrt_node = create_node(number);
	if (!isrt_node)
		return (NULL);
	if ((*head) == NULL || isrt_node->n <= (*head)->n)
	{
		isrt_node->next = *head;
		*head = isrt_node;
		return (isrt_node);
	}
	else
	{
		tmp = *head;
		for (; tmp;)
		{
			if (tmp->next == NULL ||
			(isrt_node->n >= tmp->n && isrt_node->n <= tmp->next->n))
			{
				isrt_node->next = tmp->next;
				tmp->next = isrt_node;
				return (isrt_node);
			}
			tmp = tmp->next;

		}
	}
	return (NULL);
}
