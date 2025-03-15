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
#print("check your volume")       
#in1 = input("enter a number between 0 to 100 ")
#if int(in1)>=0 and int(in1)<=30:
 #   print("Low volume")
#elif int(in1)>30 and int(in1)<=60:
    #print("medium volume")
#elif int(in1)>60 and int(in1)<=100:
   # print("high volume")    
#else:
#    print("not valid")
# print("your name  ")
# in1 = input(" your name is ram or sham ")
# if in1 == "ram" or in1 == "Ram" or in1=="RAM":
#     print("hello ",  in1)
# elif in1 == "shyam" or in1 == "Shyam" or in1=="SHYAM":
#     print("hello ",  in1)
# else:
#     print("jai shree ram") 
     
## 1. Ask user - 1.Add,2.subtract,3.multiply,4.divide
## based on choice of add,sub,mul,div ask user to enter number 1 and enter number 2 and then display the resut as per user choice.
print("1 is for add")
print("2 is for sub")
print("3 is for multiplication")
print("4 is for division")
in1 = input("choose from add,sub,multiplication or division  ")
if int(in1) == 1:
    print("you have choosen add")
    num1 = input("Enter num1 ")
    num2 = input("Enter num2 ")
    print("The addition is ", int(num1)+int(num2))
    
elif int(in1) == 2:
    print("you have choosen sub")
    num1 = input("enter num1 ")
    num2 = input("enter num2 ")
    print("the sub is", int(num1)-int(num2))
elif int(in1) == 3:
    print("you have choosen multiplication")
    num1 = input("enter num1 ")
    num2 = input("enter num2 ")
    print("the multiplication is", int(num1)*int(num2))
elif int(in1) == 4:
    print("you have choosen division")
    num1 = input("enter num1 ")
    num2 = input("enter num2 ")
    print("the division is", int(num1)/int(num2))
else:
    print("try again")    