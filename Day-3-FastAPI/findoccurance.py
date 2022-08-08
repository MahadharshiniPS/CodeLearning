#input ----> haveagoodday
# a
#output ---> 3

# inp_str = input("Enter the input string : ") 
# inp_char = input("Enter the input charachter : ")

# count1 = inp_str.count(inp_char)
# print(count1)

inp_str = input("Enter the input string : ") 
inp_char = input("Enter the input charachter : ")
def count_occ(inp_str,inp_char):
    count = 0
    for i in inp_str:
        if i == inp_char:
            count+=1
    print(f"The count of {inp_char} is :" ,count)
count_occ(inp_str,inp_char)


