#include <stddef.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - inserts a new node in the list
 *@head: pointer to the head pointer
 *@number: the new number to be inserted
 *Return: returns null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if(new->n < node->n || !node)
	{
		new->next = node;
		return (*head = new);
	}
	while (node)
	{
		if (new->n < node->next->n || !node->next)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
