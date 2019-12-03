def mapDecoding(message):

    return decode(message)%1000000007
    
def decode(thestring):
    n = len(thestring)
    if n==0:
        return 1
    tmp0 = thestring[0]
    if tmp0 == "0":
        return 0
    if n==1:
        return 1
    tmp1 = thestring[1]
    if tmp0 >="3":
        return decode(thestring[1:])
    if tmp1 == "0":
        return decode(thestring[2:])
    
    
    if tmp0 == "1":
        if tmp1 == "1" or tmp1 == "2":
            return decode(thestring[1:]) + decode(thestring[2:])
        else:
            return 2* decode(thestring[2:])
    if tmp1 <= "6":
        return decode(thestring[1:]) + decode(thestring[2:])
    return decode(thestring[2:])
