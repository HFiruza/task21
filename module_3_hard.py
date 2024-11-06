data_structure = ([1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}]))

def calculate_structure_sum(data_structure):
    total_sum = 0
    total_length = 0
    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum_, length_ = calculate_structure_sum(item)
            total_sum += sum_
            total_length += length_
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_key, length_key = calculate_structure_sum(key)
            sum_value, length_value = calculate_structure_sum(value)
            total_sum += sum_key + sum_value
            total_length += length_key + length_value
    elif isinstance(data_structure, str):
        total_length += len(data_structure)
    elif isinstance(data_structure, int):
        total_sum += data_structure
    return total_sum, total_length

result = calculate_structure_sum(data_structure)
print(result)

# def count_sum_and_lengths(data):
#     total_sum = 0
#     total_length = 0
#     if isinstance(data, (list, tuple, set)):
#         for item in data:
#             sum_, length_ = count_sum_and_lengths(item)
#             total_sum += sum_
#             total_length += length_
#     elif isinstance(data, dict):
#         for key, value in data.items():
#             sum_key, length_key = count_sum_and_lengths(key)
#             sum_value, length_value = count_sum_and_lengths(value)
#             total_sum += sum_key + sum_value
#             total_length += length_key + length_value
#     elif isinstance(data, str):
#         total_length += len(data)
#     elif isinstance(data, int):
#         total_sum += data
#     return total_sum, total_length
# print(count_sum_and_lengths(data))

