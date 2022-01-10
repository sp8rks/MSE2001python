#https://www.w3schools.com/python/python_regex.asp
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())



txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


info_string = 'ADDRESS: XXX North XXX East, City: Salt Lake City, State: Utah, ZIP: 84108'
x = re.sub("ADDRESS: ", "", info_string)
x = re.sub("City: ", "", x)
x = re.sub("State: ", "", x)
x = re.sub("ZIP: ", "", x)
address = x.split(',')


print(x)












