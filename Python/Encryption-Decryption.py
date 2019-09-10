import string
from time import *
total_list=list(string.lowercase[:26])
#menu
flag = 0
while True:
    while flag == 0:
        print "1-encrypt"
        print "2-decrypt"
        choice = raw_input("which one?:\n")
        if choice == "1":
            flag = 3
            break
        if choice =="2":
            flag = 2
            break
        if choice!="1" or choice!="0" :
            flag = 0

#-----------------------------------------------------------------------------------

    if flag == 3:
        sumation = 0
        example = raw_input("the sentence u wanna encrypt?:")
        inputc =raw_input("what number is the code decryptor?:")
        try:
             int(inputc)
             inputc = int(inputc)
        except:
                list_char = list(inputc)
                for item in list_char:
                    sumation = sumation + ord(item)
                inputc=sumation
        list1 = list(example)
        incrypt = ""
        for item in list1:
            if item in total_list:
                index=total_list.index(item)
                if index-inputc>=0:
                    character = total_list[index-inputc]
                else:
                    extra = index-inputc
                    while extra < -26:
                        extra = extra+26
                    character = total_list[extra]
            else:
                character = item
            incrypt = incrypt +character
        print incrypt
        sleep(3)
        flag = 0
#---------------------------------------------------------------------------------------

    if flag == 2:
        sumation2 = 0
        example2 =  raw_input("the sentence u wanna decrypt?:")
        inputc2 = raw_input("what number is the code decryptor?:")
        try:
            int(inputc2)
            inputc2 = int(inputc2)
        except:
            list_char2 = list(inputc2)
            for item in list_char2:
                sumation2 = sumation2 + ord(item)
            inputc2=sumation2
        decrypt = ""
        list2 = list(example2)
        for item in list2:
            if item in total_list:
                index=total_list.index(item)
                if index+inputc2 <= len(total_list)-1:
                    character2 = total_list[index+inputc2]
                else:
                    xtra = index + inputc2-26
                    while xtra > 25:
                        xtra=xtra - 26
                    character2 = total_list[xtra]
            else:
                character2 = item
            decrypt =decrypt +character2
        print decrypt
        sleep(3)
        flag = 0
            
            
    
    
