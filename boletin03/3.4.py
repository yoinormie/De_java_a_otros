total=int(input("Total €: "))
bill100=total//100
total=total%100
bill20=total//20
total=total%20
bill5=total//5
mon=total%5
print ("Billetes 100: "+str(bill100)+"\nBilletes 20: "+str(bill20)+"\nBilletes 5: "+str(bill5)+"\nMonedas 1€: "+ str(mon))