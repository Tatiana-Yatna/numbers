age = int(input('Enter your age: '))
year = 2017
born = year - age
print('In this', year, 'year you are', age, 'years old and You was born  in ', born, 'year')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
i = 0
for born in range(born, year + 1):
    i = i + 1
    for month in months:
        print(born, 'year - ', month)
