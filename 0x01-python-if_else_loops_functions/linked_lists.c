/*
 * Author: Francis Ofori Anane
 * Date: 3/04/2023
 */

#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * print_listint - Prints all the elements of a listint_t list.
 *
 * @h: The list to print elements of.
 * Return: The number of nodes of the list.
 */

size_t print_listint(const listint_t *h)
{
	size_t nodes = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		nodes += 1;
	}
	return (nodes);
}

/**
 * add_nodeint - Adds a new node at the
 * beinning of a list_t list.
 *
 * @head: The pointer to the head node of the list.
 * @n: Data for the new node.
 * Return: The address of the new node.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

/**
 * free_listint - Frees a listint_t list.
 *
 * @head: The list to free.
 */

void free_listint(listint_t *head)
{
	listint_t *node;

	if (head == NULL)
		return;

	while (head != NULL)
	{
		node = head->next;
		free(head);
		head = node;
	}
}

/**
 * add_nodeint_end - Adds a new node at
 * the end of a listint_t list.
 *
 * @head: The pointer to the head node of the list.
 * @n: Data for the new node.
 * Return: The address of the new node.
 * or NULL if it fails.
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	listint_t *node = *head;

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}
	else
		node = *head;

	while (node->next != NULL)
	{
		node = node->next;
	}

	if (node->next == NULL)
		node->next = new_node;

	return (node);
}
