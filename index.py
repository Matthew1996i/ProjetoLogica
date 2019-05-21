######## Programa de controle de logins dos Funcionarios ####################
import time
import getpass
usuarios = ('admin','admin')


print('='*100)
print(' '*40,'BEM VINDO A FSOCIETY')
print('='*100)
print('')

while True:

################################### CODIGO DE LOGIN DO USUARIO, COM VALIDAÇÃO ##################################

    user = str(input('Digite o nome de Usuario: '))
    password = getpass.getpass('Digite a Senha: ')
    print(' ')
    if user != usuarios[0] or password != usuarios[1]:
        print('\033[31m'+"***USUARIO OU SENHA INVALIDO***"+'\033[0;0m')
        print('')
    elif user == usuarios[0] and password == usuarios[1]:
        print('\033[32m'+"***ACESSO PERMITIDO***"+'\033[0;0m')
        print('')
        break
################################### DEPOIS, DARÁ AS OPÇOES DE ESCOLHAS PARA O USER ##################################
print('Digite uma opção: \n')
print('1 - Funcionarios')
print('2 - Cargos')
print('3 - Renda do Mensais')
print('4 - Salarios e Comissões')
print('')

################################### IRÁ CAIR NUM LOOP PARA AS ESCOLHAS DO USER ##################################
while True:
    choice = int(input())
    print('')
    print('Aguarde, Estamos Buscando sua Solicitação...')
    time.sleep(2)
################################### ESCOLHA 1 FUNCIONARIOS DA EMPRESA ##################################
    if choice == 1:
        print('='*100)
        print(' '*30,'FUNCIONARIOS DA FSOCIETY')
        print('='*100)
        
        funcionarios = ['Weslley', 'Thiago', 'Matheus', 'Karol', 'Bruno', 'Dykson']
        for index, i in enumerate(funcionarios):
            print(f'{index+1} {i}')
            print('='*100)
        print('')
################################### ESCOLHA 2 CARGOS DA EMPRESA ##################################
    elif choice == 2:
        print('='*100)
        print(' '*30,'CARGOS DA PRINTSHOP FSOCIETY')
        print('='*100)
        print('')

        setores = [
            'Presidente: Matheus',
            'Diretor: Weslley',
            'Recursos Humanos: Karoline',
            'Analista de TI: Dykson',
            'Marketing: Bruno',
            'Produção: Thiago'
        ]
        for i in setores:
            print(i)
        print('')
################################### ESCOLHA 3 RENDAS MENSAL DA EMPRESA DE ACORDO COM O MÊS ##################################
    elif choice == 3:
        print('='*100)
        print(' '*30,'RENDAS MENSAIS')
        print('='*100)
        print('')

        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outrubro', 'Novembro', 'Dezembro']
        renda = 5000.43
        for index, i in enumerate(meses):
            print(f'{index + 1} - {i}')
        print('')
        ##################################### LOOP DE ESCOLHA DO USER, PODENDO ACESSAR VARIOS MESES SEM SAIR DO LOOP #####################################
        while True:
            rendaMes = int(input('Selecione o Mês Para Consulta: '))
            print('')
            print('Buscando o Mês Solicitado...')
            time.sleep(2)
            print('='*100)
            print(f'No Mês de {meses[rendaMes-1]} tivemos um crescimento de 'f'+R$%.2f'%(renda * rendaMes))
            print('='*100)
            print('')

            breakMes = str(input('Deseja Consultar Outro Mês? Y/N '))
            pararMês = breakMes.lower()
            if pararMês == 'n':
                print('')
                break
################################### ESCOLHA 4 SALARIOS E COMISSOES, COM PERMISSÃO DE ACESSO COM LOGIN E SENHA ##################################
    elif choice == 4:
        funcionario = {
            'nome':{
                '2218203564':'Matheus Pereira',
                '2218205083':'Bruno Lima',
                '2218201075':'Weslley Alves',
                '2218205089':'Karolayne Silva',
                '2218201526':'Dykson Santos',
                '2218200229':'Thiago Ruas'
            },
            'cargo':{
                '2218203564':'Presidente',
                '2218205083':'Capitao Marketing',
                '2218201075':'Diretor',
                '2218205089':'Capitao de RH',
                '2218201526':'Capitão de TI',
                '2218200229':'Capitão de Produção'
            },
            'salario':{
                '2218203564':14970.00,
                '2218205083':2994.00,
                '2218201075':7984.00,
                '2218205089':2994.00,
                '2218201526':4990.00,
                '2218200229':3952.00
            }
        }

        def holerites():
            print('='*100)
            print(' '*30,'Olá ' + funcionario['nome'][login_salario])
            print(' '*30,'Cargo/Setor: ' + funcionario['cargo'][login_salario])
            print('='*100)
            print(' ')
            print('='*100)
            print(' '*15,f'SEU HOLERITE DESSE MÊS ',' '*8,f'cod_Funcionario: {login_salario}' )
            print('='*100)
            print('='*100)
            print(' '*15,f'SALARIO ',' '*15,f'R$ %.2f'%(funcionario["salario"][login_salario]))
            print('='*100)
            print('='*100)
            print(' '*15,f'COMISSÃO ',' '*14,f'R$ %.2f' %(funcionario["salario"][login_salario]*0.05))
            print('='*100)
            print(' ')


        print('='*100)
        print(' '*15,'BEM VINDO A ÁREA DOS FUNCIONARIOS')
        print(' '*15,'AQUI VOCE PODE TER ACESSO AO SEU SALARIO E SE TEM ALGUMA COMISSÃO A RECEBER')
        print(' '*15,'VAMOS COMEÇAR?')
        print('='*100)
        print('')
        time.sleep(3)
        while True:
            login_salario = str(input('Digite o seu RA: '))
            pass_salario = getpass.getpass('Digite sua Senha: ')
            print('')
            print('Buscando seu login... Aguarde!')
            print('')
            time.sleep(0.5)

############# CADASTRO DOS FUNCIONARIOS A PARTIR DAQUI ########################

            if(login_salario == "2218203564" and pass_salario == "MatheusP"):
                holerites()
                time.sleep(2)
                break
            ################################### PROXIMO FUNCIONARIO #######################
            elif(login_salario == "2218200229" and pass_salario == "1598753"):
                holerites()
                time.sleep(2)
                break
            ################################### PROXIMO FUNCIONARIO #######################
            elif(login_salario == "2218201526" and pass_salario == "23356"):
                holerites()
                time.sleep(2)
                break
            ################################### PROXIMO FUNCIONARIO #######################
            elif(login_salario == "2218201075" and pass_salario == "520135"):
                holerites()
                time.sleep(2)
                break
            ################################### PROXIMO FUNCIONARIO #######################
            elif(login_salario == "2218205089" and pass_salario == "ka1997"):
                holerites()
                time.sleep(2)
                break
            ################################### PROXIMO FUNCIONARIO #######################
            elif(login_salario == "2218205083" and pass_salario == "bruno0905"):
                holerites()
                time.sleep(2)
                break
            else:
                print('='*100)
                print(' '*30 + '\033[41;1;37m'+'RA OU SENHA INVALIDOS... TENTE NOVAMENTE!!!'+'\033[0;0m')
                print('='*100)

################################### FIM DO CODIGO, USUARIO DECIDE SE IRÁ VOLTAR PARA O LOOP OU NÃO ##################################
    print('\033[32m'+"Retornando ao Menu Inicial..."+'\033[0;0m')
    print('')
    time.sleep(1.2)
    retorno = str(input('Deseja fazer outra consulta? Y/N '))
    return01 = retorno.lower()
    print('')

    if return01 == 'n':
        print('='*100)
        print(' '*30,'OBRIGADO POR ACESSAR A FSOCIETY!')
        print('='*100)
        time.sleep(2)
        break
    elif return01 == 'y':
        print('Digite uma opção: \n')
        print('1 - Funcionarios')
        print('2 - Setores')
        print('3 - Renda do Mês')
        print('4 - Salarios e Comissões')
        print('')
    else:
        print('Desculpe, opção invalida =/')
        print('Finalizando o programa...')
        print('')
        time.sleep(2)
        break
