class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        spisok = open(self.__file_name, 'r')
        p = spisok.read()
        spisok.close()
        return p

    def add(self, *products):
        for p in products:
            if p.name not in self.get_products():
                spisok = open(self.__file_name, 'a')
                spisok.write(p.__str__() + '\n')
                spisok.close()
            else:
                print(f'Продукт {p.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
