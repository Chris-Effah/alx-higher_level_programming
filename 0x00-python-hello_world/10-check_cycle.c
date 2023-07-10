#include "lists.h"
/**
  * check_cycle - a function that checks if a singly linked list has a cycle
  * @list: singly linked list to be checked
  * Return: 0 if there is no cycle and 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (fast != slow)
	{
		if (fast == NULL || fast->next == NULL)
		{
			return (0);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (-1);
}
