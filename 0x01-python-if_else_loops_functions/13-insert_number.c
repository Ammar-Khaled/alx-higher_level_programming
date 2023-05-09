#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the list
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *cur;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);	
	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}

	if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	cur = prev = *head;
	cur = cur->next;
	while (cur && cur->n < number)
	{
		cur = cur->next;
		prev = prev->next;
	}
	
	prev->next = new;
	new->next = cur;
	return (new);
}
