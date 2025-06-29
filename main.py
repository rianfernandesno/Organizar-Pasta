from  pathlib import Path
import shutil

print("="*10 + " Organizador de arquivo! " + "="*10)

name = input("Informe o caminho da onde você quer organizar suas pastas: ").replace("\\", "/")
path = Path(name)
send_to = input("Informe o local que você quer organizar: ")
path_files = Path(send_to).iterdir()
Path(str(path) + "/Pasta Organizada").mkdir(exist_ok=True)

types = []

while True:
    print("Qual extensão de arquivo deseja organizar? (COM PONTO) ")
    ext = input("Digite a extensão: ")
    if ext == None or ext == "":
        print("Você precisa digitar alguma coisa! ")
        continue
    types.append(ext)
    resp = input("Deseja continuar? ").upper()[0]
    if resp == "N":
        break

# Backup
resp_backup = input("Você deseja fazer um backup? ").upper()[0]

if resp_backup == "S":
    for file in path_files:
        Path(name + "/backup").mkdir(exist_ok=True)
        if file.suffix in types:
            shutil.copy2(file, str(name) + "/backup")


# Move
for file in path_files:
     if file.suffix in types:
         path_ext = str(name) + "/Pasta Organizada/" + file.suffix[1:]
         Path(path_ext).mkdir(exist_ok=True)
         shutil.move(file, path_ext)

      # if file.suffix == ".jpg":
      #     path_jpg = str(name) + "/Pasta Organizada/jpg"
      #     Path(path_jpg).mkdir(exist_ok=True)
      #     shutil.move(file, path_jpg)
      #
      # if file.suffix == ".gif":
      #     path_gif = str(name) + "/Pasta Organizada/gif"
      #     Path(path_gif).mkdir(exist_ok=True)
      #     shutil.move(file, path_gif)
      #
      # if file.suffix == ".pdf":
      #     path_pdf = str(name) + "/Pasta Organizada/pdf"
      #     Path(path_pdf).mkdir(exist_ok=True)
      #     shutil.move(file, path_pdf)