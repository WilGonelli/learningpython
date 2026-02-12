# -------- 1° maneira de listar arquivos ---------------

# from pathlib import Path

# pasta = Path("C:\projects\IBM\estudo\learningpython")
# ignore = [""]

# # Lista arquivos recursivamente
# for arquivo in pasta.rglob("*"):
#     if arquivo.is_file():
#         print(f"Arquivo: {arquivo.name} | Extensão: {arquivo.suffix}")

# rglob("*") percorre todos os arquivos e subpastas.
# suffix retorna a extensão (ex: .txt, .jpg).



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



# from pathlib import Path

# pasta = Path("C:\projects\IBM\estudo\learningpython")
# resultado = []
# ignorar = ["__pycache__", ".venv", "venv"]

# for item in pasta.rglob("*"):  # percorre recursivamente
#     if any(folder in item.parts for folder in ignorar):
#         continue
#     if item.is_file():
#         resultado.append({
#             "file_name": item.stem,   # nome sem extensão
#             "type": "file",
#             "ext": item.suffix        # extensão (ex: ".py")
#         })
#     elif item.is_dir():
#         resultado.append({
#             "file_name": item.name,
#             "type": "folder",
#             "ext": ""
#         })

# for r in resultado:
#     if r["type"] == "folder":
#         print(r, end="\n")


import os

target_dir = "C:/projects/IBM/estudo/learningpython"
final_ignore_set = ["__pycache__", "node_modules", ".git", ".venv", "venv"]
extensions = []

for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in final_ignore_set]

        for f in files:
            name, extension = os.path.splitext(f)
            if extension not in extensions:
                extensions.append(extension)

for e in extensions:
     print(e)

# for raiz, dirs, arquivos in os.walk(pasta):
#     # Remove todas as pastas indesejadas da lista de diretórios
#     dirs[:] = [d for d in dirs if d not in ignorar]

#     # Pastas
#     for d in dirs:
#         resultado.append({
#             "file_name": d,
#             "type": "folder",
#             "ext": ""
#         })
#     # Arquivos
#     for f in arquivos:
#         nome, extensao = os.path.splitext(f)
#         resultado.append({
#             "file_name": nome,
#             "type": "file",
#             "ext": extensao
#         })

# for r in resultado:
#     if r["type"] != "folder":
#         print(r, end="\n")
