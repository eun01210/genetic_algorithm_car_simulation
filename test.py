import random
import time

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 선행 작업 - 유전자 생성, 형질 설정 (실제로는 입력 받을 내용)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

dna = 10
genepool = []
gene = 64
smartgene = 8
genetrait = []

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 유전자를 n개 생성하는 함수
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def creatgene(n, dna):
    genepool = []
    for i in range(n):
        genepool.append([])

    for i in range(dna):
        for j in range(0, n):
            randna = random.randint(1, 10)
            genepool[j].append(randna)
    
    return genepool
    
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 형질 순서 매기기 함수
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def retrait(genepool):
    genetrait = []

    for i in range(0, len(genepool)):
        temptr = 0
        for j in genepool[i]:
            temptr += j
        genetrait.append(temptr)

    return genetrait

genepool = creatgene(gene, dna)
genetrait = retrait(genepool)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 순위를 반환하는 함수 (선발 방식 1에 활용)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def rank(genetrait):
    ranking = []
    for i in range(len(genetrait)):
        ranking.append(0)
    for i in range(len(genetrait)):
        for j in range(len(genetrait) ):
            if i==j: continue
            elif genetrait[i] > genetrait[j]: ranking[j]+=1
    for i in range(len(ranking)):
        while ranking.count(i) >= 2:
            ranking[ranking.index(i)] += 1

    return ranking

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 교배 함수
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def crossbreeding(mf):
    tempsd = [[], []]
    sd = []
    for i in range(0, len(mf[0])):
        mfr = random.randint(0, 1)
        tempsd[0].append(mf[mfr][i])
        mfr = random.randint(0, 1)
        tempsd[1].append(mf[mfr][i])
        sd.append(tempsd[0])
        sd.append(tempsd[1])
    return sd

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 극단적 성 선택 교배 함수 (교배 방식 1)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def extreme(genepool, genetrait):
    ranking = rank(genetrait)
    sd = []
    for i in range(0, smartgene, 2):
        mf = []
        mf.append(genepool[ranking.index(i)])
        mf.append(genepool[ranking.index(i+1)])
        tempsd = crossbreeding(mf)
        sd.append(tempsd[0])
        sd.append(tempsd[1])
    return sd
        
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 무작위 선택 교배 함수 (교배 방식 2)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def randomly(genepool):
    rand = []
    for i in range(len(genepool)):
        rand.append(i)
    
    sd = []
    while len(sd)<8:
        mf = []
        mf.append(genepool[rand.pop(random.randrange(0, len(rand)))])
        mf.append(genepool[rand.pop(random.randrange(0, len(rand)))])
        tempsd = crossbreeding(mf)
        sd.append(tempsd[0])
        sd.append(tempsd[1])

    return sd

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 룰렛 선발 교배 함수 (교배 방식 3)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def roulette(genepool, genetrait):
    ranking = rank(genetrait)
    weight = []

    for i in range(0, 8):
        for j in range(8-i):
            weight.append(ranking.index(i))
    sd = []

    while len(weight):
        mf = []
        popping = weight[random.randrange(0, len(weight))]
        mf.append(genepool[popping])
        while weight.count(popping):
            weight.remove(popping)
        popping = weight[random.randrange(0, len(weight))]
        mf.append(genepool[popping])
        while weight.count(popping):
            weight.remove(popping)
        tempsd = crossbreeding(mf)
        sd.append(tempsd[0])
        sd.append(tempsd[1])

    return sd


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 일부 다처제 교배 함수 (교배 방식 4)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def manywife(genepool, genetrait):
    ranking = rank(genetrait)
    sd = []

    for i in range(1, 8):
        mf = []
        mf.append(genepool[ranking.index(0)])
        mf.append(genepool[ranking.index(i)])
        tempsd = crossbreeding(mf)
        sd.append(tempsd[0])
    return sd

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 교배 반복 설정 함수
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 극단적
def evalute(generation, genepool, genetrait):
    gration = 1
    while generation-gration >= 0:
        print(gration)
        genepool = extreme(genepool, genetrait)
        print(genepool)
        gration += 1
        cgene = creatgene(56, dna)
        while len(cgene):
            genepool.append(cgene.pop(0))
        genetrait = retrait(genepool)

# evalute(15, genepool, genetrait)


# 룰렛
def evalute(generation, genepool, genetrait):
    gration = 1
    while generation-gration >= 0:
        print(gration)
        genepool = roulette(genepool, genetrait)
        print(genepool)
        gration += 1
        cgene = creatgene(56, dna)
        while len(cgene):
            genepool.append(cgene.pop(0))
        genetrait = retrait(genepool)
        time.sleep(1)

# evalute(10, genepool, genetrait)

# 무작위
def evalute(generation, genepool):
    gration = 1
    while generation-gration >= 0:
        print(gration)
        genepool = randomly(genepool)
        print(genepool)
        gration += 1
        cgene = creatgene(56, dna)
        while len(cgene):
            genepool.append(cgene.pop(0))
        time.sleep(1)

# evalute(100, genepool)

# 일부 다처제
def evalute(generation, genepool, genetrait):
    gration = 1
    while generation-gration >= 0:
        print(gration)
        genepool = manywife(genepool, genetrait)
        print(genepool)
        gration += 1
        cgene = creatgene(57, dna)
        while len(cgene):
            genepool.append(cgene.pop(0))
        genetrait = retrait(genepool)
        time.sleep(1)

# evalute(10, genepool, genetrait)



def muta(arr, n):
    for i in range(0, len(arr)):
        able = random.random()
        if able<n:
            mut = random.randrange(-180, 181)
            for j in range(i, len(arr)):
                arr[j] += mut
    return arr
        

a = [180, 180, 180, 180, 180, 180]

a = muta(a, 0.99)
print(a)