def timeAdder( time1 , time2 ):
    firstTime = time1.split(":")
    firstHours = int(firstTime[0])
    firstMinutes = int(firstTime[1])

    secondTime = time2.split(":")
    secondHours = int(secondTime[0])
    secondMinutes = int(secondTime[1])

    totalHours = firstHours + secondHours
    totlaMinutes = firstMinutes + secondMinutes
    totalHours += totlaMinutes/60 ;
    totlaMinutes = totlaMinutes % 60 ;
    return ("%02d : %02d" %(totalHours,totlaMinutes) )



#Main
def main():
    print("Hello User")
    print(timeAdder("1:45" ,"0:0"))
   

main()
