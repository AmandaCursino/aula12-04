cadastro = {}
while True:
    nome = input('Digite o nome completo: ')
    if nome == '':
        break
    idade = int(input('Digite a idade: '))
    cidade = input('Digite a cidade: ')
    
    #adiciona os dados ao dicionario
    cadastro[nome] = {'idade': idade, 'cidade': cidade}
    
#imprima o cadastro completo
print('Cadastro')
print(cadastro)
for nome, dados in cadastro.items():
    print('- nome', nome)
    print('- idade', dados['idade'])
    print('- cidade', dados['cidade'])
    