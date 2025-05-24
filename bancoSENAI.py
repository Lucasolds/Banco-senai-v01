#MENU DO SISTEMA BANCÁRIO

opcao = input("========== Banco Python ==========\n"
                " | [1] - Depósito         |\n"
                " | [2] - Saque            |\n"
                " | [3] - Extrato          |\n"
                " | [4] - Sair             |\n"
                " Digite a opção desejada:" )

#INICIA COM OS VALORES ZERADOS EM CONTA
dep = 0.0
saq = 0.0

#OPÇÃO 4 - ENCERRAMENTO DO SISTEMA RÁPIDO
if opcao == '4':
     print("Encerrando atendimento! \nSaindo do sistema...")
     
elif opcao == '1': #OPÇÃO 1 - REALIZA A PERGUNTA DO VALOR PARA SER DEPOSITADO, APÓS SOLICITA A INSERÇÃO DO VALOR
    print("Qual o valor do depósito? ")
    dep = float(input("Digite o valor a ser depositado: R$ "))
    print(f'Deposito de R$ {dep} realizado com sucesso!')
    
elif opcao == '2':#OPÇÃO 2 - REALIZA A PERGUNTA DO VALOR PARA SER SACADO, APÓS SOLICITA A INSERÇÃO DO VALOR
    print("Qual o valor do saque? ")
    saq = float(input("Digite o valor a ser sacado: R$ "))
    print(f'Saque de - R$ {saq} efetuado com sucesso!')
    
elif opcao == '3': #OPÇÃO 3 - IMPRIME O EXTRATO DA CONTA COM OS VALORES ATUALIZADOS DAS OPERAÇÕES REALIZADAS
    print(f'Imprimindo extrato: \n'
          f'Saque: - R$ {saq}\n'
          f'Deposito + R$ {dep}\n'
          f'Saldo atual R$ {dep}-{saq}\n')
    
else:
    print("Não é possivel realizar nenhuma operação") #CASO NÃO SEJA SELECIONADO NENHUMA DAS OPÇÕES DO MENU, SERÁ EXIBIDA A MENSAGEM.
    