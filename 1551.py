N = int(input())

for _ in range(N):
    letras = []
    frase = input()
    for letra in frase:
        if letra not in letras:
            letra.append(letras)
        