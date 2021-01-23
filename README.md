# Ramani-
对Ramani的scHiC数据，用scHiCluster的方式进行预处理

“处理Ramani原始按cell存.py” 需要运行两次（ML1一次，ML3一次）然后再运行 “处理后数据统计与检查.py” 这两份代码运行结果示例在 “代码执行结果.ipynb” 中。

“scHiCluster_by_scHiCTools.py” 用刚才处理出来的数据进一步处理，然后包含scHiCluster的画图与ARI演示。其中用到了scHiCTools库，我在原代码基础上进行过改动，请在 https://drive.google.com/drive/folders/14LnEz-rK0-ccNST0--XRYhx9ThVzkatZ?usp=sharing
下载，整个文件夹都下载完成后cd到这个文件夹，python setup.py install进行安装。然后这个下载的文件夹里也放了“scHiCluster_by_scHiCTools.py”执行结果示例的ipynb文件，可供参考。

“human_chromsize.txt” 包含人类每个染色体长度信息，在“处理Ramani原始按cell存.py”需要用到。

代码中路经需要根据使用做对应改动（存的数据路经对应改动，创建按cell存的文件夹cell_matrix_data，创建存scHiCTools所需格式数据的cell_matrix_data_schictools文件夹）
