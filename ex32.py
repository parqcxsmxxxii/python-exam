# count = [ 5,4,3,2,1]
# fruits = ["apple","banna","guava","kiwi","tomato"]
#for i in fruits:
   #print("The fruits are ",i)
#for c in count:
 #   print("the count is ",c)
# jj = ["a","b","c","d","e"]
# for j in jj:
#     print("the jj is ",j)    
#number = [ 1,2,3,4,5,6,7,8,9,10]
# for n in number:
#     print("the table for 3 is 3x",n,"=",n*3 )
# for n in number:
#     print("the table of 4 is 4x",n,"=",n*4)
# for n in number:
#     print("the table of 5 is 5x ",n,"=",n*5)
print("learning nested loop")
# matrix = [[3,6,9],
#           [2,4,8],
#           [1,3,6]]
# for m in matrix:
#     for n in m:
#         print("the element of  matrix is ",n)
# for i in range(5,51,5):
#     print("The number is ",i)
# money = [2,5,7,3,4]
# for m in money:
#     print("the money ",m)
student = [{"id":25,
            "name":"mama",
            "age":15,
            "num":[4,7,8,2,4]},
           {"id":21,
            "name":"batrang",
            "age":16,
            "num":[1,5,7,9,3]},
           {"id":22,
            "name":"jacob",
            "age":18,
            "num":[3,8,9,0,2,6]},
           {"id":30,
            "name":"tolouse",
            "age":29,
            "num":[6,8,9,0,3,2]},
           {"id":28,
            "name":"orang",
            "age":17,
            "num":[4,6,7,5,0]}]
for s in student:
    print("student name ",s["name"],"their num is ",s["num"]*2)
