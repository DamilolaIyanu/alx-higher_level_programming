#include "lists.h"
/**
 *check_cycle - checks if the linked list is cycled or not
 *@list: the singly linked list
 *Return: either 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || !list->next)
		return (0);

	slow = list;
	fast = list;

	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
