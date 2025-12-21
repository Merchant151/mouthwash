import logging
from dataclasses import dataclass


class shopping_list: 
    def __init__(self, listofItems = None):
        #TODO: create a constructor!
        logging.info("creating the init")
        pass

    #create list item
    def create(self, li = None):
        pass
    #update list item
    def update(self, li):
        pass
    #delete list item
    def delete(self, li):
        pass
    #get list item
    def getList(self,index = 0):
        pass
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
    name = 'mouthwash'
