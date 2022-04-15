import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    try:
        if len(sys.argv) < 2:
            print(f.read(), end='')
        elif len(sys.argv) == 2:
            i = int(sys.argv[1])
            result = f.readlines()
            print(result[i - 1], end='')
        elif len(sys.argv) == 3:
            i = int(sys.argv[1])
            j = int(sys.argv[2])
            result = f.readlines()
            for i in result[i - 1:j]:
                print(i, end='')
    except IndexError:
        print('Цена отсутствует')
