import random
import math
from prettytable import PrettyTable


populationSize = 50

# lL berarti Lower Limit atau batas bawah, sedangkan uL berarti batas atas
lL1 = -1
uL1 = 2
lL2 = -1
uL2 = 1

# genLength adalah 1/2 dari panjang sebuah Chromosome, genLength juga memegang value x1/x2
genLength = 6
chromosomeLength = genLength * 2

crossoverProbability = 0.64
mutationProbability = 0.1

fitnessThreshold = 4.060769704837473

tournamentSize = 5


def initChromosome(length=chromosomeLength):
    chromosome = []
    for _ in range(length): chromosome.append(random.randint(0, 1))
    return chromosome


def decodeChromosome(chromosome):

    cLength = int(len(chromosome))
    cLengthHalf = int(len(chromosome) / 2)
    tempChromosome = chromosome.copy()
    sumGen = 0

    for i in range(cLengthHalf):
        tempChromosome[i] = chromosome[i] * (2 ** -(i + 1))
        tempChromosome[i + cLengthHalf] = chromosome[i + cLengthHalf] * (2 ** -(i + 1))
        sumGen += (2 ** -(i + 1))

    x1 = lL1 + ((uL1 - lL1) / sumGen) * sum(tempChromosome[0:cLengthHalf])
    x2 = lL2 + ((uL2 - lL2) / sumGen) * sum(tempChromosome[cLengthHalf:cLength])
    del tempChromosome
    return x1, x2


def calculateFitness(chromosome):
    x1, x2 = decodeChromosome(chromosome)
    return 2 ** -(math.cos(x1) * math.sin(x2) - (x1 / (x2 ** 2 + 1)))


def firstPopulation(popSize=populationSize):
    population = []
    for _ in range(popSize):
        population.append(initChromosome())
    return population


def parentTournamentSelection(population, tSize=tournamentSize):
    winner = None
    randomNum = random.sample(range(0, len(population) - 1), tSize)
    for i in randomNum:
        chromosome = population[i]
        if winner is None or calculateFitness(chromosome) > calculateFitness(chromosome):
            winner = chromosome
    return winner


def crossoverOnePoint(chromosome1, chromosome2, probability=crossoverProbability):
    randomProbability = random.random()
    if (randomProbability <= probability):
        randomPoint = random.randint(0, chromosomeLength - 1)
        child1 = (chromosome1[0:randomPoint] + chromosome2[randomPoint:chromosomeLength])
        child2 = (chromosome2[0:randomPoint] + chromosome1[randomPoint:chromosomeLength])
        return child1, child2
    return chromosome1, chromosome2


def crossoverTwoPoint(chromosome1, chromosome2, probability=crossoverProbability):
    randomProbability = random.random()
    if (randomProbability <= probability):
        randomPoint = random.sample(range(0, chromosomeLength - 1), 2)
        randomPoint.sort()
        child1 = (chromosome1[0:randomPoint[0]] + chromosome2[randomPoint[0]:randomPoint[1]] + chromosome1[randomPoint[1]:chromosomeLength])
        child2 = (chromosome2[0:randomPoint[0]] + chromosome1[randomPoint[0]:randomPoint[1]] + chromosome2[randomPoint[1]:chromosomeLength])
        return child1, child2
    return chromosome1, chromosome2


def crossoverThreePoint(chromosome1, chromosome2, probability=crossoverProbability):
    randomProbability = random.random()
    if (randomProbability <= probability):
        randomPoint = random.sample(range(0, chromosomeLength - 1), 3)
        randomPoint.sort()
        child1 = (chromosome1[0:randomPoint[0]] + chromosome2[randomPoint[0]:randomPoint[1]] + chromosome1[randomPoint[1]:randomPoint[2]] + chromosome2[randomPoint[2]:chromosomeLength])
        child2 = (chromosome2[0:randomPoint[0]] + chromosome1[randomPoint[0]:randomPoint[1]] + chromosome2[randomPoint[1]:randomPoint[2]] + chromosome1[randomPoint[2]:chromosomeLength])
        return child1, child2
    return chromosome1, chromosome2


def mutation(chromosome, probability=mutationProbability):
    randomProbability = random.random()
    if (randomProbability <= probability):
        randomIndex = random.randint(0, chromosomeLength - 1)
        chromosome[randomIndex] = 1 if (chromosome[randomIndex] == 0) else 0


def changeGeneration(currentPopulation):
    newPopulation = []

    while len(newPopulation) != len(currentPopulation) - 2:
        parent1 = parentTournamentSelection(currentPopulation)
        parent2 = parentTournamentSelection(currentPopulation)
        while parent1 == parent2:
            parent2 = parentTournamentSelection(currentPopulation)
        child1, child2 = crossoverThreePoint(parent1, parent2)

        mutation(child1)
        mutation(child2)

        newPopulation.append(child1)
        newPopulation.append(child2)

    newPopulation.append(elitismFirstBest(currentPopulation))
    newPopulation.append(elitismSecondBest(currentPopulation))

    return newPopulation


def elitismFirstBest(population):
    best = None
    for i in range(len(population)):
        if (best == None or calculateFitness(population[i]) > calculateFitness(best)):
            best = population[i]
    return best


def elitismSecondBest(population):
    best = elitismFirstBest(population)
    best2nd = None
    for i in range(len(population)):
        if (best2nd == None or (calculateFitness(population[i]) > calculateFitness(best2nd) and calculateFitness(population[i]) < calculateFitness(best) and population[i] != best)):
            best2nd = population[i]
    return best2nd


def outputPopulation(x):
    t = PrettyTable(['Chromosome', 'Fitness'])
    for i in range(len(x)):
        tempChromosome = "".join(str(j) for j in x[i])
        tempFitness = calculateFitness(x[i])
        t.add_row([tempChromosome, tempFitness])
    print(t)

# +++++++++++++++++ MAIN PROGRAM +++++++++++++++++
bestFromRun = []
x = firstPopulation()
print('gen', 0, "--- Cromosome :", "".join(str(j) for j in elitismFirstBest(x)),
      "--- Fitness :", calculateFitness(elitismFirstBest(x)),
      "--- x1,x2 :", decodeChromosome(elitismFirstBest(x)))
i = 0

while calculateFitness(elitismFirstBest(x)) < fitnessThreshold:
    i += 1
    x = changeGeneration(x)
    bestFromRun.append(elitismFirstBest(x))
    print('gen', i, "--- Cromosome :", "".join(str(j) for j in elitismFirstBest(x)),
          "--- Fitness :", calculateFitness(elitismFirstBest(x)),
          "--- x1,x2 :", decodeChromosome(elitismFirstBest(x)))

print("============== Best From Run ==============")
chosenOne = elitismFirstBest(bestFromRun)
print("Cromosome    : ", "".join(str(i) for i in chosenOne))
print("Fitness      : ", calculateFitness(chosenOne))
print("X1,X2        : ", decodeChromosome(chosenOne))
