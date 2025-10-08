n = int(input("diga numero"))
def faça_numeros(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
faça_numeros(n)