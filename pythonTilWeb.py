from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
import openpyxl
from selenium.webdriver.common.by import By
import numpy as np
from help import helpUdebane, fjernNavne, helpHjemmebane


def printTable(name,cursor,conn):

    cursor.columns(table=name)
    columns = cursor.fetchall()

    for column in columns:
        column_name = column.column_name
        data_type = column.type_name
        max_length = column.column_size
        is_nullable = column.nullable

        print(f"Column Name: {column_name}")
        print(f"Data Type: {data_type}")
        print(f"Max Length: {max_length}")
        print(f"Nullable: {is_nullable}")
        print()





        conn.commit()

def pointmash(input_list):
    aggregated_dict = {}
    for group in input_list:
        # Iterate over the names and points within each group
        for name, points in group:
            if name in aggregated_dict:
                # If the name already exists in the dictionary, add the points
                aggregated_dict[name] += points
            else:
                # If the name doesn't exist, initialize it with the points
                aggregated_dict[name] = points

    # Convert the aggregated dictionary into a list of lists
    result_list = [[name, points] for name, points in aggregated_dict.items()]
    return(result_list)


def NavneLængde(liste): 
    List = []
    for i in range(len(liste)): 
        List.append(len(liste[i])) 
    return(List)


def people(navn,liste): 
    for i in range(len(liste)): 
        if navn == liste[i]:  
            return(i)

def udebane(x,tekst,lst): 
    klist = []
    allList = []
    for i in range(500,len(x)-13): 
        for j in range(len(lst)): 
            print(lst[j])
            point,sejre,nederlag,kampe,sæt,SingleSejr,SingleNederlag,MixNederlag,MixSejr,DoubleSejr,DoubleNederlag,TosætSejr,TresætSejr,TosætNederlag,TresætNederlag,PointKampe,ModstanderPointKampe,Vundet_18,Vundet_19,Vundet_20,tabt_18,tabt_19,tabt_20,Under_10,Under_5,Givet_10,Givet_5,Vundet_modstanderFlestPoint,Tabt_vundetFlestPoint = helpUdebane(x,lst[j],tekst)
            klist.append([lst[j],point])
            allList.append([lst[j],point,sejre,nederlag,kampe,sæt,SingleSejr,SingleNederlag,MixNederlag,MixSejr,DoubleSejr,DoubleNederlag,TosætSejr,TresætSejr,TosætNederlag,TresætNederlag,PointKampe,ModstanderPointKampe,Vundet_18,Vundet_19,Vundet_20,tabt_18,tabt_19,tabt_20,Under_10,Under_5,Givet_10,Givet_5,Vundet_modstanderFlestPoint,Tabt_vundetFlestPoint])
        return(klist,allList)
def hjemmebane(x,tekst,lst): 
    klist = []
    allList = []
    for i in range(500,len(x)-13): 
        for j in range(len(lst)): 
            point,sejre,nederlag,kampe,sæt,SingleSejr,SingleNederlag,MixNederlag,MixSejr,DoubleSejr,DoubleNederlag,TosætSejr,TresætSejr,TosætNederlag,TresætNederlag,PointKampe,ModstanderPointKampe,Vundet_18,Vundet_19,Vundet_20,tabt_18,tabt_19,tabt_20,HjemmeSejre,HjemmeNederlag,UdeSejre,UdeNederlag,Herlev,ar,Under_10,Under_5,Givet_10,Givet_5,Vundet_modstanderFlestPoint,Tabt_vundetFlestPoint= helpHjemmebane(x,lst[j],tekst)
            klist.append([lst[j],point])
            allList.append([lst[j],point,sejre,nederlag,kampe,sæt,SingleSejr,SingleNederlag,MixNederlag,MixSejr,DoubleSejr,DoubleNederlag,TosætSejr,TresætSejr,TosætNederlag,TresætNederlag,PointKampe,ModstanderPointKampe,Vundet_18,Vundet_19,Vundet_20,tabt_18,tabt_19,tabt_20,Under_10,Under_5,Givet_10,Givet_5,Vundet_modstanderFlestPoint,Tabt_vundetFlestPoint])
        return(klist,allList)


def kørSpil(x,y,lst) :
    lstt = []
    endnu = []
    for i in range(len(x)): 
            PATH = "C:\webdrivers\chromedriver.exe" 
            driver = webdriver.Chrome(PATH)
            driver.get(x[i])
            #refuse = driver.find_element(by=By.ID, value ="didomi-notice-agree-button")
            #refuse.click()
            #driver.implicitly_wait(10)
            main = driver.find_element_by_id("aspnetForm")
            tekst = str(main.text)
            finalTekst = (fjernNavne(tekst))
            print(finalTekst)
            lstt.append(udebane(finalTekst,tekst,lst)[0])
            endnu.append(udebane(finalTekst,tekst,lst)[1])
    for j in range(len(y)):
            
            PATH = "C:\webdrivers\chromedriver.exe" 
            driver = webdriver.Chrome(PATH)
            driver.get(y[j])
            #refuse = driver.find_element(by=By.ID, value ="didomi-notice-agree-button")
            #refuse.click()
            #driver.implicitly_wait(10)
            main = driver.find_element_by_id("aspnetForm")
            tekst = str(main.text)
            finalTekst = (fjernNavne(tekst))
            print(finalTekst)
            lstt.append(hjemmebane(finalTekst,tekst,lst)[0])
            print(y)
            endnu.append(hjemmebane(finalTekst,tekst,lst)[1])
    pointy = pointmash(lstt)
    #print(pointmash(endnu))
    return(pointy,endnu)
                #print("Hejmmebane holdkamp opdateret nummer",i, "\n")
            
#print(kørSpil(udebanelinks,["Asger Feldbæk Nielsen","Sebastian Magnussen","Rasmus nnn"]))