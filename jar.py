"""
__init__ should initialize a cookie jar with the given capacity,
which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int,
though, __init__ should instead raise a ValueError.

__str__ should return a str with n 🍪, where n is the number of cookies in the cookie jar.
For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar;s capacity,
though, deposit should instead raise a ValueError.
withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren't that many cookies in the cookie jar,
though, withdraw should instead raise a ValueError.
capacity should return the cookie jar's capacity.
size should return the number of cookies actually in the cookie jar, initially 0.
"""


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = ""
        for _ in range(self.size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        self.size += n


    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Invalid size")
        elif size > self.capacity:
            raise ValueError("Exceed the max capacity")
        self._size = size

def main():
    jar = Jar(0)
    print(f"jar capacity: {jar.capacity}, jar size: {jar.size}")



if __name__ == "__main__":
    main()