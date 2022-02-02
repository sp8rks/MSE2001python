
for x in range(0, 10, 5):
    print("We're on time ", x)


bands = ["Jimmy Eat World", "Pearl Jam", "Shakey Graves",
         "Ozma", "David Bowie", "Dispatch"]

# for num, rad_bands in enumerate(bands, start=1):
#     if rad_bands == "Shakey Graves":
#         continue
#     print(rad_bands, "is band number", num)
# else:
#     print('there is no other good music')


for num, rad_bands in enumerate(bands, start=1):
    for letter in rad_bands:
        print(letter,'\n')
    print(rad_bands, "is band number", num)
else:
    print('there is no other good music')

band_with_i = [x for x in bands if "i" in x]

elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O']
element_dict = {x: num+1 for num, x in enumerate(elements)}

liar = True
while liar ==True:
    age = int(input("What\'s your age?"))
    if age > 0:
        liar = False

# %%
name_list = [['kai','hardmin'],['jeremy','baird'],['Halli','Thompson']]

for x in range(0,10):  only works if we know length ahead of time

 for x in range(0,len(name_list)):
     print(name_list[x])


for x in name_list:
    #print(x)
    #print(x[0])
    #print(x[1])
    for y in x:
        
        if y == 'jeremy':
            break
        print(y)





for i,x in enumerate(name_list):
    print(i)
    print(x)

#try it for a dictionary
name_dict = {"formula": "ABO3",'color':'grey'}
for i,x in enumerate(name_dict):
    print(i)
    print(x)

newlist = [x for x in name_list if "kai" in x]
dict_variable = {key:value for (key,value) in name_dict.items()}


while(x!=5):
    x=input('type a number:')
