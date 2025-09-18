import pygame
import random
import math
import time
import copy

pygame.init() # pygame 초기화

# 추출
# 엘리트집단
def elet(gene):
    if len(gene) >= 8:
        return gene[:8]
    else:
        return gene
    
# 무작위 추출

def rannd(gene):
    if len(gene) >= 8:
        main = copy.copy(gene)
        next_gen = []
        random.shuffle(gene)
        p_next_gen = gene[:8]
        for i in main:
            for j in p_next_gen:
                if i == j:
                    next_gen.append(i)
        return next_gen
    else:
        return gene
# 일부다처제 -> 어느정도는 엘리트집단과 동일

def maaanny(gene):
    if len(gene) >= 8:
        next_gen = []
        next_gen.append(gene[0])
        del gene[0]
        main = copy.copy(gene)
        random.shuffle(gene)
        p_next_gen = gene[:7]
        for i in main:
            for j in p_next_gen:
                if i == j:
                    next_gen.append(i)
        return next_gen
    else:
        return gene



# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 내용 추가
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def crossbreeding(mf):
    tempsd = [[], []]
    sd = []
    if mf[0][len(mf[0])-1] == -999:
        for i in range(0, len(mf[1])):
            if mf[0][i] != -999:
                tempsd[0].append(mf[1][i]+random.randrange(abs(int((mf[1][i]-mf[0][i])/2))*-1, abs(int((mf[1][i]-mf[0][i])/2)+1)))
                tempsd[1].append(mf[1][i]+random.randrange(abs(int((mf[1][i]-mf[0][i])/2))*-1, abs(int((mf[1][i]-mf[0][i])/2)+1)))
            elif mf[1][i] == 999: break
            else:
                tempsd[0].append(mf[1][i])
                tempsd[1].append(mf[1][i])
    else:
        for i in range(0, len(mf[0])):
            try:
                if mf[1][i] != -999:
                    tempsd[0].append(mf[0][i]+random.randrange(abs(int((mf[0][i]-mf[1][i])/2))*-1, abs(int((mf[0][i]-mf[1][i])/2)+1)))
                    tempsd[1].append(mf[0][i]+random.randrange(abs(int((mf[0][i]-mf[1][i])/2))*-1, abs(int((mf[0][i]-mf[1][i])/2)+1)))
                elif mf[0][i] == 999: break
                else:
                    tempsd[0].append(mf[0][i])
                    tempsd[1].append(mf[0][i])
            except:
                break

    sd.append(tempsd[0])
    sd.append(tempsd[1])
    return sd

def randomly(fingene):
    sd = []

    num = len(fingene)
    if len(fingene)>8:
        num = 8
    elif num==1:
        sd.append(fingene[0])
        return sd
    elif num==0:
        return sd
    elif num % 2 == 1:
        num -= 1

    rand = []

    for i in range(len(fingene)):
        rand.append(i)
    
    while len(sd)<8:
        mf = []
        mf.append(fingene[rand.pop(random.randrange(0, len(rand)))])
        mf.append(fingene[rand.pop(random.randrange(0, len(rand)))])
        tempsd = crossbreeding(mf)
        sd.append(tempsd[0])
        sd.append(tempsd[1])

    return sd

def roulette(fingene):
    weight = []

    sd = []

    num = len(fingene)
    if len(fingene)>8:
        num = 8
    elif num==1:
        sd.append(fingene[0])
        return sd
    elif num==0:
        return sd
    elif num % 2 == 1:
        num -= 1

    for i in range(0, num):
        for j in range(num-i):
            weight.append(i)

    while len(weight):
        mf = []
        popping = weight[random.randrange(0, len(weight))]
        mf.append(fingene[popping])
        while weight.count(popping):
            weight.remove(popping)
        popping = weight[random.randrange(0, len(weight))]
        mf.append(fingene[popping])
        while weight.count(popping):
            weight.remove(popping)
        tempsd = crossbreeding(mf)
        sd.append(tempsd[0])
        sd.append(tempsd[1])

    return sd

def extreme(fingene):
    sd = []

    num = len(fingene)
    if len(fingene)>8:
        num = 8
    elif num==1:
        tempret = []
        tempret.append(fingene[0])
        return tempret
    elif num==0:
        return sd
    elif num % 2 == 1:
        num -= 1

    for i in range(0, num, 2):
        mf = []
        mf.append(fingene[i])
        mf.append(fingene[i+1])
        tempsd = crossbreeding(mf)
        sd.append(tempsd[0])
        sd.append(tempsd[1])
    return sd


def manywife(fingene):
    sd = []

    num = len(fingene)
    if len(fingene)>9:
        num = 9
    elif num==1:
        tempret = []
        tempret.append(fingene[0])
        return tempret
    elif num==0:
        return sd

    for i in range(1, num):
        mf = []
        mf.append(fingene[0])
        mf.append(fingene[i])
        tempsd = crossbreeding(mf)
        del(tempsd[1])
        
        try:
            for i in range(1):
                del(tempsd[len(tempsd)-1])
        except: pass
        

        sd.append(tempsd[:])
    return sd

def lineconf(cx, cy, a, yitc, ys, curve):
    if curve:
        if (cy-(cx*a+yitc))*ys > 0:
            return True
        else:
            return False
    else:
        if a == 0:
            if (cy-yitc)*ys > 0:
                return True
            else:
                return False
        else:
            if (cx-a)*ys > 0:
                return True
            else:
                return False

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


sect = 0

checkp = []
checkp.append((-1, 1150, -1, True))
checkp.append((870, 0, -1, False))
checkp.append((0.8, -488, 1, True))
checkp.append((1.25, -587.5, 1, True))
checkp.append((520, 0, -1, False))
checkp.append((390, 0, -1, False))
checkp.append((0.95, 29.5, 1, True))
checkp.append((0, 385, 1, False))
checkp.append((-1, 740, 1, True))
checkp.append((440, 0, 1, False))
checkp.append((600, 0, 1, False))
checkp.append((760, 0, 1, False))
checkp.append((910, 0, 1, False))
checkp.append((1, -565, -1, True))
checkp.append((0, 350, -1, False))
checkp.append((0, 350, 1, False))

bestgene = []
bestestcar = []
bgxy = []
bgxy_temp = [0, 0]
bgangle = [180]
bgangle_temp = [0]
bgxy.append([1055, 300])
for i in range(len(checkp)):
    bestgene.append([])


class obj(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()

class cars(pygame.sprite.Sprite):

    def __init__(self, img, x, y, angle):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()
        self.x = x  
        self.y = y
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(img)
        self.go = False
        self.dt = 5
        self.dirx = 1   
        self.diry = 1
        self.angle = angle
        self.go = True

        rotated = pygame.transform.rotate(car_image, self.angle)
        self.image = rotated
        self.rect = rotated.get_rect() # 회전한 이미지의 위치 객체
        self.rect.center = (self.x, self.y) # 위치 객체의 위치 설정


    def move(self, con):
        if not self.go : return self.x, self.y, self.angle, self.go
              
        xd = math.sin(math.radians(self.angle)) * self.dt *self.dirx
        yd = math.cos(math.radians(self.angle)) * self.dt *self.diry
        self.x += xd
        self.y += yd

        rotated = pygame.transform.rotate(car_image, self.angle)
        self.image = rotated
        self.rect = rotated.get_rect() # 회전한 이미지의 위치 객체
        self.rect.center = (self.x, self.y) # 위치 객체의 위치 설정

        if pygame.sprite.collide_mask(line, self):
            if bestestcar == genepool[con]: return self.x, self.y, self.angle, self.go
            self.go = False
            return self.x, self.y, self.angle, self.go

        if lineconf(self.x, self.y, checkp[sect][0], checkp[sect][1], checkp[sect][2], checkp[sect][3]):
            if bestestcar == genepool[con]: return self.x, self.y, self.angle, self.go


            templist = list(genepool[con])
            if len(templist)>0:
                while templist[len(templist)-1] == -999:
                    del(templist[len(templist)-1])

            fingene.append(templist)

            if bestgene[sect]:
                if len(bestgene[sect]) > len(templist):
                    for i in range(len(templist)-1, len(templist)-8, -1):
                        xd = math.sin(math.radians(templist[i])) * self.dt *self.dirx
                        yd = math.cos(math.radians(templist[i])) * self.dt *self.diry
                        self.x -= xd
                        self.y -= yd
                        del(templist[i])

                    bestgene[sect] = list(templist)
                    bgxy_temp[0] = self.x
                    bgxy_temp[1] = self.y
                    bgangle_temp[0] = int(templist[len(templist)-1])
            else:
                for i in range(len(templist)-1, len(templist)-8, -1):
                    xd = math.sin(math.radians(templist[i])) * self.dt *self.dirx
                    yd = math.cos(math.radians(templist[i])) * self.dt *self.diry
                    self.x -= xd
                    self.y -= yd
                    del(templist[i])

                bestgene[sect] = list(templist)
                bgxy_temp[0] = self.x
                bgxy_temp[1] = self.y
                bgangle_temp[0] = int(templist[len(templist)-1])

            self.go = False

        return self.x, self.y, self.angle, self.go


screen = pygame.display.set_mode((1280, 720))
board = pygame.Surface(screen.get_size()) # 크기를 기반으로 게임판 설정
pygame.display.set_caption("자율 주행 시뮬레이션") # 게임 이름 설정

objects = pygame.sprite.Group()

line_image = pygame.image.load("line2.png").convert_alpha() # 이미지 업로드

car_image = pygame.image.load("car.png").convert_alpha() # 이미지 업로드

line = obj(line_image)
line.rect.x = 0
line.rect.y = 0
line.mask = pygame.mask.from_surface(line.image)
objects.add(line)

def inits(n, cros, extr):
    global caros, car_image, lin_image, leftimg, rightimg, midimg, genepool, lifetime, fme, fingene

    caros = pygame.sprite.Group()

    carpos = []
    genepool = []
    lifetime = []
    fingene = []

    fme = 0
    genetic = 0

    gen = n
    if cros == "manywife":
        genetic = len(extr)

    while gen:
        if genetic:
            genepool.append(extr.pop(0))
            genetic -= 1
            lifetime.append(0)
        else:
            genepool.append([])
        lifetime.append(0)
        if bestestcar:
            car = cars(car_image, bgxy[0][0], bgxy[0][1], bgangle[0])
        else:
            car = cars(car_image, bgxy[sect][0], bgxy[sect][1], bgangle[sect])
        car.mask = pygame.mask.from_surface(car.image)
        caros.add(car)

        gen -= 1
        
fme = 0
inits(64, "X", "X")


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 시뮬레이터 시작
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

generation = 1

done = True # 무한 반복을 위한 done 변수를 True로 설정

while done : # done이 True일 경우 (무한 반복)
    for event in pygame.event.get() : # 이벤트 인식
        if event.type == pygame.QUIT : # 종료 버튼을 누른 경우
            done = False # done을 False로 설정

    carpos = []

    con = 0
    for i in caros:
        tempx, tempy, angle, go = i.move(con)
        carpos.append((tempx, tempy, angle, go))
        con += 1


    con = 0
    for i in caros:
        try:
            if genepool[con][fme] != -999: pass
            if i.go:
                if genepool[con][fme] != -999:
                    i.angle = genepool[con][fme]
                    lifetime[con] += 1
                    con += 1
                    continue
                else: 
                    if genepool[con][fme] == 999: i.angle = genepool[con][fme-1]
                    i.angle += random.randrange(-30, 31)
                    genepool[con][fme] = i.angle
                    lifetime[con] += 1
                    con += 1
                    continue

            else: 
                while genepool[con][len(genepool[con])-1] == -999:
                    del(genepool[con][len(genepool[con])-1])
                genepool[con].append(-999)
        except:
            if i.go:
                i.angle += random.randrange(-30, 31)
                genepool[con].append(i.angle)
                lifetime[con] += 1
            else:
                genepool[con].append(-999)
                
            con += 1

    fme += 1

    con = 0
    stk = 0
    for i in caros:
        if i.go:
            break
        else: 
            stk += 1
            if stk == len(carpos): 
                if generation < 10:
                    print("%d 세대" % generation)
                    generation += 1
                    sd = manywife(fingene)
                    inits(64, "manywife", sd)
                else:
                    bgxy.append(list(bgxy_temp))
                    bgangle.append(bgangle_temp[0])
                    print("%d 세대" % generation)
                    print("%d 구역 종료" % sect)
                    generation = 1
                    sect += 1
                    if sect < 15:
                        inits(64, "X", "X")
                    else:
                        bestestcar = []
                        for j in bestgene:
                            for k in j:
                                if k != -999:
                                    bestestcar.append(k)
                        print(len(bestestcar))
                        print(bestestcar)
                        gg = []
                        gg.append(bestestcar)
                        inits(64, "manywife", gg)


    board.fill((255, 255, 255))
    objects.draw(board)
    caros.draw(board)
    screen.blit(board, (0, 0))

    pygame.display.flip() # 게임판을 그린다


    pygame.time.delay(1) # 딜레이 설정 (0.01초)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 현재까지 교배는 없음. 유전자 풀에는 각 프레임 마다의 개체의 각도가 유한개 담김.
# 라이프 타임에는 생존한 프레임 수가 나타남. 제너레이션은 몇 번의 세대가 지났는지를 나타냄.
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


