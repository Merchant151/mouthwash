from operator import itemgetter
from shopping_list import shopping_list,list_item

myList = shopping_list()

myList.create()
myList.update('str')
myList.getList()
myList.getFullList()
myList.readList()

myList.saveList()

print(myList)
print(myList.getList())
