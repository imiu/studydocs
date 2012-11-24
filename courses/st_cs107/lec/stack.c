#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "stack.h"

void stackNew(stack *s) {
  s->logical_len = 0;
  s->alloc_len = 4;
  s->elems = malloc(4 * sizeof(int));

  assert(s->elems != NULL);
}

void stackDispose(stack *s) {
  free(s->elems);
}

void stackPush(stack *s, int value) {
  if (s->logical_len == s->alloc_len) {
    s->alloc_len *= 2;
    s->elems = realloc(s->elems, s->alloc_len * sizeof(int));
  }
  s->elems[s->logical_len] = value;
  s->logical_len++;
}

int stackPop(stack *s) {
  assert(s->logical_len > 0);
  s->logical_len--;
  return s->elems[s->logical_len];
}

int main() {
  stack s;
  stackNew(&s);

  for (int i = 0; i < 5; i++) {
    stackPush(&s, i);
  }

  for (int i = 0; i < 5; i++) {
    int elem = stackPop(&s);
    printf("Elem %d: %d\n", i, elem);
  }

  /* stackDispose(&s); */
}
