from math import sqrt
import random
from turtle import st
import numpy as np
ungroup = []

#reading the data source into a list.
read = open("inputs/a.in", "r")
for line in read:
    row = list(map(int, line.strip().split(" ")))
    ungroup.append(row)

print("The Ungrouped array")
print(np.array(ungroup))


#My Algorithm
grouped = []
for i in ungroup:
    grouped.extend(i)
print("The Grouped array")
grouped.sort(reverse=True)

#lets arrage everything by getting more details based on an occurance
num_det = {}
for i in grouped:
    if i in num_det.keys():
        #print("here or not")
        num_det[i] = num_det[i] + 1
    else:
        num_det[i] = 0

#lets get the roots in a similar way
num_det_roots = {}
for i in num_det:
    num_det_roots[i] = int(sqrt(num_det[i]))


print("Sorted List: ", np.array(grouped))
print("SUmmary of Details" , num_det)
print("Highest Possible Sqaure: " , num_det_roots)

start = 0
present_pair = {"height": start, "width": start }
n = sqrt(len(grouped))
limit_pair = [n-1, n-1]


answer = []
already = []
predefined_pairs = []
for __h in range(int(n)):
    row = []
    for __w in range(int(n)):
        row.append(-1)
        pd_pair = [__h, __w]
        predefined_pairs.append(pd_pair)
    answer.append(row)

def path_is_free(ran):
    ret = True
    for _h in ran:
        cont = 1
        for _w in ran:
            pair = [_h, _w]
            #print(pair, already)
            if pair in already:
                #print("yes")
                cont = 0
                ret = False
                break
        if cont == 0:
            break


def fill_up(n_mat, value, _dir):
    for h in range(present_pair["height"], present_pair["height"]+n_mat):
        for w in range(present_pair["width"], present_pair["width"]+ n_mat):
            answer[h][w] = value
            already.append([h, w])
            predefined_pairs.remove([h, w])
            #print(np.array(predefined_pairs))

#path_is_free(range(present_pair["height"], present_pair["height"]+n_mat))
#print(np.array(predefined_pairs))
def place_the_matrix():
    #print(n_mat)
    #print(already)
    if ((present_pair["height"] + n_mat <= n and present_pair["width"] + n_mat <= n) and (path_is_free(range(present_pair["height"], present_pair["height"]+n_mat)) or already == []) ):
        #print(n_mat)
        fill_up(n_mat, value, "vertical")
        present_pair["height"] = present_pair["height"] + n_mat
        present_pair["width"] = present_pair["width"] + n_mat
    else:
        #print(np.array(predefined_pairs))
        for i in predefined_pairs:
            present_pair["height"] = i[0]
            present_pair["width"] = i[1]
            #print("inside")
            if ((present_pair["height"] + n_mat <= n and present_pair["width"] + n_mat <= n)  ):
                #print("penitrate here")
                fill_up(n_mat, value, "vertical")
                break

    # elif (present_pair["width"] + n_mat <= n):
    #     fill_up(n_mat, value, "horizontal")    

for h in num_det_roots:
    value = h
    n_mat = num_det_roots[h]
    
    place_the_matrix()



print
print("The Possible Arrange.")
print(np.array(answer))