

line = "y"
while line[0] not in ("n", "N"):
    height = input("What is your height?(In Cm):\n")
    weight = input("What is your weight?:(In Kg)\n")
    age = input("How young are you ?:\n")
#calculate BMI
    BMI = (float)(weight*10000)/(height**2)
    print "your BMI is %.2f" %BMI

#find out normal weight    
    normal_weight = 0 ;
    if  ( age >= 19  and age <= 24 ) :
        normal_weight = 22
        
    elif ( age >= 25 and age <= 34 ) :
        normal_weight = 23 
     
    elif ( age >= 35 and age <= 44 ) :
        normal_weight = 24
        
    elif ( age >= 45 and age <= 54 ) :
        normal_weight = 25
        
    elif ( age >= 55 and age <= 64 ) :
        normal_weight = 26
        
    elif ( age >= 65 ) :
        normal_weight = 27

#calculate overweight
    overweight = BMI - normal_weight

    if BMI<16.5:      
        print "Way TOO THIN. Gain some weight ( about %d Kg)",(overweight*-1 )
        
    elif 16.5<=BMI<18.5:
        print "you are a little UNDERWEIGHT( about %d Kg)",(overweight*-1 )
        
    elif 18.5<=BMI<25:
        print "congrats, your BMI is  NORMAL"
        
    elif 25<=BMI<30:
        print "you are fat a little bit,lose some weight( about :  %.2f Kg ) " %overweight
        
    elif 30<=BMI<35:
        print "you are fat (class 1),lose weight( about :  %.2f Kg ) " %overweight
        
    elif 35<=BMI<40:
        print "you are fat (class 2),lose some weight( about  %.2f Kg ) " %overweight       
    elif 40<=BMI :
        print "High Obesity. Visit a Doctor Please ! ( about  %.2f Kg ) " %overweight
        
    line = raw_input("Play again (Y/N)?")
    
    print "-----------------------------------------------------------------------"

