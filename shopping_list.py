import logging
from operator import attrgetter
from dataclasses import dataclass, field, asdict


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
            for i in range(len(self.listOfItems)):
                itemStr = shopping_list.itemToStr(self.listOfItems[i])
                f.write(itemStr+"\n")

    def itemToStr(item): 
        #ussing a method here incase I need to change how this works
        return str(asdict(item))
    #openlist
    @staticmethod
    def readList():
        outputList = []
        with open('list.txt') as f:
            for line in f: 
                #outItem = list_item()
                line = line.strip()
                line = line.replace('{',"")
                line = line.replace('}',"")
                line = line.replace("'","")
                line = line.replace(" ","")
                attrs = line.split(',')
                for i in attrs:
                    key, value = i.split(':')
                    #setattr(outItem,key,value)
                    #settme = attrgetter(key)
                    #x = settme(outItem)
                    #x = value
                    print(value ,end=' <-')
                    print(key)
                    name = None
                    interval = None
                    match key:
                        case 'name':
                            name = key
                        case 'interval':
                            interval = value
                        case _:
                            raise Exception(f"ERROR READING FILE PLS FIX! AT KEY:{key}|value:{value}")
                outItem = list_item(name,interval)
                outputList.append(outItem)
        return outputList

@dataclass
class list_item:
    name: str = field(default = 'mouthwash')
    interval: int = field(default = 1)
