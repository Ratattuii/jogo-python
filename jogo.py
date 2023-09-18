import tkinter as tk

def intro():
    text.insert(tk.END, "Bem-vindo à Caverna Misteriosa!\n")
    text.insert(tk.END, "Você é um destemido aventureiro em busca de tesouros escondidos.\n")
    text.insert(tk.END, "Você está parado na entrada da caverna. Seu objetivo é explorar seu interior.\n")
    text.insert(tk.END, "Escolha sabiamente, pois suas decisões moldarão seu destino!\n")

def choose_path():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Escolha o seu próximo passo:\n")
    text.insert(tk.END, "1. Seguir pelo caminho à esquerda.\n")
    text.insert(tk.END, "2. Seguir em frente\n")
    text.insert(tk.END, "3. Entrar na passagem estreita à direita.\n")

    button1.config(command=path_left)
    button2.config(command=path_center)
    button3.config(command=path_right)

def path_left():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Você segue pelo caminho à esquerda e encontra uma sala cheia de brilhantes cristais.\n")
    text.insert(tk.END, "1. Coletar os cristais.\n")
    text.insert(tk.END, "2. Continuar explorando a caverna.\n")

    button1.config(command=collect_crystals)
    button2.config(command=choose_path)

def collect_crystals():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Você coleta os cristais e coloca-os na sua mochila.\n")
    text.insert(tk.END, "Sua mochila agora está mais pesada, mas você tem belos cristais!\n")
    text.insert(tk.END, "1. Continuar explorando a caverna.\n")
    
    button1.config(command=choose_path)
    
def path_center():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Você encontra uma estátua de ouro em cima de um pedestal\n")
    text.insert(tk.END, "1. Pegar a estatua\n")
    text.insert(tk.END, "2. Investigar a estatua\n")
    
    button1.config(command=take_statue)
    button2.config(command=investigate_statue)

def take_statue():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Você pega a estátua e guarda na sua mochila\n")
    text.insert(tk.END, "1. Voltar para o inicio da caverna\n")
    
    button1.config(command=statue_exit)

def statue_exit():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Quando você está a preste a sair da sala você sentee um tremor\n")
    text.insert(tk.END, "Pedras começam a desmoronar, bloqueando a saída\n")
    text.insert(tk.END, "Você tenta achar um jeito de sair mas uma pedra te atinge e você desmaia\n")
    text.insert(tk.END, "1. Continuar...")
    
    button1.config(command=game_over)
    
def investigate_statue():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Você se aproxima do pedestal onde estatua está\n")
    text.insert(tk.END, "Você consegue observar que existe algum mecanismo que ativará se você tirar a estátua de cima\n")
    text.insert(tk.END, "Mas se você colocar algo no lugar rapidamente talvez consiga pegar a estátua\n")
    text.insert(tk.END, "1. Pegar a estátua\n")
    text.insert(tk.END, "2. Pegar a estátua e colocar os cristais no lugar\n")
    text.insert(tk.END, "3. Continuar explorando\n")
    
    button1.config(command=take_statue)
    button2.config(command=statue_crystals)
    button3.config(command=choose_path)
    
def statue_crystals():
    text.delete('1,0', tk.END)
    text.insert(tk.END, "Você pega a estátua e rapidamente coloca os cristais no lugar\n")
    text.insert(tk.END, "Você fica parado, atento, esperando algo acontecer\n")
    text.insert(tk.END, "Depois de um bom tempo tempo esperando, nada acontece\n")
    text.insert(tk.END, "1. Continuar explorando\n")
    text.insert(tk.END, "2. Continuar esperando\n")

    button1.config(command=choose_path)
    button2.config(command=wait_crystals)
    
def wait_crystals():
    text.delete('1,0', tk.END)
    text.insert(tk.END, "Você espera por 5 minutos e nada acontece, você decide ir embora\n")
    text.insert(tk.END, "Mas quando você está prestes a sair um cristal cai do pedestal e o chão treme\n")
    text.insert(tk.END, "Você olha para o pedestal bem a tempo de uma pedra acertar sua cabeça\n")
    text.insert(tk.END, "1. Continuar...")
    
    button1.config(command=game_over)
    
def path_right():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Você entra na passagem estreita à direita e encontra uma sala escura com um baú.\n")
    text.insert(tk.END, "1. Abrir o baú com cuidado.\n")
    text.insert(tk.END, "2. Ignorar o baú e voltar para o caminho principal.\n")

    button1.config(command=open_chest)
    button2.config(command=choose_path)

def open_chest():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Ao abrir o baú, você encontra uma adaga mágica!\n")
    text.insert(tk.END, "Você a guarda em sua bainha.\n")
    text.insert(tk.END, "1. Continuar explorando a caverna.\n")
    
    button1.config(command=choose_path)

def leave_cave():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Você decide sair da caverna.\n")
    text.insert(tk.END, "O ar fresco e a luz do sol são um alívio após a escuridão da caverna.\n")
    text.insert(tk.END, "Sua aventura chegou ao fim. Obrigado por jogar!\n")
    text.insert(tk.END, "1. Jogar novamente")
    button1.config(command=choose_path)
    
def game_over():
    text.delete('1.0', tk.END)
    text.insert(tk.END, "GAME OVER\n")
    text.insert(tk.END, "1. Jogar novamente")
    
    button1.config(command=choose_path)

def main():
    intro()
    choose_path()
    
janela = tk.Tk()
janela.title("Jogo")

text = tk.Text(janela)
text.pack()

frame = tk.Frame(janela)
frame.pack(side=tk.BOTTOM)

button1 = tk.Button(frame, text="Escolha 1")
button1.pack(side = tk.LEFT)

button2 = tk.Button(frame, text="Escolha 2")
button2.pack(side = tk.LEFT)

button3 = tk.Button(frame, text="Escolha 3")
button3.pack(side = tk.LEFT)

if __name__ == "__main__":
    main()

janela.mainloop()