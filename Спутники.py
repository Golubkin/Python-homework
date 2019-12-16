def nod(x, y):
 while x != 0 and y != 0:
     if x > y:
         x = x - y
         else:
             y = y - x
 return x + y #Нахождение НОД(x;y) по алгоритмц Евклида
def nok(x, y):
    return x * y / nod(x, y) #Формула связи НОК И НОД
def nok3(l, m, k):
    return nok(nok(l, m), k) #НОК трех периодов - это есть частота выстрраивания спутников в одну линию

# Тест
if __name__ == __main__:
    assert nok3(2, 5, 15) == 30.0
    assert nok3(3, 6, 13) == 78.0
