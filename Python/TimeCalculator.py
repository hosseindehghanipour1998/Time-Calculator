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
    totalHours += totlaMinutes/60 ;
    totlaMinutes = totlaMinutes % 60 ;
    return ("%02d : %02d" %(totalHours,totlaMinutes) )

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
    return ("%02d : %02d" %(finalHours,finalMinutes) )
        
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
#Main
def main():
    print("Hello User")
    #print(timeAdder("1:45" ,"0:0"))
    #print(timeSubtractor("1:45" ,"12:0"))
    print(timeDivider("1:44" ,"12:0"))
   

main()
