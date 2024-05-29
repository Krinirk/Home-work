my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('Список: ', my_list)
start = 0
while start < len(my_list):
    number = int(input())
    start += 1
    if number == my_list[start] > 0:
        continue
    # elif number == my_list[1] > 0:
    #     continue
    # elif number == my_list[2] > 0:
    #     continue
    # elif number == my_list[3] > 0:
    #     continue
    else:
        if number != my_list[start]:
        break
        
    # elif number > my_list[0] > 0:
    #     print(my_list[0])
    # elif number > my_list[0] > 0:
    #     print(my_list[0])
    # elif number > my_list[0] > 0:
    #     print(my_list[0])
