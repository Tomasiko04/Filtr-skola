
from PIL import Image

def soucet(a,b):
    return a+b


def rozdil(a,b):
    return a-b

#menu
#cyklus/volba/ aktivace fce/ návrat




def filtr1():
    obrazek = Image.open("1.jpg")
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

def filtr2():
    obrazek = Image.open("1.jpg")
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

def filtr3():
    obrazek = Image.open("1.jpg")
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

def slovnik():
  y=0
  druh={"1":"Barevný",
        "2":"Modročerný",
        "3":"Zelenočerný"}
  #print("Vyber si:")
  for key,value in druh.items():
    y+=1
    print(f"{key}. {value}")



slovnik()
while True:
  volba=input("Vyber si filtr(1/2/3): ")
  
  if volba=="1":
    filtr1()
    pokracovat=input("Chcete pokračovat(ano/ne): ").lower()
  elif volba=="2":
    filtr2()
    pokracovat=input("Chcete pokračovat(ano/ne): ").lower()
  elif volba=="3":
    filtr3()
    pokracovat=input("Chcete pokračovat(ano/ne): ").lower()
    
  else:
      print("Zadal si špatnou vstupní honotu.")

  if pokracovat=="ano":
     continue
  else:
     break
print("Program skončil.")
     
     



