# O intuito deste código é para realizar a busca de um item em uma lista e informar se o mesmo esta presente ou não. 

corEstoque = ['azul', 'amarelo', 'verde', 'roxo', 'cinza']

def loop():
    global continuar # Reconhece a variavel continuar que esta fora da função

    resultadoLoop = input('\nDeseja pesquisar mais outra cor? Y/N \n')

    if resultadoLoop.lower() == 'y' or resultadoLoop.lower() == 'yes':
        continuar = True
    else: 
        continuar = False


continuar = True

while continuar is True:
    corCliente = input('Informe a cor desejada: ')

    if corCliente.lower() in corEstoque:
        print('\nA cor esta disponível no estoque.')

    else: 
        print('\nA cor não esta disponível no estoque.')
    
    loop()