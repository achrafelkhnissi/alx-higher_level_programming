#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Double pointer to the head of the linked list
 *
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * compare_lists - Compares two linked lists
 * @list1: Pointer to the head of the first list
 * @list2: Pointer to the head of the second list
 *
 * Return: 1 if the lists are identical, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *mid = NULL;
	listint_t *second_half = NULL;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (palindrome);
	/* Find the middle of the list and reverse the first half */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	/* Handle odd or even number of nodes */
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	second_half = slow;
	prev_slow->next = NULL;
	/* Reverse the second half of the list */
	reverse_list(&second_half);
	/* Compare the first and second half of the list */
	palindrome = compare_lists(*head, second_half);
	/* Restore the original list by reversing the second half again */
	reverse_list(&second_half);
	/* Handle odd number of nodes */
	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = second_half;
	}
	else
		prev_slow->next = second_half;
	return (palindrome);
}
