digit={"один":1,"два":2,"три":3,"четыре":4,"пять":5,"шесть":6,"семь":7,"восемь":8,"девять":9,\
    "одиннадцать":11,"двенадцать":12,"тринадцать":13,"четырнадцать":14,"пятнадцать":15,"шестнадцать":16,"семнадцать":17,"восемнадцать":18,"девятнадцать":19,\
    "десять":10,"двадцать":20,"тридцать":30,"сорок":40,"пятьдесят":50,"шестьдесят":60,"семьдесят":70,"восемьдесят":80,"девяносто":90,\
    'плюс':'+','минус':'-','умножить':'*', 'разделить':'/', 'степени':'**'}

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
    if exp[1] != 'плюс' and exp[1] != 'минус' and exp[1] != 'умножить' and exp[1] != 'разделить' and exp[1] != 'степени':
        a = digit[exp[0]] + digit[exp[1]]
        b = digit[exp[3]]
        if len(exp) == 5:
            b += digit[exp[4]]
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
    else:
        a = digit[exp[0]]
        b = digit[exp[2]]
        if len(exp) == 4:
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
    if res <= 20 or res % 10 == 0:
        return get_key(digit, res)
    else:
        a_res = res % 100 - res % 10
        b_res = res % 10
        return get_key(digit, a_res) + " "+ get_key(digit, b_res)
print(calc())
    
    
