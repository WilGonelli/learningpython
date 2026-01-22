## Utilidades para o python

### Para a criação de um novo projeto:

* projeto com dependencias de bibliotecas:
    * boa pratica criar uma env - uma env é um ambiente variavel do python onde é possivel instalar as bibliotecas do projeto sem afeta os outros projetos do sistema
    * para criar a env:
        * use o comando:
        ```bash
        python -m venv venv
        ``` 
        * depois ative o venv
        ```bash
        venv\Scripts\activate
        ``` 
    * instalando dependencias - bibliotecas prontas para uso no projeto:
        *   use o comando
        ```bash
        pip install nome_da_biblioteca
        ```
    *   criando arquivo requirements.txt - esse arquivo serve para documentar todas as dependencias de bibliotecas do seu projeto
        *   use o comando para criar o arquivo
        ```bash
        pip freeze > requirements.txt
        ```
        *   use o comando para usar o arquivo e instalar as dependencias
        ```bash
        pip install -r requirements.txt
        ```
    * criando um executavel para rodar o projeto mesmo sem o ambiente python configurado - !! necessario biblioteca pyinstaller instalado !!
        * use o comando 
        ```bash
        pyinstaller nome_do_arquivo_principal --onefile --noconsole
        or
        pyinstaller nome_do_arquivo_principal -F -w
        ```
# 

### tipos de variaveis (listas, tuplas, dicionarios)

##### lista - lista de itens mutaveis (valor pode mudar)
* cria com "[]" separados os itens por ","
    * ex.:
    ```python
        frutas = ["maça", "abacaxi"]
    ```
    * sempre começa em 0 o index (posição) da lista

* para usar a lista usa o "[]" passando a posição que quer acessar
    * ex.:
    ```python
        print(frutas[0])
    ```

* para adicionar um item usa metodos (funções) da lista, existe diversos metodos para lista
    * ex.:
    ```python
        frutas.append("banana")
    ```

##### tuplas - lista de itens imutaveis (os valores não pode mudar)

* cria com "()" separados os itens por ","
    * ex.:
    ```python
        meses = ("jan", "fev")
    ```
    * sempre começa em 0 o index (posição) da lista

* para usar a lista usa o "[]" passando a posição que quer acessar
    * ex.:
    ```python
        print(meses[0])
    ```

* NÃO É POSSIVEL ALTERAR OS VALORES 

##### dicionarios - lista com chave e valor

* cria com "{}" chave : valor separados por ","
    * ex.:
    ```python
        usuarios = {
            "nome": "william",
            "cidade": "sorocaba"
        }
    ```
    * sempre começa em 0 o index (posição) da lista

* para usar a lista usa o "[]" passando a chave que quer acessar
    * ex.:
    ```python
        print(usuarios["nome"])
    ```

* Para manipular os valores acessa a propriedade acessando a chave
    * ex.:
    ```python
        usuario["nome"] = "william gonelli"
    ```

* Para criar novas propriedade para o dicionario, acessa a lista passando uma chave que nao existe ainda
    * ex.:
    ```python
        usuario["idade"] = 33
    ```

#

### Condicional if em linha unica
* serve para quando tem um valor caso condiçao verdadeira e outro para condição falsa
    * ex.:
    ```python
        "verdadeiro" if True else "falso" # <- isso retornara o verdadeiro, caso condição do if seja falsa iria retornar o falso
    ```
#

### programação orientada ao objeto - POO

* para definir um objeto utiliza-se uma class
* por padrao utiliza-se primeira letra do nome com maiuscula
    *ex.:
    ```python
        class Casa:
    ```
* metodo construtor - o que define o objeto
* o metodo construtor é uma função chamada __init__ passando como parametros as ele mesmo (self) e as propriedades do objeto
    * ex.:
    ```python
        class Casa:
            def __init__(self, tamanho, cor, bairro):
                self.tamanho = tamanho
                self.cor = cor
                self.bairro = bairro
    ```
* para definir um parametro como opcional pode-se definir como None ao declarar
    * ex.:
    ```python
        class Casa:
            def __init__(self, tamanho, cor, bairro=None):
                self.tamanho = tamanho
                self.cor = cor
                self.bairro = bairro
    ```
* é possivel criar metodos (funçoes) para esse objetos 
* essa funçao sempre tera ele mesmo como parametro podendo receber mais parametros
    * ex.:
    ```python
        class Casa:
            def __init__(self, tamanho, cor, bairro):
                self.tamanho = tamanho
                self.cor = cor
                self.bairro = bairro
            
            def mostrar_casa(self)
                print(f"a casa tem {self.tamanho} mt2 e fica no bairro {self.bairro}")
    ```

* instanciando uma classe (criar objeto)
* utiliza-se uma variavel para criar a instancia do objeto
    * ex.:
    ```python
        casa1 = Casa(50, "branca", "centro")
    ```

* para usar os metodos desse objeto basta chamar os metodos da variavel
    * ex.:
    ```python
        casa1.mostrar_casa()
    ```

#### Herança
* classe PAI onde possui seus parametros e metodos
* classe FILHO herda as propriedades do PAI e pode receber novos parametros e metodos
    * ex.:
    ```python
        class Animal:
            def __init__(self, cor, nome):
                self.nome = nome
                self.cor = cor
            
            def apresentar(self)
                print(f"o {self.nome} tem a cor {self.cor}")
        
        class Gato(Animal):
            pass # <- serve para ignorar a função

        gato1 = Gato("branco", "bichano")
        gato1.apresentar()
            
    ```
* funçao super() para herança
    * ex.:
    ```python
        class Animal:
            def __init__(self, cor, nome):
                self.nome = nome
                self.cor = cor
            
            def apresentar(self)
                print(f"o {self.nome} tem a cor {self.cor}")
        
        class Gato(Animal):
            def __init__(self,cor, nome, raca):
                super().__init__(cor, nome) # <- acessa as propriedades do PAI
                self.raca = raca
            
            def apresentar(self) # <- sobreescreve o metodo do PAI
                super().apresentar() # <- usa o metodo do PAI
                print(f"o {self.nome} tem a cor {self.cor}")


        gato1 = Gato("branco", "bichano", "siames")
        gato1.apresentar()
            
    ```


#### usando dotend


```bash
pip install python-dotenv
```
```python
from dotenv import load_dotenv
import os

load_dotenv()

CLI_KEY = os.environ.get("CLI_KEY")

# Coloque sua chave aqui
genai.configure(api_key=CLI_KEY)
```