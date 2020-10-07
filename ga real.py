import random
#Jumlah populasi yang akan di gunakan
JUMLAH_POPULASI = 100
# lL berarti Lower Limit atau batas bawah, sedangkan uL berarti batas atas
lL1 = -1
uL1 = 2
lL2 = -1
uL2 = 1
genLength = 4


#Inisialisasi kromosom
def initCromosom(l = genLength*2):
    cromosom = []
    for _ in range(l):
        cromosom.append(random.random())
    return cromosom

# Dekode kromosom
# Parameter c adalah sebuah cromosom
def decodeCromosom(c):
    cLength = int(len(c))
    cLengthHalf = int(len(c)/2)
    x1 = lL1 + (((uL1 - lL1) / genLength) * sum(c[0:cLengthHalf]))
    x2 = lL2 + (((uL2 - lL2) / genLength) * sum(c[cLengthHalf:cLength]))
    return x1,x2

# Perhitungan fitness
def fitness():
    return 0

# Pemilihan orangtua
def parentSelection():
    return 0

# Crossover (pindah silang)
def crossover(c1,c2,a = 0.5):

    return 0
# Mutasi
def mutation():
    return 0
# Pergantian Generasi
def changeGeneration():
    return 0

x = initCromosom()
print(x)
x1,x2 = decodeCromosom(x)
print(x1,x2)
