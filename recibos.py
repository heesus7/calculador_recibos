class Piso:
    total_volumen=float(input("ingrese el volumen de agua total = "))
    costo_agua=float(input("ingrese el costo solo del agua  = "))
    costo_alcantarillado=float(input("ingrese el costo del alcantarillado = "))
    costo_fijo=1.008
    mora=0.148

    def __init__(self,lectura):
        self.lectura=lectura

    def agua(self):
        agua_piso=self.lectura*Piso.costo_agua/Piso.total_volumen
        alcantarillado_piso=self.lectura*Piso.costo_alcantarillado/Piso.total_volumen
        igv=(agua_piso+alcantarillado_piso+Piso.costo_fijo)*0.18
        precio_total=agua_piso+alcantarillado_piso+igv+Piso.mora+Piso.costo_fijo
        return precio_total,agua_piso,alcantarillado_piso,igv

piso1=Piso(lectura=float(input("ingrese lectura del piso 1 = ")))
piso2=Piso(lectura=float(input("ingrese lectura del piso 2 = ")))
piso3=Piso(lectura=float(input("ingrese lectura del piso 3 = ")))
piso4=Piso(lectura=float(input("ingrese lectura del piso 4 = ")))
piso5=Piso(lectura=float(input("ingrese lectura del piso 5 = ")))

p1=list(piso1.agua())
p2=list(piso2.agua())
p3=list(piso3.agua())
p4=list(piso4.agua())
p5=list(piso5.agua())
total=p1[0]+p2[0]+p3[0]+p4[0]+p5[0]

print("el monto a pagar del piso 1 es = ",p1)
print("el monto a pagar del piso 2 es = ",p2)
print("el monto a pagar del piso 3 es = ",p3)
print("el monto a pagar del piso 4 es = ",p4)
print("el monto a pagar del piso 5 es = ",p5)
print("el monto total es = ",total)
