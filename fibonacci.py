def sequencia_fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        sequencia.append(sequencia[-2] + sequencia[-1])
    return sequencia

def pertence_fibonacci(n):
    sequencia = sequencia_fibonacci(n)
    return n in sequencia

# Example usage:
numero = int(input("Digite um número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} faz parte da sequência fibonacci.")
else:
    print(f"O número {numero} não faz parte da sequência fibonacci.")

