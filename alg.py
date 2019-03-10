import numpy
import math
import random

# Генерируем матрицу A размером (20х20)
def GenerateMatrix():
    A = []
    A = numpy.random.randint(1, 50, size=(20, 20))
    print(A)
    return A
def Matrix():
    A = [[0, 2, 30, 9, 1],
         [4, 0, 47, 7, 7],
         [31, 33, 0, 33, 36],
         [20, 13, 16, 0, 28],
         [9, 36, 22, 22, 0]]
    return A
def Alg(A):
    distance = []
    note = []
    Tau = []
    C = []
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if i != j:
                C.append(i)
                C.append(j)
                note.append(C)
                distance.append(A[i][j])
                tau = random.randint(1, 3)
                Tau.append(tau)
            C = []
    for i in range(len(note)):
        print(str(note[i])+"  "+str(distance[i])+"   "+str(Tau[i]))
    town = []
    for i in range(0, len(note)):
        town.append(note[i][0])
    town = set(town)
    sum_town = sum(town)

    ant_value = 100
    ant_count = 0
    way = []
    distance_smallest = []
    #Муравьиный алгоритм
    while ant_count != ant_value:
        Sum = 0
        P = []
        New_tau = []
        new_tau = []
        start = note[0][0]
        zapresheny_note = []
        zapresheny_note.append(start)
        count = start
        point = []
        
        
        distance_len = 0
        
        while count != sum_town:
            tau = []
            new_tau = []
            i = 0
            P = []
            
            point.append(start)
            for i in range(0, len(note)):
                if start == note[i][0]:
                    Sum = Sum + Tau[i]**1
                    tau.append(start)
                    tau.append(note[i][1])
                    tau.append(Tau[i]**1)
                    tau.append(distance[i])
                    new_tau.append(tau)
                    tau = []
            old_note = start


            for i in range(0, len(new_tau)):
                flag = 0
                for j in range(0, len(zapresheny_note)):
                    if zapresheny_note[j] != new_tau[i][1]:
                        flag = flag + 0
                    else:
                        flag = flag + 1
                if flag == 0:
                    New_tau.append(new_tau[i])
            print(New_tau)
            if len(New_tau) != 0:       
                for k in range(0, len(New_tau)):
                    p = New_tau[k][1] / Sum
                    print(p)
                    P.append(p)
                    New_tau[k].append(p)
                ver = random.choice(P)
                for p in range(0, len(P)):
                    if ver == New_tau[p][4]:
                        new_note = New_tau[p][1]
                        distance_len = distance_len + New_tau[p][3]
                        delta_tau = 1 / New_tau[p][3]
                        for i in range(0, len(note)):
                            if (note[i][0] == New_tau[0][0]) and (note[i][1] == New_tau[0][1]):
                                Tau[i] = delta_tau
                                #print("это тау итый "+str(Tau[i]))
                                print(Tau)
                start = new_note 
                New_tau = []
                
                print(new_note)
                print("---------")
                print(str(old_note)+"->"+str(new_note))
                
                
                point.append(new_note)
                way.append(point)
                zapresheny_note.append(new_note)
                count = count + new_note
                print(zapresheny_note)
                print("----------")


                r = 0.02
                for i in range(0, len(Tau)):
                    Tau[i] = (1 - r) * Tau[i]
                
                
        
        distance_smallest.append(distance_len)
        print("примерный путь"+str(distance_len)+" км")
        print("Все города пройдены")
        ant_count = ant_count + 1
    print(distance_smallest)
    print("Массив возможных наименьших путей")
    for i in range(0, len(distance_smallest)):
        if distance_smallest[i] ==min(distance_smallest):
           print(way[i])
    print("Самый короткий путь: "+str(min(distance_smallest)))
        
def main():
    A = Matrix()
    
    #AntAlg(table)
    #A = GenerateMatrix()
    Alg(A)
main()

    
            







