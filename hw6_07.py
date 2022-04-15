import sys
import fileinput

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    try:
        if len(sys.argv) < 2:
            print(f.read(), end='')
        elif len(sys.argv) == 2:
            i = int(sys.argv[1])
            result = f.readlines()
            print(result[i - 1], end='')
        elif len(sys.argv) == 3:
            i = int(sys.argv[1])
            j = float(sys.argv[2])
            result = f.readlines()
            if j in range(len(result)):
                for i in result[i - 1:j]:
                    print(i, end='')
            else:
                with fileinput.input('bakery.csv', inplace=True) as f1:
                    for line in f1:
                        new_line = line.replace(result[i-1], str(j)+'\n')
                        print(new_line, end='')
    except IndexError:
        print('Цена отсутствует')
