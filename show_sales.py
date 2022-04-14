import sys
import linecache

with open('bakery.csv', 'r', encoding='utf-8') as f:
    i = sys.argv[1]
    # j = sys.argv[2]
    f.seek(int(i))
    # print(linecache.getline('bakery.csv', int(i)))
    print(f.readline())
