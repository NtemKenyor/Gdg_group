from math import sqrt
import random
import numpy as np
import sys

sys.setrecursionlimit(10**6)
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
        num_det[i] = 1

#lets get the roots in a similar way
num_det_roots = {}
remains_lst = []
for i in num_det:
    num_det_roots[i] = int(sqrt(num_det[i]))
    remains = num_det[i] - num_det_roots[i] ** 2
    if remains != 0:
        remains_lst.extend(map(int, list(str(str(i)*remains))) )



print("Sorted List: ", np.array(grouped))
print("Summary of Details" , num_det)
print("Highest Possible Sqaure: " , num_det_roots)
print("The remains and non n possible: ", remains_lst)

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
        row.append('*')
        pd_pair = [__h, __w]
        predefined_pairs.append(pd_pair)
    answer.append(row)

def path_is_free(height, width, length):
    ret = True
    for _h in range(height, height+length):
        cont = 1
        for _w in range(width, width+length):
            pair = [_h, _w]
            #print(pair, already)
            if pair in already:
                #print("yes")
                cont = 0
                ret = False
                break
        if cont == 0:
            break

    return ret

def fill_up(n_mat, value, _dir):
    for h in range(present_pair["height"], present_pair["height"]+n_mat):
        for w in range(present_pair["width"], present_pair["width"]+ n_mat):
            answer[h][w] = value
            already.append([h, w])
            predefined_pairs.remove([h, w])
            #print(np.array(predefined_pairs))

def place_the_matrix():
    placed = 0
    if (present_pair["height"] + n_mat > n):
        present_pair["height"] = 0
    if (present_pair["width"] + n_mat > n):
        present_pair["width"] = 0
    
    if ((present_pair["height"] + n_mat <= n and present_pair["width"] + n_mat <= n) and (path_is_free(present_pair["height"], present_pair["height"], n_mat)) ):
        fill_up(n_mat, value, "vertical")
        present_pair["height"] = present_pair["height"] + n_mat
        present_pair["width"] = present_pair["width"] + n_mat
        placed = 1
    else:
        for i in range(len(predefined_pairs)):
            present_pair["height"] = predefined_pairs[i][0]
            present_pair["width"] = predefined_pairs[i][1]
            #print(present_pair, n_mat)
            if ((present_pair["height"] + n_mat <= n and present_pair["width"] + n_mat <= n) and (path_is_free(present_pair["height"], present_pair["width"], n_mat)) ):
                #print(present_pair, n_mat)
                fill_up(n_mat, value, "vertical")
                placed = 1
                break
        if placed != 1:
            remains_lst.extend(map(int, list(str(str(value)*(n_mat**2)))) )  

for h in num_det_roots:
    value = h
    n_mat = num_det_roots[h]
    
    place_the_matrix()

print
print("The Possible Arrange.")
print(np.array(answer))

print("Remaining numbers: ", remains_lst)
print("Free coordinates: ", predefined_pairs)
for io in range(len(remains_lst)):
    # if len(remains_lst) == len(predefined_pairs):
    #     print("Joor on point. LOL")
    h = predefined_pairs[io][0]
    w = predefined_pairs[io][1]
    value = remains_lst[io]
    answer[h][w] = value
    # already.append([h, w])
    # predefined_pairs.remove([h, w])
    



print
print("The Possible Arrange.")
print(np.array(answer))


