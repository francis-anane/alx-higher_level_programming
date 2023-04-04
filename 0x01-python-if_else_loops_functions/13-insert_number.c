/*
 * Author: Francis Ofori Anane
 * Date: 3/04/2023
 */

#include "lists.h"

/**
 * *insert_node - inserts a number into a sorted singly linked list.
 * @head: The pointer to the head node of the list.
 * @number: The number to insert
 * Return: The address of the new node.
 * or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp, *prev, *rt;
	int chk = -1;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	tmp = *head;
	if (new_node->n < tmp->n)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}
	while (tmp->next != NULL)
	{
		if (tmp->n < new_node->n)
		{
			prev = tmp;
			rt = prev->next;
			chk = 1;
		}
		tmp = tmp->next;
	}
	if ((chk == 1) && (new_node->n < rt->n))
	{
		prev->next = new_node;
		new_node->next = rt;
	}
	else
		tmp->next = new_node;
	return (new_node);
}
