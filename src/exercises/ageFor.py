age = int(input('Enter your age: '))
year = 2017
born = year - age
print('In this', year, 'year you are', age, 'years old')
for year in range(year - 1, born, -1):
    age = age - 1
    print('In', year, 'you was', age, 'years old')
print('You was born in ', born)