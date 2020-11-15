x = {'cat', 'dog', 'fish','fish'}
empty_set = set()

y = [1, 2, 3, 4, 2, 3, 5, 6]
y = set(y)

x.add('zebra')
x.discard('horse')

z = [1, 2, 3, 4, 2, 3, 5, 6]
frozenset(z)


new_tuple = (1, 2, 3, 4, 5)


a = 5
b = 6

tmp = a
a = b
b = tmp


#use tuples instead!
a, b = (1, 2)
a, b =  b, a

Fellowship = (['Pippin', 'Merry', 'Frodo', 'Samwise'],
              ['Aragorn', 'Gandalf','Boromir'],'Gimli', 'Legolas')

Hobbits, Humans, Dwarves, Elves = Fellowship