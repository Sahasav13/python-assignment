RUPEES = int(input("enter rupees :"))

YEN = round(1.74*RUPEES)
USD = round(0.012*RUPEES)
DIRHAM = round(0.043*RUPEES)
EURO = round(0.011*RUPEES)
WON = round(16.94*RUPEES)

print(F"{RUPEES} Rupees is equal to \n{YEN} \n{USD} \n{DIRHAM} \n{EURO} \n{WON}") 
