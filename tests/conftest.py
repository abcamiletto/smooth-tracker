import pytest

mono_signals = [
    {
        "signal": [[0, 0], [1, 1], [2, 2], [3, 3], None],
        "upper_bound": [5, 5],
        "lower_bound": [2, 2],
    },
    {
        "signal": [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],
        "upper_bound": [5, 5],
        "lower_bound": [3, 3],
    },
    {
        "signal": [[0, 0], [-1, -1], [-2, -2], [-3, -3], [-4, -4], None],
        "upper_bound": [-3, -3],
        "lower_bound": [-6, -6],
    },
    {
        "signal": [[0, 0], None, None, None, [4, 4], [5, 5]],
        "upper_bound": [6, 6],
        "lower_bound": [4, 4],
    },
    {
        "signal": [None, None, [2, 2], [3, 3], [4, 4], None],
        "upper_bound": [6, 6],
        "lower_bound": [3, 3],
    },
    {
        "signal": [[0, 0], None, [2, 2], None, None, [5, 5]],
        "upper_bound": [6, 6],
        "lower_bound": [3, 3],
    },
    {
        "signal": [[0, 0], None, [2, -2], None, [4, -4], [5, -5]],
        "upper_bound": [6, -4],
        "lower_bound": [4, -6],
    },
    {
        "signal": [[0, 1, -1], [1, 2, -2], [2, 3, -3], [3, 4, -4], [4, 5, -5]],
        "upper_bound": [5, 6, -4],
        "lower_bound": [3, 4, -6],
    },
    {"signal": [[0], [1], [2], [3], [4], [5]], "upper_bound": [6], "lower_bound": [4]},
]
