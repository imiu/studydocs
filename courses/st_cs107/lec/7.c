#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "gen_stack.h"

void stringFree(void *elem) {
  free(*(char**)elem);
}

void rotate(void *front, void *middle, void *end) {
  int frontSize = (char *)middle - (char *)front;
  int backSize = (char *)end - (char *)middle;

  char buffer[frontSize];
  memcpy(buffer, front, frontSize);
  memmove(front, middle, backSize);
  memcpy((char *)end - frontSize, buffer, frontSize);
}

int main() {
  const char *friends[] = {"Al", "Bob", "Carl"};
  stack stringStack;
  stackNew(&stringStack, sizeof(char*), stringFree);
  int i;
  for (i = 0; i < 3; i++) {
    char *copy = strdup(friends[i]);
    stackPush(&stringStack, &copy);
  }

  /* char *name; */
  /* for (i = 0; i < 3; i++) { */
    /* stackPop(&stringStack, &name); */
    /* printf("Elem %d: %s\n", i, name); */
    /* free(name); */
  /* } */
  stackDispose(&stringStack);

  return 0;
}
