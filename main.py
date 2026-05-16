# main.py
# significasdos das siglas modernas
meme_dict = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "STALKEAR": "Investigar a vida de alguém online",
    "VDD": "abreviação da palavra verdade",
    "BISCOITAR": "Postar algo apenas para chamar a atenção",
    "HATER": "Pessoa que está constantemente criticando os outros",
    "VLW": "Abreviação da palavra valeu",
    "67": "meme muito ultilizado pelos jovens",
    "SLA": "Abreviação da palavra sei la",
    "PSE": "Abreviação da palavra pois e",
    "NRML": "Abreviação da palavra na moral,quando se trata de algo serio,sem zueira"
}

for i in range(5):
    word = input("Digite abaixo,uma palavra moderna que você não entende (escreva todas as palavra em letras maiúsculas,para obter o funcinamento correto do sistema): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("infelizmente,sua palavra nao foi encontrada,tente outra")
