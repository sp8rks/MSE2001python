x = 6

if x<5:
    print('x is 5')
    x_squared = x**2
    print(f'x squared is {x_squared:.3f}')
elif x < 4:
    print('second test')
elif x == 3:
    print('x is 3')
elif x>=5 and x<=10:
    print('less than 10, more than 5')
else:
    print('nope')



if x != 5:
    print('x is not 5')


if not x==5:
    print('x is not 5')
# %%
#build duct tape wd40 flowchart

affirmatives = ['yes','Yes','ya', 'Ya', 'yup']
does_it_move = input('Does it move? ')
if does_it_move['actual'] == 'yes' :
    should_it_move = input('Should it move (Y/N)? ')
    if should_it_move in affirmatives:
        print('no problem')
    elif should_it_move == 'no':
        print('use duct tape')
else:
    should_it_move = input('Should it move? ')
    if should_it_move == 'yes':
        print('use wd40')
    elif should_it_move == 'no':
        print('no problem')




