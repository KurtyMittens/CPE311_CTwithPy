# list of the items in the Warehouse
items = ["set-n-forget cooker", "electric water boiler", "energy regulator-1", "turkey fryer", "microwave oven",
         "thermal immersion circulator", "panini sandwich grill", "washing machine", "thermal mass refrigerator", "sous-vide cooker",
         "energy generator-2", "air conditioner","internet refrigerator","beverage opener","home server",
         "flattop grill", "icebox","halogen oven","sewing machine","embroidery machine"
         "pneumatic vacuum", "aroma lamp", "coffee percolator","convection microwave","food steamer"]

aisle = [1, 1, 1, 1, 1,
         2, 2, 2, 2, 2,
         3, 3, 3, 3, 3,
         4, 4, 4, 4, 4,
         5, 5, 5, 5, 5
         ]

price = [2949, 4590, 564, 4791, 4390,
         3656, 3564, 2584, 1686, 2958,
         4129, 2389, 2361, 3812, 4148,
         2923, 1128, 1402, 2844, 2780,
         1996, 1617, 2738, 2506, 3228
         ]

weight = [1458, 1302, 598, 973, 616,
          715, 1241, 1408, 1313, 751,
          646, 957, 1193, 1002, 934,
          1585, 739, 1452, 973, 1973,
          1223, 155, 950, 1470, 1841
          ]


truck_capacity = 20000 # for the capacity of the truck
fl_capacity = 2000 # The capacity of the forklift


class Items:
  def __init__(self, name, aisle, price, weight):
    self.__name = name
    self.__aisle = aisle
    self.__price = price
    self.__weight = weight

  def get_name(self):
    return self.__name
  
  def get_aisle(self):
    return self.__aisle
  
  def get_price(self):
    return self.__price
  
  def get_weight(self):
    return self.__weight


def menu_of_items(arrOfNames, arrOfAisle,arrOfPrice,arrOfWeight):
  items = []
  for i in range(len(arrOfNames)):
    items.append(Items(arrOfNames[i], arrOfAisle[i], arrOfPrice[i], arrOfWeight[i]))
  return items


def tab_knapsack(cap,items):
  n = len(items)
  table = [[0 for i in range(cap+1)] for i in range(n+1)]
  for i in range(n+1):
    for j in range(cap+1):
      if i == 0 or j == 0:
        table[i][j] = 0
      elif items[i-1].get_weight() <= j:
        table[i][j] = max(items[i-1].get_price() + table[i-1][j - items[i-1].get_weight()], table[i-1][j])
  print(table[i][j])
  
  k = n
  l = cap
  while k > 0 and l > 0:
    if table[k][l] == table[k-1][l]:
      items.remove(items[k-1])
      k-=1
    else:
      k-=1
      l-=items[k].get_weight()

  items.sort(key=lambda x: x.get_aisle())
  for i in items:
    print(f"{i.get_name()} will be picked @ aisle {i.get_aisle()}")
  return items


#To test:
item_menu = menu_of_items(items, aisle, price, weight)
tab_knapsack(truck_capacity, item_menu)