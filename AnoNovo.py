# Feliz ano novo
# Prof. Claudio Bonel
# 01/01/2023
# Faça a sua mensagem de ano novo em Python também!

n=0 #Controle de loop
i=0 #Controle das mensagens
t=15 #Tamanho da árvore
y=" " #Espaço
x="#" #Folhas da árvore
msg=["PAZ","SAÚDE","AMOR","PROSPERIDADE","CIÊNCIA","DADOS"] #lista das mensagens

while n < t:
    if n == 0:
        print((y*9) + " Feliz 2023\n               *")
    elif (n%2) == 0 or n == 1:
        print((y*(t-n))+ "*"+((n+(n-1))*x +"*")) 
    elif ((n%2) != 0):
        k = len(msg[i])
        if (i%2) == 0:
            print((y*(t+(n-k))) + msg[i])
        else:
            print((y*(t-n)) + msg[i] + ((n+(n-k-1))*y)) 
        i=i+1

    n = n +1
print("   Desejo um 2023 com muita \n      CIÊNCIA DE DADOS!")