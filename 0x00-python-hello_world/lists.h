#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * @next: points to the next node.
 * @n: integer
 * struct listint_s - singly linked list.
 *
 * Description: singly linked list node structure.
 *
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

#endif /* LIST_H */
