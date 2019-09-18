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
def timeDivider( time1 , time2 ):
    firstTime = timeExtractor(time1)
    firstHours = firstTime[0]
    firstMinutes = firstTime[1]

    secondTime = timeExtractor(time2)
    secondHours = secondTime[0]
    secondMinutes = secondTime[1]

    firstTotalMinutes = firstHours*60 + firstMinutes
    secondTotalMinutes = secondHours*60 + secondMinutes
    return ("%.2f" %((firstTotalMinutes)/(secondTotalMinutes)))

#=============================================================================
def printEachInputData( time , operation):
    status = ""
    if ( operation == "+"):
        status = "SUMMATE"
    elif ( operation == "-"):
        status = "SUBTRACT"
    print("Time :\t %s \t Status: %s" %(time,status))
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
    
    print("%d:%.2d" %(hourResult,minuteResult))
#=============================================================================            
#Main
def main():

    timesList = []
    print("[Time]<Space>[Operator] or E to end")
    
    while (True):
        time,operator = input().split(' ')
        
        if ( time =='e' or operator == 'e' or time =='E' or operator == 'E'):
            print()
            break
        if (operator != '+' and operator != '-' ):
            print ("Wrong Operator...Try Again")
            continue
       
        tempTime = Entery(time,operator)
        timesList.append(tempTime)

        
    for timeItem in timesList:
        result = printEachInputData(timeItem.time,timeItem.operator)
    calculate(timesList)





main()
