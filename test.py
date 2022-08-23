import pandas as pd
from openpyxl import Workbook
import random
score = pd.read_excel("C:/Users/ihans/OneDrive/바탕 화면/동물병원2.xlsx")

score = score.values.tolist()

wb = Workbook()
ws = wb.active


for i in range(3000, len(score)):
    score[i][2] = str(score[i][2])
    score[i][3] = str(score[i][3])
    score[i].append([])
    score[i].append([])
    score[i].append([])
    score[i][4] = str(random.randrange(30,35)*1000)
    score[i][5] = str(random.randrange(20,30)*1000)
    score[i][6] = str(random.randrange(20,30)*1000)
    s = "','".join(score[i])
    st = "insert into MAP VALUES(null,'"+s+"');"
    print(st)
    # ws.append(list(st))
    # wb.save("C:/Users/tpdls/OneDrive/바탕 화면/final_project/동물병원3.xlsx")
# for i  in range(len(score)):
#     score[i][6],score[i][7] = transform(proj_1, proj_2,score[i][6],score[i][7])
#     ws.append(score[i])

# for i  in range(len(score)):
#     print(score[i][6],score[i][7])

# wb.save("C:/Users/tpdls/OneDrive/바탕 화면/final_project/동물병원1.xlsx")
