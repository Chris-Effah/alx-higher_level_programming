#include "lists.h"
/**
  * check_cycle - a function that checks if a singly linked list has a cycle
  * @list: singly linked list to be checked
  * Return: 0 if there is no cycle and 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
	{
		return (0);
	}

	while (fast && slow && fast->next)
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
