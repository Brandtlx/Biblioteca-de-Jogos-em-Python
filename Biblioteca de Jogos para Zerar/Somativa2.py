import json

def carregar_dados():
    try:
        with open("Memoria.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("\033[1;31mERRO: Arquivo corrompido ou vazio. Iniciando lista vazia.\033[m")
        return []


def salvar_dados(lista):
    try:
        with open("Memoria.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)
    except:
        print("\033[1;31mERRO: Não foi possível salvar os dados.\033[m")

memory_card = carregar_dados()

while True:
    print("\033[1;034m=-\033[m" * 100)
    comando = input("\033[1mDigite Um Comando: ").upper()
    print("\033[1;034m=-\033[m" * 100)

    if comando == "ABOUT":
        print("\033[1;035;040mBem Vindo A Biblioteca De Jogos Para Zerar De Antonio Brandt!\033[m")

    elif comando == "QUIT":
        salvar_dados(memory_card)
        print("\033[1;31mSaindo Da Biblioteca De Jogos De Antonio Brandt...\033[m")
        break

    elif comando == "ADD":
        try:
            Quantidade_jogos = int(input("\033[1mDigite Quantos Jogos Quer Zerar:\033[m "))

            if Quantidade_jogos <= 0:
                print("\033[1;31mERRO: INFORME UM NUMERO VALIDO\033[m")
            else:
                for jogos in range(Quantidade_jogos):
                    Nome_jogos = input("\033[1mDigite O Nome Do jogo Que Quer Zerar: ")

                    if Nome_jogos.strip() == "":
                        print("\033[1;31mERRO: Nome inválido.\033[m")
                    else:
                        memory_card.append(Nome_jogos)
                        print(f"\033[1;036mO {Nome_jogos} Foi Cadastrado Com Sucesso!\033[m")

                print(
                    '\033[1;33mOs Jogos Estão Salvos! Use o comando \033[1;32mLIST\033[m \033[1;33mpara verificar!\033[m')

        except ValueError:
            print("\033[1;31mERRO: Digite um número válido.\033[m")

    elif comando == "LIST":
        if len(memory_card) == 0:
            print('\033[1mNão há nenhum jogo cadastrado no momento! Use o comando ADD.')
        else:
            for i in range(len(memory_card)):
                print(f"\033[1m{memory_card[i]}\033[m")

    else:
        print("\033[1;31mComando inválido!\033[m")