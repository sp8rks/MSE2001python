# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:03:36 2020

@author: taylo
"""
fellowship = ["Frodo", "Gandalf", "Samwise", "Merry", "Pippin"
              , "Legolas", "Aragorn", "Gimli", "Boromir"]

fellowship.insert(2,"Golem")
#fellowship.remove("Boromir")
#fellowship.remove("Boromir")
#fellowship.pop(8)
fellowship.append(100)

len(fellowship)

grocery_list1 = ["apples", "bananas"]
grocery_list2 = ["donuts", "hot chocolate"]
new_list = grocery_list2+grocery_list1
new_list.clear()

fellowship.reverse()
copy_of_list1 = grocery_list1.copy()
grocery_list1.pop(1)


