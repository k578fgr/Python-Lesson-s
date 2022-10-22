#Режим w -write, r - read, a - append(дописать)
file = open("devices.txt", "r")

for item in file:
    item = item.strip()
    print(item)

file.close()