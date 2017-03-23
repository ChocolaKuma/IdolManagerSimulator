import random

firstName = ["Haruto","Riku","Haru","Hinata","Sora"]
lastName = ["Saito","Kobayashi","Nakamura","Yamamoto","Ito"]

def trainingDay(talent):
    print("\nTime For Some Training\n")
    talent = talent + random.randint(1,4)
    return talent
    


    
class girl(object):
    def NameMaker(name):
        pick = random.randint(0,4)  
        r = name[pick]
        return r
    def bdaygen():
        month = random.randint(1,12)
        day = random.randint(1,12)
        r = str(month)+"/"+str(day)
        return r
    def __init__(self):
        self.fName = girl.NameMaker(firstName)
        self.lName = girl.NameMaker(lastName)
        self.age = random.randint(14,22)
        self.bday = girl.bdaygen() 
        self.talent = random.randint(1,5)
        self.energy = random.randint(5,20)
        self.cuteness = random.randint(1,10)
        self.signed = False

bla = girl()
while bla.signed==False:
    print(bla.fName,bla.lName)
    print(bla.age,"years Old")
    print("Birthday:",bla.bday)
    print("Talent:",bla.talent,"/5 Possable")
    print("Energy:",bla.energy,"/20 Possable")
    print("Cuteness:",bla.cuteness,"/10 Possable")
    print("Signed:",bla.signed)
    print("\n")
    print("Would You like to sign this girl?")
    print("(1)Yes(2)No")
    yn = input()
    if(int(yn)==1):
        print("You Signed her")
        bla.signed=True
        break
    bla = girl()

    
keepGoing=True
while keepGoing==True:   

    print(bla.fName,bla.lName)
    print(bla.age,"years Old")
    print("Birthday:",bla.bday)
    print("Talent:",bla.talent,"/5 Possable")
    print("Energy:",bla.energy,"/20 Possable")
    print("Cuteness:",bla.cuteness,"/10 Possable")
    print("Signed:",bla.signed)
    print("\n")
    print("\nWhat would you like to do\n\n")
    print("(0) Quit The Game")
    print("(1) Give Your Girl a break(+1-2 Energy)")
    print("(2) To Do some Talent Training(-1 Energy +1 Talent)")
    
    
    select = int(input("\nOption number:"))
    if(select == 0):
        print("Looks like your dreams of being an\nIdol manager are over eh?")
        keepGoing = False
    if(select == 1):
        bla.energy = bla.energy + random.randint(1,2)    
    if(select == 2):
        if(bla.energy>0):
            bla.energy = bla.energy - 1
            bla.talent = trainingDay(bla.talent)
        if(bla.energy<0):
            print("You dont have enough energy")

