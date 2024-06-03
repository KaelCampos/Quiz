import sys
import time


print("Seja bem vindo ao projeto Quiz *_* !")
comeca = input("Você deseja começar a jogar? (S/N) ").strip() .upper()
print(comeca)
if comeca != "S":
    time.sleep(1)
    print("Saindo do jogo. Até a Próxima!")


else:
    print("Carregando.....")
    time.sleep(1)
    pontos = 0
    print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games\n (B) Ubisoft \n (C) Activision \n (D) EA \n")
    resposta1 = input("Sua opção: ").strip() . upper()
    time.sleep(1)

    if resposta1 == "A":
        time.sleep(1)
        print("Parabéns *_* !")
        pontos += 1

    else:
        print("Errado. A resposta correta é Rockstar Games!")
    time.sleep(1)
    print("Qual é a capital da França? \n (A) Paris \n (B) Londres \n (C) Bagda \n (D) Roma \n ")
    resposta2 = input("Sua opção: ").strip() .upper()
    time.sleep(1)

    if resposta2 == "A":
        time.sleep(1)
        print("Parabéns *_* !")
        pontos += 1
    else:
        print("Errado. A resposta correta é Paris!")

    print("Qual é a capital do Brasil? \n (A) Brasilia \n (B) Rio de Janeiro \n (C) Salvador \n (D) Porto Alegre \n")
    resposta3 = input("Sua opção: ").strip() .upper()
    time.sleep(1)

    if resposta3 == "A":
        print("Parabéns *_* !")
        pontos += 1
        print(f"Sua pontuação é {pontos}/3 pontos!")
    else:
        print("Errado. A resposta correta é Brasilia!")
        print(f"Sua pontuação é {pontos}/3 pontos!")







