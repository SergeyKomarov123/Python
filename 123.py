def topResult():
    try:
        f = open("TOP.dat", "r")
        m = f.readline()
        m = f.readline()
        f.close()
    except FileNotFoundError:
        print("Файла не существует")
    return m

g = topResult()
print(g)