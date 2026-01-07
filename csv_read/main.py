import csv

gastos = {}

def csv_read():
    total_gasto = 0
    with open('bills.csv', newline='') as csvfile:
        # cria um dicionario usando a primeira linha do csv como chave
        # ex. {'mercado': 87.0, 'conta mensal': 297.0}
        #               |
        #               V
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            gasto = row['type']
            valor = row['value']
            
            # verifica se um valor nao pertence a uma chave de um dicionario
            #           |
            #           V
            if gasto not in gastos:
                gastos[gasto] = 0
            
            gastos[gasto] += float(valor)
            total_gasto += float(valor)
    print(
        f"total gasto: {total_gasto}, "                     #   |
        # define o tamanho das casas decimais no float          V
        f"mercado: {((gastos['mercado'] / total_gasto) * 100):.2f}%, "
        f"contas mensais: {(gastos['conta mensal'] / total_gasto) * 100:.2f}%"
        )
    
            

if __name__ == '__main__':
    csv_read()
    