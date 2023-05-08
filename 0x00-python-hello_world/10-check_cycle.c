#include "lists.h"

/**
 * check_cycle - checks whether there is a cycle
 * in a singly-linked list using Floyd’s Cycle-Finding Algorithm
 * @list: pointer to the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *S, *F;

	S = F = list;

	while (S && F && F->next)
	{
		S = S->next;
		F = F->next->next;
		if (S == F) /* then there is a loop */
		{
			return (1);
		}
	}

	return (0);
}

