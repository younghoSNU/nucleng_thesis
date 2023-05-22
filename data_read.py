import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import glob
import tools


root_dir = os.path.join("C:\\", "Users", "82106" ,"OneDrive - SNU" ,"23-1-youngho" ,"원자핵_졸업논문")
target_dir = "temp_macro"
target_file = "*.use"
curve_files = glob.glob(os.path.join(root_dir, target_dir, target_file))

curves = np.array([])

# tools.verify_data(curve_files)

for file in curve_files:
    np.append(curves, tools.get_curve(file))

sample_curves = np.random.choice(curves, size=3, replace=False)

# figure 객체 생성
fig = plt.figure(figsize=(10,5))

# 3개의 subplot 생성
for i in range(3):
    ax = fig.add_subplot(1, 3, i+1)
    # graphs[i]번째 그래프를 그리는 코드
    # 예시로 단순히 y = x 그래프를 그리는 코드를 작성하였습니다.
    x = np.arange(0, 10, 0.1)
    y = x
    ax.plot(x, y)
    ax.set_title("Graph {}".format(graphs[i]+1))

# 그래프 출력
plt.show()

# with open(file_path, 'r') as f:
#     lines = f.readlines()
#     data = lines[281:762]
#     data = list(map(lambda str: list(map(float, str.split(","))) ,data))
#     print(data[0])
#     print(data[-1])

# x = [el[0] for el in data]
# y = [el[1] for el in data]

# plt.plot(x, y, 'b')
# plt.show()

