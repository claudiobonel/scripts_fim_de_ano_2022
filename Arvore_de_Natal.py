# Árvore de Natal em Python
# Prof. Claudio Bonel
# 25/12/2022
# Faça a sua árvore de Natal tb!

n = 0 #Controle de loop
y=" " #Espaço
x="^" #Folhas da árvore

while n < 10:
    if n == 0:
        print("Árvore de Natal em Python")
    else:
        print((y*(10-n)) + ((n+(n-1))*x)) 
    n = n +1

print("Ho!Ho!Ho! Feliz Natal!")