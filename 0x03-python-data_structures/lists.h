#ifndef LISTS_H
#define LISTS_H

#include<stdlib.h>
#include <stdio.h>

/**
*struct listint_s - singly linked list
*@i: int
*@next: pointing to the next node
* Description:A singly linked list node structure
*/

typedef struct listint_s
{
        int i;
        struct listint_s *next;

}listint_t;

int is_palindrome(listint_t **head);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
#endif
