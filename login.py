attempt = 0
while True:
    name = input('Digite o nome de usuario: ')
    password = input('Digite sua senha: ')
    if name == "admin" and password == "1234":
        print('Login realizado com sucesso!')
        break
    else:
        print('O usuario e senha não coincidem.')
        attempt += 1
        if attempt < 3:
            print('Tente novamente!')
        else:
            print('O seu acesso foi bloqueado!')
            break