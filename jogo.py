import tkinter as tk

def choose_path():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Bem-vindo à Caverna Misteriosa! \n Você é um destemido aventureiro em busca de tesouros escondidos.\n Você está parado na entrada da caverna. Seu objetivo é explorar seu interior.\n Escolha sabiamente, pois suas decisões moldarão seu destino!\n\n Escolha o seu próximo passo:\n 1. Seguir pelo caminho à esquerda.\n 2. Seguir em frente\n 3. Entrar na passagem estreita à direita.\n")

    button1.config(command=path_left)
    button2.config(command=path_center)
    button3.config(command=path_right)

def path_left():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Indo pelo caminho à esquerda você acha uma sala cheia de cristais brilhantes.\n\n 1. Coletar os cristais.\n 2. Continuar explorando a caverna.\n")

    button1.config(command=collect_crystals)
    button2.config(command=choose_path)

def collect_crystals():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Você coleta os cristais e coloca-os na sua mochila.\n Sua mochila agora está mais pesada, mas você tem belos cristais!\n\n 1. Continuar explorando a caverna.\n")
    
    button1.config(command=choose_path)
    
def path_center():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Você encontra uma estátua de ouro em cima de um pedestal\n\n 1. Pegar a estatua\n 2. Investigar a estatua\n 3. Voltar\n")
    
    button1.config(command=take_statue)
    button2.config(command=investigate_statue)
    button3.config(command=choose_path)

def take_statue():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Você pega a estátua e guarda na sua mochila\n\n 1. Voltar\n")
    
    button1.config(command=statue_exit)

def statue_exit():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Quando você está a preste a sair da sala você sente um tremor\n Pedras começam a desmoronar, bloqueando a saída\n Você tenta achar um jeito de sair mas uma pedra te atinge e você desmaia\n\n 1. Continuar...")
    
    button1.config(command=game_over)
    
def investigate_statue():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Você se aproxima do pedestal onde estatua está\n Você consegue observar que existe algum mecanismo que ativará se você tirar a \n estátua de cima\n Mas se você colocar algo no lugar rapidamente talvez consiga pegar a estátua\n\n 1. Pegar a estátua\n 2. Pegar a estátua e colocar os cristais no lugar\n 3. Continuar explorando\n")
    
    button1.config(command=take_statue)
    button2.config(command=statue_crystals)
    button3.config(command=choose_path)
    
def statue_crystals():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Você pega a estátua e rapidamente coloca os cristais no lugar\n Você fica parado, atento, esperando algo acontecer\n Depois de um bom tempo tempo esperando, nada acontece\n\n 1. Continuar explorando\n 2. Continuar esperando\n")
    
    button1.config(command=choose_path)
    button2.config(command=wait_crystals)
    
def wait_crystals():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Você espera por 5 minutos e nada acontece, você decide ir embora\n Mas quando você está prestes a sair um cristal cai do pedestal e o chão treme\n Você olha para o pedestal bem a tempo de uma pedra acertar sua cabeça\n\n 1. Continuar...\n")

    button1.config(command=game_over)
    
def path_right():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Você entra na passagem estreita à direita e vê uma sala escura com dois baús.\n\n 1. Abrir o baú da esquerda.\n 2. Abrir o baú da direita \n 3. Voltar")

    button1.config(command=open_chest_left)
    button2.config(command=open_chest_right)
    button3.config(command=choose_path)

def open_chest_left():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Ao abrir o baú, você encontra uma adaga mágica!\n Você a guarda em sua bainha.\n\n 1. Abrir o baú da direita.\n 2. Continuar explorando a caverna.\n 3. Voltar \n")
    
    button1.config(command=open_chest_left)
    button2.config(command=open_chest_right)
    button3.config(command=choose_path)

def open_chest_right():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Você se aproxima do baú para abri-lo\n Quando você nota algo muito estranho \n O baú na verdade era um mimico \n Ele está preste a te atacar \n O que você faz? \n\n 1. Atacar ele com a adaga \n 2. Correr")
    
    button1.config(command=attack_chest)
    button2.config(command=chest_run)
    
def attack_chest():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Quando ele abre a boca para te atacar você vê uma oportunidade e enfia a adaga  na 'cabeça' da criatura\n Com a adaga atravessada contra o seu corpo ele começa a se transformar em pó,   você não sabe bem o por que. \n\n 1. Voltar\n")
    
    button1.config(command=choose_path)
    
def chest_run():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " Você tenta fugir mas a criatura já está muito perto\n Ela agarra seu pé e te puxa pro chão, já sem forças você percebe que não \n conseguirá se salvar sem uma arma para defender-se.\n\n 1. Continuar...")
    
    button1.config(command=game_over)

def game_over():
    text.delete('1.0', tk.END)
    text.insert(tk.END, " \n GAME OVER\n\n")
    text.insert(tk.END, " 1. Jogar novamente")
    
    button1.config(command=choose_path)

def main():
    choose_path()
    
janela = tk.Tk()
janela.title("Jogo")

text = tk.Text(janela)
text.pack()

frame = tk.Frame(janela)
frame.pack()

button1 = tk.Button(frame, text="Escolha 1")
button1.pack(side = tk.LEFT)

button2 = tk.Button(frame, text="Escolha 2")
button2.pack(side = tk.LEFT)

button3 = tk.Button(frame, text="Escolha 3")
button3.pack(side = tk.LEFT)

if __name__ == "__main__":
    main()

janela.mainloop()