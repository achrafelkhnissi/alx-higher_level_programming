#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head) {
  if (*head == NULL) {
    return 1;
  }

  // Get the middle of the linked list.
  listint_t *mid = *head;
  listint_t *prev = NULL;
  while (mid->next != NULL) {
    prev = mid;
    mid = mid->next;
  }

  // Reverse the second half of the linked list.
  listint_t *curr = mid;
  listint_t *next = NULL;
  while (curr != NULL) {
    next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }

  // Compare the first half of the linked list with the reversed second half.
  listint_t *first = *head;
  while (first != prev) {
    if (first->n != prev->n) {
      return 0;
    }
    first = first->next;
    prev = prev->next;
  }

  // The linked list is a palindrome.
  return 1;
}
