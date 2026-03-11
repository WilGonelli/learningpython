import tkinter as tk
from word_service import random_word, verify_word

category = input("digite uma categoria entre: animais, objetos, paises, tecnologia ou frutas ")
word = random_word(category)
letters_correct = []
letters_incorrect = []
    
def handman_game():
   end_game = False

   while not end_game:
      word_show = verify_word(letters_correct, word)
      if word == word_show:
         print(f"voce descobriu a palavra {word}")
         end_game = True
         break
      print(word_show)
      letter = input("digite uma letra: ")
      if letter in word:
         letters_correct.append(letter)
      else:
         letters_incorrect.append(letter)
         print(f"não tem a(s) letra(s) {letters_incorrect} na palavra, tente novamente")

def interface():
   window = tk.Tk() 
   window.geometry("500x500") 
   window.config(bg='blue', padx=10,pady=20) 
   window.title('Jogo da forca') 

   canvas = tk.Canvas(window, width=400, height=400)
   canvas.pack()

   forca_img = tk.PhotoImage(file="./assets/forca.png")

   canvas.create_image(200, 200, image=forca_img)

   window.mainloop()
      
if __name__ == "__main__":
    interface()
   #  handman_game()