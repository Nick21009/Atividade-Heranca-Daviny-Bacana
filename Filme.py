class Filme:
    def __init__(self, nome, genero, ano_lancamento):
        self.nome = nome
        self.genero = genero
        self.ano_lancamento = ano_lancamento

    def vender(self):
        return f"O filme {self.nome}, {self.genero}, lançado em {self.ano_lancamento} está à venda nos streamings."

    def gratis(self):
        return f"O filme {self.nome}, {self.genero}, lançado em {self.ano_lancamento} está disponível gratuitamente nos streamings."


filme1 = Filme("O Diabo Veste Prada", "Comédia/Drama", "2006")
filme2 = Filme("Divertidamente", "Infantil/Comédia", "2015")
filme3 = Filme("Frankenstein", "Terror/Ficção Científica", "2025")


print(filme1.gratis())
print(filme2.gratis())
print(filme3.vender())
