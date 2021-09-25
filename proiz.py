products = {'Bread': ['Bread', 2.5, '$', '250gr', 25, 'шт'],
            'Sausages': ['Sausades', 5, '$', '500gr', 10, 'шт'],
            'Sugar': ['Sugar', 1.5, '$', '500gr', 5, 'шт'],
            'Vegetables': ['Vegetables', 3, '$', '1kg', 26, 'шт'],
            'Butter': ['Butter', 1, '$', '250gr', 4, 'шт'],
            }
print(products)
ch = int(input())
choose = dict()
i = 1
while i < ch:
   print(i)

   key = str(input('введите продукты'))
   value = int(input('ведите количество'))
   if key not in choose:
      choose[key] = value
      key_1 = products.keys()
      key_2 = choose.keys()
   elif
   i = i + 1
print(choose)
