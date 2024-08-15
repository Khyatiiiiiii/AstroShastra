#Game start
import time
a=input("Are you interested in playing(y/n)")
if a=="Y" or a=="y":
    print("think of your birth date")
    time.sleep(2)
    print("now double the number you have thought of....")
    time.sleep(5)
    x=input("if you have done press** done **")
    if x=="done":
        print("now add 8 to the number")
        time.sleep(2)
        print("now half the number")
        time.sleep(5)
        y=input("if you have completed the above steps press ** yes**")
        if y=="yes":
            print("the no you got now subtract the no you thought at the starting of the game i.e your birthdate")
            time.sleep(5)
            print("now at last choose the letter acc to number i.e \n 1=A,2=B.......26=Z \n")
            time.sleep(3)
            print("let me predict the letter🧐🧐.............")
            time.sleep(3)
            print("i think🤫")
            time.sleep(2)
            print("you have😗")
            time.sleep(2)
            print("got😌")
            time.sleep(2)
            print("///😃😃///😁😁///*D*///😁😁///😃😃///")
        else:
            print("invalid input")
    else:
        print("invalid input")
else:
    print("you missed a chance to play the game")
time.sleep(2)
#Game end
i=1
list1=["You are beyond beautiful!!","Confidence and happiness is the most beautiful thing you can wear!!","If it makes you feel beautiful, do it!!","Darling!! You are magic and so is your beauty...","Hey gorgeous!! You were chosen to pursue hard thins in life. So believe in yourself.","You are a tornado with pretty eyes and a beautiful smile!!"]
list2=["Be yourself and recognise your worth!!","Confidence and happiness is the most beautiful thing you can wear!!","You are brave enough to face challenges!!","You are a loving human being!!","You are going to become a great leader!!","Your smile is contagious","You are dedicated and sharp minded!!"]
list3=["You make a bigger impact tha you realize!!","Your inside is even more beautiful than your outside1!!","You bring out the best in people and nothing can stop you...","You are a great example to others...","You have a gift for making people comfortable and that's stunning!!","Your ideas will change the world one day!!"]
j=1
for j in range(0,10,1):
    while i<10:
        date=int(input("Please enter your date")) 
        if date<=0 or date>31: 
            print("Oops wrong date!!\n Please enter your date again")
            i=i+1
        else:
            break
    while i<10:
        month=int(input("Please enter your month"))
        if month<=0 or month>12:
            print("Oops wrong month!!\n Enter your month again")
            i=i+1
        else:
            break
    while i<10:
        year=int(input("Please enter your year"))
        if year>=2023:
            print("Oops wrong year!!\n Please enter your year again")
            i=i+1
        else:
            break
    def leap(year):
        if year%4==0:
            return 1
        else:
            return 0
    if month==2:
        if leap(year)==1:
            if date==30 or date==31:
                print("Oops wrong date!!")
                date1=int(input("Enter date again"))
                date=date1
        else:
            if date==29 or date==30 or date==31:
                print("Oops wrong date!!")
                date2=int(input("Enter date again"))
                date=date2
    if month==4 or month==6 or month==9 or month==11:
        if date==31:
            print("Oops wrong date!!")
            date3=int(input("Enter date again"))
            date=date3
    while i<10:
        gender=input("Please enter your gender")
        if gender!='f' and gender!='F' and gender!='m' and gender!='M' and gender!='O' and gender!='o':
            print("Invalid gender!!\n Enter your gender again")
            i=i+1
        else:
            break
    current_m=12*2023+2
    new_m=12*year
    actual_m=current_m-(new_m+month)
    years=actual_m//12
    months=actual_m%12
    print(years,"years and ",months,"months")
    if gender=='F' or gender=='f':
        print(list1[j])
    elif gender=='M' or gender=='m':
        print(list2[j])
    else:
        print(list3[j])
    if date==1 or  date==10 or date==19 or date==28:
        print("""Your personality traits reveal you live life on your terms. You are dominating and confident. You like to maintain practical approach in your
personal and professional life. You like to keep things clear and transparent.  You will speak exactly what is on your mind. You always know what to say and
when to say.""")
    elif date==2 or date==11 or date==20 or date==29:
        print("""Your personality traits reveal that you are sentimental. You attach emtional aspect to your things and relations. You may easily start crying.
But you are brave enough for facing challenges. You value sentiments over practical facts. You  may however be not so good at expressing yourfeelings.
You are good for positions that require looking after people.""")
    elif date==3 or date==12 or date==21 or date==30:
        print("""Your personality traits reveal you are a spiritual individual. You usually say wise things and are a good advisor. You like to accumulate
knowledge and plan your life in a practical way. Sometimes you become impatient and becomes angry. You are good with finances. You may into investing a lot.
You are good at money management.""")
    elif date==4 or date==13 or date==22 or date==31:
        print("""Your personality traits reveal you are  highly intellectual. You are also sharp, clever, and adventurous. You like
to be energetic and cannot be idle for long. You sometimes lose temper on unnecessary things. You are good at multitasking and good for positions in
fields of science and technalogy. """)
    elif date==5 or date==14 or date==23:
        print("""Your personality traits reveal that you are calm, joyful, and a mix of practical and emotional. You like to live life to the fullest. You may
be the happiest when you get to life without any restrictions. You will enjoy careers that let you be free and creative and not be bound in a routine.
You are stubborn and possess anger issues. In professional life you have a sharp business minded approach.""")
    elif date==6 or date==15 or date==24:
        print("""Your personality traits reveal you are obsessed with lifestyle and money. You like things lavisg and luxurious. You are very good at
connecting with people You are not good at managing money and savings. You like to travel and usually are found in careers that take you to places. You
are usually not good at leadership positions as you may lack in discipline.""")
    elif date==7 or date==16 or date==25:
        print("""Your personality traits reveal you may be secretive, spiritual. You like being around your family alot. You are extremely detail oriented.
You enjoy working in fields such as research, data science etc. You are always on a look for somethimg interesting. You are a procrastinator and this habit
sometimes lead to stress near deadlines. You usually reach top management positions due to your calm and scholar mind.""")
    elif date==8 or date==17 or date==26:
        print("""Your personality traits reveal you are an extremely good decision maker. You are a believer of hardwork and you are extremely practical.
You will put your energy into one thing at a time. However, this sometimes leads to losing other things in life. You value your commitments very much.
You usually grow mature early of your age.""")
    elif date==9 or date==18 or date==27:
        print("""Your personality traits reveal you may keep a tough exterior however you have soft heart. You value your relationships and family above all.
But sometimes people argue with you on wrong things. You usually are a good leader. Your business and money management skills are gift which take you to
higher positions in life.""")
    else:
        print("Invalid date")
    yon=input("Do you want to continue(yes/no)")
    if yon=='yes':
        j=j+1
    else:
        break
print("THANK YOU:)") 
    

