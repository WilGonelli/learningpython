import tkinter as tk
from PIL import Image, ImageTk
from word_service import random_word, verify_word

letters_correct = []
letters_incorrect = []
word = ""
word_show = ""
errors = 0

images = []

def start_game(category):
    """
        função responsavel por iniciar o jogo,
        ela recebe a categoria selecionada pelo usuario
        e seleciona uma palavra random dessa categoria
    """
    global word, letters_correct, letters_incorrect, errors

    letters_correct = []
    letters_incorrect = []
    errors = 0

    word = random_word(category)

    category_frame.pack_forget()
    game_frame.pack()

    reset_keyboard()
    update_word()
    update_image()

def update_word():
    """
        função responsavel por atualiza a visualização da palavra, 
        ela recebe um array de letras corretas e a palavra, 
        atualiza a palavra de exebição com " " onde ainda não descobriu a letra
        e adiciona a letra no local ja descoberto
    """
    global word_show

    word_show = verify_word(letters_correct, word)

    formatted = " ".join(word_show)
    word_label.config(text=formatted)

    if word_show == word:
        word_label.config(text=f"Você venceu!\nPalavra: {word}")
        disable_keyboard()


def update_image():
    """
        função para atualizar a imagem dos erros
    """
    canvas.itemconfig(stickman, image=images[errors])


def guess_letter(letter, button):
    """
        função que verifia se a letra chutada contem na palavra,
        caso não tenha ele acrescenta um erro e chama a função para atualizar a imagem,
        caso atinja o limite de erro ele apresenta que o usuario perdeu
    """
    global errors

    button.config(state="disabled")

    if letter in word:
        letters_correct.append(letter)
    else:
        letters_incorrect.append(letter)
        errors += 1
        update_image()

    update_word()

    if errors == 6:
        word_label.config(text=f"Você perdeu!\nPalavra: {word}")
        disable_keyboard()


def disable_keyboard():
    """
        função responsavel por desabilitar os botões da interface
    """
    for btn in keyboard_frame.winfo_children():
        btn.config(state="disabled")


def reset_keyboard():
    """
        função responsavel por resetar os botões da interface
    """
    for btn in keyboard_frame.winfo_children():
        btn.config(state="normal")


def restart_game():
    """
        função responsavel por restartar o jogo
    """
    global letters_correct, letters_incorrect, errors

    letters_correct = []
    letters_incorrect = []
    errors = 0

    game_frame.pack_forget()   
    category_frame.pack() 

    reset_keyboard()
    update_image()

window = tk.Tk() # inicializa a tela
window.geometry("500x650") # define o tamanho da tela
window.title("Jogo da Forca") # defin o titulo da tela
window.config(bg="white") # define uma cor de fundo para a tela

for i in range(7): # esse for carrega as imagens dos erros
    img = Image.open(f"./assets/erro{i}.png")
    img = img.resize((50, 100))
    img = ImageTk.PhotoImage(img)
    images.append(img)

forca_img = Image.open("./assets/forca.png") # carrega a imagem da forca
forca_img = forca_img.resize((200, 200))
forca_img = ImageTk.PhotoImage(forca_img)

category_frame = tk.Frame(window, bg="white") # define o frame inicial onde seleciona a categoria
category_frame.pack()

tk.Label(
    category_frame,
    text="Escolha uma categoria",
    font=("Arial", 18),
    bg="white"
).pack(pady=20) # apresenta uma menssagem na tela

categories = ["animais", "objetos", "paises", "tecnologia", "frutas"] # opções de categoria

for cat in categories:
    tk.Button(
        category_frame,
        text=cat,
        width=20,
        height=2,
        command=lambda c=cat: start_game(c)
    ).pack(pady=5) # apresenta botões com a categoria disponivel

game_frame = tk.Frame(window, bg="white") # define o frame do jogo

canvas = tk.Canvas(game_frame, width=300, height=250, bg="white", highlightthickness=0)
canvas.pack()

forca = canvas.create_image(150, 120, image=forca_img)

stickman = canvas.create_image(150, 135, image=images[0])

canvas.forca_img = forca_img
canvas.images = images

word_label = tk.Label(
    game_frame,
    text="",
    font=("Arial", 28),
    bg="white"
)
word_label.pack(pady=20)

keyboard_frame = tk.Frame(game_frame, bg="white")
keyboard_frame.pack()

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

row = 0
col = 0

for letter in letters: # loop para a criação dos botões de letras na tela

    btn = tk.Button(
        keyboard_frame,
        text=letter,
        width=4,
        height=2
    )

    btn.config(command=lambda l=letter, b=btn: guess_letter(l.lower(), b))

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1

    if col > 6:
        col = 0
        row += 1

restart_button = tk.Button(
    game_frame,
    text="Jogar novamente",
    font=("Arial", 12),
    command=restart_game
) # botão para recomeçar o jogo apos vitoria ou derrota

restart_button.pack(pady=20) # posicionamento do botão restart

window.mainloop()