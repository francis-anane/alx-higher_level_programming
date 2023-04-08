/*
 * Author: Francis Ofori Anane
 * Date: 6/04/2023
 */

#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: The pointer to the head node of the list.
 * Return: 0 if not palindrome, or 1 if list is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *chk_nodes, *node, *start, *end;
	int chk = 1, index;
	int size = listint_len(*head);

	if (size == 0)
		return (1);
	index = 0;
	start = chk_nodes = node = *head;
	while (node != NULL)
	{
		if (index == size - 1)
		{
			end = node;
			if (end->n != chk_nodes->n)
			{
				chk = 0;
				break;
			}
			index = 0;
			size--;
			chk_nodes = chk_nodes->next;
			node = start;
		}
		node = node->next;
		index++;
	}
	return (chk);
}

/**
 * listint_len - Returns the number of
 * elements in a linked listint_t list.
 *
 * @h: The list to return the elements of.
 * Return: The number of elements of the list.
 */

int listint_len(const listint_t *h)
{
	int elements = 0;

	while (h != NULL)
	{
		h = h->next;
		elements += 1;
	}
	return (elements);
}
