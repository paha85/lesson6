import sys
import linecache

with open('bakery.csv', 'r', encoding='utf-8') as f:
    a = sys.argv[0]
    print(f.read())

    # i = int(sys.argv[1])
    # j = int(sys.argv[2])
    # f.seek(a)

    # result = f.readlines()
    # for i in result[i - 1:j]:
    #     print(i, end='')
