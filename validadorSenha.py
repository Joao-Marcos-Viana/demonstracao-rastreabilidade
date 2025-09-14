import os

def limpar_tela():
    """
    Função para limpar a tela do terminal.
    Funciona tanto no Windows quanto no Linux/Mac.
    """
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')

senha = ''
senhaForte = False

print('='*30)
print('Bem-Vindo ao validador de senha...')

# Primeira validação da senha
while not senhaForte:
    problemas = 0
    print('Primeiro digite sua senha: ', end='')
    senha = input()
    print('='*30)
    
    
    if len(senha) < 8:
        print('A senha deve conter ao menos 8 caracteres*')
    else:
        # Verificar cada requisito individualmente
        if not any(c.isdigit() for c in senha):
            print('A senha deve conter ao menos 1 número*')
            problemas += 1
        
        if not any(c.isalpha() for c in senha):
            print('A senha deve conter ao menos 1 letra*')
            problemas += 1
        
        if not any(not c.isalnum() for c in senha):
            print('A senha deve conter ao menos 1 caractere especial*')
            problemas += 1
        
        if not any(c.isupper() for c in senha):
            print('A senha deve conter ao menos uma letra maiúscula*')
            problemas += 1
        
        if not any(c.islower() for c in senha):
            print('A senha deve conter ao menos uma letra minúscula*')
            problemas += 1
        
        if problemas >= 1:
            print('SENHA FRACA ✖️')
        else:
            print('SENHA FORTE ✔️')
            senhaForte = True
    
    input('Pressione qualquer tecla para continuar...')
    limpar_tela()
    print("Obrigado por utilizar nosso validador de senha")
