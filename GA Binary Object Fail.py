import random
import math
from prettytable import PrettyTable

# Jumlah populasi yang akan di gunakan
populationSize = 100
# lL berarti Lower Limit atau batas bawah, sedangkan uL berarti batas atas
lL1 = -1
uL1 = 2
lL2 = -1
uL2 = 1
# genLength adalah 1/2 dari panjang sebuah Chromosome, genLength juga memegang value x1/x2
genLength = 4
chromosomeLength = genLength * 2


# Inisialisasi kromosom
def initChromosome(l=chromosomeLength):
    chromosome = []
    for _ in range(l):
        chromosome.append(random.randint(0, 1))
    return chromosome


# Dekode kromosom
# Parameter c adalah sebuah Chromosome
def decodeChromosome(c):
    # clength bisa diganti sama genLength atau chromosomeLength
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
    # print("mestinya aman :", -(math.cos(x1) * math.sin(x2) - (x1 / (x2 ** 2 + 1))))
    return -(math.cos(x1) * math.sin(x2) - (x1 / (x2 ** 2 + 1)))


def firstPopulation(popSize):
    population = []
    for _ in range(popSize):
        population.append(DNA(initChromosome()))
    return population


# Pemilihan orangtua
def parentTournamentSelection(population, tSize=5):
    winner = None
    # t = PrettyTable(['Chromosome', 'Fitness'])
    randomNum = random.sample(range(0, len(population) - 1), 5)
    for i in randomNum:
        DNA = population[i]
        # tempChromosome = "".join(str(j) for j in DNA.chromosome)
        # tempFitness = DNA.fitness
        # t.add_row([tempChromosome, tempFitness])
        if (winner == None or DNA.calculateFitness > winner.fitness):
            winner = DNA
    # print(t)
    return winner


# Crossover (pindah silang)
def crossover(DNA1, DNA2, probability=0.65):
    randomProbability = random.random()
    if (randomProbability > probability):
        randomPoint = random.randint(0, chromosomeLength - 1)
        c1 = (DNA1.chromosome[0:randomPoint] + DNA2.chromosome[randomPoint:chromosomeLength])
        c2 = (DNA2.chromosome[0:randomPoint] + DNA1.chromosome[randomPoint:chromosomeLength])
        return DNA(c1),DNA(c2)
    return DNA1,DNA2


# Mutasi
def mutation(DNA, probability=0.3):
    randomProbability = random.random()
    if (randomProbability > probability):
        randomIndex = random.randint(0, chromosomeLength - 1)
        DNA.chromosome[randomIndex] = 1 if (DNA.chromosome[randomIndex] == 0) else 0


# Pergantian Generasi
def changeGeneration(currentPopulation):
    newPopulation = []

    while len(newPopulation) != len(currentPopulation)-2:
        parent1 = parentTournamentSelection(currentPopulation)
        parent2 = parentTournamentSelection(currentPopulation)
        child1, child2 = crossover(parent1,parent2)
        mutation(child1)
        mutation(child2)
        newPopulation.append(child1)
        newPopulation.append(child2)
    newPopulation.append(elitism(currentPopulation))
    newPopulation.append(elitism(currentPopulation))

    return newPopulation


def elitism(population):
    best = None
    for i in range(len(population)):
        if (best == None or population[i].calculateFitness > best.fitness):
            best = population[i]
    return best

def main():
    return

def outputPopulation(x):
    t = PrettyTable(['Chromosome', 'Fitness'])
    for i in range(len(x)):
        tempChromosome = "".join(str(j) for j in x[i].chromosome)
        tempFitness = x[i].calculateFitness
        t.add_row([tempChromosome, tempFitness])
    print(t)


class DNA():
    def __init__(self,chromosome):
        self.chromosome = chromosome
        self.fitness = fitness(chromosome)


x = firstPopulation(10)
outputPopulation(x)
x = changeGeneration(x)
outputPopulation(x)
x = changeGeneration(x)
outputPopulation(x)

# x = firstPopulation(100)
# for i in range(100):
#     # outputPopulation(x)
#     # for i in x:
#     #     print("===================================================")
#     #     bad = i.fitness
#     #     good = fitness(i.chromosome)
#     #     print("Cromosome : ",i.chromosome,"--- Fitness : ",i.fitness)
#     #     print("Cromosome : ", i.chromosome, "--- Fitness : ",fitness(i.chromosome) )
#
#     print('gen', i, "--- Cromosome :","".join(str(j) for j in elitism(x).chromosome), "--- Fitness :", fitness(elitism(x).chromosome), "--- x1,x2 :", decodeChromosome(elitism(x).chromosome))
#     # print()
#     x = changeGeneration(x)




# d1 = DNA(initChromosome())
# d2 = DNA(initChromosome())
# print(d1.chromosome)
# print(d2.chromosome)
# d3,d4 = crossover(d1,d2)
# print(d3.chromosome)
# print(d4.chromosome)
# outputPopulation(x)

# for i in range(100):
#     # print("+++++++++ Chromosome > ",i)
#     # print(x[i].chromosome)
#     x1,x2 = decodeChromosome(x[i].chromosome)
#     print(x1,x2,x[i].fitness)
#     if((x1 > 2 and x1 <-1) or (x2>1 and x2<-1)):
#         print("shit +++++++++++ ",i)
#         print(x)
#         print(x1,x2)
#         print("end shit")
#
# c1 = DNA()
# c2 = DNA()
# print(c1.chromosome)
# print(c2.chromosome)
# mutation(c1)
# mutation(c2)
# print(c1.chromosome)
# print(c2.chromosome)
