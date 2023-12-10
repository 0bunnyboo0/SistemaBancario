MENU = """

[1] depositar 
[2] sacar 
[3] extrato
[0] sair


=>  """

saldo = 100
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3




while True:          

    opção = input(MENU)



    if opção == "1":
        print("Depósito")

        deposito = float(input("informe o valor que você deseja depositar: R$"))
        
        if deposito > 0:
            extrato += f"deposito: R$ {deposito: .2f}\n"
            saldo += deposito
            print(f'o valor depositado foi: R${deposito:.2f}. seu saldo atual é de: R${saldo: .2f}')
            

        else:
            (print("Não é possivel depositar valores nulos ou negativos"))

    

################################################################################################################################################
    
    elif opção == "2":
        print("Saque")

        saque = float(input("informe o valor que você deseja sacar: R$"))

        if saque > LIMITE:
                print("limite de saque ultrapassado")
                       
        elif saque > saldo:
             print("saldo insuficiente")
        
        elif saque > 0:
                numero_saques += 1
                if numero_saques > 3:
                     print('numero de saques excedido')
                     print(numero_saques)

                else:
                 saldo -= saque
                 extrato += f"saque: R$ {saque:.2f}\n"
                 print(f'o valor sacado foi de: R${saque:.2f}. o valor atual é de: R${saldo: .2f}')
               

                
                     
        else:
                print("impossivel concluir a operação")

        

        

###############################################################################################################################################

    elif opção == "3":
        
        print("\n==========extrato==========")
        print("não houveram operaçoes" if not extrato else extrato)
        print(f'\nsaldo: R$: {saldo:.2f}')
        print("===========================")
    
        


        

    

        
##############################################################################################################################################

    elif opção == "0":
        break

    else:
        print("Operação inválida, por favor tente novamente a operação desejada.")
