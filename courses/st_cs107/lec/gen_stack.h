typedef struct {
  void *elems;
  int elemSize;
  int logicalLen;
  int allocLen;
} stack;

void stackNew(stack *s, int elemSize);
void stackDispose(stack *s);
void stashPush(stack *s, void *elemAddr);
void stackPop(stack *s, void *elemAddr);
