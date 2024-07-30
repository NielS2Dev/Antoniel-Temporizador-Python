import time

def cronometro():
    print("Cronômetro iniciado. Pressione Ctrl+C para parar.")
    inicio = time.time()
    try:
        while True:
            tempo_decorrido = time.time() - inicio
            minutos, segundos = divmod(int(tempo_decorrido), 60)
            horas, minutos = divmod(minutos, 60)
            print(f"\r{horas:02}:{minutos:02}:{segundos:02}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCronômetro parado.")

def temporizador(duracao):
    print(f"Temporizador iniciado para {duracao} segundos.")
    while duracao > 0:
        minutos, segundos = divmod(duracao, 60)
        print(f"\r{minutos:02}:{segundos:02}", end="")
        time.sleep(1)
        duracao -= 1
    print("\nTempo esgotado!")

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Cronômetro")
        print("2. Temporizador")
        print("3. Sair")
        escolha = input("Digite o número da opção: ")
        if escolha == '1':
            cronometro()
        elif escolha == '2':
            try:
                duracao = int(input("Digite a duração do temporizador em segundos: "))
                temporizador(duracao)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
