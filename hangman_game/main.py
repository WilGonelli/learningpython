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
    global word_show

    word_show = verify_word(letters_correct, word)

    formatted = " ".join(word_show)
    word_label.config(text=formatted)

    if word_show == word:
        word_label.config(text=f"Você venceu! Palavra: {word}")
        disable_keyboard()


def update_image():
    canvas.itemconfig(stickman, image=images[errors])


def guess_letter(letter, button):
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
        word_label.config(text=f"Você perdeu! Palavra: {word}")
        disable_keyboard()


def disable_keyboard():
    for btn in keyboard_frame.winfo_children():
        btn.config(state="disabled")


def reset_keyboard():
    for btn in keyboard_frame.winfo_children():
        btn.config(state="normal")


def restart_game():
    global letters_correct, letters_incorrect, errors

    letters_correct = []
    letters_incorrect = []
    errors = 0

    game_frame.pack_forget()   # esconde tela do jogo
    category_frame.pack()      # mostra categorias

    reset_keyboard()
    update_image()


# ------------------ JANELA ------------------

window = tk.Tk()
window.geometry("500x650")
window.title("Jogo da Forca")
window.config(bg="white")

# ------------------ CARREGAR IMAGENS ------------------

for i in range(7):
    img = Image.open(f"./assets/erro{i}.png")
    img = img.resize((50, 100))
    img = ImageTk.PhotoImage(img)
    images.append(img)

forca_img = Image.open("./assets/forca.png")
forca_img = forca_img.resize((200, 200))
forca_img = ImageTk.PhotoImage(forca_img)

# ------------------ TELA DE CATEGORIA ------------------

category_frame = tk.Frame(window, bg="white")
category_frame.pack()

tk.Label(
    category_frame,
    text="Escolha uma categoria",
    font=("Arial", 18),
    bg="white"
).pack(pady=20)

categories = ["animais", "objetos", "paises", "tecnologia", "frutas"]

for cat in categories:
    tk.Button(
        category_frame,
        text=cat,
        width=20,
        height=2,
        command=lambda c=cat: start_game(c)
    ).pack(pady=5)

# ------------------ TELA DO JOGO ------------------

game_frame = tk.Frame(window, bg="white")

canvas = tk.Canvas(game_frame, width=300, height=250, bg="white", highlightthickness=0)
canvas.pack()

# forca (fundo)
forca = canvas.create_image(150, 120, image=forca_img)

# stickman (por cima)
stickman = canvas.create_image(150, 135, image=images[0])

# garantir referência
canvas.forca_img = forca_img
canvas.images = images

word_label = tk.Label(
    game_frame,
    text="",
    font=("Arial", 28),
    bg="white"
)
word_label.pack(pady=20)

# ------------------ TECLADO ------------------

keyboard_frame = tk.Frame(game_frame, bg="white")
keyboard_frame.pack()

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

row = 0
col = 0

for letter in letters:

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

# ------------------ BOTÃO REINICIAR ------------------

restart_button = tk.Button(
    game_frame,
    text="Jogar novamente",
    font=("Arial", 12),
    command=restart_game
)

restart_button.pack(pady=20)

window.mainloop()