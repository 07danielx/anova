import numpy
import scipy.stats

direccion = input("Ingrese el nombre del archivo CSV: ")+".csv"
ncol=(numpy.loadtxt(open(direccion), delimiter=",")).shape[1]
aux=[None]*ncol
dataset=[None]*ncol
tamanos=[None]*ncol
medias=[None]*ncol
sumatorias=[None]*ncol
varianzas=[None]*ncol
contador=0
tratamientos=0
media_dataset=0

alfa=1-float(input("Ingrese el parámetro ALFA: "))

for columna in range(0,ncol):
	dataset[columna]=numpy.loadtxt(open(direccion), delimiter=",", usecols=columna)
	tamanos[columna]=len(dataset[columna])
	medias[columna]=sum(dataset[columna])/len(dataset[columna])
	aux[columna]=[]
	for filas1 in range(0, tamanos[columna]):
		aux[columna].append((dataset[columna][filas1]-medias[columna])**2)
	sumatorias[columna]=sum(aux[columna])
	varianzas[columna]=sumatorias[columna]/(tamanos[columna]-1)
	tratamientos=tratamientos+tamanos[columna]
	contador=contador+1
	
for columna in range(0,ncol):
	media_dataset=media_dataset+medias[columna]
media_dataset=media_dataset/ncol

sct=contador-1
scr=tratamientos-1
scf=scr-sct

ssa=0
sse=0
for columna in range(0,ncol):
	ssa=ssa+(medias[columna]-media_dataset)**2
	sse=sse+(varianzas[columna])
ssa=ssa*tamanos[1]
sse=sse*(tamanos[1]-1)
sst=ssa+sse

msa=ssa/sct
mse=sse/scf
fvalue=msa/mse

fcri=scipy.stats.f.ppf(alfa, sct, scf)

print("")
print("TABLA ANOVA")
print("Fuente		","Suma de cuadrados		","gl		","Media cuadrática		", "Valor F 	", "F crítico	")
print("Tratamientos	",str(ssa),"		",str(sct),"		",str(msa),"	",str(fvalue),"	",str(fcri))
print("Error		",str(sse),"		",str(scf),"		",str(mse))
print("Total		",str(sst),"		",str(scr))
print("")
print("Resultados:")

if(fvalue>fcri):
	print("Con un nivel de significancia del",str(alfa*100),"%, SE RECHAZA la hipótesis nula de que las medias de los tratamientos sean iguales")
else:
	print("Con un nivel de significancia del",str(alfa*100),"%, NO se rechaza la hipótesis nula y SE CONFIRMA las medias de los tratamientos sean iguales")
