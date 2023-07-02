numbers = [1, 2, 3]

new_list = [n+1 for n in numbers]
new_list1 = [n+1 for n in numbers]

name = 'Abhay'
letter_list = [letter for letter in name]

numbers = range(1,5)
new_range = [number*2 for number in numbers]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

long_name = [name.upper() for name in names if len(name) > 5]
