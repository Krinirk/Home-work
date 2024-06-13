data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    summ = 0
    if isinstance(data_structure, list):
        for i in data_structure:
            summ += calculate_structure_sum(i)
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summ += calculate_structure_sum(key)
            summ += calculate_structure_sum(value)
    if isinstance(data_structure, int):
        summ += data_structure
    if isinstance(data_structure, str):
        summ += len(data_structure)
    if isinstance(data_structure, tuple):
        for k in data_structure:
            summ += calculate_structure_sum(k)
    if isinstance(data_structure, set):
        for m in data_structure:
            summ += calculate_structure_sum(m)
    return summ


result = calculate_structure_sum(data_structure)
print(result)
