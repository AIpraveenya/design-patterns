from collections.abc import Iterator, Iterable

# Concrete Iterator
class MyIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration()

# Concrete Iterable
class MyCollection(Iterable):
    def __init__(self):
        self._items = []

    def __iter__(self):
        return MyIterator(self._items)

    def add_item(self, item):
        self._items.append(item)

# Client code
if __name__ == "__main__":
    collection = MyCollection()
    collection.add_item("item 1")
    collection.add_item("item 2")
    collection.add_item("item 3")

    for item in collection:
        print(item)
