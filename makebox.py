width = int(input('What do you want the width to be?: '))
length = int(input('What do you want the length to be?: '))
symbol = str(input('What symbol do you want to use?: '))

for i in range(length):
    for j in range(width):
        print(symbol, end="")
    print()
    
