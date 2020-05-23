import pandas as pd
import glob
import os
import json
import concurrent.futures
from multiprocessing import Process




f = open('config.json', "r") 
data = json.loads(f.read())['OptionsTickDataAggregator'] 
f.close() 




def getSubDir(m_path):
    return [os.path.basename(x[0]) for x in os.walk(m_path)][1:]




def fileToDf(m_path):

    all_df = []

    for n in sub_dirs:
        i_path = os.path.join(m_path , n)
        all_files = glob.glob(i_path + "/*.csv")
        li = []
        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            names = os.path.splitext(os.path.basename(filename))[0].split()
            df.insert(0,'StrikePrice', int(float(names[5])), True)
            df.insert(0,'OptionType', names[4],True)
            df.insert(0,'ExpiryDate', f'{names[1]}-{names[2]}-{names[3]}', True)
            df.insert(0,'Symbol',names[0],True)

            li.append(df)

        frame = pd.concat(li, axis=0, ignore_index=True)
        frame = frame.applymap(str)
        all_df.append(frame)
        
    return all_df



def mergeFiles(sd,ed):
    
    frames = fileToDf(dir_path)
    
    for n, frame  in enumerate(frames):
        dt = sub_dirs[n]
        if int(sd) <= int(dt) <= int(ed):
            opath = os.path.join(data['OutputDirectory'], dt)
            frame.to_csv(f'{opath}.csv' , encoding='utf-8', index=False)



if __name__ == "__main__":
    try:  
        os.mkdir(data['OutputDirectory']) 
    except Exception as error:  
        print(error) 

    dir_path = data['InputDirectory']
    sub_dirs = getSubDir(dir_path)
    
    sd = data['StartDate']
    ed = data['EndDate']

    mergeFiles(sd,ed)

