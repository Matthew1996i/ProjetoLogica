# Codigo login dos funcionarios

usuarios = ('test','test01')


print('='*100)
print(' '*40,'BEM VINDO A FSOCIETY')
print('='*100)
print('')

while True:
    user = str(input('Digite o nome de Usuario: '))
    password = str(input('Digite a senha: '))
    print(' ')
    if user != usuarios[0] and password != usuarios[1]:
        print("***USUARIO OU SENHA INVALIDO***")
        print('')
    elif user == usuarios[0] and password == usuarios[1]:
        print("***ACESSO PERMITIDO***\n")
        break
        
print('Digite uma opção: \n')
print('1 - Funcionarios')
print('2 - Setores')
print('3 - Renda do Mês\n')

choice = int(input())

if choice == 1:
    funcionarios = ['Weslley', 'Thiago', 'Matheus', 'Karol', 'Bruno', 'Dykson']
    for index, i in enumerate(funcionarios):
        print(f'{index+1}) {i}')
