def main():
    myjar = Jar(-1)
    print(myjar.capacity)

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be less than Zero")
        self.capacity = capacity
        self.size = 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            ValueError("Capacity cannot be zero or negative")
        else:
            self._capacity = capacity

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Sorry, Can't hold that many")
        else:
            self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Sorry, Not enough cookies to withdraw")
        else:
            self.size -= n


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size cannot be greater than capacity")
        else:
            self._size = size

    def __str__(self):
        return f"{'🍪'*self.size}"

if __name__ == "__main__":
    main()