import shopping_list

Welcome = 'Welcome to Mouthwash, please enter in the items you are accustomed to getting weekly.' 
WelcomeBack = 'Welcome back to Mouthwash, your current list is ' + 'userlist'
ToAdd = 'To add an item select + and type in each item you like and press enter.\nWhen you are done simply press @'
ToRemove = 'To remove press - select the number of the item on the list you would like to remove, if several items seperate with coma.'
ToAlter = 'To alter just type * and the number of the item you would like to edit.'
Options = 'Please take a look at our menu options' + ' ' + ToAdd + ' ' + ToRemove + ' ' + ToAlter 
YouAdded = 'You added ' + 'listItemfuction' + ' to list'
YouRemoved = 'You removed ' + 'listItemfuction' + ' from your list'
PresentList = 'Here is your list'



if list == None:
  myList.create('My Shopping List')
  print(Welcome)
  print(ToAdd)
  if list != None:
    println(WelcomeBack)
    println(Options)

def readCommand():
    print(Welcome)
    print(ToAdd)
    user_in = input()
    match user_in: 
        case "+":
            global Shoplist
            Shoplist = []
            userinput = input()
            while userinput != '@':
              Shoplist.append(userinput)
              print('You added, ' + userinput + ' to your list.')
              userinput = input()
            print(PresentList)
            print(Shoplist)
        case "$":
            print('This is your current list' + str(Shoplist))
            print(Options)
        case "exit":
          exit()
        case _: 
            print('I do not recoginze this command')

while(True):
  readCommand()
