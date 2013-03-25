from __future__ import print_function


class Ex11(object):
    def e6(self, n):
        f = 0
        g = 1
        for i in range(n):
            f = f + g
            g = f - g
        return f

    def e11(self, arr):
        arr_repr = []
        for line in arr:
            for elem in line:
                arr_repr.append((' ', '*')[elem])
            arr_repr.append("\n")
        return ''.join(arr_repr)

    def e13(self, arr):
        return [list(tup) for tup in zip(*arr)]
        # return zip(*arr)

    def e15(self, arr):
        hist = [0 for i in range(max(arr) + 1)]
        for elem in arr:
            hist[elem] += 1
        return hist

    def e18(self, a, b):
        if b == 0:
            return 0
        if b % 2 == 0:
            return self.e18(a + a, b / 2)
        return self.e18(a + a, b / 2) + a

    def gcd(self, p, q):
        if q == 0:
            return p
        return self.gcd(q, (p % q))

    def bs(self, elem, arr):
        lo = 0
        hi = len(arr) - 1
        while (lo <= hi):
            mid = lo + (hi - lo) / 2
            if (elem < arr[mid]):
                hi = mid - 1
            elif (elem > arr[mid]):
                lo = mid + 1
            else:
                return mid

    def e30(self, n):
        arr = [[False for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                print(i, j, self.gcd(i, j))
                if self.gcd(i, j) == 1:
                    arr[i][j] = True
                else:
                    arr[i][j] = False
        print(arr)
        return arr


if __name__ == '__main__':
    e = Ex11()
    # print(e.e21(1, [0, 1, 2, 3, 5, 7]))
