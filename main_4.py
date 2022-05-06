nested_list = [
    [['aa', 'bb', 'cc'],
     ['dd', 'ee', 'ff'],
     [11, 22, 33]],
    ['d', 'e', 'f'],
    [1, 2, None],
]

#
# nested_list = [
#     [1, 2, 3, [['aa', 'bb', 'cc'],
#                ['dd', 'ee', 'ff'],
#                [11, 22, 33]],
#      ['d', 'e', 'f'],
#      [1, 2, None], 4]
# ]


def flat(nested_lst):
    flat_array = []
    for nest_value in nested_lst:
        if isinstance(nest_value, list):
            flat_array += flat(nest_value)
        else:
            flat_array.append(nest_value)
    return flat_array


def flat_generator(nested_list_):
    for value in nested_list_:
        if isinstance(nested_list_, list):
            for flat_val in flat(value):
                yield flat_val


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)
