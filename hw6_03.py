from itertools import zip_longest
import sys

with open('users.csv', 'r', encoding='utf-8') as f_names:
    names = []
    for i in f_names.readlines():
        names.append(i.replace('\n', ' ').replace(',', ' '))
    print(names)

with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
    hobbies = []
    for i in f_hobby.readlines():
        hobbies.append(i.replace('\n', ' ').replace(',', ', '))
    print(hobbies)

data = dict(zip_longest(names, hobbies))
for k, v in data.items():
    if k == None:
        sys.exit('1')
    else:
        print("Resultant dictionary is : " + str(data))



with open('list.txt', 'w', encoding='utf-8') as name_hobby:
    name_hobby.write(str(data))
