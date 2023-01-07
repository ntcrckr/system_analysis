import json
import numpy as np
import pandas as pd


def read_csv_from_file(csv_file_name: str) -> pd.DataFrame:
    _df = pd.read_csv(csv_file_name, header=None)
    return _df


def read_csv_from_string(csv_string: str) -> pd.DataFrame:
    _df = pd.DataFrame([row.split(',') for row in csv_string.split('\n')])
    return _df


def get_comparisons(df: pd.DataFrame) -> list:
    _comp_matrices = []
    for _, expert in df.iterrows():
        _row = expert.to_numpy()
        _mat = np.matrix([
            [
                1 if x > y else 0.5 if x == y else 0
                for x in _row
            ]
            for y in _row
        ])
        _comp_matrices.append(_mat)
    return _comp_matrices


def get_combined_comparison(comp_matrices: list) -> np.matrix:
    _comb_matrix = sum(comp_matrices) / len(comp_matrices)
    return _comb_matrix


def get_valued_coefficients(comb_matrix: np.matrix) -> np.matrix:
    _x = comb_matrix
    _l = comb_matrix.shape[0]
    _k = np.matrix([1/_l] * _l).T
    _e = 0.001
    _o = np.matrix([1, 1, 1])

    while True:
        _y = np.dot(_x, _k)
        _la = np.dot(_o, _y)
        _k_new = np.dot(1/_la, _y.T).T
        if np.max(np.abs(_k_new - _k)) < _e:
            break
        _k = _k_new

    _valued_coefficients = np.round(_k_new, int(-np.log10(_e)))
    return _valued_coefficients


def answer_to_json(valued_coefficients: np.matrix) -> str:
    _json_ans = json.dumps(valued_coefficients.T.tolist()[0])
    return _json_ans


def task(csv_string: str):
    df = read_csv_from_string(csv_string)
    comp_matrices = get_comparisons(df)
    comb_matrix = get_combined_comparison(comp_matrices)
    valued_coefficients = get_valued_coefficients(comb_matrix)
    json_ans = answer_to_json(valued_coefficients)
    return json_ans


if __name__ == '__main__':
    # read_csv_from_file("input.csv")
    print(task("1,3,2\n2,2,2\n1.5,3,1.5"))

