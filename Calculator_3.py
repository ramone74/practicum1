# создать отдельный(?) словарь и добавить туда значения дробной части(они начинаются с числ женского рода). Подумать как реализовать дописывание дробной части через точку(кастануть к флоату и просто добавить дробную часть

digit={"один":1,"два":2,"три":3,"четыре":4,"пять":5,"шесть":6,"семь":7,"восемь":8,"девять":9,\
    "одиннадцать":11,"двенадцать":12,"тринадцать":13,"четырнадцать":14,"пятнадцать":15,"шестнадцать":16,"семнадцать":17,"восемнадцать":18,"девятнадцать":19,\
    "десять":10,"двадцать":20,"тридцать":30,"сорок":40,"пятьдесят":50,"шестьдесят":60,"семьдесят":70,"восемьдесят":80,"девяносто":90,\
    'плюс':'+','минус':'-','умножить':'*', 'разделить':'/', 'степени':'**', 'остаток': '%', "сто":100, "двести":200, "триста":300, "четыреста":400, "пятьсот":500, "шестьсот":600, "семьсот":700, "восемьсот":800, "девятьсот":900, "одна":1, "две":2, "сотая":100, "сотые":100, "сотых":100, "десятая":10, "десятые":10, "десятых":10, "тысячная":1000, "тысячные":1000, "тысячных":1000, "ноль":0}

#Таки прописать отдельный словарь для дробных?

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def calc(exp=list(str(input('Вводите: ')).split(' '))):
    c = ''.join(exp)
    try:
        delete = c.find('на')
        if delete:
            exp.remove('на')
    except:
        pass
    
    try:
        delete = c.find('в')
        if delete != 0:
            exp.remove('в')
    except:
        pass
    
    f1 = 0 #флаг действия 1-слож, 2-выч, 3-умн, 4-разд, 5-степ
    f2 = 0 #флаг дробной части
    f2_1 = 0 #конкретный флаг дробной части, 1 - тыс, 2 - сот, 3 - дес
    a = 0
    for i in range(len(exp)):
        if exp[i] != 'плюс' and exp[i] != 'минус' and exp[i] != 'умножить' and exp[i] != 'разделить' and exp[i] != 'степени' and exp[i] != 'остаток':
            if exp[i] == 'и':
                f2 = 1
                a_f = 0 #дробная часть
                continue
            if f2 == 1:
                if exp[i] == 'тысячная' or exp[i] == 'сотая' or exp[i] == 'десятая' or exp[i] == 'тысячных' or exp[i] == 'сотых' or exp[i] == 'десятых' or exp[i] == 'тысячные' or exp[i] == 'сотые' or exp[i] == 'десятые':  
                    if exp[i] == 'тысячная' or exp[i] == 'тысячных' or exp[i] == 'тысячные':
                        a_f /= 1000
                        a += a_f
                        f2_1 = 1
                    elif exp[i] == 'сотая' or exp[i] == 'сотых' or exp[i] == 'сотые':
                        a_f /= 100
                        a += a_f
                        f2_1 = 2
                    else:
                        a_f /= 10
                        a += a_f
                        f2_1 = 3
                    continue
                else:
                    a_f += digit[exp[i]]
                    continue
            a += digit[exp[i]]
        else:
            if exp[i] == 'плюс':
                f1 = 1
                exp = exp[i + 1:]
                break
            elif exp[i] == 'минус':
                f1 = 2
                exp = exp[i + 1:] 
                break
            elif exp[i] == 'умножить':
                f1 = 3
                exp = exp[i + 1:] 
                break
            elif exp[i] == 'разделить':
                f1 = 4
                exp = exp[i + 1:] 
                break
            elif exp[i] == 'остаток':
                f1 = 5
                exp = exp[i + 1:]
                break                
            else:
                f1 = 6
                exp = exp[i + 1:]
                break
    f2 = 0
    f2_1 = 0
    b = 0
    for j in range(len(exp)):
        if exp[j] == 'и':
            f2 = 1
            b_f = 0 #дробная часть
            continue        
        if f2 == 1:
            if exp[j] == 'тысячная' or exp[j] == 'сотая' or exp[j] == 'десятая' or exp[j] == 'тысячных' or exp[j] == 'сотых' or exp[j] == 'десятых' or exp[j] == 'тысячные' or exp[j] == 'сотые' or exp[j] == 'десятые':  
                if exp[j] == 'тысячная' or exp[j] == 'тысячных' or exp[j] == 'тысячные':
                    b_f /= 1000
                    b += b_f
                elif exp[j] == 'сотая' or exp[j] == 'сотых' or exp[j] == 'сотые':
                    b_f /= 100
                    b += b_f
                else:
                    b_f /= 10
                    b += b_f
                continue
            else:
                b_f += digit[exp[j]]
                continue
        b += digit[exp[j]]
    print(a, b)
    if f1 == 1:
        res = a + b
    elif f1 == 2:
        res = a - b
    elif f1 == 3:
        res = a * b
    elif f1 == 4:
        res = a / b
    elif f1 == 5:
        res = a % b
    else:
        res = a ** b
    #Реализовать проверку на int и float и в зависимости от этого разные выводы(реализовано?)
    #Результат считает нормально!
    res_int = int(res)
    res_frac = round(res - res_int, 3)
    if (res_frac * 1000) % 100 == 0:
        f2_1 = 3
    elif (res_frac * 1000) % 10 == 0:
        f2_1 = 2
    else:
        f2_1 = 1
    #Воткнуть проверку на кол-во знаков после запятой сюда
    print(res_int, res_frac)
    if res_frac == 0.0 or res_frac == 0:
        if res_int <= 20 or res_int % 10 == 0:
            return get_key(digit, res_int)
        else:
            a_res = res_int % 100 - res_int % 10
            b_res = res_int % 10
            return get_key(digit, a_res) + " "+ get_key(digit, b_res)
    else:
        print(f2_1)
        if res_int <= 20 or res_int % 10 == 0:
            if f2_1 == 1:
                res_frac = int(res_frac * 1000)
                a_res = res_frac % 1000 - res_frac % 100
                b_res = res_frac % 100 - res_frac % 10
                c_res = res_frac % 10    
                if 10 < res_frac % 100 < 20:
                    return get_key(digit, res_int) + " и " + get_key(digit, a_res) + " " + get_key(digit, b_res + c_res) + " тысячных"
                return get_key(digit, res_int) + " и " + get_key(digit, a_res) + " " + get_key(digit, b_res)+ " " + get_key(digit, c_res) + " тысячных"
            elif f2_1 == 2:
                res_frac = int(res_frac * 100)
                a_res = res_frac % 100 - res_frac % 10
                b_res = res_frac % 10
                if 10 < res_frac % 100 < 20:
                    return get_key(digit, res_int) + " и " + get_key(digit, a_res + b_res) + " сотых"             
                return get_key(digit, res_int) + " и " + get_key(digit, a_res) + " " + get_key(digit, b_res) + " сотых"
            elif f2_1 == 3:
                res_frac = int(res_frac * 10)
                a_res = res_frac % 10               
                return get_key(digit, res_int) + " и " + get_key(digit, a_res) + " десятых"
        else:
            if f2_1 == 1:
                a_res1 = res_int % 100 - res_int % 10
                b_res1 = res_int % 10
                res_frac = int(res_frac * 1000)
                a_res = res_frac % 1000 - res_frac % 100
                b_res = res_frac % 100 - res_frac % 10
                c_res = res_frac % 10    
                if 10 < res_frac % 100 < 20:
                    return get_key(digit, a_res1) + " " + get_key(digit, a_res2) + " и " + get_key(digit, a_res) + " " + get_key(digit, b_res + c_res) + " тысячных"
                return get_key(digit, a_res1) + " " + get_key(digit, b_res1) + " и " + get_key(digit, a_res) + " " + get_key(digit, b_res)+ " " + get_key(digit, c_res) + " тысячных"
            elif f2_1 == 2:
                a_res1 = res_int % 100 - res_int % 10
                b_res1 = res_int % 10
                res_frac = int(res_frac * 100)
                a_res = res_frac % 100 - res_frac % 10
                b_res = res_frac % 10
                if 10 < res_frac % 100 < 20:
                    return get_key(digit, a_res1) + " " + get_key(digit, a_res2) + " и " + get_key(digit, a_res + b_res) + " сотых"             
                return get_key(digit, a_res1) + " " + get_key(digit, a_res2) + " и " + get_key(digit, a_res) + " " + get_key(digit, b_res) + " сотых"
            elif f2_1 == 3:
                a_res1 = res_int % 100 - res_int % 10
                b_res1 = res_int % 10                
                res_frac = int(res_frac * 10)
                a_res = res_frac % 10               
                return get_key(digit, a_res1) + " " + get_key(digit, b_res1) + " и " + get_key(digit, a_res) + " десятых"    
    
print(calc())