from Vectors import Vector


def read_vector(raw_vec: str) -> Vector:
    output = []

    for crd in raw_vec.split():
        if crd != ' ':
            output.append(int(crd))

    return Vector(output)


def read_file(file: str) -> list:
    list_of_vec = []

    with open(file) as file:
        raw_list_of_vec = file.readlines()

        for raw_vec in raw_list_of_vec:
            vec = read_vector(raw_vec)
            list_of_vec.append(vec)

    return list_of_vec


def largest_dim(list_of_vec: list):
    list_of_dim = []

    for vec in list_of_vec:
        list_of_dim.append(vec.dimension())

    copy = list_of_dim.copy()
    copy.sort()

    max_dim = copy[-1]

    if list_of_dim.count(max_dim) == 1:
        return list_of_vec[list_of_dim.index(max_dim)]

    else:
        min_len = []

        index = 0

        for val in list_of_dim:
            if val == max_dim:
                min_len.append(list_of_vec[index].length())

            index += 1

        return min(min_len)


def longest_vect(list_of_vec: list):
    list_of_lengths = []

    for vec in list_of_vec:
        list_of_lengths.append(vec.length())

    copy = list_of_lengths.copy()
    copy.sort()

    max_val = copy[-1]

    if list_of_lengths.count(max_val) == 1:
        return list_of_vec[list_of_lengths.index(max_val)]

    else:
        dim = []

        index = 0

        for val in list_of_lengths:
            if val == max_val:
                dim.append(list_of_vec[index].dimension())

            index += 1

        return min(dim)


def average_len(list_of_vec: list):
    list_of_lengths = []

    for vec in list_of_vec:
        list_of_lengths.append(vec.length())

    return sum(list_of_lengths) / len(list_of_lengths)


def count_above_av_len(list_of_vec: list):
    counter = 0
    av_val = average_len(list_of_vec)

    for vec in list_of_vec:
        if vec > av_val:
            counter += 1

    return counter


def find_largest_component(list_of_vec: list):
    list_of_max_comp = []

    for vec in list_of_vec:
        list_of_max_comp.append(vec.max())

    max_val = max(list_of_max_comp)

    if list_of_max_comp.count(max_val) == 1:
        return max_val

    else:
        indexes = []
        ind = 0
        min_min = []

        for val in list_of_max_comp:
            if val == max_val:
                indexes.append(ind)

            indexes += 1

        for i in indexes:
            min_min.append(list_of_vec[i].min())

        return list_of_vec[indexes[min_min.index(min(min_min))]]




