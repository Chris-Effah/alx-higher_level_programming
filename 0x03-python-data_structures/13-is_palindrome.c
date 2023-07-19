#include "lists.h"
/**
  * reverse_list - a function to reverse a linked list
  * @head: head of the linked list
  * @Return: reversed linked list
  */
listint_t *reverse_list(listint_t *head)
{
	listint_t *current, *prev, *next;

	current = head;
	prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);

}
/**
  * is_palindrome - a function that checks if a linked list is a palindrome
  * @head: head of the linked list
  * @Return: 0 if the linked list is a palindrome and i if not
  */
int is_palindrome(listint_t **head)
{
	int i, n = 0;
	listint_t *middle;
	listint_t *current = *head;
	while (current != NULL)
	{
		n++;
		current = current->next;
	}


	current = *head;
	middle = *head;

	for (i = 0; i < n / 2; i++)
	{
		middle = middle->next;
	}
	middle = reverse_list(middle);

	while (middle != NULL)
	{
		if (current->n != middle->n)
			return (0);

		current = current->next;
		middle = middle->next;
	}

	reverse_list(*head);

	return (1);

}
