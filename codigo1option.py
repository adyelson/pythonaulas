print("Choose an option")
print("Add Item [1]")
print("Buy Item [2]")
print("Exit     [3]")

option = input("Option: ")

while option != 99:
    def option99():
        global option
        option = input("Option: ")   
   
    def option1():
        global Names, n_names
        Names = [] + []
        n_names = int(input("Insert quantity of items: "))
        for i in range(n_names):
            print("Item["+str(i)+"]-------------")
            Names = Names + [[input("Name: ")]+ [input("Value: ")]]
            with open('item.txt','w') as arquivo:
                for item in Names:
                    arquivo.write(str(item) + '\n')
        options.get(99)()
    def option2():
        print("choose wich and how many of thoose items: ")

        for i in range(n_names):
                print("Item["+str(i)+"]: " + str(Names[i][0]) + " $ " + str(Names[i][1]))
        
        n_item= int(input("Item: "))
        amount= int(input("Amount: "))

        print("You must pay " +str(int(Names[n_item][1])*amount)+" $ to buy "+str(amount)+" amount of "+ str(Names[n_item][0]))
        options.get(99)()
    def option3():        
        print("Have a nice Day")
        options.get(99)()
        return()
    options = { 1:option1, 2:option2, 3:option3, 99:option99}

    options.get(int(option))()