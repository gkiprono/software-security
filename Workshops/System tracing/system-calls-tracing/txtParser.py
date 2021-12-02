'''
Gabriel Kiprono
System calls tracing
10/17/21
'''
import re
import string
import pandas as pd

#  open file and read contents
#  loop thru contents of file and save to dataframe
#  return df

def readFile(fileName):
    systemCalls = pd.DataFrame(columns=['System_Call','Time','Count'])


    with open(fileName) as file:
        contents = file.readlines()
        
    for line in contents:
        try:
            call = str(re.findall(r'\w+', line)[3]) #  sys call is always third elemet
            time = float(re.findall(r'<(.+?)>', line)[0]) #  assuming time is in tags <**>

            systemCalls.loc[-1] = [call, time,1]
            systemCalls.index+=1 
            systemCalls = systemCalls.sort_index()

        except ValueError as e:
            print(str(e))
        except IndexError as er:
            print(str(er))


    return systemCalls
    


def main():
    systemCalls = pd.DataFrame(columns=['System_Call','Time','Count'])
    finalSysCalls = pd.DataFrame()
    buggySrc = "buggy-python.txt"
    neutralSrc = "neutral-python.txt"

    #buggy python txt, read file and group by and merge on system  call
    finalSysCalls =  readFile(buggySrc)
    callsTime = finalSysCalls['Time'].groupby(finalSysCalls['System_Call'])
    callsCount = finalSysCalls['Count'].groupby(finalSysCalls['System_Call'])

    systemCalls = pd.merge(callsTime.mean(), callsCount.count(),how='inner', on='System_Call')
    systemCalls.to_csv('output_buggy_python.csv')

    #neutral python txt, read file and group by and merge on system  call
    finalSysCalls =  readFile(neutralSrc)
    callsTime = finalSysCalls['Time'].groupby(finalSysCalls['System_Call'])
    callsCount = finalSysCalls['Count'].groupby(finalSysCalls['System_Call'])
    
    systemCalls = pd.merge(callsTime.mean(), callsCount.count(),how='inner', on='System_Call')
    systemCalls.to_csv('output_neutral_python.csv')


if __name__ == "__main__":
    main()