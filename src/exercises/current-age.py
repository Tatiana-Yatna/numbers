import datetime
born = int(input('What year were you born?'))


def age(born):
    return datetime.datetime.now().year - born


print(age(born))



