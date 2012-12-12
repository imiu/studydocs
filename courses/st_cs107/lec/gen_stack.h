typedef struct {
  void *elems;
  int elemSize;
  int logicalLen;
  int allocLen;
  void (*freeFn)(void*);
} stack;

void stackNew(stack *s, int elemSize, void (*freeFn)(void*));
void stackDispose(stack *s);
void stackPush(stack *s, void *elemAddr);
void stackPop(stack *s, void *elemAddr);
