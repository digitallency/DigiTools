import pandas as pd
from datetime import datetime, timedelta
import requests
import os



def df2Excel(df,directory,excelFileName,addTimeStampToFileName):
    os.makedirs(directory, exist_ok=True)  

    if not isinstance(addTimeStampToFileName, bool):
        print(addTimeStampToFileName,"  veri tipi boolean olmadigi dataframe excele donusturulemedi, bu degeri true veya false yapmalisiniz")
        return
    now=datetime.now()
    datestr = f"{now.year:04d}-{now.month:02d}-{now.day:02d} {now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    if(addTimeStampToFileName):
        excelFileName=excelFileName+"_GenDateTime_"+datestr+".xlsx"

    filePath=directory+"/"+excelFileName
    df.to_excel(filePath)

def downloadAFile(link,directory,fileName):
    # Dosyayı indirmek için bağlantıyı belirtin
    url = link
    # Dosyayı indirmek için bir istek gönderin
    response = requests.get(url)
    # Dosyayı bir dosyaya kaydedin
    with open(directory+"/"+fileName, "wb") as f:
        f.write(response.content)
        # Dosyayı kapatın
        f.close()