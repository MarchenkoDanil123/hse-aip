def abc(w):
    qwerty = ""
    if w % 3:
        qwerty += "Pling"
    if w % 5:
        qwerty += "Plang"   
    if w % 7:
        qwerty += "Plong"
    if qwerty:
        return qwerty
    return w
