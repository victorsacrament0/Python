matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

soma = (matriz[0])+(matriz[1])+(matriz[2])
print('\nA soma dos elementos é de: {}'.format(soma)) 
print('_' * 60, '\n')

diagonal = [matriz[i][i] for i in range(len(matriz))]

print("Matriz:")
for linha in matriz:
    print(linha)

print('_' * 60, '\n')
print("\nDiagonal principal:", diagonal,'\n')