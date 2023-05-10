#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: address of new node or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current;

    if (!head)
        return (NULL);

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);

    new->n = number;

    if (!*head)
    {
        new->next = NULL;
        *head = new;
        return (new);
    }

    current = *head;
    if (current->n > number)
    {
        new->next = current;
        *head = new;
        return (new);
    }

    while (current->next)
    {
        if (current->next->n > number)
        {
            new->next = current->next;
            current->next = new;
            return (new);
        }
        current = current->next;
    }

    new->next = NULL;
    current->next = new;
    return (new);
}
