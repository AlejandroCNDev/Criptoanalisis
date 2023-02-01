
import math
import time
import numpy as np


def esCuadradoPerfecto(n):
    if n > 0:
        radical = math.sqrt(n)
    else:
        return False

    entero = int(radical)
    resto = radical % entero
    if (resto==0):
        return True
    else:
        return False
def fermat(n):
    A = math.ceil(math.sqrt(n))
    B = pow(A, 2) - n
    # while not (math.isqrt(B) ** 2 == B):  # while B no sea un cuadrado perfecto:
    while not esCuadradoPerfecto(B):  # while B no sea un cuadrado perfecto:
        A = A + 1
        B = pow(A, 2) - n

    return [int(A - math.sqrt(B)), int(A + math.sqrt(B))]


# Defining main function
def main():


    print(fermat(3695526079414531893395022629007992021988206660305594610729925173736166936948997168935976670015508196531263777370987923756353827517410361630989271608863379924531118495081938656755856366563112069))
    print(fermat(4950129588660811557140961251020953839650561470365148964685138895788178915475087659467373881976213469340009844708920361866795893918995209207299729868766983))  # n <32>
    print(fermat(16839536187678128309571382513772678125962917888256826521928995194411409717506922278397615027121706430329211567489109))  # n <32>
    print(fermat(1660995949077575790108209383531907547278415551489541950273354728654315878758042274997985213202209))  # n <32>
    # print(fermat(53704534926032574491266129220638793927980100349806821300313337187242717396013))  # n <48>
    # print(fermat(19747584697483807111173738562471763699165033955210632295208855614091))  # n <48>
    # print(fermat(15465577754445358282012384100265945923480853028748056031310000602069))  # n <64>
    # print(fermat(5798888407308328283351944114262809289247316815842820879109))  # n <64>
    # print(fermat(3216870142799598490322654446099509948303510505753647619457))  # n <64>
    # print(fermat(499261438794579864881109321218418276779965603169))  # n <80>>
    # print(fermat(197628881444442442728148135740402563449))  # n <80>>

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


    """
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

    times_experiments = []

    print("#################################################################")
    print("#################################################################")
    print("##############################<68>###################################\n")

    for i in num_68:
        print("#################################################################")
        print("######################" + " Experimento " + str(i) + " ############################\n")

        # Para calcular el tiempo de ejecución
        ini_time = time.time()

        print(fermat(i))

        fin_time = time.time()
        timeOneExperiment = fin_time - ini_time
        times_experiments.append(timeOneExperiment)
        print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

    print("#################################################################")
    print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
    print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
    print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))


    times_experiments = []

    print("#################################################################")
    print("#################################################################")
    print("##############################<72>###################################\n")

    for i in num_72:
        print("#################################################################")
        print("######################" + " Experimento " + str(i) + " ############################\n")

        # Para calcular el tiempo de ejecución
        ini_time = time.time()

        print(fermat(i))

        fin_time = time.time()
        timeOneExperiment = fin_time - ini_time
        times_experiments.append(timeOneExperiment)
        print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

    print("#################################################################")
    print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
    print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
    print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))


    times_experiments = []

    print("#################################################################")
    print("#################################################################")
    print("##############################<76>###################################\n")

    for i in num_76[:50]:
        print("#################################################################")
        print("######################" + " Experimento " + str(i) + " ############################\n")

        # Para calcular el tiempo de ejecución
        ini_time = time.time()

        print(fermat(i))

        fin_time = time.time()
        timeOneExperiment = fin_time - ini_time
        times_experiments.append(timeOneExperiment)
        print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

    print("#################################################################")
    print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
    print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
    print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))
    """
    """
    times_experiments = []

    print("#################################################################")
    print("#################################################################")
    print("##############################<80>###################################\n")

    for i in num_80[:10]:
        print("#################################################################")
        print("######################" + " Experimento " + str(i) + " ############################\n")

        # Para calcular el tiempo de ejecución
        ini_time = time.time()

        print(fermat(i))

        fin_time = time.time()
        timeOneExperiment = fin_time - ini_time
        times_experiments.append(timeOneExperiment)
        print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

    print("#################################################################")
    print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
    print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
    print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))

    times_experiments = []

    print("#################################################################")
    print("#################################################################")
    print("##############################<92>###################################\n")

    for i in num_92[:10]:
        print("#################################################################")
        print("######################" + " Experimento " + str(i) + " ############################\n")

        # Para calcular el tiempo de ejecución
        ini_time = time.time()

        print(fermat(i))

        fin_time = time.time()
        timeOneExperiment = fin_time - ini_time
        times_experiments.append(timeOneExperiment)
        print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

    print("#################################################################")
    print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
    print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
    print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))

    
    times_experiments = []

    print("#################################################################")
    print("#################################################################")
    print("##############################<104>###################################\n")

    for i in num_104:
        print("#################################################################")
        print("######################" + " Experimento " + str(i) + " ############################\n")

        # Para calcular el tiempo de ejecución
        ini_time = time.time()

        print(fermat(i))

        fin_time = time.time()
        timeOneExperiment = fin_time - ini_time
        times_experiments.append(timeOneExperiment)
        print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

    print("#################################################################")
    print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
    print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
    print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))



    times_experiments = []

    print("#################################################################")
    print("#################################################################")
    print("##############################<116>###################################\n")

    for i in num_116:
        print("#################################################################")
        print("######################" + " Experimento " + str(i) + " ############################\n")

        # Para calcular el tiempo de ejecución
        ini_time = time.time()

        print(fermat(i))

        fin_time = time.time()
        timeOneExperiment = fin_time - ini_time
        times_experiments.append(timeOneExperiment)
        print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

    print("#################################################################")
    print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
    print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
    print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))


    times_experiments = []

    print("#################################################################")
    print("#################################################################")
    print("##############################<128>###################################\n")

    for i in num_128:
        print("#################################################################")
        print("######################" + " Experimento " + str(i) + " ############################\n")

        # Para calcular el tiempo de ejecución
        ini_time = time.time()

        print(fermat(i))

        fin_time = time.time()
        timeOneExperiment = fin_time - ini_time
        times_experiments.append(timeOneExperiment)
        print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

    print("#################################################################")
    print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
    print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
    print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))


if __name__ == "__main__":
    main()
