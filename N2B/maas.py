import sys
import os
import requests
import pandas as pd

# Bu dosyanın bulunduğu dizinin üst dizinini sys.path'e ekleyin
ust_dizin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ust_dizin not in sys.path:
    sys.path.append(ust_dizin)


import constants as cons
import utils

yillikBurutMaliyetIndex=206-1
yillikGelirVergisi=182-1
damgaVergisi=197-1
sskIsveren=204-1

def calculateAnualSalary(strMaas):
    #urlstr='https://www.verginet.net//maas2009.aspx?tip=1&yil=2021&mDurum=0&eCalisiyormu=0&cocukSayisi=&sgkDis=true&ts=1633524565500&m1=5000&m2=5000&m3=5000&m4=5000&m5=5000&m6=5000&m7=5000&m8=5000&m9=5000&m10=5000&m11=5000&m12=5000'
    #urlstr = urlstr.replace('4950',strMaas)
    print("url:",urlstr)
    r=requests.get(urlstr, verify=False)
    data=r.text
    vals=data.split(';')
    lst.append([int(strMaas),float(vals[yillikBurutMaliyetIndex].replace('.','').replace(',','.')),float(vals[yillikGelirVergisi].replace('.','').replace(',','.')),float(vals[damgaVergisi].replace('.','').replace(',','.')),float(vals[sskIsveren].replace('.','').replace(',','.'))])
    print(strMaas,"Is Ok.")
 
initMaas=cons.Net2BurutParameters.startSalary
yil="yil="+cons.Net2BurutParameters.yil
initRate=cons.Net2BurutParameters.initRate
maxMaas=cons.Net2BurutParameters.endSalary

urlstr=cons.Net2BurutParameters.urlstr.replace('5000',initMaas).replace('yil=2021',yil)
r=requests.get(urlstr, verify=False)
data=r.text
vals=data.split(';')
lst=[[int(initMaas),float(vals[yillikBurutMaliyetIndex].replace('.','').replace(',','.')),float(vals[yillikGelirVergisi].replace('.','').replace(',','.')),float(vals[damgaVergisi].replace('.','').replace(',','.')),float(vals[sskIsveren].replace('.','').replace(',','.'))]]

salary=int(initMaas)#+initRate
while (salary < int(maxMaas)):
    salary = salary + initRate
    urlstr='https://www.verginet.net//maas2009.aspx?tip=1&yil=2021&mDurum=0&eCalisiyormu=0&cocukSayisi=&sgkDis=true&ts=1633524565500&m1=5000&m2=5000&m3=5000&m4=5000&m5=5000&m6=5000&m7=5000&m8=5000&m9=5000&m10=5000&m11=5000&m12=5000'
    urlstr=urlstr.replace('5000',str(salary)).replace('yil=2021',yil)
    calculateAnualSalary(str(salary))
    

df=pd.DataFrame(lst,columns=['NetMaas','YillikBrutMaliyet','AylikGelirVergisi','DamgaVergisi','SskIsVeren'])
# df.to_csv('sonuc_2024_Final.csv')  
addTimeStampToFileName=True
excelFileName="sonuc_Year_"+cons.Net2BurutParameters.yil+"_From_"+cons.Net2BurutParameters.startSalary+"_To_"+cons.Net2BurutParameters.endSalary
utils.df2Excel(df,cons.GenericParameters.GlobalWorkingFolder,excelFileName,addTimeStampToFileName)
# test deneme