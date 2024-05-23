my_dict={'John':1985, 'Elizabeth':1988,'James':1991,'William':1982,'Kate':1995}
print('Словарь: ',my_dict)
print('Присутствует: ', my_dict['James'])
print('Отсутствует: ', my_dict.get('Ivan'))
my_dict.update({'Julia':1984,
               'Din':1992})
a=my_dict.pop('Din')
print('Удаленное: ',a)
print('Измененный словарь: ',my_dict)
print()
my_set={2,2,'c','c',3.5,3.5}
print('Множество: ',my_set)
my_set.add(85)
my_set.add('string')
my_set.discard(2)
print('Измененное множество:',my_set)
