# Verificando similaridade com a palavra Reveillon
# Similaridade é uma técnica de processamento de linguagem natural
# Prof. Claudio Bonel
# 27/12/2022
# Faça você também

# pip install spacy
import spacy

# acessar site https://spacy.io/models e instalar o modelo em portugês
nlp = spacy.load("pt_core_news_sm")

texto = input("Que mensagem você gostaria de receber?")
texto = nlp(texto)
texto_comparativo = nlp("reveillon")

def mensagem():
    print("Feliz 2023! Saúde, paz, amor e PLN!")

similaridade = round((texto.similarity(texto_comparativo) * 100),2)
if similaridade == 100:
    print("A palavra {} é {}% similar a palavra reveillon".format(texto.text,similaridade))
    mensagem()
elif similaridade >= 25 and similaridade < 100:
    pergunta_similidade = input("Vc digitou {}. Quer uma mensagem de reveillon? (S ou N)".format(texto.text))
    if pergunta_similidade.upper() == "S":
        print("A palavra {} é {}% similar a palavra reveillon".format(texto.text,similaridade))
        mensagem()
    else:
        print("Ok! Por favor, refaça sua solicitação.")
else:
    print("Não encontrei sua solicitação, por favor refaça.",similaridade)