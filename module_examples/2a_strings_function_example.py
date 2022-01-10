
import re

def pythagorean(a, b):
    return((a**2+b**2)**(0.5))


a = 3
b = 4
print(pythagorean(a,b))


bikes = ['  Yamaha!', 'har##ley  ', 'HOnda', ' husqvarna?']

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

clean_bike_list = clean_strings(bikes)


#Let's compare this with an alternative method which is more generic
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

bikes = ['Yamaha!', 'har#ley', 'HOnda', 'husqvarna?']
clean_ops = [str.strip,remove_punctuation,str.title]


def clean_strings2(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

clean_bike_list = clean_strings2(bikes,clean_ops)

