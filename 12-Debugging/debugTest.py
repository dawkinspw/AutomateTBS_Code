#! python3

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol needs to be 1 character')
    if (width < 2) or (height < 2):
        raise Exception('width and height should be 2 or more')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width -2) + symbol))
    
    print(symbol * width)

boxPrint('*', 33, 33) 