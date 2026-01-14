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
