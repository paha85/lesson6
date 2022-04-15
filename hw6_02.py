from collections import Counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    pars = []
    for line in data:
        word = line.split()
        del word[1:5], word[1:]
        pars.append(word)

pars_one = [j for i in pars for j in i]
result = Counter(pars_one).most_common(1)

print(f'IP адрес {result[0][0]} обращался {result[0][1]} раз')
