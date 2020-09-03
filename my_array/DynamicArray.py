import ctypes


def _make_array(capacity):
    return (capacity * ctypes.py_object)()


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = _make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, item):
        if not 0 <= item < self._n:
            raise IndexError('invalid index')
        return self._A[item]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, capacity):
        B = _make_array(capacity)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = capacity

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k,self._n-1):
                    self._A[j] = self._A[j+1]
                self._A[self._n -1] = None
                self._n -= 1
                return

        raise ValueError("value not found")