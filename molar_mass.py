compound = input()

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
           "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
           "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
           "y", "z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

while(compound != ""):
    stack = []
    expr = [] 

    # weights are stored as ints for precision
    weights = {"H": 101, "He": 400, "Li": 694, "Be": 901, "B": 1081,
        "C": 1201, "N": 1401, "O": 1600, "F": 1900, "Ne": 2018,
        "Na": 2299, "Mg": 2431, "Al": 2698, "Si": 2809, "P": 3097,
        "S": 3207, "Cl": 3545, "Ar": 3995, "K": 3910, "Ca": 4008,
        "Sc": 4496, "Ti": 4787, "V": 5094, "Cr": 5200, "Mn": 5494,
        "Fe": 5585, "Co": 5893, "Ni": 5869, "Cu": 6355, "Zn": 6539,
        "Ga": 6972, "Ge": 7261, "As": 7492, "Se": 7896, "Br": 7990,
        "Kr": 8380, "Rb": 8547, "Sr": 8762, "Y": 8891, "Zr": 9122,
        "Nb": 9291, "Mo": 9594, "Tc": 9800, "Ru": 10107, "Rh": 10291,
        "Pd": 10642, "Ag": 10787, "Cd": 11241, "In": 11482, "Sn": 11871,
        "Sb": 12176, "Te": 12760, "I": 12690, "Xe": 13129, "Cs": 13291,
        "Ba": 13733, "La": 13891, "Hf": 17849, "Ta": 18095, "W": 18384,
        "Re": 18621, "Os": 19023, "Ir": 19222, "Pt": 19508, "Au": 19697,
        "Hg": 20059, "Tl": 20438, "Pb": 20720, "Bi": 20898, "Po": 20900,
        "At": 21000, "Rn": 22200, "Fr": 22300, "Ra": 22600, "Ac": 22700,
        "Rf": 26100, "Db": 26200, "Sg": 26600, "Bh": 26400, "Hs": 26900,
        "Mt": 26800, "Ce": 14012, "Pr": 14091, "Nd": 14424, "Pm": 14500,
        "Sm": 15036, "Eu": 15196, "Gd": 15725, "Tb": 15893, "Dy": 16250,
        "Ho": 16493, "Er": 16726, "Tm": 16893, "Yb": 17304, "Lu": 17497,
        "Th": 23204, "Pa": 23104, "U": 23803, "Np": 23700, "Pu": 24400,
        "Am": 24300, "Cm": 24700, "Bk": 24700, "Cf": 25100, "Es": 25200,
        "Fm": 25700, "Md": 25800, "No": 25900, "Lr": 26200}

    # parsing the input
    it = iter(compound)
    for char in it:
        # if is in alphabet
        if(char in letters):
            if(char.islower()):
                expr[len(expr) - 1] += char
            else:
                expr.append(char)
        
        elif(char in numbers):
            if(type(expr[len(expr) - 1]) is int):
                expr[len(expr) - 1] *= 10;
                expr[len(expr) - 1] += int(char)
                
            else:
                expr.append(int(char))

        elif(char == "(" or char == ")"):
            expr.append(char)

    temp = []

    # replacing elements with their weights
    for part in expr:
        if(part in weights):
            stack.append(weights[part])
        
        elif(type(part) is int): 
            stack.append(stack.pop() * part)

        elif(part == "("):
            temp = stack
            stack = []

        elif(part == ")"):
            subexpr_total = sum(stack)
            stack = temp
            stack.append(subexpr_total)

    # add together the weight of all the atoms
    total = sum(stack)
    # and make it look like a decimal
    total = str(total)
    total = total[:(len(total) - 2)] + "." + total[(len(total) - 2):]

    print(total)

    compound = input()
