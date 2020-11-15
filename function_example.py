first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

def name_joiner(a, b):
    name = a+b
    return(name)

dict1 = {}
dict1['Name'] = name_joiner(first_name, last_name)
