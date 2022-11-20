import numpy as np
import json


def parse_str(s_data: str):
    levels = json.loads(s_data)
    args = sorted(
        np.hstack(levels),
        key=lambda e: int(e)
    )
    return levels, args


def construct_matrix(levels: list, args: list[str]):
    size = len(args)
    matrix = np.zeros((size, size))
    passed = []

    for level in levels:
        if passed:
            left = np.delete(args, passed)
        else:
            left = args

        if type(level) is list:
            for elem in level:
                arg = int(elem) - 1
                for idx in left:
                    matrix[arg, int(idx) - 1] = 1
                passed.append(int(elem) - 1)
        else:
            elem = level
            arg = int(elem) - 1
            for idx in left:
                matrix[arg, int(idx) - 1] = 1
            passed.append(int(elem) - 1)

    return np.matrix(matrix)


def merge_matrices(matrix_1: np.matrix, matrix_2: np.matrix):
    return np.multiply(matrix_1, matrix_2) + np.multiply(matrix_1.T, matrix_2.T)


def get_differences(matrix: np.matrix):
    diff = np.array(np.where(matrix == 0)).T
    upper_diff = np.array([d for d in diff if d[0] < d[1]]) + 1
    return upper_diff


def dumps_answer(array: np.array):
    return json.dumps([[str(elem) for elem in pair.tolist()] for pair in array])


def task(string_1: str, string_2: str):
    levels_1, args_1 = parse_str(string_1)
    levels_2, args_2 = parse_str(string_2)

    matrix_a = construct_matrix(levels_1, args_1)
    matrix_b = construct_matrix(levels_2, args_2)

    merged_matrix = merge_matrices(matrix_a, matrix_b)

    differences = get_differences(merged_matrix)

    answer = dumps_answer(differences)

    return answer


if __name__ == "__main__":
    range_A = '["1", ["2","3"],"4", ["5", "6", "7"], "8", "9", "10"]'
    # range_B = '[["1","2"], ["3","4","5"], "6", "7", "9", ["8","10"]]'
    range_B = '[["3","4"], ["1","2","5"], "7", "6", "9", ["8","10"]]'
    # range_B = '["10","9","8","7","6","5","4","3","2","1"]'
    # target_difference = '[["8","9"]]'

    ans = task(range_A, range_B)

    print(ans)
