SECRET = 'xyzzy'

while True:
    password = raw_input('Insira a senha: ')
    if not password:
        continue
    elif password == SECRET:
        break

    print('Senha incorreta!')


print('Bem vindo!')
