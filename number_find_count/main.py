
def find_and_count(number, total):
    count = 0
    for i in range(total + 1):
        nmr_str = str(i)
        for digit in nmr_str:
            if(int(digit) == number):
                count += 1
    return count

def main():
    number = int(input("digite o numero que quer contar: "))
    total = int(input("digite o valor total : "))
    count = find_and_count(number, total)

    print(f'tem {count} numeros {number} de 0 ate {total}')

if __name__ == "__main__":
    main()