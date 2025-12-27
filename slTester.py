from operator import itemgetter
from shopping_list import shopping_list,list_item

myList = shopping_list()

myList.create()
nextItem = list_item('bar')
myList.create(nextItem)
shopping_list.readList()

myList.saveList()

print(myList)
print(myList.getList())
print(myList.getFullList())
nextItem = list_item('eggs')
myList.update(0,nextItem)
print(myList.getList(0))
print(myList.getFullList())
myList.delete(0)
print(myList.getFullList())
