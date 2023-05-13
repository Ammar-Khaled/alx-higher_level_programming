#include "lists.h"

/**
 * reverse_listint -  reverses a listint_t linked list.
 * @head: pointer to pointer to the list
 *
 * Return: pointer to the new reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prevNode, *curNode;

    if (!(*head))
        return (NULL);

    prevNode = (*head);
    *head = (*head)->next;
    curNode = *head;

    prevNode->next = NULL; /*disconnect first node*/

    while (*head)
    {
        *head = (*head)->next;
        curNode->next = prevNode;
        prevNode = curNode;
        curNode = (*head);
    }
    *head = prevNode;
    return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *reversed_head;

    /* An empty list is considered a palindrome */
    if (!head)
        return (1);

    reversed_head = reverse_listint(head);

    while (*head)
    {
        if ((*head)->n != reversed_head->n)
            return (0);
        *head = (*head)->next;
        reversed_head = reversed_head->next;
    }

    return (1);
}
