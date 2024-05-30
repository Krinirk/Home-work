my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0
while start < len(my_list):
    start += 1
    if my_list[start] > 0:
        continue       
    elif my_list[start] < 0:
        break        
print(my_list[start])
