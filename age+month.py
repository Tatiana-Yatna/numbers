age = int(input('Enter your age: '))
year = 2017
born = year - age
print('In this', year, 'year you are', age, 'years old')
#print('You was born in ', born)
all = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
i = 0
for born in range(born + 1, year):
    i = i + 1
    print('In', born, 'you was', i, 'years old and you lived month')
    for month in all:
        print(month)
