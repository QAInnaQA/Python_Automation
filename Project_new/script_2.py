
import random
#random.send(34)
data_old = [274, 737, 734, 485, 522, 697, 812, 887, 890, 9, 325, 6, 979, 759, 957, 116, 99, 452, 584, 861, 863, 500, 908, 138, 291, 585, 758, 880, 356, 628, 678, 373, 515, 8, 746, 404, 559, 165, 78, 91, 994, 31, 698, 875, 985, 603, 687, 819, 214, 209, 185, 594, 544, 837, 912, 716, 831, 476, 520, 235, 59, 656, 506, 626, 279, 292, 779, 176, 620, 352, 766, 931, 430, 924, 961, 6, 978, 916, 87, 788, 73, 974, 313, 825, 899, 764, 681, 380, 188, 886, 674, 405, 322, 597, 170, 378, 715, 322, 677, 437]

data = [random.randint(0,1000) for x in range(100)]

with open("data.txt", "w+") as file:
    for item in data:
        file.write(f"{item}\n")


with open("data.txt", "r") as f:
    our_data = f.readlines()

print(type(our_data))

#exit()
#our_data = our_data.strip("[]")
#our_data = our_data.split(", ")
#our_data = list(map(lambda x: int(x), our_data))

#count = 0
#for x in our_data:
    #if x in data:
        #count += 1
#print(count)
#print(data