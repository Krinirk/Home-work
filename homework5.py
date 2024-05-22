immutable_var = (1,2,'Hello!',True,2.5)
print(immutable_var)
#immutable_var[1] = 5
#print(immutable_var)
# При выводе на экран программа выдает ошибку, потому что кортеж является неизменяемым объектом.
mutable_list = [8,10.3,'carrot',False]
print(mutable_list)
mutable_list[2] = 'арбуз', True #возможно ли в одной строке кода изменить за раз два элемента списка (не срез, а два отдельных на два новых) или необходимо менять по одному элементу в новой строке кода?
print(mutable_list)
