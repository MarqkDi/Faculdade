#Atividade Abud
#Data 1/04/26
LOG = 0
while LOG == 0:
    CHO = int(input("Você deseja efetuar registro ou login? \n1 - Login\n2 - Registro\n"))
    if (CHO != 1) and (CHO != 2):
        print("Escolha inválida!")
    else:
        if CHO == 1:
            for i in range (1, 4):
                TUSER = str(input("LOGIN \nUSUÁRIO: "))
                TPASS = str(input("SENHA: "))
                if TUSER == LUSER and TPASS == LPASS:
                    print("Login efetuado com sucesso!")
                    LOG = 1
                    break
                else:
                    print("Usuário/Senha incorretos!")
                    print(f"Tentativas Restantes: {3-i}")
            if LOG == 0:
                print("Número máximo de tentativas excedidos! Conta Bloqueada!")
                break
        else:
            TUSER = str(input("REGISTRO \nUSUÁRIO: "))
            TPASS = str(input("SENHA: "))
            LUSER = TUSER
            LPASS = TPASS
            print("Registro efeutado com sucesso!")
            LOG = 0