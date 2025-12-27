import logging
from dataclasses import dataclass, field


class shopping_list: 
    def __init__(self, listOfItems = None):
        #TODO: create a constructor!
        logging.info("creating the init")
        if listOfItems == None:
            listOfItems: list[list_item] = []
        self.listOfItems = listOfItems

    #create list item
    def create(self, li = None):
        if li == None: 
            li = list_item()
        self.listOfItems.append(li)

    #update list item
    def update(self, index, li):
        self.listOfItems[index] = li
    #delete list item
    def delete(self, index):
        self.listOfItems.pop(index)
    #get list item
    def getList(self,index = 0):
        return self.listOfItems[index]

    #get full list
    def getFullList(self):
        return self.listOfItems

    #savelist
    def saveList(self): 
        with open('list.txt', 'w') as f: 
            f.write(self.listOfItems)
        pass
    #openlist
    @staticmethod
    def readList():
        pass

@dataclass
class list_item:
    name: str = field(default = 'mouthwash')
