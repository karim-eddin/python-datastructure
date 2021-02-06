import ArrayStack


class DequeWithStacks:
    def __init__(self):
        self.s1 = ArrayStack()
        self.s2 = ArrayStack()

    def __len__(self):
        return len(self.s1) + len(self.s2)

    def is_empty(self):
        return len(self) == 0

    def add_first(self, elem):
        self.s1.push(elem)

    def add_last(self, elem):
        self.s2.push(elem)

    def remove_front(self):
        if self.is_empty():
            raise Empty('The Deque is Empty')

        elif self.s1.is_empty():  # front elem in back of s2
            while not self.s2.is_empty():
                self.s1.push(self.s2.pop())
            return self.s1.pop()
        else:
            return self.s1.pop()

    def remove_last(self):
        if self.is_empty():
            raise Empty('The Deque is Empty')
        elif self.s2.is_empty():  # back elem must be in s1 if not empty
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
            # the 'back' elem is now top of s2
            return self.s2.pop()

        else:  # neither s1 or s2 is empty, so back is in proper place
            return self.s2.pop()

    def first(self):
        if self.is_empty():
            raise Empty('The Deque is Empty')

        elif self.s1.is_empty():  # front elem in back of s2
            while not self.s2.is_empty():
                self.s1.push(self.s2.pop())
            return self.s1.top()

        else:
            return self.s1.top()

    def last(self):
        if self.is_empty():
            raise Empty('The Deque is Empty')

        elif self.s2.is_empty():  # back elem must be in s1 if not empty
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
            # the 'back' elem is now top of s2
            return self.s2.top()

        else:  # neither s1 or s2 is empty, so back is in proper place
            return self.s2.top()
