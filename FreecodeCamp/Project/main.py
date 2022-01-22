from Item import Item

item1 = Item("Phone", 100, 2)
print(item1.calculate_total_price())

Item.instantiate_from_csv()
print(Item.all)