tasks = []

while True:
    print("\n1-Ekle 2-Liste 3-Sil 4-Çıkış")
    choice = input("Seçim: ")

    if choice == "1":
        task = input("Görev: ")
        tasks.append(task)

    elif choice == "2":
        print("\nGörevler:")
        for i, t in enumerate(tasks):
            print(i, t)

    elif choice == "3":
        index = int(input("Silinecek index: "))
        if 0 <= index < len(tasks):
            tasks.pop(index)

    elif choice == "4":
        break
