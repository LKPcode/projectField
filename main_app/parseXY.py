import re

def parseFile():
    List = []
    xy = {"X":0 , "Y":0 }
    xFlag = False
    yFlag = False
    i = 0
    with open('/home/spectator/Desktop/projectKtima/django_project_ktima/uploads/uploads/ParsedResult.txt') as openfileobject:
        for line in openfileobject:
            if line == "X\n": 
                xFlag = True
                continue
            if line == "Y\n": 
                yFlag = True
                xFlag = False
                continue    
            if xFlag == True: 
                print("X = " , line )
                result = re.findall(r'\d+\.?\d+', line)
                result = float(result[0])
                xy["X"] = result
                List.append(xy)
            else:
                print("Y = " , line )
                result = re.findall(r'\d+\.?\d+', line)
                result = float(result[0])
                List[i]["Y"] = result
                i = i + 1
    return List




for xy in parseFile():
    print(xy)

