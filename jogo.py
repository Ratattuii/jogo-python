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
    text.insert(tk.END, "2. Entrar na passagem estreita à direita.\n")
    text.insert(tk.END, "3. Voltar para fora da caverna.\n")

    button1.config(command=path_left)
    button2.config(command=path_right)
    button3.config(command=leave_cave)

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
    button1.config(state=tk.DISABLED)
    button2.config(state=tk.DISABLED)
    button3.config(state=tk.DISABLED)

# Função principal
def main():
    intro()
    choose_path()

janela = tk.Tk()
janela.title("Jogo ;-;")

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