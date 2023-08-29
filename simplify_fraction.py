numerator = int(input("Numerator: "))
denominator = int(input("Denominator: "))

def gcd(a, b):
    if a < 0:
        a *= -1

    if b < 0:
        b *= -1
    
    if a > b:
        small = b
    
    else:
        small = a
    
    for i in range(1, small + 1):
        if((a % i == 0) and (b % i == 0)):
            result = i
    
    return result

fraction_gcd = gcd(numerator, denominator)

print(str(int(numerator / fraction_gcd)) + "/" + str(int(denominator / fraction_gcd)))
