from Vector import Vector


files_list = ["input01.txt", "input02.txt", "input03.txt", "input04.txt"]


def read_file(file: str) -> list:
    with open(file) as file:
        raw_args_list = file.readlines()
        args_list = []
        vectors_list = []

        for raw_args in raw_args_list:
            args = list(map(float, raw_args.split()))
            args_list.append(args)

        for args in args_list:
            if len(args) > 0:
                vectors_list.append(Vector(*args))

        return vectors_list


def list_max_dimension(vectors_list: list) -> (int, float):
    pass


def list_max_length(vectors_list: list) -> (int, float):
    pass


def list_max_component(vectors_list: list) -> (int, float):
    pass


def list_min_component(vectors_list: list) -> (int, float):
    pass


if __name__ == "__main__":
    list_of_vectors = read_file('input01.txt')

    for vector in list_of_vectors:
        print(vector)



