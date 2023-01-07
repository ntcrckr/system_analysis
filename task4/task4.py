import csv
import numpy as np


def read_csv_contents(csv_string: str) -> list[list]:
    reader = csv.reader(csv_string.split("\n"))
    csv_data = [[int(r[0]) - 1, int(r[1]) - 1] for r in list(reader)]
    return csv_data


def get_entropy(connections: list[list]) -> float:
    nodes = sorted(set(np.hstack(connections)))
    types = 5
    n_nodes = len(nodes)
    l_ji = np.zeros(shape=(types, n_nodes))
    for connection in connections:
        # Type 1
        l_ji[0, connection[0]] += 1
        # Type 2
        l_ji[1, connection[1]] += 1
        for other_connection in [c for c in connections if c != connection]:
            if connection[1] == other_connection[0]:
                # Type 3
                l_ji[2, connection[0]] += 1
                # Type 4
                l_ji[3, other_connection[1]] += 1
            elif connection[0] == other_connection[0]:
                # Type 5
                l_ji[4, connection[1]] += 1

    p_ri_mj = l_ji / (n_nodes-1)

    stacked_values = np.hstack(p_ri_mj)

    non_zeros = stacked_values[stacked_values != 0]

    values, counts = np.unique(non_zeros, return_counts=True)

    h_mr = -np.sum(values * counts * np.log2(values))

    return h_mr


def task(csv_string: str) -> float:
    csv_data = read_csv_contents(csv_string)
    entropy = get_entropy(csv_data)
    return entropy


if __name__ == "__main__":
    csv_input = "1,2\n1,3\n3,4\n3,5"

    ans = task4(csv_input)

    print(ans)
