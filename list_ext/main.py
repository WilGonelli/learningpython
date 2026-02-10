# -------- 1° maneira de listar arquivos ---------------

# from pathlib import Path

# pasta = Path("C:\projects\IBM\estudo\learningpython")

# # Lista arquivos recursivamente
# for arquivo in pasta.rglob("*"):
#     if arquivo.is_file():
#         print(f"Arquivo: {arquivo.name} | Extensão: {arquivo.suffix}")

# # rglob("*") percorre todos os arquivos e subpastas.
# # suffix retorna a extensão (ex: .txt, .jpg).



# -------- 2° maneira de listar arquivos ---------------
# import os

# # Caminho da pasta
# pasta = "C:\projects\IBM\estudo\learningpython"

# # Percorre todos os arquivos e subpastas
# for raiz, dirs, arquivos in os.walk(pasta):
#     print(f"Pasta: {raiz}")
#     for arquivo in arquivos:
#         nome, extensao = os.path.splitext(arquivo)
#         print(f"  Arquivo: {arquivo} | Extensão: {extensao}")



# -------- 3° maneira de listar arquivos (unicos) ---------------
# from pathlib import Path

# pasta = Path("C:\projects\IBM\estudo\learningpython")

# extensoes = {arquivo.suffix for arquivo in pasta.rglob("*") if arquivo.is_file()}

# print("Extensões encontradas:", extensoes)



from pathlib import Path

pasta = Path("C:\projects\IBM\estudo\learningpython")
resultado = []

for item in pasta.rglob("*"):  # percorre recursivamente
    if item.is_file():
        resultado.append({
            "file_name": item.stem,   # nome sem extensão
            "type": "file",
            "ext": item.suffix        # extensão (ex: ".py")
        })
    elif item.is_dir():
        resultado.append({
            "file_name": item.name,
            "type": "folder",
            "ext": ""
        })

print(resultado)

