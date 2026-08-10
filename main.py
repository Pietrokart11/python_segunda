# 1. Dicionário
meme_dict = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "STALKEAR": "Investigar a vida de alguém online",
    'VDD': 'Abreviação da palavra verdade',
}

# 2. Entrada do usuário
word = input("Digite uma palavra moderna que você não entende: ")

# 3. Processamento (A resposta do seu exercício)
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("A palavra não foi encontrada!")
