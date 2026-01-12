textkey = ['Hi welcome to mouthwash'
,"Enter a command or press help"
,"type add to add an item to your list, remove to remove an item, and change to swap an item with another."                                
           
]



def add():
    print("You added an item")
    pass

def remove():
    print('You removed an item')
    pass

def change():
    print('You swapped this item for this one.')
    pass

def help():
    print(textkey[2])
    pass
def printlist():
   print('Printing your list')
   pass

def main():
  print(textkey[0])
  #print list

  while(True):
    #print actions
    print(textkey[1])
    #recod user
    user_in= input()
    match user_in:
     case "add":
        add()
        pass
     case "remove":
        remove()
        pass
     case "change":
        change()
        pass
     case "help":
        help()
        pass
     case 'print list':
          printlist()
     case "exit":
        print('exiting mouth wash')
        exit()
     case _:
      print(textkey[2])
      
    

if __name__ == "__main__":
  main()