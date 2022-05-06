nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, nested_list_):
        self.nested_list_ = nested_list_

    def __iter__(self):
        self.n = 0
        self.k = 0
        return self

    def __next__(self):
        while self.n < len(self.nested_list_):
            if self.k < len(self.nested_list_[self.n]):
                result = self.nested_list_[self.n][self.k]
                self.k += 1
                return result
            self.n += 1
            self.k = 0
        raise StopIteration


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)