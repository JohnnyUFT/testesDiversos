print("Informe a velocidade do carro")
v = int(input()) #necessário fazer a conversãopara inteiros
if(v >= 110):
    print('acima da velocidade permitida! MULTA:', (v-110)*5, 'reais') #cuidado com a precedência dos operadores
else:
    print('dentro dos limites permitidos')
