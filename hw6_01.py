with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    pars = []
    for line in data:
        word = line.split()
        clear_word = [i.replace('"', '') for i in word]
        del clear_word[1:5], clear_word[3:]
        pars.append(tuple(clear_word))
print(pars)
