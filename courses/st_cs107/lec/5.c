#include <stdio.h>
#include <string.h>

// Int search
int isearch(int key, int array[], int size) {
  for (int i = 0; i < size; i++) {
    if (array[i] == key) {
      return i;
    }
  }
  return -1;
}

void *llsearch(void *key, void *base, int n, int elemSize) {
  for (int i = 0; i < n; i++) {
    void *elemAddr = (char *)base + i * elemSize;
    if (memcmp(key, elemAddr, elemSize) == 0) {
      return elemAddr;
    }
  }
  return NULL;
}

void *lsearch(void *key, void *base, int n, int elemSize,
    int (*cmpfn)(void *, void *)) {
  for (int i = 0; i < n; i++) {
    void *elemAddr = (char *)base + i * elemSize;
    if (cmpfn(key, elemAddr) == 0) {
      return elemAddr;
    }
  }
  return NULL;
}

int intCmp(void *elem1, void  *elem2) {
  int *ip1 = elem1;
  int *ip2 = elem2;

  return *ip1 - *ip2;
}

int StrCmp(void *vp1, void *vp2) {
    char *s1 = *(char **)vp1;
    char *s2 = *(char **)vp2;

    return strcmp(s1, s2);
}

int main() {
  // Using the lsearch
  int array[] = {4, 2, 3, 7, 11, 6};
  int size = 6;
  int number = 11;

  int *found = lsearch(&number, array, size, sizeof(int), intCmp);
  if (found == NULL) {
    printf("Not Found\n");
  } else {
    printf("Found: %d\n", *found);
  }

  // Searching for strings
  char *notes[] = {"Ab", "F#", "B", "Gb", "D"};
  char *favNote = "D";

  char **nfound = lsearch(&favNote, notes, 5, sizeof(char *), StrCmp);
  if (nfound == NULL) {
      printf("Not Found\n");
  } else {
      printf("Found: %s\n", *nfound);
  }
}
