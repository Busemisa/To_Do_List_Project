tasks=[]

def add(task): #We want the value we want to add to the list
    tasks.append(task)
    print("added to the list")

def remove(task_index):  #We get the value you want to delete from the list
    value_of_remove=tasks.pop(task_index-1)  #Since the indexes start from 0, we decreased by one.
    print("{} value subtracted".format(value_of_remove))

def list():  #We are viewing the current list
    print("values in your list :{}  ".format(tasks))


while True:  #We choose our choice thanks to the endless loop
    print("1) add\n2) remove\n3) list\n4) exit\n\n ")
    select=int(input("select the number you want to select:"))


    if select==1:
        new_task=input("\nEnter the value to be added to the list : ")
        add(new_task)



    elif select==2:
        list()
        remove_task=int(input("\nenter the value you want to delete : "))
        remove(remove_task)
        list()



    elif select==3:
        list()

    elif select==4:
        print("EXIT")
        break

    else:
        print("\nplease enter a valid number")






