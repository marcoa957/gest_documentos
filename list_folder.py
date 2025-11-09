import os

def listar_documentos(pasta): # Função que busca o caminho da pasta
    arquivos_por_tipo = {} # Cria um dicionário vazio para agrupar os arquivos por tipo
    for raiz, _, arquivos in os.walk(pasta): # Percorre cara raiz (caminho) e arquivo (com a extenção) da pasta
        for arquivo in arquivos: # Para cada nome de arquivo dentro da pasta
            ext = arquivo.split('.')[-1] # Fará um split separando por ponto e retornará apenas a ultima parte (extenção do arquivo)
            arquivos_por_tipo.setdefault(ext, []).append(os.path.join(arquivo)) # Cria uma chave de extensão caso seja uma extensão nova e adiciona o nome dos arquivos relacionados
    return arquivos_por_tipo # Retorna o dicionário final

pasta = "biblioteca" # Define o nome da pasta que será navegada
resultado = listar_documentos(pasta) # Chama a função Listar Documentos
for tipo, arquivos in resultado.items(): # Para cada tipo e arquivo dentro dos arquivos presentes na variavel resultado
    print(f"\nArquivos .{tipo}:") # Printará um título com a extenção
    for a in arquivos:
        print(f" - {a}") # e o nome dos próprios arquivos da biblioteca
