nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(nested_list_):
    for value in nested_list_:
        if isinstance(value, list):
            for nested_value in value:
                yield nested_value


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)
