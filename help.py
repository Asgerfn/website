import re 
from selenium import webdriver


def help21(Herlev,Modstander):
    Under = False
    nyHerlev =[]
    nyModstander = []
    if len(Herlev) == 3: 
        if int(Herlev[0]) > int(Modstander[0]) and int(Herlev[1]) > int(Modstander[1]):
            nyHerlev.append(Herlev[0])
            nyHerlev.append(Herlev[1])
            nyModstander.append(Modstander[0])
            nyModstander.append(Modstander[1])
        elif int(Herlev[0]) < int(Modstander[0]) and int(Herlev[1]) < int(Modstander[1]):
            nyHerlev.append(Herlev[0])
            nyHerlev.append(Herlev[1])
            nyModstander.append(Modstander[0])
            nyModstander.append(Modstander[1])
        elif int(Herlev[0]) < int(Modstander[0]) and int(Herlev[1]) > int(Modstander[1]):
            nyHerlev = Herlev
            nyModstander = Modstander
            if int(Herlev[2]) < 21 and int(Modstander[2]) < 21:
                Under = True
        elif int(Herlev[0]) > int(Modstander[0]) and int(Herlev[1]) < int(Modstander[1]):
            nyHerlev = Herlev
            nyModstander = Modstander
            if int(Herlev[2]) < 21 and int(Modstander[2]) < 21:
                Under = True
        else:
            nyHerlev = Herlev
            nyModstander = Modstander
    elif len(Herlev) < 3:      
        if int(Herlev[-1]) < 21 and int(Modstander[-1]) < 21: 
            Under = True
        else:
            nyHerlev = Herlev
            nyModstander = Modstander            
    return(nyHerlev,nyModstander,Under)

def helpHold(x,Homecourt):
    Herlev = 0
    if "Skinderskovhallen" in x: 
        Homecourt = True
    if "Herlev/Hjorten 2" in x or "Herlev Badminton 2" in x:
        Herlev = 2
    elif "Herlev/Hjorten 3" in x or "Herlev Badminton 3" in x:
        Herlev = 3
    elif "Herlev/Hjorten 4" in x or "Herlev Badminton 4" in x:
        Herlev = 4
    elif "Herlev/Hjorten 5" in x or "Herlev Badminton 5" in x: 
        Herlev = 5
    else: 
        Herlev = 1
    return(Herlev)

def helpTæt(HerlevList,ModstanderList):
    ag,ah,ai,ad,ae,af = 0,0,0,0,0,0
    for loop in range(len(HerlevList)):
        if HerlevList[loop] == "18" and ModstanderList[loop] == "21": 
            ag = ag+1
        elif HerlevList[loop] == "19" and ModstanderList[loop] == "21": 
            ah = ah+1
        elif int(HerlevList[loop]) > 19 and int(ModstanderList[loop]) > int(HerlevList[loop]) :
            ai = ai+1
        elif HerlevList[loop] == "21" and ModstanderList[loop] == "18": 
            ad = ad+1
        elif HerlevList[loop] == "21" and ModstanderList[loop] == "19": 
            ae = ae+1
        elif int(ModstanderList[loop]) > 19 and int(ModstanderList[loop]) < int(HerlevList[loop]) :
            af = af+1
    return(ag,ah,ai,ad,ae,af)

def helpFordeling(Point,bane):
    if len(Point) < 3:
        return([0],[0])
    if len(Point)%2 == 1: 
                    del Point[-1]
    if len(Point) < 1: 
        return([0],[0])      
    HSHerlevListe = []
    HSModstanderListe = []
    leng = len(Point)
    if len(Point) > 6:
        leng = 6
    if bane == False:
        for r in range(leng):
            if r%2 == 0 : 
                HSModstanderListe.append(Point[r])
            else: 
                HSHerlevListe.append(Point[r])
    elif bane == True:
        for r in range(leng):
            if r%2 == 0 : 
                HSHerlevListe.append(Point[r])
            else: 
                HSModstanderListe.append(Point[r])
    return(HSHerlevListe,HSModstanderListe)



def helpIndmad(HerlevListe,ModstanderListe,Point,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,kat,l,p,m,o,HoldSejre,ax,ay):
                    Excelx = sum(map(int,HerlevListe))+Excelx
                    y = sum(map(int,ModstanderListe))+y
                    e = e+1
                    sejr = False
                    nyHerlev,nyModstander,Under = help21(HerlevListe,ModstanderListe)
                    
                    if Under == True: 
                        return(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                    if HerlevListe != nyHerlev:
                        HerlevListe.pop(-1) and ModstanderListe.pop(-1)
                    if len(HerlevListe) == 0: 
                        return(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                    if int(HerlevListe[-1]) < 21 and int(ModstanderListe[-1]) < 21: 
                        return(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                    ag,ah,ai,ad,ae,af = helpTæt(HerlevListe,ModstanderListe)
                    
                    if len(set(Point)) == 2:
                        if len(HerlevListe) == 3:
                                    point = point+6
                        elif len(HerlevListe) == 2: 
                            point = point+3
                    if "30" in (HerlevListe):
                        point = point+5   
                    if int(HerlevListe[-1]) > int(ModstanderListe[-1]) : 
                        wins = wins +1
                        sejr = True
                        if sum(map(int,HerlevListe)) < sum(map(int,ModstanderListe)):
                            point = point+3
                            ax = ax+1
                        if Homecourt == True: 
                            HjemmeSejre = HjemmeSejre+1
                        else: 
                            UdeSejre = UdeSejre+1
                        if len(ModstanderListe) == 3 and len(ModstanderListe) == 3: 
                                point=point+4 
                                c = c+1
                                f = f+3
                                s = s+1
                                if (int(HerlevListe[0])+int(HerlevListe[1])+int(HerlevListe[2])+int(ModstanderListe[0])+int(ModstanderListe[1])+int(ModstanderListe[2])) > 124:
                                        point = point+3
                        elif len(ModstanderListe) == 2 and len(ModstanderListe) == 2 : 
                                point=point+5
                                c = c+1
                                f = f+2
                                Excelr = Excelr+1
                                if (int(HerlevListe[0])+int(HerlevListe[1]))+(int(ModstanderListe[0])+int(ModstanderListe[1])) > 89:
                                        point = point+3
                    else: 
                        if Homecourt == True: 
                            HjemmeNederlag = HjemmeNederlag+1
                        else: 
                            UdeNederlag = UdeNederlag+1
                        if sum(map(int,HerlevListe)) > sum((map(int,ModstanderListe))):
                            point = point+3
                            ay = ay+1
                        if len(HerlevListe) == 3:
                                point=point+2
                                f = f+3
                                u = u+1
                                excelD = excelD+1
                        else: 
                                point=point+1
                                f = f+2      
                                t = t+1
                                excelD = excelD+1
                    for j in range(len(HerlevListe)): 
                        if int(HerlevListe[j]) < 6: 
                            point = point-5
                            au = au+1
                        elif int(HerlevListe[j]) < 11: 
                            point = point-3
                            at = at+1
                        if int(ModstanderListe[j]) < 6:
                            point = point+5
                            aw = aw+1
                        elif int(ModstanderListe[j]) <11:
                            point = point +3 
                            av = av+1
                    if (kat == "DS") or (kat == "HS"): 
                        if sejr == True: 
                            ExcelI = 1
                        else: 
                            ExcelJ = 1
                    if kat == "MD": 
                        if sejr == True: 
                            m = 1
                        else: 
                            l = 1
                    if (kat == "HD") or (kat == "DD"): 
                        if sejr == True: 
                            o = 1
                        else: 
                            p = 1      
                    if wins == 2: 
                        point = point+2
                    if wins == 2 and HoldSejre != [0,0] :
                        if int(HoldSejre) < 5:
                            point = point+6
                    elif wins == 1 and HoldSejre != [0,0]: 
                        if int(HoldSejre) < 4: 
                            point = point+3
                
                    return(Point,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay)
                
def helpResultat(x,point,homecourt):
    pattern = "[0-9]+"
    HoldSejre = 0
    for j in range(len(x)-10):
        if x[j:j+8] == "Resultat": 
            Holdkampsresultat = (re.findall(pattern,x[j+9:j+14]))
            if Holdkampsresultat == []: 
                return(0,[0,0])
            if homecourt == False:
                HoldSejre = Holdkampsresultat[-1]
                if int(Holdkampsresultat[-1]) == 0: 
                    point = point-5
                elif int(Holdkampsresultat[-1]) > 6: 
                    point = point+4
                elif int(Holdkampsresultat[-1]) == 13: 
                    point = point+10
                else: 
                    point = point+2
            elif homecourt == True: 
                HoldSejre = Holdkampsresultat[0]
                if int(Holdkampsresultat[0]) == 0: 
                    point = point-5
                elif int(Holdkampsresultat[0]) > 6: 
                    point = point+4
                elif int(Holdkampsresultat[0]) == 13: 
                    point = point+10
                else: 
                    point = point+2

    return(point,HoldSejre)
def helpUdebane(x:str,navn:str,ifhjemmebane):
    pattern = "[0-9]+"
    ar,wins,at,au,av,aw,Herlev,HjemmeSejre,HjemmeNederlag,UdeSejre,UdeNederlag, point, HD, MD, DD, excelD, c,e,f, ExcelI, ExcelJ,l,m,o,p,Excelr,s,t,Excelx,y,u,ad,af,ae,ag,ah,ai,HjemmeSejre,HjemmeNederlag,UdeSejre,UdeNederlag,HS,DS,ax,ay = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    Homecourt = False 
    Herlev = helpHold(ifhjemmebane,Homecourt)
    antal = 0
    if "protestafgørelse" in ifhjemmebane: 
        print("protest")
        return(0)
    for i in range(len(x)-20):  
        if x[i:i+len(navn)] == navn:
            if antal == 0:  
                point,HoldSejre= helpResultat(x,point,Homecourt)
                antal = 1
            ar = ar+1/2
            for k in range(80):
                if "HS" in x[i-k-2:i-k]: 
                    if HS < 1: 
                        HS = 2
                        HSPoint = (re.findall(pattern,x[i:i+50+len(navn)]))
                        HSHerlevListe,HSModstanderListe = helpFordeling(HSPoint,False)
                        if len(HSHerlevListe) and len(HSModstanderListe) > 1:
                            HSPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay = helpIndmad(HSHerlevListe,HSModstanderListe,HSPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"HS",l,p,m,o,HoldSejre,ax,ay)
                elif "HD" in x[i-k-2:i-k]: 
                    if HD < 1: 
                        HD = 2
                        HDPoint = (re.findall(pattern,x[i:i+80+len(navn)]))
                        HDHerlevListe,HDModstanderListe = helpFordeling(HDPoint,False)
                        if len(HDHerlevListe) and len(HDModstanderListe) > 1:
                            HDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay = helpIndmad(HDHerlevListe,HDModstanderListe,HDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"HD",l,p,m,o,HoldSejre,ax,ay)
                elif "MD" in x[i-k-2:i-k]: 
                    if MD < 1: 
                        MD = 2
                        MDPoint = (re.findall(pattern,x[i:i+80+len(navn)]))
                        MDHerlevListe,MDModstanderListe = helpFordeling(MDPoint,False)
                        if len(MDHerlevListe) and len(MDModstanderListe) > 1:
                            MDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay = helpIndmad(MDHerlevListe,MDModstanderListe,MDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"MD",l,p,m,o,HoldSejre,ax,ay)
                elif "DS" in x[i-k-2:i-k]: 
                    if DS < 1: 
                        DS = 2                 
                        DSPoint = (re.findall(pattern,x[i:i+50+len(navn)]))
                        DSHerlevListe,DSModstanderListe = helpFordeling(DSPoint,False)
                        if len(DSHerlevListe) and len(DSModstanderListe) > 1:
                            DSPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay = helpIndmad(DSHerlevListe,DSModstanderListe,DSPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"DS",l,p,m,o,HoldSejre,ax,ay)
                elif "DD" in x[i-k-2:i-k]: 
                    if DD < 1: 
                        DD = 2
                        DDPoint = (re.findall(pattern,x[i:i+80+len(navn)]))
                        DDHerlevListe,DDModstanderListe = helpFordeling(DDPoint,False)
                        if len(DDHerlevListe) and len(DDModstanderListe) > 1:
                            DDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay = helpIndmad(DDHerlevListe,DDModstanderListe,DDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"DD",l,p,m,o,HoldSejre,ax,ay)
    return(point,c,excelD,e,f,ExcelI,ExcelJ,l,m,o,p,Excelr,s,t,u,Excelx,y,ad,ae,af,ag,ah,ai,at,au,av,aw,ax,ay)
    
def helpHjemmebane(x:str,navn:str,ifhjemmebane):
    pattern = "[0-9]+"
    wins,at,au,av,aw,Herlev,HjemmeSejre,HjemmeNederlag,UdeSejre,UdeNederlag, point, HD, MD, DD, excelD, c,e,f, ExcelI, ExcelJ,l,m,o,p,Excelr,s,t,Excelx,y,u,ad,af,ae,ag,ah,ai,HjemmeSejre,HjemmeNederlag,UdeSejre,UdeNederlag,ar,HS,DS,ax,ay = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    Homecourt = True  
    antal = 0
    Herlev = helpHold(ifhjemmebane,Homecourt)
    if "protestafgørelse" in ifhjemmebane: 
        print("protest")
        return(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,ar,Herlev,0,0)
    for i in range(len(x)-20): 
        if x[i:i+len(navn)] == navn: 
            ar = ar+1/2
            if antal == 0: 
                point,HoldSejre = helpResultat(x,point,Homecourt)
            for k in range(45):
                if "HS" in x[i-3:i-1]: 
                    if HS < 1: 
                        HS = 2
                        HSPoint = (re.findall(pattern,x[i:i+70+len(navn)]))
                        HSHerlevListe,HSModstanderListe = helpFordeling(HSPoint,True)
                        if len(HSHerlevListe) and len(HSModstanderListe) > 1:
                            HSPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay = helpIndmad(HSHerlevListe,HSModstanderListe,HSPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"HS",l,p,m,o,HoldSejre,ax,ay)                        
                elif "HD" in x[i-k-2:i-k]: 
                    if HD < 1: 
                        HD = 2 
                        HDPoint = (re.findall(pattern,x[i:i+100+len(navn)]))
                        HDHerlevListe,HDModstanderListe = helpFordeling(HDPoint,True)
                        if len(HDHerlevListe) and len(HDModstanderListe) > 1:
                            HDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay = helpIndmad(HDHerlevListe,HDModstanderListe,HDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"HD",l,p,m,o,HoldSejre,ax,ay)
                elif "MD" in x[i-k-2:i-k]: 
                    if MD < 1: 
                        MD = 2
                        MDPoint = (re.findall(pattern,x[i:i+100+len(navn)]))
                        MDHerlevListe,MDModstanderListe = helpFordeling(MDPoint,True)
                        if len(MDHerlevListe) and len(MDModstanderListe) > 1:
                            MDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av ,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay= helpIndmad(MDHerlevListe,MDModstanderListe,MDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"MD",l,p,m,o,HoldSejre,ax,ay)                        
                elif "DS" in x[i-3:i-1]: 
                    if DS < 1: 
                        DS = 2
                        DSPoint = (re.findall(pattern,x[i:i+70+len(navn)]))
                        DSHerlevListe,DSModstanderListe = helpFordeling(DSPoint,True)
                        if len(DSHerlevListe) and len(DSModstanderListe) > 1:
                            DSPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay = helpIndmad(DSHerlevListe,DSModstanderListe,DSPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"DS",l,p,m,o,HoldSejre,ax,ay)
                elif "DD" in x[i-k-2:i-k]: 
                    if DD < 1: 
                        DD = 2
                        DDPoint = (re.findall(pattern,x[i:i+100+len(navn)]))
                        DDHerlevListe,DDModstanderListe = helpFordeling(DDPoint,True)
                        if len(DDHerlevListe) and len(DDModstanderListe) > 1:
                            DDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,l,p,m,o,ag,ah,ai,ad,ae,af,ax,ay = helpIndmad(DDHerlevListe,DDModstanderListe,DDPoint,Homecourt,e,aw,c,f,ExcelI,s,Excelr,point,HjemmeNederlag,HjemmeSejre,UdeNederlag,wins,u,excelD,t,Excelx,y,UdeSejre,av,ExcelJ,at,au,"DD",l,p,m,o,HoldSejre,ax,ay)
    return(point,c,excelD,e,f,ExcelI,ExcelJ,l,m,o,p,Excelr,s,t,u,Excelx,y,ad,ae,af,ag,ah,ai,HjemmeSejre,HjemmeNederlag,UdeSejre,UdeNederlag,Herlev,ar,at,au,av,aw,ax,ay)

def fjernNavne(x): 
    for i in range(len(x)): 
        if x[i:i+8] == "Resultat": 
            return(x[i:-1])

