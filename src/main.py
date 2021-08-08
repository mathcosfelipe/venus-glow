def main():
    
    while True:
        try:
            informacao = int(input("De qual informação você dispõe? \n1) distância Terra-Vênu \n2) ângulo Sol-Terra-Vênus \n3) ângulo Sol-Vênus-Terra \n4) ângulo Vênus-Sol-Terra \n5) data - entre a última conjunção inferior (03 de junho de 2020) e a próxima (08 de janeiro de 2022) \nDigite apenas o número correspondente: "))
        except:
            print("Erro! Opção inválida.")
        else:
            if informacao < 0 and informacao > 5:
                print("Erro! Opção inválida.")
            else:
                break           

main()