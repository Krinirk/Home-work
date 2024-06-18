from true_math import divide as tm
from fake_math import divide as fm

result1 = fm(69, 3)
result2 = fm(3, 0)
result3 = tm(49, 7)
result4 = tm(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)


# функция из true_math:
# from math import inf
# def divide(first, second):
#     if second == 0:
#         return inf
#     else:
#         x = first / second
#         return x
# ________________
# функция из fake_math:
# def divide(first, second):
#     if second == 0:
#         x = 'Ошибка'
#         return x
#     else:
#         x = first / second
#         return x
