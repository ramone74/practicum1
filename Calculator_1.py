digit={"ноль":0, "один":1,"два":2,"три":3,"четыре":4,"пять":5,"шесть":6,"семь":7,"восемь":8,"девять":9,\
    "одиннадцать":11,"двенадцать":12,"тринадцать":13,"четырнадцать":14,"пятнадцать":15,"шестнадцать":16,"семнадцать":17,"восемнадцать":18,"девятнадцать":19,\
    "десять":10,"двадцать":20,"тридцать":30,"сорок":40,"пятьдесят":50,"шестьдесят":60,"семьдесят":70,"восемьдесят":80,"девяносто":90,\
    'плюс':'+','минус':'-','умножить':'*', 'разделить':'/', 'степени':'**'}

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def calc1(exp=list(str(input('Вводите: ')).split(' '))):
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
    flag_minus = 1
    if exp[0] == 'минус':
        flag_minus = -1
        exp.pop(0)
        print(exp)
        
    if exp[1] != 'плюс' and exp[1] != 'минус' and exp[1] != 'умножить' and exp[1] != 'разделить' and exp[1] != 'степени':
        if flag_minus == -1:
            a = flag_minus * (digit[exp[0]] + digit[exp[1]])
            flag_minus = 1
        else:
            a = digit[exp[0]] + digit[exp[1]]
        if exp[3] == 'минус':
            b = (-1) * digit[exp[4]]
            flag_minus = -1
            exp.pop(3)
        else:
            b = digit[exp[3]]
        if len(exp) >= 5:
            if flag_minus == -1:
                b -= digit[exp[4]] #тута поменял
                flag_minus = 1
            else:
                b += digit[exp[4]]
                flag_minus = 1
        if exp[2] == 'плюс':
            res = a + b
        elif exp[2] == 'минус':
            res = a - b
        elif exp[2] == 'умножить':
            res = a * b
        elif exp[2] == 'разделить':
            res = a / b
        else:
            res = a ** b
    else:
        if flag_minus == -1:
            a = flag_minus * digit[exp[0]]
            flag_minus = 1
        else:
            a = digit[exp[0]]
        if exp[2] == 'минус':
            b = (-1) * digit[exp[3]]
            flag_minus = -1
            exp.pop(2)
        else:
            b = digit[exp[2]]
        if len(exp) >= 4:
            if flag_minus == -1:
                b -= digit[exp[3]]
                flag_minus = 1
            else:
                b += digit[exp[3]]
        if exp[1] == 'плюс':
            res = a + b
        elif exp[1] == 'минус':
            res = a - b
        elif exp[1] == 'умножить':
            res = a * b
        elif exp[1] == 'разделить':
            res = a / b
        else:
            res = a ** b
    if res < 0:
        flag_res = -1
        res = abs(res)
    else:
        flag_res = 1
    if res <= 20 or res % 10 == 0:
        if flag_res == -1:
            return "минус " + get_key(digit, res)
        else:
            return get_key(digit, res)
    else:
        a_res = res % 100 - res % 10
        b_res = res % 10
        if flag_res == -1:
            return "минус " + get_key(digit, a_res) + " "+ get_key(digit, b_res), a, b, res
        else:
            return get_key(digit, a_res) + " "+ get_key(digit, b_res), a, b, res
print(calc1())
    
    
#Проблема с однозначными вторыми числами и двузначными первыми
