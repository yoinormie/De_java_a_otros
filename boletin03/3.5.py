sueldo_fijo=float(input("Sueldo fijo: "))
itv=float(input("Importe total de ventas: "))
comision=5%itv
kilometraje=float(input ("kilometraje: "))
quilometraje=kilometraje*2
dias_desplazamiento=float(input("Días de desplazamiento: "))
dietas=30*dias_desplazamiento
IRPF=18%sueldo_fijo
rss=36
sueldo_bruto=sueldo_fijo+comision+quilometraje+dietas
print("Sueldo bruto: " +str(sueldo_bruto))
sueldo_liquido=sueldo_bruto-IRPF-rss
print("Sueldo líquido: "+str(sueldo_liquido))
