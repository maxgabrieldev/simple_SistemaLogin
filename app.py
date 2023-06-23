#Sistema de login que permite novos usuários se cadastrarem e usuários já cadastrados se logarem.

#Permitir que novos usuários se cadastrem
#Permitir que usuários já cadastrados se loguem
#Não permitir que usuários já cadastrados se cadastrem novamente
#Alertar o usuário caso ele digite uma senha errada

init_resposta = input('[1] - Cadastrar novo usuário \n[2] - Fazer login \n') #input inicial

usuarios = ['Max', 'João', 'Maria'] #lista de usuários
senhas = ['123', '456', '789'] #lista de senhas

if init_resposta == '1': #se o usuário digitar 1

    usuario = input('Digite seu nome de usuário: ') #input do usuário
    if usuario in usuarios:
        print('Usuário já cadastrado')
    else:
        senha = input('Digite sua senha: ') #input da senha

        usuarios.append(usuario) #adiciona o usuário na lista de usuários
        senhas.append(senha) #adiciona a senha na lista de senhas

elif init_resposta == '2':
    usuario = input('Digite seu nome de usuário: ') #input do usuário
    senha = input('Digite sua senha: ') #input da senha
    
    encontrado = False #variável booleana que verifica se o usuário está cadastrado
    for indice, item in enumerate(usuarios):
        if usuario == usuarios[indice] and senha == senhas[indice]:
            print('Login realizado com sucesso!')
            encontrado = True
        elif encontrado == False:
            print('Usuário não encontrado ou senha incorreta')
            
else: 
    print('Opção inválida')
        