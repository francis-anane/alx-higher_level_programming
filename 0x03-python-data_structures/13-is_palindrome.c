/*
 * Author: Francis Ofori Anane
 * Date: 6/04/2023
 */

#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: The pointer to the head node of the list.
 * Return: 0 if not palindrome, or 1 if list is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *chk_nodes, *node;
	int chk = 1, index;
	int size = listint_len(*head);
	listint_t **tmp;

	if (size == 0)
		return (1);
	tmp = malloc(size * sizeof(listint_t));
	if (tmp == NULL)
		return (0);
	index = size - 1;
	chk_nodes = node = *head;
	while (node != NULL)
	{
		tmp[index] = node;
		node = node->next;
		index--;
	}
	index = 0;
	while (chk_nodes != NULL)
	{
		if (tmp[index]->n != chk_nodes->n)
			chk = 0;
		chk_nodes = chk_nodes->next;
		index++;
	}
	free(tmp);
	tmp = NULL;

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
