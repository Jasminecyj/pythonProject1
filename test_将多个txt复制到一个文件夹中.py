import os
import shutil

# 获取txt路径
read_path = "Z:\ganhao\Fisheye\MW-R\MW-18Mar-4"
# 存放txt路径
sava_path = "Z:\ganhao\Fisheye\MW-R\MW-18Mar-4\labels"
if not os.path.exists(sava_path):
    os.mkdir(sava_path)
fileType = '.txt'
# with open('Z:\ganhao\Fisheye\MW-R\MW-18Mar-4','r') as f:
#     for name in f:
for file in os.listdir(read_path):
    if file[-4:]== fileType:
        shutil.copy(os.path.join(read_path,file),sava_path)