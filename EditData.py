
with open("Untitled.txt", 'r', encoding='utf-8') as data:
    datainput = data.readlines()[-100:]
    for i in range(25, 300, 25):
        try:
           y = [float(x[i:i+25]) for x in datainput]
           eve = sum(y) / len(y)
           print("data:%.6f"%eve)
        except:
            pass