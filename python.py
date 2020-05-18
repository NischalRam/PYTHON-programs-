import os
path=r"G:\"
l=os.listdir(path)
for e in l:
   print(f"File name {e} and the extension is{e.split('.')[1]}")
   
   
   
   program to calculatr area of circlr
   
   pi=3.14
   r=float(input("Enter the radius of the circle:"))
   area=pi*r**2
   print("area of the circle is",area)
