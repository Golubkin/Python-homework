def pal(t1): #создали функцию pal с произвольным аргументом t1, который будет присутствовать в функции"
    t1 = t1.lower() #переобозначили переменную t1
    t2 = reversed(t1) #ввели новую переменную,которая читает переменную t1 наоборот
    for i, j in zip(t1, t2): #сравниваем по-элементно буквы переменных t1 и t2
        if i == j:
            print("yes")
        else:
            print("no")

#Тесты
if __name__ == __main__:
    assert ("ABBA" == reversed("ABBA")), "is not polindrom"
    assert ("area" == reversed("area")), "is not polindrom"
    
            
    
