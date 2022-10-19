from time import sleep

class Quadrado():
    def atributos(self, lado):
        self.lado = lado
        print('ATRIBUTOS criados com sucesso.')
    def metodos(self):
        self.lado = float(input('Digite o valor do lado: '))
        print(f'Calculando a área...')
        sleep(2)
        print(f'O valor da área é: {self.lado**2}m2')

verificar = Quadrado()
verificar.atributos(12)
verificar.metodos()