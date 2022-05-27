import pandas as pd
import numpy as np
import Matrix
import os

def ClearW(): # Limpiar pantalla en Linux, Mac o Windows
    try:
        os.system('cls')
    except:
        os.system('clear')

def ShowData1(Data):
    #print(f'l\u2093: {Data[0]} mm\nl\u1D67: {Data[1]} mm\nlz: {Data[2]} mm\n\u03c3\u2093: {Data[3]} Pa\n\u03c3\u1D67: {Data[4]} Pa')
    for n in range(len(Data)):
        print(f"{Data[n]['Name']} ({Data[n]['Symbol']}): {Data[n]['Value']}")

def CheckisNumber(List):
    R = True
    for n in range(len(List)):
        if not List[n]['Value'].isdigit():
            print('\nUn valor no es un Numero')
            R = False
            break
            
    return R

def IngresarDatos(Data):
    for n in range(len(Data)):
        while True:
            val = input(f"{Data[n]['Name']}: ")
            if val.isdigit():
                Data[n]['Value'] = val
                break
            else:
                print('No es un valor numerico')
    ShowData1(Data)
    while True:
        op = input('Desea modificar valores? (y/n): ')
        if op =='y':
            Data = ModificarDatos(Data)
        elif op == 'n':
            break
        else: 
            print('Opcion No valida')
    return Data

def ModificarDatos(Data):
    while True:
        print('Modificar: ')
        for n in range(len(Data)):
            print(f'{n+1}. {Data[n]["Symbol"]}')
        op = input('Opcion: ')
        try:
            if int(op) >= 1 and int(op) <= len(Data):
                break
            else:
                print('Opcion Incorrecta')
        except:
                print('Opcion Incorrecta')
    while True:
        val = input('Valor: ')
        if val.isdigit():
            break
        else:
            print('No es un valor numerico') 
    Data[int(op)-1]['Value'] = val
    ShowData1(Data)
    return Data

def InputDimention(Data):

    if not Data:
        Data =[{'Name': 'longitud en x', 'Symbol':'lx','Value':0},{'Name': 'longitud en y','Symbol':'lx', 'Value':0},{'Name': 'longitud en z','Symbol':'lz', 'Value':0}]
        Data = IngresarDatos(Data)
    else:
        Data = ModificarDatos(Data)
        
    return Data

def InputEsfuerzos(Data):

    if not Data:
        Data =[{'Name': 'Esfuerzo en x', 'Symbol':'\u03c3\u2093','Value':0},{'Name': 'Esfuerzo en y','Symbol':'\u03c3\u1D67', 'Value':0},{'Name': 'Esfuerzo Cortante','Symbol':'Gxy', 'Value':0}]
        Data = IngresarDatos(Data)
    else:
        Data = ModificarDatos(Data)
        
    return Data

def InputPropiedades(Data):

    if not Data:
        Data =[{'Name': 'Modulo de elasticidad', 'Symbol':'E1','Value':0},{'Name': 'Modulo de elasticidad','Symbol':'E2', 'Value':0},
        {'Name': 'Modulo Poison','Symbol':'v12', 'Value':0},{'Name': 'Modulo Poison','Symbol':'v21', 'Value':0},{'Name': 'Modulo Cortante','Symbol':'Yxy', 'Value':0}]
        Data = IngresarDatos(Data)
    else:
        Data = ModificarDatos(Data)
        
    return Data

def GetValues(Data):
    Data = pd.DataFrame(Data)
    Data = Data['Value'].to_numpy()
    Data = Data.astype(np.float64)
    
    return Data.T
  

while True:
    ClearW()
    print('Selecciona un tipo de analisis\n\n1. \n2. \n3 \ne.')
    AnalysisType = input('Opcioón: ')
    if AnalysisType == 'e':
        print('Bye!')
        break
    elif AnalysisType == '1':
        while True:
            op = input('\ni. Ingresar Datos\nm. Modificar Datos\na. Analisis\ne. Salir\nOpcion: ')
            if op =='i':
                 while True:
                    op = input('\nIngresar: \n1. Dimensiones\n2. Esfuerzos\n3. Propiedades\n4. Angulo\ne. Salir\nOpcion: ')
                    if op =='1':
                        Dimentions = InputDimention(False)
                        print(GetValues(Dimentions))
                    elif op=='2':
                        Esfuerzos = InputEsfuerzos(False)
                    elif op =='3':
                        Propiedades = InputPropiedades(False)
                    elif op =='4':
                        Angulo = input('Angulo: ')
                    elif op=='e':
                        break
                    else:
                        print('Opcion No valida')
            elif op =='m':
                while True:
                    op = input('\nModificar:\n\n\t1. Dimensiones\n\t2. Esfuerzos\n\t3. Propiedades\n\te. Salir\n\nOpcion: ')
                    if op =='1':
                        try:
                            Dimentions = ModificarDatos(Dimentions)
                        except:
                            print('\n\tNo hay valores')
                    elif op=='2':
                        try:
                            Esfuerzos = ModificarDatos(Esfuerzos)
                        except:
                            print('\n\tNo hay valores')
                    elif op =='3':
                        try:
                            Propiedades = ModificarDatos(Propiedades)
                        except:
                            print('\n\tNo hay valores')
                    elif op=='e':
                        break
                    else:
                        print('\n\tOpcion No valida')
            elif op =='a':
                try:
                    D = Matrix.MD(Angulo)
                    Tp = Matrix.MTp(Angulo)
                except:
                    print('\n\tFalta el Angulo')
            elif op =='e':
                pass
            else:
                print('Opcion No valida')
    else:
        print('\n\tOpcion No valida')