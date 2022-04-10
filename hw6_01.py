
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        word = line.split()
        del word[1:5], word[3:]
        for item in word:
            item.replace('"', '')
            print(word)