#Function Definitions :
def multiplier ( score , unit ):
    return score * unit

def showHelp():
    print ("Welcome!")
    print ("At each state, All the scores you have entered will be illustrated to you.")
    print ("1st question of each  By pushing '-' before the row number you can edit the score you wish.")
    print ("If you don't want to edit anything just enter your desired score.")
    print ("at 1st question of each   level by entering 'H/h' the help menu would be shown to you. ")
    print ("at 1st question of each  level by entering 'Q/q' theyou may exit the program.")
    print ("at 1st question of each level by entering 'R/r' theyou may reset the program.")

def getInput(allCourses):
    print("Enter Course Name : ")
    courseName = raw_input();


    if (courseName == 'h' or courseName == 'H' or courseName == 'Q' or courseName == 'q' or courseName == 'R' or courseName == 'r' or courseName == '-' ):
        return courseName

    try:
        print("Enter Course Unit : ")
        courseUnit = input();

        print("Enter Course Score : ")
        courseScore = input();
        sampleCourse = Course(courseName,courseUnit,courseScore)
        allCourses.append(sampleCourse)
    except Exception as e:
        print("Wrong input. Try again. ")
        courseName = "repeat_again"

    return courseName



class Course:
    def __init__(self , courseName , courseUnit , courseScore):
        self.courseName = courseName
        self.courseUnit = courseUnit
        self.courseScore = courseScore
    def showInformation(self):
        print("Course Name : %s \t Course Score : %.2f \t  Course Unit : %d " %(self.courseName ,self.courseScore,self.courseUnit) )

#Main()
def main():
    showHelp()
    allCourses = []
    courseName = ""
    courseScore = 1
    courseUnit = 1

    while ( True ):

        flags = getInput(allCourses)


        if ( flags == "Q" or  flags == "q"):
            break
        elif ( flags == "H" or  flags == "h"):
            showHelp()
        elif ( flags == "R" or  flags == "r"):
            allCourses.clear()
        elif ( flags == "repeat_again"):
            continue

        for course in allCourses:
            course.showInformation()


main()
