def copia_arquivo(arq1):

    with open(arq1) as arquivo1:
        with open("frase_copiada.txt", 'w') as arquivo2:
            for linha in arquivo1:
                if '//' not in linha:
                    print(linha, file = arquivo2)
copia_arquivo("frase.txt")    