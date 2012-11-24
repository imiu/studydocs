#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "gen_stack.h"

static void stackGrow(stack *s) {
  s->allocLen *= 2;
  s->elems = realloc(s->elems, s->allocLen * s->elemSize);
}

void stackNew(stack *s, int elemSize) {
  assert(elemSize > 0);
  s->elemSize = elemSize;
  s->logicalLen = 0;
  s->allocLen = 4;
  s->elems = malloc(4 * elemSize);
  assert(s->elems != NULL);
}

void stackDispose(stack *s) {
  free(s->elems);
}

void stackPush(stack *s, void *elemAddr) {
  if (s->logicalLen == s->allocLen) {
    stackGrow(s);
  }
  void *target = (char*) s->elems + s->logicalLen * s->elemSize;
  memcpy(target, elemAddr, s->elemSize);
  s->logicalLen++;
}

void stackPop(stack *s, void *elemAddr) {
  assert(s->logicalLen > 0);
  s->logicalLen--;
  void *source = (char*) s->elems + (s->logicalLen) * s->elemSize;
  memcpy(elemAddr, source, s->elemSize);
}

int main() {
  stack s;
  stackNew(&s, sizeof(int));

  for (int i = 0; i < 5; i++) {
    stackPush(&s, &i);
  }

  for (int i = 0; i < 5; i++) {
    int top;
    stackPop(&s, &top);
    printf("Elem %d: %d\n", i, top);
  }
}
