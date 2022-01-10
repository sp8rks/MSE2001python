
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
