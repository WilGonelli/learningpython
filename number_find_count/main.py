import tkinter as tk

def find_and_count(number, total, label):
    if not number or not total:
        print('retornou')
        return

    count = 0
    for i in range(int(total) + 1):
        nmr_str = str(i)
        for digit in nmr_str:
            if(int(digit) == int(number)):
                count += 1
    
    if(label):
        label.config(text=f'total de numero {number} de 0 a {total} é de {count}')

    return count

def cmd():
    number = int(input("digite o numero que quer contar: "))
    total = int(input("digite o valor total : "))
    count = find_and_count(number, total, None)

    print(f'tem {count} numeros {number} de 0 ate {total}')

def interface():
    window = tk.Tk() # instancia uma interface do tkinter
    window.geometry("400x200") # define um tamanho para a interface
    window.config(bg='blue', padx=10,pady=20) # configuraçoes da tela
    window.title('find and count number') # titulo da aba
    window.iconphoto(False, tk.PhotoImage(file='logo.png')) # remove e altera o icone da aba

    # cria uma label (texto) para um campo .grid define a posiçao 
    tk.Label(window, text='numero para procurar e contar: ', bg='blue').grid(row=0) 
    tk.Label(window, text='ultimo numero da lista: ', bg='blue').grid(row=1)

    # cria um campo de input na tela
    e1 = tk.Entry(window)
    e2 = tk.Entry(window)

    # define a posição do input
    e1.grid(row=0,column=1,)
    e2.grid(row=1,column=1)

    # cria uma label e salva em uma variavel
    label = tk.Label(window, text='', bg='blue')
    # define o layout da label
    label.grid(row=3) 

    # cria um botao
    tk.Button(window, text='iniciar', command=lambda: find_and_count(e1.get(),e2.get(),label)).grid(row=2, columnspan=2)

    # cria a visualização e mantem em loop
    tk.mainloop()


if __name__ == "__main__":
    on_interface = False
    
    if not on_interface:
        cmd()
    else:
        interface()