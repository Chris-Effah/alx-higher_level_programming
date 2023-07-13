#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
* insert_node - a function that inserts a number into a sorted singly-linked list
* @head: A pointer to the beggining of the linked list
* @number: the number going to be inserted
* Return: the address of the new node or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	
	return (new);
}
