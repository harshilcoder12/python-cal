maths = float(input("Enter marks scored in maths out of 80: "))
sci = float(input("Enter marks scored in science out of 80: "))
eng = float(input("Enter the number of marks scored in english out of 80: "))
hindii= float(input("Enter the marks scored in hindi out of 80: "))
ss = float(input("Enter the number of marks scored in ss out of 80: "))
Ai  = float(input("Enter marks scored in Ai out of 50: "))
def all():
    total_marks = maths + sci + eng + hindii + ss + Ai
    total_per =  total_marks*100/450
    print(total_per)

def permaths():
    per = maths*100/80
    print("maths", per)
def pereng():
    per1 = eng*100/80
    print("english",per1)
def perhin():
    per2 = hindii*100/80
    print("Hindi", per2)
def perAI():
    per3 = Ai*100/50
    print("AI", per3)
def sst():
    per4 = ss*100/80
    print("SS", per4)
def scie():
    per5 = sci*100/80
    print("Science", per5)
def all():
    total = maths+ hindii+ ss+ Ai+ sci+ eng
    per32 = total*100/450
    print("Total percentage", per32)

print("subject wise percentage")
permaths()
pereng()
perhin()
perAI()
sst()
scie()

print("overall percentage")
all()
