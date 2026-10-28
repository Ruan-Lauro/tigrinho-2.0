import random


class User:
    def __init__(self, nome):
        self.nome = nome

    def escolha(self):
        return f"Olá, {self.nome}!"


class Tigrinho:
    def __init__(self, pontos):
        self.pontos = pontos

    def escolha(self, numero):
        numeroDaSorte = random.randint(1, 10)
        if numero == numeroDaSorte:
            self.pontos += 10
            return f"Parabéns! Você acertou o número da sorte: {numeroDaSorte}!"
        else:
            self.pontos -= 10
            return f"Que pena! O número da sorte era: {numeroDaSorte}. Tente novamente!"


def main():
    print("Bem-vindo ao programa Tigrinho!")
    input_nome = input("Digite seu nome: ")
    user = User(input_nome)
    input_pontos = input("Quer apostar quanto: ")
    tigrinho = Tigrinho(int(input_pontos))
    print(user.escolha())

    while True:
        print(f"Seus pontos: {tigrinho.pontos}")
        resposta = input("Queres continuar no tigrinho? (s/n): ").strip().lower()
        if resposta == 's':
            input_pontos = input("Escolha um número de 1 a 10: ")
            print(tigrinho.escolha(int(input_pontos)))
        elif resposta == 'n':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")


if __name__ == "__main__":
    main()