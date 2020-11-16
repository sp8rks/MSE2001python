def f2c (temp = 15):
    new_temp = (temp-32)*5/9
    return new_temp

t1 = 75 #23C
t2 = 50 #10C

tempC = f2c()



def try_recursion(i):
    if i>0:
        result = i + try_recursion(i-1)
        print(result)
    else:
        result = 0
    return result

try_recursion(5)


list_of_words = ['caterpillar', 'puppy', 'bat', 'monster']
list_of_words.sort(key=lambda x: len(set(list(x))))