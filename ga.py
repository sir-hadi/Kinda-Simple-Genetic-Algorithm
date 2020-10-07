import random
import math
from prettytable import PrettyTable

# Jumlah populasi yang akan di gunakan
JUMLAH_POPULASI = 100
# lL berarti Lower Limit atau batas bawah, sedangkan uL berarti batas atas
lL1 = -1
uL1 = 2
lL2 = -1
uL2 = 1
# genLength adalah 1/2 dari panjang sebuah Chromosome, genLength juga memegang value x1/x2
genLength = 4


# Inisialisasi kromosom
def initChromosome(l=genLength * 2):
    chromosome = []
    for _ in range(l):
        chromosome.append(random.randint(0, 1))
    return chromosome


# Dekode kromosom
# Parameter c adalah sebuah Chromosome
def decodeChromosome(c):
    cLength = int(len(c))
    cLengthHalf = int(len(c) / 2)
    tempC = c.copy()
    sumGen = 0

    for i in range(cLengthHalf):
        # print("+++++++++++ > ",i)
        tempC[i] = c[i] * (2 ** -(i + 1))
        tempC[i + cLengthHalf] = c[i + cLengthHalf] * (2 ** -(i + 1))
        # print("this is tempc > ",tempC)
        sumGen += (2 ** -(i + 1))
        # print("this is sum gen > ",sumGen)

    x1 = lL1 + ((uL1 - lL1) / sumGen) * sum(tempC[0:cLengthHalf])
    x2 = lL2 + ((uL2 - lL2) / sumGen) * sum(tempC[cLengthHalf:cLength])
    del tempC
    return x1, x2


# Perhitungan fitness
def fitness(c):
    x1, x2 = decodeChromosome(c)
    return -(math.cos(x1) * math.sin(x2) - (x1 / (x2 ** 2 + 1)))


def createPopulation(popSize):
    population = []
    for _ in range(popSize):
        population.append(DNA())
    return population


# Pemilihan orangtua
def parentTournamentSelection(pop, tSize=5):
    winner = None
    # t = PrettyTable(['Chromosome', 'Fitness'])
    randomNum = random.sample(range(0, len(pop) - 1), 5)
    for i in randomNum:
        DNA = pop[i]
        # tempChromosome = "".join(str(j) for j in DNA.chromosome)
        # tempFitness = DNA.fitness
        # t.add_row([tempChromosome, tempFitness])
        if (winner == None or DNA.fitness > winner.fitness):
            winner = DNA
    # print(t)
    return winner


# Crossover (pindah silang)
def crossover(c1, c2, a=0.5):
    return 0


# Mutasi
def mutation():
    return 0


# Pergantian Generasi
def changeGeneration():
    return 0


def outputPopulation(x):
    t = PrettyTable(['Chromosome', 'Fitness'])
    for i in range(len(x)):
        tempChromosome = "".join(str(j) for j in x[i].chromosome)
        tempFitness = x[i].fitness
        t.add_row([tempChromosome, tempFitness])
    print(t)


class DNA():
    def __init__(self):
        self.chromosome = initChromosome()
        self.fitness = fitness(self.chromosome)


x = createPopulation(10)
winner = parentTournamentSelection(x)
print("Parrent >> ", "".join(str(i) for i in winner.chromosome))
outputPopulation(x)

for i in range(20):
    # print("+++++++++ Chromosome > ",i)
    x.append(DNA())
    print(x[i].chromosome)
    x1,x2 = decodeChromosome(x[i].chromosome)
    print(x1,x2,x[i].fitness)
    if((x1 > 2 and x1 <-1) or (x2>1 and x2<-1)):
        print("shit +++++++++++ ",i)
        print(x)
        print(x1,x2)
        print("end shit")
