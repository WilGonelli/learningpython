import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('financeiro2.csv', sep=';')

df = df[df['dispesas'] != 'total de ganhos']

meses = df.columns[1:13]

for m in meses:
    df[m] = (
        df[m]
        .str.replace('R$ -', '0', regex=False)
        .str.replace('R$', '', regex=False)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
        .astype(float)
    )

df.set_index('dispesas').T.plot(kind='bar')

plt.title("Evolução dos Gastos no Ano")
plt.ylabel("R$ por mês")
plt.grid(True)
# plt.show()

total = df.set_index('dispesas').sum()
print(df ,total)