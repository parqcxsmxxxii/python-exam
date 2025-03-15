#print("Compare two number ")
#input1 = input("enter any number ")
#input2 = input("enter any other number ")
#if int(input1)>int(input2 ):
    #print("input1:",input1,"is grater than input2",input2)
#if int(input1)<int(input2):
    ##print("input1:",input1,"is less than input2",input2)
#if int(input1)==int(input2):
   # print("both are equal")
#print("enter a number")
#print("1 is for circle ")
#print("2 for rectangle ")
#print("3 for square ")
#in1 = input("choose circle or rectangle    ")
#if int(in1) == 1:
  #  print("output is a circle")
#elif int(in1) == 2:
    # elif is used to chec multiple if statement inside one if block
 #   print("output is rectangle")
#elif int(in1) == 3:
 #   print("output is square")
#else:
 #   print("Invalid input") 
print("check your volume")       
in1 = input("enter a number between 0 to 100 ")
if int(in1)>=0 and int(in1)<=30:
    print("Low volume")
elif int(in1)>30 and int(in1)<=60:
    print("medium volume")
elif int(in1)>60 and int(in1)<=100:
    print("high volume")    
else:
    print("not valid")