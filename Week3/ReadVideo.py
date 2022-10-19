#Week 3 Programming Assignment
#运行方式：命令行运行以下代码
#python D:\PythonLearningCode\CoursersCryptographyI\Week3\ReadVideo.py D:\PythonLearningCode\CoursersCryptographyI\ceshi.mp4
#argv[1] 为运行当前.py文件传入的参数,本文件所需参数即为需加密的视频文件路径

from hashlib import sha256
from sys import argv

with open(argv[1], "rb") as f:
    blocks = []    
    block = f.read(1024)
    while block:
        blocks.append(block)
        block = f.read(1024)

    h = sha256(blocks[-1])  #取数组最后一个元素
    for block in reversed(blocks[:-1]):
        h = sha256(block + h.digest())
        
    print(h.hexdigest())