import numpy as np

start_line, end_line = 281, 761

def verify_data(files):
    target_V = 0.3
    count = 0

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            target_data = lines[start_line: end_line+1]

            #string to float
            data = list(map(lambda str: list(map(float, str.split(","))), target_data))
            assert data[0][0] == target_V, f"start V is not 0.3V but {data[0][0]}V in {file}"
            assert data[-1][0] == target_V, f"end V is not 0.3V but {data[-1][0]}V in {file}"
        count += 1

    print(f"all {count} of files are verified successfully")

# 커브를 파일로부터 얻는다
def get_curve(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        target_data = lines[start_line: end_line+1]
        target_data = list(map(lambda str: list(map(float, str.split(","))), target_data))

        return np.array(target_data)

#경로를 넣으면 마지막 파일이름에서 그래프 정보르 가져온다.
def get_simulation_settings(file):
    filename = file.split('\\')[-1]
    file_num, ks, D, c1, c2, temp = filename[:-4].split('^')
    return {"file_num": file_num, "ks": ks, "D": D, "c1": c1, "c2": c2, "temp": temp}