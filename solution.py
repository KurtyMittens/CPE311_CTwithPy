# list of the items in the Warehouse
items = ["set-n-forget cooker", "washing machine", "thermal mass refrigerator", "sous-vide cooker", "electric water boiler",
          "energy regulator", "thermal immersion circulator","air conditioner", "energy regulator", "internet refrigerator",
          "clothes dryer", "turkey fryer", "beverage opener", "home server", "vacuum cleaner",
          "humidifier", "panini sandwich grill","flattop grill","microwave oven","icebox"]

aisle = [1,3,5,3,1,
         4,2,6,1,6,
         2,1,6,4,5,
         4,2,4,1,3,]

price = [2949,2584,1686,2958,4590,
         4129,3656,2389,564,2361,
         2671,4791,3812,4148,864,
         2690,3564,1545,4390,2405]

weight = [1458,1408,1313,751,1302,
          646,715,957,598,1193,
          1079,973,1002,934,1346,
          792,1241,1352,616,1275]
capacity = 10000 # for the capacity of the truck

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
  aisles = []
  for i in items:
    print(f"{i.get_name()}, is in aisle {i.get_aisle()}, {i.get_weight()}")
    aisles.append(i.get_aisle())
  return list(set(aisles))



#To test:
item_menu = menu_of_items(items, aisle, price, weight)
print(tab_knapsack(capacity, item_menu))