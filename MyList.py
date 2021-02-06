import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for ind in range(self.n):
            new_array[ind] = self.data[ind]
        self.data = new_array
        self.capacity = new_size

    def extend(self, other):
        for elem in other:
            self.append(elem)

    def __getitem__(self, ind):
        if not(0 <= ind <= self.n - 1):
            raise IndexError('MyList index is out of range')
        return self.data[ind]

    def __setitem__(self, ind, val):
        if not(0 <= ind <= self.n - 1):
            raise IndexError('MyList index is out of range')
        self.data[ind] = val


mylst1 = MyList()
for i in range(5):
    mylst1.append(i)

mylst2 = MyList()
for i in range(6):
    mylst2.append(10 * i)



