class Livros:
    def __init__(self,titulo,genero,capitulos,numeros_paginas):
        self.titulo = titulo
        self.genero = genero
        self.capitulos = capitulos
        self.numeros_paginas = numeros_paginas

    def escolher_titulo(self,novo_titulo):
        self.titulo = novo_titulo
    
    def mudar_genero(self,n_genero):
        self.genero = n_genero

    def mostrar_capitolos(self):
        print(self.capitulos)

    def total_paginas(self):
        print(self.numeros_paginas)

    def imprimir(self):
        print(f"## um belo livro ##\ntitulo: {self.titulo}\ngênero: {self.genero}\ncapitulos: {self.capitulos}\npaginas: {self.numeros_paginas}")

l1 = Livros("se fosse real!","suspence",22, 328)
l1.escolher_titulo("Castelo de vidro")
l1.mudar_genero("romance")
l1.mostrar_capitolos()
l1.total_paginas()
l1.imprimir()