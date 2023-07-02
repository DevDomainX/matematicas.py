import random
from colorama import init, Fore, Back, Style


def suma():
    print(Fore.LIGHTGREEN_EX+"""                  
    ########################################################################|| 
    ||===> Practica de sumas  responde correctamente las sumas siguientes   ||
    ||====> Para cambiar el problema solo responde 0:                       || 
    ########################################################################||""")
    
    n1 = random.randint(1, 500)
    n2 = random.randint(1, 500)
    while True:
        print(f"""
              ############################
              ||Cuanto es {n1} + {n2} = ||
              ############################
              """)
        op = int(input("Ingresa la respuesta correcta ==>: "))
        if op == int(n1)+int(n2):
            print("""
            #######################
            |Correcto Has Ganado!!|
            #######################""")
            respuesta = input("Quieres seguir practicando (si/no) o (atras) para ir al menu: \n")
            if respuesta == "si":
                suma()
            elif respuesta == "atras":
                menu()
        elif op == 0:
            print("Nueva suma")
            suma()
        else:
            suma()


def resta():
    print(Fore.LIGHTBLUE_EX+"""
    ########################################################################
    || Practica de restas, responde correctamente las restas siguientes ||
    ######################################################################
    
    """)
    print("""\nPara cambiar el problema solo responde 0: """)
    
    n1 = random.randint(1, 500)
    n2 = random.randint(1, 500)
    while True:
        print(f"Cuanto es {n1} - {n2} = ")
        op = int(input("Ingresa la respuesta correcta: "))
        if op == n1-n2:
            print("Correcto Has Ganado!!")
            respuesta = input("Quieres seguir practicando (si/no) o (atras) para ir al menu: \n")
            if respuesta == "si":
                resta()
            if respuesta == "atras":
                menu()
        elif op == 0:
            print("Nueva resta")
            resta()
        elif op == "atras":
            menu()
        else:
            resta()


def divisiones():
    print(Fore.LIGHTMAGENTA_EX+"""
    ################################################################################
    || Practica de 'divisiones', responde correctamente las divisiones siguientes ||
    ################################################################################
    """)
    print("\nPara cambiar el problema solo responde 0: \n\n")
    
    n1 = random.randint(1, 500)
    n2 = random.randint(1, 500)
    while True:
        print(f"Cuanto es {n1} / {n2} = ")
        op = int(input("Ingresa la opcion correcta: "))
        if op == n1/n2:
            print("Correcto Has Ganado!!")
            respuesta = input("Quieres seguir practicando (si/no) o (atras) para ir al menu: \n")  
            if respuesta == "si":
                divisiones()
            if respuesta == "menu":
                menu()
        elif op == 0:
            print("Nueva diviosion")
            divisiones()
        elif op == "atras":
            menu()
        else:
            divisiones()



def multiplicaciones():
    print(Fore.LIGHTYELLOW_EX+""" 
    ############################################################################################
    || Practica de 'Multiplicaciones', responde correctamente las multiplicaciones siguientes ||
    ############################################################################################
    
    """)
    print("\nPara cambiar el problema solo responde 0: \n\n")
    
    n1 = random.randint(1, 12)
    n2 = random.randint(1, 12)
    while True:
        print(f"Cuanto es {n1} x {n2} = ")
        op = int(input("Ingresa la respuesta correcta: "))
        if op == n1*n2:
            print("Correcto Has Ganado!!")
            respuesta = input("Quieres seguir practicando (si/no) o (atras) para ir al menu: \n")
            if respuesta == "si":
                multiplicaciones()
            if respuesta == "menu":
                menu()
        elif op == 0:
            print("Nueva diviosion")
            multiplicaciones()
        elif op == "atras":
            menu()
        else:
            multiplicaciones()

def potencias():
    print(Fore.LIGHTRED_EX+"""
    ############################################################################
    || Practica de 'potencias'responde correctamente las potencias siguientes ||
    ############################################################################\n""")
    print("\n[para volver al menu (atras)]\n")
    print("\nPara cambiar el problema solo responde 0: ")
    
    
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    
    while True:
      print(f"Cuanto es {n1} elevado {n2} = ")
      op = int(input("Ingresa la respuesta correcta: "))
      if op == n1**n2:
            print("Correcto Has Ganado!!")
            respuesta = input("Quieres seguir practicando (si/no) o (atras) para ir al menu: \n")
            if respuesta == "si":
                potencias()
            elif respuesta == "no":
                break
            else:
                print("la opcion ingresada no es valida")
      elif op == 0:
        print("Nueva division")
        potencias()
      elif op == "atras":
        menu()
      else:
        potencias()

def raices():
    print(Fore.LIGHTBLACK_EX+"Practica de 'raices' \n responde correctamente las raices siguientes\n\n")
    print("Para cambiar a otra operacion escriba (atras)\n")
    print("Para cambiar el problema solo responde 0: \n\n")
    
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    while True:
        print(f"Cuanto es {n1} raiz de {n2} = ")
        op = int(input("Ingresa la respuesta correcta: "))
        if op == n1**n2:
            print("Correcto Has Ganado!!")
            respuesta = input("Quieres seguir practicando (si/no) o (atras) para ir al menu: \n")
            if respuesta == "si":
                raices()
            if respuesta == "atras":
                menu()
        elif op == 0:
            print("Nueva diviosion")
            raices()
        else:
            raices()


def menu():
    while True:
        print(Style.NORMAL+Fore.RED+Back.LIGHTBLUE_EX+"[create by Hans Saldias] \n")
        print("[Practica de matematicas] \n\n[solo elige la opcion que quieras practicar y COMIENZA.....]\n\n")
        print("\n[Uso exclusivo para (3 y 4 A) profesor: Luis Cid] \n")
        print("\n[para salir responde (0)]")
        print("""
                ############ 
        [1]     ||  SUMAS ||
                ############


                ################
        [2]     ||   RESTAS   ||
                ################


                ####################
        [3]     ||   DIVISIONES   ||
                ####################

                ##########################
        [4]      ||   MULTIPLICACIONES   ||
                ##########################
                  
                ####################
        [5]      ||   POTENCIAS    ||
                ####################

                ################
        [6]      ||   RAICES   ||
                ################""")
        op = int(input("Ingresa opcion a elegir: "))
        if op == 1:
            suma()
        elif op == 2:
            resta()
        elif op == 3:
            divisiones()
        elif op == 4:
            multiplicaciones()
        elif op == 5:
            potencias()
        elif op == 6:
            pass
        elif op == 0:
            print("""
###########################################################
|| Gracias por usar mi programa Created by: Hans Saldias ||
###########################################################
""")
            break
print("""
###########################################################
|| Gracias por usar mi programa Created by: Hans Saldias ||
###########################################################
""")
menu()