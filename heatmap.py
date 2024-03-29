import pandas as pd
import numpy as np
commits = {'Student_login':['0livia_Okoro','Ikemefuna_Ikesee','Cleverjohnson','Fraupozh','Marina_Pozhid','Amit021','shreeja_shreeja','MadalinaLupecescu','asfandyarsheikh','Wijube','Jane_Amolo','raquel_el_Silva','michelleschmidt','timht9','chloe1111','Yadwinder1905','Mahsa_Rouzkhatouni','Trevor_Jay','Tanmaytc25','Vidakwo','Alexandra18636','Yilkaninaj','Ziadso','Aleksa05','Mariam0109','Joachim_Onyebuagu','Kizzy_Adrian','Ucy_brown','Saurav','Vladmired88','Milli_muener','Ricardo090','Abu_zaid','Iyke_muller03','Meech_faya','Ifeanyi_Okechukwu','Faith_bacho','Pascal_Lima','Ahmed_0204','Bazzi_Kui'],

          'Sesmester': ['22S','22S','22S','22W','22S','22S','21W','22S','22W','21W','22W','21W','22S','21W','22S','22S','22W','21W','22W','21W','21W','22W','22S','22W','21W','22W','22S','22S','22S','22S','22S','21W','22W','22S','21W','21W','22W','22W','21W','22W'],
          'S1': [90,100,100,100,100,100,100,100,100,100,100,100,100,100,2,0,92,4,0,0,0,0,0,0,0,0,0,0,0,0,11,0,8,0,0,2,0,0,7,0],
          'S2': [100,92,75,70,65,68,76,56,34,45,56,78,47,23,5,90,90,92,94,94,60,40,3,7,0,0,0,0,0,0,54,57,0,0,4,0,1,0,46,7],
          'S3': [100,90,90,86,80,34,45,50,8,2,8,9,65,0,7,90,64,30,28,0,4,0,0,67,0,9,0,6,34,3,100,21,0,0,5,0,8,0,0,6,0,0,17,0,19],
          'S4': [100,90,78,56,65,80,60,45,58,78,34,24,45,24,12,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,2,0,6,0,0,7],
          'S5': [100,86,67,48,69,80,35,67,49,34,12,8,0,9,0,7,72,14,8,0,0,0,1,0,0,4,0,0,6,0,0,81,0,0,0,0,1,0,0,0,6],
          'S6': [100,70,45,56,76,64,35,0,0,68,0,7,45,0,16,45,21,0,5,7,0,7,0,19,16,9,13,7,1,1,63,0,0,0,0,0,3,0,0,1],
          'S7': [100,57,45,61,31,22,3,0,0,0,0,0,0,0,0,45,7,20,11,0,7,0,0,0,0,43,44,27,0,30,0,70,0,0,80,0,0,90,0,0],
          'S8': [100,79,40,40,0,0,0,0,0,0,0,0,0,0,0,40,45,38,9,6,0,0,1,0,0,0,9,0,3,0,4,3,1,13,0,16,0,4,0,9],
          'S9': [100,54,0,0,0,0,0,0,0,0,0,0,0,0,0,16,12,7,0,0,0,0,0,0,0,0,0,0,0,0,28,21,14,7,0,0,0,0,0,0],
         'S10': [100,19,6,2,0,0,0,0,0,0,0,0,0,22,11,9,4,1,0,0,0,0,7,0,0,0,0,0,5,1,0,8,0,0,9,0,5,0,2,0],
         'S11': [100,35,2,1,0,0,0,0,0,0,0,0,0,0,0,23,17,5,1,2,1,0,0,0,0,0,0,0,0,0,33,35,30,21,11,6,9,0,0,4],
         'S12': [100,15,3,0,0,0,0,0,0,0,0,0,0,0,0,70,50,40,35,21,7,0,0,0,0,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
         'S13': [100,4,4,5,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,3,1,2,0,0,0,0,0],
         'S14': [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         'S15': [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}

students_rating = pd.DataFrame(commits, columns = ['S1','S2','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','S14','S15'], index='Student_login')
print(students_rating)
