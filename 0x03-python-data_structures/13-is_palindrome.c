#include "lists.h"
#include <stddef.h>
/**
 *checkPal- checks if its pallindrome or not
 *@head: pointer to the head pointer
 *@end: end of the list
 *Return: return 0 or 1 depending
 */
int checkPal(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (checkPal(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 *is_palindrome - palindrome or not
 *@head: pointer to the pointer head
 *Return: returns the pointer to the head
 */


int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return(checkPal(head, *head));
}
