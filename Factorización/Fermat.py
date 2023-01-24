import math


def fermat(n):
    A = math.ceil(math.sqrt(n))
    B = pow(A, 2) - n

    while not (math.isqrt(B) ** 2 == B):  # while B no sea un cuadrado perfecto:
        A = A + 1
        B = pow(A, 2) - n

    return [int(A - math.sqrt(B)), int(A + math.sqrt(B))]


# Defining main function
def main():
    print(fermat(2534389177))  # n <32>
    print(fermat(2901095863))  # n <32>
    print(fermat(137253386980207))  # n <48>
    print(fermat(176058464422483))  # n <48>
    # print(fermat(9233918223012772517))  # n <64>
    # print(fermat(9916239399178531379))  # n <64>
    # print(fermat(416607178535732029239241))  # n <80>>
    #print(fermat(644466866774061586188803))  # n <80>>

    with open("ExtensionRetosFactorizacion.txt", "r") as f:
        lines = f.readlines()

    num_40 = []
    num_44 = []
    num_48 = []
    num_52 = []
    num_56 = []
    num_60 = []
    num_64 = []
    num_68 = []
    num_72 = []
    num_76 = []
    num_80 = []
    num_92 = []
    num_104 = []
    num_116 = []
    num_128 = []

    for line in lines:
        if line.strip() == "" or line.startswith("#"):
            continue
        try:
            t, n = line.strip().split(",")
            t = int(t.strip())
            n = int(n.strip())
            if t == 40:
                num_40.append(n)
            elif t == 44:
                num_44.append(n)
            elif t == 48:
                num_48.append(n)
            elif t == 52:
                num_52.append(n)
            elif t == 56:
                num_56.append(n)
            elif t == 60:
                num_60.append(n)
            elif t == 64:
                num_64.append(n)
            elif t == 68:
                num_68.append(n)
            elif t == 72:
                num_72.append(n)
            elif t == 76:
                num_76.append(n)
            elif t == 80:
                num_80.append(n)
            elif t == 92:
                num_92.append(n)
            elif t == 104:
                num_104.append(n)
            elif t == 116:
                num_116.append(n)
            elif t == 128:
                num_128.append(n)

        except ValueError:
            print(f"Line {line} is not in the expected format")

    print(num_40)
    print(num_44)
    print(num_48)
    print(num_52)
    print(num_56)
    print(num_60)
    print(num_64)
    print(num_68)
    print(num_72)
    print(num_76)
    print(num_80)
    print(num_92)
    print(num_104)
    print(num_116)
    print(num_128)


    for i in num_40:
        print(fermat(i))
    for i in num_44:
        print(fermat(i))
    for i in num_48:
        print(fermat(i))
    for i in num_52:
        print(fermat(i))

"""        
    for i in num_56:
        print(fermat(i))
    for i in num_60:
        print(fermat(i))
    for i in num_64:
        print(fermat(i))
    for i in num_68:
        print(fermat(i))
    for i in num_72:
        print(fermat(i))
    for i in num_76:
        print(fermat(i))
    for i in num_80:
        print(fermat(i))
    for i in num_92:
        print(fermat(i))
    for i in num_104:
        print(fermat(i))
    for i in num_116:
        print(fermat(i))
    for i in num_128:
        print(fermat(i))
"""

if __name__ == "__main__":
    main()
