with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    pars = []
    for line in data:
        word = line.split()
        del word[1:5], word[3:]
        pars.append(tuple(word))
print(pars)
