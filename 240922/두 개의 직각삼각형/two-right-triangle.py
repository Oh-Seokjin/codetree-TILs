def reverse_string(string):
    name_list = list(string)  
    name_list.reverse() 
    name2 = ''.join(name_list)
    return name2

n = int(input())

for i in range(0, n):
    half_str = "*"*(n-i) + " "*i
    print(half_str+reverse_string(half_str))