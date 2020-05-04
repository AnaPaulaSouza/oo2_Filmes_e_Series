class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} minutos - {self.likes} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes'

class PlayList:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def __len__(self):
        return len(self._programas)

vingadores = Filme('Vingadores', 2018, 160)
riverdale = Serie('Riverdale', 2017, 9)
tmep = Filme('Todo mundo em pânico', 1999, 100)
visxvis = Serie('Vis a Vis', 2018, 10)

vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
visxvis.dar_likes()
visxvis.dar_likes()
riverdale.dar_likes()
riverdale.dar_likes()

filmes_e_series = [vingadores, riverdale, visxvis, tmep]
playlist_fim_de_semana = PlayList('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

print(playlist_fim_de_semana[0])

len(playlist_fim_de_semana)

for programa in playlist_fim_de_semana:
    print(programa)
