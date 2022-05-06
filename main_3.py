# nested_list = [
#     [1, 2, 3, [['aa', 'bb', 'cc'],
#                ['dd', 'ee', 'ff'],
#                [11, 22, 33]],
#      ['d', 'e', 'f'],
#      [1, 2, None], 4]
# ]

nested_list = [
    [['aa', 'bb', 'cc'],
     ['dd', 'ee', 'ff'],
     [11, 22, 33]],
    ['d', 'e', 'f'],
    [1, 2, None],
]

class FlatIterator:

    def flat_n(self, nested_list_):
        flat_array = []
        for nest_val in nested_list_:
            if isinstance(nest_val, list):
                flat_array += self.flat_n(nest_val)
            else:
                flat_array.append(nest_val)
        return flat_array

    def __init__(self, nested_list_):
        self.nested_list_ = nested_list_
        self.nested_list_ = self.flat_n(self.nested_list_)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        while self.n < len(self.nested_list_):
            result = self.nested_list_[self.n]
            self.n += 1
            return result
        raise StopIteration


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
