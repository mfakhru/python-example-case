# LED Display

pola = [['*****','*   *','*   *','*   *','*****'], # index 0
        ['   * ','  ** ','   * ','   * ','  ***'], # index 1
        ['*****','    *','*****','*    ','*****'], # index 2
        ['*****','    *','*****','    *','*****'], # index 3
        ['*   *','*   *','*****','    *','    *'], # index 4
        ['*****','*    ','*****','    *','*****'], # index 5
        ['*****','*    ','*****','*   *','*****'], # index 6
        ['*****','    *','    *','    *','    *'], # index 7
        ['*****','*   *','*****','*   *','*****'], # index 8
        ['*****','*   *','*****','    *','*****']] # index 9

def inputan():
    try:
        number = int(input('Enter input data: '))
    except:
        print('Input not valid, must be number.')
        inputan()
    dump = list(str(number))
    lst = [int(a) for a  in dump]
    print(lst)
    for i in range(5):
        for j in lst:
            print(pola[j][i],end=' ')
        print()
inputan()
