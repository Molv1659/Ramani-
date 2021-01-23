# 数据处理成scHiCTools所需格式
all_cells = open('all_cells.txt').readlines()
cell_num = len(all_cells)
num = 0
for cellname in all_cells:
    cellname = cellname.strip()
    data = open('./cell_matrix_data/' + cellname + '_1000000.matrix').readlines()
    f = open('./cell_matrix_data_schictools/' + cellname, 'w')
    for line in data:
        items = line.split()
        new_line = '\t'.join([items[4][9:], items[0], items[5][9:], items[1], items[2]])
        f.write(new_line + '\n')
    f.close()
    num = num + 1
    if num % 10 == 0:
        print(num)

# 检验
import os
file_list = os.listdir('./cell_matrix_data_schictools')

num_1000000_K562 = 0
num_1000000_GM12878 = 0
num_1000000_HeLa = 0
num_1000000_HAP1 = 0

for name in file_list:
    if 'K562' in name:
        num_1000000_K562 += 1
    elif 'GM12878' in name:
        num_1000000_GM12878 += 1
    elif 'HeLa' in name:
        num_1000000_HeLa += 1
    elif 'HAP1' in name:
        num_1000000_HAP1 += 1
    else:
        continue
# 应为493，245，19，12，43
print(len(file_list))
print(num_1000000_HeLa)
print(num_1000000_HAP1)
print(num_1000000_GM12878)
print(num_1000000_K562)


######################################################
# 从这里下载https://drive.google.com/drive/folders/14LnEz-rK0-ccNST0--XRYhx9ThVzkatZ?usp=sharing
# 是scHiCTools的基础上进行过代码改动的，需要cd到对应文件夹进行安装
# % cd /content/drive/MyDrive/毕设/scHiCTools
# ! python setup.py install

from sklearn.decomposition import PCA
import numpy as np
from scHiCTools import scHiCs
from scHiCTools import scatter
labels = np.load("../data/Ramani/cell_label.npy")
all_cells = open('../data/Ramani/all_cells.txt').readlines()
cell_files = ['../data/Ramani/cell_matrix_data_schictools/' + cellname.strip() for cellname in all_cells]

y = scHiCs(cell_files,
                reference_genome='hg19', resolution=1000000,
                max_distance=None, format='shortest_score',
                adjust_resolution=False, chromosomes='except Y',
                operations=['log2', 'convolution', 'random_walk'], kernel_shape=3, keep_n_strata=None,
                store_full_map=True)
matrix = []
for ch in y.chromosomes:
    A = y.full_maps[ch].copy()
    A.shape = (A.shape[0],A.shape[1]*A.shape[2])
    thres = np.percentile(A, 80, axis=1)
    A = (A > thres[:,None])
    pca = PCA(n_components = 20)
    R_reduce = pca.fit_transform(A)
    matrix.append(R_reduce)
matrix = np.concatenate(matrix, axis=1)
print('matrix.shape:', matrix.shape)

pca = PCA(n_components = 20)
matrix_reduce = pca.fit_transform(matrix)


cell1_x = []; cell1_y = []
cell2_x = []; cell2_y = []
cell3_x = []; cell3_y = []
cell4_x = []; cell4_y = []
for i in range(len(matrix_reduce)):
    if labels[i] == 'HeLa':
        cell1_x.append(matrix_reduce[i][0])
        cell1_y.append(matrix_reduce[i][1])
    if labels[i] == 'HAP1':
        cell2_x.append(matrix_reduce[i][0])
        cell2_y.append(matrix_reduce[i][1])
    if labels[i] == 'K562':
        cell3_x.append(matrix_reduce[i][0])
        cell3_y.append(matrix_reduce[i][1])
    if labels[i] == 'GM12878':
        cell4_x.append(matrix_reduce[i][0])
        cell4_y.append(matrix_reduce[i][1])

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
cell1 = ax.scatter(cell1_x, cell1_y, c = '#1f77b4')
cell2 = ax.scatter(cell2_x, cell2_y, c = '#ff7f0e')
cell3 = ax.scatter(cell3_x, cell3_y, c = '#d62728')
cell4 = ax.scatter(cell4_x, cell4_y, c = '#2ca02c')

ax.legend((cell1, cell2, cell3, cell4), ('HeLa', 'HAP1', 'K562', 'GM12878'), loc = 0)

plt.show()


# ARI
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
y_pred = KMeans(n_clusters = 4, n_init = 20).fit_predict(matrix_reduce[:,:10])
score = adjusted_rand_score(labels, y_pred)
print(score)