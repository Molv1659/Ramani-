import os
file_list = os.listdir('./cell_matrix_data')

num_1000000_K562 = 0
num_1000000_GM12878 = 0
num_1000000_HeLa = 0
num_1000000_HAP1 = 0

for name in file_list:
    if '1000000' in name and 'K562' in name:
        num_1000000_K562 += 1
    elif '1000000' in name and 'GM12878' in name:
        num_1000000_GM12878 += 1
    elif '1000000' in name and 'HeLa' in name:
        num_1000000_HeLa += 1
    elif '1000000' in name and 'HAP1' in name:
        num_1000000_HAP1 += 1
    else:
        continue
# 应为493，245，19，12，43
print(len(file_list))
print(num_1000000_HeLa)
print(num_1000000_HAP1)
print(num_1000000_GM12878)
print(num_1000000_K562)


# 读cell_matrix_data文件名得到所有细胞
import os
file_list = os.listdir('./cell_matrix_data')
labels = []
f = open('all_cells.txt','w')
for name in file_list:
    f.write(name[:-15] + '\n')
    labels.append(name.split(sep='_')[0])
f.close()
np.save('cell_label.npy', labels)
