import datetime

print("================================")
'''
time_str = '13:55:26'
time_object = datetime.strptime(time_str, '%H:%M:%S').time()
print(time_object)  # Output: 13:55:26
'''

with open('D:/ahihi.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

a = slice(0, 8)
b = slice(17, 25)
c = slice(9, 12)
d = slice(26, 29)

hourind = slice(0, 2)
minind = slice(3, 5)
secind = slice(6, 8)

addmin = 1; addsec = 31


for i in range (len(content)): #11, len(content)
    if("-->" in content[i]):
        #print("a",content[i])
        hourtime1 = int(content[i][a][hourind]); hourtime2 = int(content[i][b][hourind])
        mintime1 = int(content[i][a][minind]); mintime2 = int(content[i][b][minind])
        secondtime1 = int(content[i][a][secind]); secondtime2 = int(content[i][b][secind])
      
        secondtime1 = secondtime1 + addsec; secondtime2 = secondtime2 + addsec
        if(secondtime1 > 59): secondtime1 = secondtime1 - 60; mintime1 = mintime1 + 1
        if(secondtime2 > 59): secondtime2 = secondtime2 - 60; mintime2 = mintime2 + 1

        mintime1 = mintime1 + addmin; mintime2 = mintime2 + addmin 
        if(mintime1 > 59): mintime1 = mintime1 - 60; hourtime1 = hourtime1 + 1
        if(mintime2 > 59): mintime2 = mintime2 - 60; hourtime2 = hourtime2 + 1
       
        hourstr1 = '0'+str(hourtime1); hourstr2 = '0'+str(hourtime2)
        minstr1 = str(mintime1); minstr2 = str(mintime2); secstr1 = str(secondtime1); secstr2 = str(secondtime2)

        if(len(minstr1) == 1): 
            minstr1 = '0'+minstr1
        if(len(minstr2) == 1): 
            minstr2 = '0'+minstr2
        if(len(secstr1) == 1): 
            secstr1 = '0'+secstr1
        if(len(secstr2) == 1):
            secstr2 = '0'+secstr2
        

        strres = hourstr1+':'+minstr1+':'+secstr1+','+content[i][c] +" --> "+ hourstr2+':'+minstr2+':'+secstr2+','+content[i][d]
        content[i] = strres+'\n'
        #print(content[i])
 

a = ['a\n', 'b', 'c', 'd', 'e']
with open('D:/hehe.txt', 'a', encoding='utf-8') as file:
    for i in range(len(content)):
       file.write(content[i])




