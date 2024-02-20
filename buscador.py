# O intuito deste código é para realizar a busca de um item em uma lista e informar se o mesmo esta presente ou não. 

corCliente = input('Informe a cor desejada: ')

corEstoque = ['azul', 'amarelo', 'verde', 'roxo', 'cinza']

if corCliente.lower() in corEstoque:
    print('A cor esta disponível no estoque.')
else: 
    print('A cor não esta disponível no estoque.')