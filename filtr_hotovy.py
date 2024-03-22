from PIL import Image

# menu
#cyklus/volba/ aktivace fce/ návrat

######### FUNKCE ####
# PUVODNI
def f_original(vyber_auta):
    while True:
        original=input("    Chcete tento obrázek ještě před úpravou(ano/ne): ")
        if original=="ano":
            obrazek = Image.open(vyber_auta)
            obrazek.show()
            print("="*62)
            break
        elif original=="ne":
            print("="*62)
            break
        else:
            print(" Zadal si špatnou vstupní honotu.")
            continue
 

# FILTRY
def filtr1(nejaky_obrazek):
    obrazek = Image.open(nejaky_obrazek)
    sirka, vyska = obrazek.size
    
    x = 0

    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x, y))
            prumer = int((r + g + b) / 3)
            obrazek.putpixel((x, y), (r, b, r))

            if prumer > 200:
                obrazek.putpixel((x, y), (255, 150, 255))  # Bílá pro světlé pixely
            elif 160 < prumer <= 200:
                obrazek.putpixel((x, y), (240, 210, 190))  # Teplý odstín s vyšší intenzitou
            elif 120 < prumer <= 160:
                obrazek.putpixel((x, y), (100, 200, 240))  # Chladný odstín s vyšší intenzitou
            elif 80 < prumer <= 120:
                obrazek.putpixel((x, y), (100, 130, 160))  # Střední intenzita šedé

            elif prumer <= 40:
                obrazek.putpixel((x, y), (140, 30, 30))      # Mírně do červena s vyšší intenzitou pro tmavé pixely

            y += 1
        x += 1

    obrazek.show()
    return obrazek

def filtr2(nejaky_obrazek):
    obrazek = Image.open(nejaky_obrazek)
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer > 150:
               obrazek.putpixel((x,y), (50, 255, 255))
            else:
               obrazek.putpixel((x,y), (0, 0, 0))
            y += 1
        x += 1
    obrazek.show()

def filtr3(nejaky_obrazek):
    obrazek = Image.open(nejaky_obrazek)
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer > 150:
                obrazek.putpixel((x,y), (150, 205, 0))
            else:
                obrazek.putpixel((x,y), (0, 60, 80))
            y += 1
        x += 1
    
    obrazek.show()

###### slovnik filtru  ###### 
def slovnik_filtr():
  y=0
  filtr={"1":"Barevný",
        "2":"Modročerný",
        "3":"Zelenočerný"}
  #print("Vyber si:")

  for key,value in filtr.items():
    y+=1
    print(f"{key}. {value}")

##### slovnik aut     ######
    # zde muho do slovníku i do budoucna přidávat hodnoty (třeba)

auta={"1":"BMW",
      "2":"Mercedes",
      "3":"Felicie"}

def slovnik_aut(auta):
   for key,value in auta.items():
      
      print(f"{key}. {value}")
    
#################   program            ###########################

o=0

### VYBER FOTKY ###
while o<2:
    o=0
    while True:
             
        slovnik_aut(auta)
        vyber_auta=input("  Jaký obrazek si přeješ upravit(1/2/3):")
        

        if vyber_auta=="1":
            vyber="1.jpg"
            f_original(vyber)
            
            break

        elif vyber_auta=="2":
            vyber="2.jpg"
            f_original(vyber)
            break

        elif vyber_auta=="3":
            vyber="images 2.jpg"
            f_original(vyber)
            break
        else:
            print(" Zadal si špatnou vstupní honotu.")
            continue
        

### VYBER FILTRU ###
    
    while True :

        slovnik_filtr()
        volba=input("   Vyber si filtr(1/2/3): ")
        
        if volba=="1":
            filtr1(vyber)
            break
        elif volba=="2":
            filtr2(vyber)
            break
        elif volba=="3":
            filtr3(vyber)
            break
            
        else:
            print(" Zadal si špatnou vstupní honotu.")
            continue
    while True:
        print("="*62)
        pokracovat=input("Chcete pokračovat(ano/ne): ").lower()
        if pokracovat=="ano":
            
            print("="*62)
            break
        elif pokracovat=="ne":
            o+=2
            print("="*62)
            break
        else:
            print(" Zadal si špatnou vstupní honotu.")

print("Program skončil.")