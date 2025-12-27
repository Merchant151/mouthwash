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
    def update(self, li):
        pass
    #delete list item
    def delete(self, li):
        pass
    #get list item
    def getList(self,index = 0):
        return self.listOfItems[index]

    #get full list
    def getFullList(self):
        pass
    #savelist
    def saveList(self): 
        pass
    #openlist
    def readList(self):
        pass

@dataclass
class list_item:
    name: str = field(default = 'mouthwash')
