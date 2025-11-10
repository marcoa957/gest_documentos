import os
import shutil


def listar_documentos(pasta): # Função que busca o caminho da pasta
    arquivos_por_tipo = {} # Cria um dicionário vazio para agrupar os arquivos por tipo
    for raiz, _, arquivos in os.walk(pasta): # Percorre cara raiz (caminho) e arquivo (com a extenção) da pasta
        for arquivo in arquivos: # Para cada nome de arquivo dentro da pasta
            ext = arquivo.split('.')[-1] # Fará um split separando por ponto e retornará apenas a ultima parte (extenção do arquivo)
            arquivos_por_tipo.setdefault(ext, []).append(os.path.join(arquivo)) # Cria uma chave de extensão caso seja uma extensão nova e adiciona o nome dos arquivos relacionados
    for tipo, arquivos in arquivos_por_tipo.items(): # Para cada tipo e arquivo dentro dos arquivos presentes na variavel resultado
        print(f"\nArquivos .{tipo}:") # Printará um título com a extenção
        for a in arquivos:
            print(f" - {a}") # e o nome dos próprios arquivos da biblioteca

def renomear_documento(): # Função para renomear o arquivo
    arquivo = input("Digite o nome do arquivo que deseja editar (com a extenção desejada) ou digite 'Menu' para retornar ao menu principal: ") # Instrução para o usuário apontar qual documento deverá ser renomeado
    caminho_antigo = f"biblioteca/{arquivo}" # Inicializa variável com o caminho antigo
    
    if arquivo.strip().lower() == "menu":
        return menu()
    
    elif not os.path.exists(caminho_antigo):
        print("Não foi possível encontrar o arquivo indicado. Verifique e tente novamente")
        return renomear_documento()
    
    else:   
        novo_nome = input("Digite o novo nome que deseja dar ao arquivo (com a devida extenção) ou digite 'Menu' para retornar ao menu principal: ") # Instrução para o usuário apontar qual será o novo nome do arquivo
        if novo_nome.strip().lower() == "menu":
            return menu()
        
        caminho_novo = f"biblioteca/{novo_nome}" # Inicializa variável com o novo caminho
            
        os.rename(caminho_antigo, caminho_novo) # Renomeia arquivo
        print(f"Arquivo renomeado com sucesso para: {novo_nome}") # Mensagem de confirmação ao usuário

def adicionar_documento(): # Função para adicionar um novo arquivo
    arquivo = input("Digite o nome do arquivo que deseja adicionar (com a extenção desejada) ou digite 'Menu' para retornar ao menu principal: ") # Comando para o usuário escrever o nome do arquivo que será adicionado (com a extenção)
    if arquivo.strip().lower() == "menu":
        return menu()   
    
    novo_arquivo = f"biblioteca/{arquivo}" # Inicializa variável com o novo caminho.
    open(novo_arquivo, 'w').close() # Abrir pasta, criar arquivo e fechar pasta.
    print(f"Seu arquivo foi adicionado com sucesso!") # Mensagem de confirmação ao usuário

def remover_documento(): # Função para remover um arquivo
    arquivo = input("Digite o nome do arquivo que deseja remover (com a extenção desejada) ou digite 'Menu' para retornar ao menu principal: ") # Comando para o usuário escrever o nome do arquivo que será removido (com a extenção)
    if arquivo.strip().lower() == "menu":
        return menu()
    
    caminho = f"biblioteca/{arquivo}"
    if not os.path.exists(caminho):
        print("Não foi possível encontrar o arquivo indicado. Verifique e tente novamente")
        return remover_documento()
    else:        
        os.remove(caminho) # Remover o arquivo com base em seu caminho
        print(f"Seu arquivo foi removido com sucesso!") # Mensagem de confirmação ao usuário

def menu(): # Função com o menu de navegação
    while True:
        print("\n=== Sistema de Biblioteca Digital ===")
        print("1. Listar documentos")
        print("2. Adicionar documento")
        print("3. Renomear documento")
        print("4. Remover documento")
        print("5. Sair")
        opcao = input("Escolha uma opção:")

            # Variáveis de resposta do usuário
        if opcao == '1':
            listar_documentos("biblioteca")
        elif opcao == '2':
            adicionar_documento()
        elif opcao == '3':
            renomear_documento()
        elif opcao == '4':
            remover_documento()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__": # Condicional para inicializar o programa
    menu()