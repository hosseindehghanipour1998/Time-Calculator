def timeExtractor(time):
    timeList = time.split(":")
    timeListInt = [ int(timeList[0]) , int(timeList[1]) ]
    return timeListInt
#==============================================================================
def printer (*args):
    for num in args:
        print(str(num) + "    ", end = '')
    print()
#==============================================================================
def timeAdder( time1 , time2 ):
    firstTime = timeExtractor(time1)
    firstHours = firstTime[0]
    firstMinutes = firstTime[1]

    secondTime = timeExtractor(time2)
    secondHours = secondTime[0]
    secondMinutes = secondTime[1]
    #Operation
    totalHours = firstHours + secondHours
    totlaMinutes = firstMinutes + secondMinutes
    totalHours += int(totlaMinutes/60) ;
    totlaMinutes = int(totlaMinutes % 60) ;
    return (totalHours,totlaMinutes)

#==============================================================================

def timeSubtractor( time1 , time2 ):
    firstTime = timeExtractor(time1)
    firstHours = firstTime[0]
    firstMinutes = firstTime[1]

    secondTime = timeExtractor(time2)
    secondHours = secondTime[0]
    secondMinutes = secondTime[1]


    #Get The Max and Min
    minHours = maxHours = minMinutes = maxMinutes = 0

    if ( firstHours > secondHours ):
        #first time is bigger than the second time
        maxHours = firstHours
        maxMinutes = firstMinutes
        minHours = secondHours
        minMinutes = secondMinutes

    elif ( secondHours > firstHours ):
        #second time is bigger than the first time
        maxHours = secondHours
        maxMinutes = secondMinutes
        minHours = firstHours
        minMinutes = firstMinutes

    #if hours are equal then we should compare them by minutes
    elif ( secondHours ==  firstHours ):
        if ( firstMinutes > secondMinutes ):
            #first time is bigger than the second time
            maxHours = firstHours
            maxMinutes = firstMinutes
            minHours = secondHours
            minMinutes = secondMinutes
        else:
            #second time is bigger than the first time
            maxHours = secondHours
            maxMinutes = secondMinutes
            minHours = firstHours
            minMinutes = firstMinutes


    #calculate
    finalHours = maxHours - minHours
    finalMinutes = maxMinutes - minMinutes
    if ( finalMinutes < 0 ):
        finalMinutes += 60 ;
        finalHours -= 1 ;
    return (int(finalHours),int(finalMinutes))

#=============================================================================
def timeQuota( time1 , time2 ):
    firstTime = timeExtractor(time1)
    firstHours = firstTime[0]
    firstMinutes = firstTime[1]

    secondTime = timeExtractor(time2)
    secondHours = secondTime[0]
    secondMinutes = secondTime[1]

    firstTotalMinutes = firstHours*60 + firstMinutes
    secondTotalMinutes = secondHours*60 + secondMinutes
    return (int(firstTotalMinutes),int(secondTotalMinutes))
#=============================================================================
def timeAverage( time1 , days ) :
    firstTime = timeExtractor(time1)
    firstHours = firstTime[0]
    firstMinutes = firstTime[1]

    #totalMinutes = firstHours*60 + firstMinutes
    averageHours = int((firstHours/days))
    remainingHours = int((firstHours%days))
    remainigMinutes = remainingHours * 60 + firstMinutes 
    averageMinutes = remainigMinutes/days 
    return (int(averageHours) , int(averageMinutes))

#=============================================================================
def printEachInputData( time , operation , inTimeResult):
    status = ""
    if ( operation == "+"):
        status = "SUMMATE"
    elif ( operation == "-"):
        status = "SUBTRACT"
    elif (operation == "/" ):
        status = "AVERAGE" 
    print("Time :\t %s \t Status: %s \t %s" %(time,status,inTimeResult))
#=============================================================================
class Entery :
    def __init__(self , time , operator):
        self.time = time
        self.operator = operator
#=============================================================================
        
def calculate(listOfTimes):
    hourResult = 0 
    minuteResult = 0 
    for timeItem in listOfTimes :
       
        if (timeItem.operator == '+' ):
            inputString = str(hourResult) +":"+str(minuteResult)
            hourResult,minuteResult = timeAdder(str(inputString),timeItem.time)
       
        if (timeItem.operator == '-' ):
            inputString = str(hourResult) +":"+str(minuteResult)
            hourResult,minuteResult = timeSubtractor(str(inputString),timeItem.time)
        if ( timeItem.operator == '/' ):
            inputString = str(hourResult) +":"+str(minuteResult)
            hourResult,minuteResult = timeAverage(str(inputString),int(timeItem.time))
            
        printEachInputData(timeItem.time,timeItem.operator,(str(hourResult) +":"+str(minuteResult)))
    print("%d:%.2d" %(hourResult,minuteResult))
#=============================================================================
def hasFile():
    print("Do you have a file to read ? <Y/N>" )
    choice = input()
    if ( choice =='Y' or choice == 'y' ):
        return True
    return False
#=============================================================================
def readFromFile(fileAddress):
    
    try:
        file = open(fileAddress)
        content = file.read()
        file.close()
        return content
    except:
        print("No such File")
        return "Restart"
        
#=============================================================================
def sortFileContent(content ,timesList ):
    
    contentArray = content.split('\n')
    contentArray = [x for x in contentArray if x != '\n']
    contentArray = [x for x in contentArray if x != ' ' and x != '']
    print("".join(contentArray))###
    for timeStr in contentArray :
        time,operator = timeStr.split(' ')
        addTime(time,operator,timesList)
     
    
#=============================================================================        
def addTime(time,operator,timesList):  
    tempTime = Entery(time,operator)
    timesList.append(tempTime)
#=============================================================================
#Main
def main():
    
    timesList = [] 
    while (True) :#start WhileTrue_1
        
        if ( hasFile() == True ):#start If hasFile
            print("What's the filePath?")
            filePath = input()
            content = readFromFile(filePath)
            if (content == "Restart"):
                continue
            sortFileContent(content ,timesList)
            print()
        #end if hasFile

            
        else :#start else hasNoFile
            
            print("[Time]<Space>[Operator] or E to end")
            
            while (True):#start WhileTrue_2
                time,operator = input().split(' ')
                
                if ( time =='e' or operator == 'e' or time =='E' or operator == 'E'):
                    print()
                    break
                if (operator != '+' and operator != '-' and operator != '/'):
                    print ("Wrong Operator...Try Again")
                    continue
               
                addTime(time,operator,timesList)
            #End WhileTrue_2

          #End else hasNoFile      

        calculate(timesList)
        print("Do You Want To Try Again ? <Y/N>")
        outOrIn = input()
        if ( outOrIn == 'y' or outOrIn == 'Y'):
            timesList.clear()
            continue
        break 

    #End WhileTrue_1




main()
