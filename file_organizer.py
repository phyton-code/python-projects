import os

folder = input("Klasör yolu: ")

for file in os.listdir(folder):
    if file.endswith(".png"):
        os.makedirs(folder + "/images", exist_ok=True)
        os.rename(folder + "/" + file, folder + "/images/" + file)

    elif file.endswith(".txt"):
        os.makedirs(folder + "/texts", exist_ok=True)
        os.rename(folder + "/" + file, folder + "/texts/" + file)

print("Düzenleme tamamlandı.")
