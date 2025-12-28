from operator import itemgetter
from shopping_list import shopping_list,list_item

def all_funcs():
    myList = shopping_list()

    myList.create()
    nextItem = list_item('bar')
    myList.create(nextItem)
    shopping_list.readList()


    print(myList)
    print(myList.getList())
    print(myList.getFullList())
    nextItem = list_item('eggs')
    myList.update(0,nextItem)
    print(myList.getList(0))
    print(myList.getFullList())
    myList.saveList()
    myList.delete(0)
    print(myList.getFullList())

def save_tester():
    print('save test:')
    save_list = shopping_list()
    #create 10 items
    for i in range(10):
        item = list_item(f'itemNumber{i}',i)
        save_list.create(item)
    
    print(save_list.getFullList())
    saved = save_list.getFullList()
    print('saving!')
    save_list.saveList()
    
    print('loading!')
    load_list = shopping_list(shopping_list.readList())
    loaded = load_list.getFullList()
    print(load_list.getFullList())

    if(saved == loaded):
        print('save and load successful')
    else: 
        print('save and load failed!')
    

    


##test all funcs
#all_funcs()

##test
save_tester()
