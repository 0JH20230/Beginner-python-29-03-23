items = ["kettle", "fork", "spoon", "oven", "microwave"]         #below this list is the index number to access the individual elements of the list
    #       0        1       2         3         4
    #      -5        -4      -3        -2        -1
items[4] = "cupboard"                                            #by selecting the item in the array using [] you can update the value
print(items[3])                                                  #Using the print statement and [] the console will display the value
print(items[-2])                                                 #You can select the index based of the back of the list as shown in line 3
print(items[:2])                                                 #By placing a colon before the index number you get all of the element before the index number and not including the one chosen
print(items[2:])                                                 #By placing a colon after the index number you select all after and including the one stated
print(items[1:4])                                                #By placing a colon between 2 indexes you get a range of elements apart from the 2nd Stated index
print(items[-3:-1])
