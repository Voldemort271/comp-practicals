import pickle

with open("filename.dat", "wb") as file:
    n = int(input("Enter no of entries: "))
    for i in range(n):
        entry = eval(input("Enter input: "))
        pickle.dump(entry)
    print("Done\n\n")

with open("filename.dat", "rb") as file:
    try:
        while True:
            item = pickle.load(file)
            print(item)
    except:
        pass
