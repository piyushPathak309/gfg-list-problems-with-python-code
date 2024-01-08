# ****************************************************************** Basic List Programs ***********************************************

# 1 .Python program to interchange first and last elements in a list

def func(x):
    k = x[0]
    l = x[-1]
    x[-1] = k
    x[0] = l
    return x


li = func([2, 3, 4, 5])
print(li)


# 2. Python | Ways to find length of list

def func(x):
    count = 0
    for i in x:
        count = count + 1
    return count


k = func([2, 6, 9, "Ram"])
print(f"the length of string is {k}")

print(len(["Ram", 1, '3', 6]))


# 3. Python | Reversing a List

def func(x):
    return x[::-1]


# 2nd app

def func(x):
    lis1 = []
    for i in range(len(x) - 1, -1, -1):
        lis1.append(x[i])
    return lis1


k = func([3, 6, 8, "Ram"])
print(f"the reverse of string is {k}")


# 4. Python | Count occurrences of an element in a list

def func(x):
    dic = {}
    for i in x:
        if i not in dic:
            dic[i] = x.count(i)
    return dic


lis = ["Ram", 2, 4, "Ram", "Shyam", 3, "Shyam", 2]
p = func(lis)
print(p)


# 5. Python Program to find sum and average of List in Python

def func(x):
    sum = 0
    for i in x:
        if type(i) == int:
            sum = sum + i
    return sum, sum / len(x)


lis = ["Ram", 2, 4, "Ram", "Shyam", 3, "Shyam", 2]
p, q = func(lis)
print(p, q)


# 6. Python | Sum of number digits in List


# 7.Python | Multiply all numbers in the list

def func(x):
    mul = 1
    for i in x:
        if type(i) == int:
            mul = mul * i
    return mul


lis = [3, 6, "Ram", 2]
k = func(lis)
print(k)

# 8.Python program to find smallest number in a list

lis = [2, 5, 9, 24, 1, 8, 9]
k = sorted(lis)
print(f"smallest number in list is {k[0]}")

# 9.Python program to find largest number in a list

lis = [2, 5, 9, 24, 1, 8, 9]
k = sorted(lis)
print(f"largest number in list is {k[-1]}")

# 10.Python program to find second largest number in a list


lis = [2, 5, 9, 24, 1, 8, 9]
k = sorted(lis)
print(f"second largest number in list is {k[-2]}")


# 11.Python program to print even numbers in a list and their sum

def func(x):
    li = []
    sum_even = 0
    for i in x:
        if type(i) != str and i % 2 == 0:
            li.append(i)
            sum_even = sum_even + i
    return li, sum_even


k, l = func([2, 6, 8, 10, "Ram", 3, 5])
print(f"even number in list is {k}")
print(f"sum of all the even number is {l}")


# 12.Python program to print odd numbers in a List and their sum


def func(x):
    li = []
    sum_odd = 0
    for i in x:
        if type(i) != str and i % 2 != 0:
            li.append(i)
            sum_odd = sum_odd + i
    return li, sum_odd


k, l = func([2, 6, 8, 10, "Ram", 3, 5])
print(f"odd number in list is {k}")
print(f"sum of all the odd number is {l}")

# 13.Python program to print all even numbers in a range as between 4 and 15

li = []
for i in range(4, 16):
    if i % 2 == 0:
        li.append(i)
print(li)

# 16.Python program to print positive numbers in a list
lis = [4, 5, -9]
for i in lis:
    if i > 0:
        print(i)

# 17.Python program to print negative numbers in a list

lis = [4, 5, -9]
for i in lis:
    if i < 0:
        print(i)

# 21.Remove multiple elements from a list in Python

# Input: [12, 15, 3, 10]
# Output: Remove = [12, 3], New_List = [15, 10]
lis = []
for i in [12, 15, 3, 10]:
    if i not in (12, 3):
        lis.append(i)
print(lis)


# 22.Python | Remove empty tuples from a list

# Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
# Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]


# 23.Python | Program to print duplicates from a list of integers

def func(x):
    sampl_lis = []
    dumpli_lis = []
    for i in x:
        if i not in sampl_lis:
            sampl_lis.append(i)
        else:
            dumpli_lis.append(i)
    return dumpli_lis


k = func([8, 4, 3, 7, 8, 9, 9, 3])
print(f"duplicates in list are {k}")



# ****************************************************************** Advance List Programs ***********************************************

# Python Program to count unique values inside a list

# input_list = [1, 2, 2, 5, 8, 4, 4, 8] ,  unique_elem = 5

def func(x):
    uniqe_lis = []
    for i in x:
        if i not in uniqe_lis:
            uniqe_lis.append(i)
    return uniqe_lis


k = func([1, 2, 2, 5, 8, 4, 4, 8])
print(f"no of unique elements are {len(k)}")


# Python – List product excluding duplicates

# The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
# Duplication removal list product : 90

def func(x):
    uniq_lis = []
    duplic_list = []
    mul = 1
    for i in x:
        if i not in uniq_lis:
            uniq_lis.append(i)
        else:
            duplic_list.append(i)
    for j in uniq_lis:
        mul = mul * j
    return mul


k = func([1, 3, 5, 6, 3, 5, 6, 1])
print(f"product post removal duplication is {k}")


# Python – Extract elements with Frequency greater than K

# Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output : [4, 3]

def func(x):
    dic = {}
    unique_lis = []
    main_outpt = []
    for i in x:
        if i not in unique_lis:
            unique_lis.append(i)
    for j in unique_lis:
        dic[j] = x.count(j)

    for k, v in dic.items():
        if v > 3:
            main_outpt.append(k)
    return main_outpt


l = func([4, 6, 4, 3, 3, 4, 3, 4, 3, 8])
print(f"the elements are {l}")


# Python – Test if List contains all elements in Range

# The original list is : [4, 5, 6, 7, 3, 9]
# start, end = 3, 10
def func(x):
    for i in x:
        if i >= 3 and i <= 10:
            pass
        else:
            break
    return 'Yes'


k = func([4, 5, 6, 7, 3, 9])
print(k)


# Python program to check if the list contains three consecutive common numbers in Python

# Input : [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output : 1, 22

def func(x):
    count=0
    main_lis=[]
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            count=count+1
        if count==2:
            main_lis.append(x[i])
            count=0
    return main_lis

k=func([1, 1, 1, 64, 23, 64, 22, 22, 22])
print(k)



# Python program to find the Strongest Neighbour

# Input: 1 2 2 3 4 5
# Output: 2 2 3 4 5

def func(x):
    main_list = []
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            main_list.append(x[i])
        else:
            main_list.append(x[i + 1])
    return main_list


k = func([1, 2, 2, 3, 4, 5])
print(f"Output is {k}")

# Python Program to print all Possible Combinations from the three Digits

# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

def func(x):
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(len(x)):
                if(i!=j and i!=k and j!=k):
                    print(x[i],x[j],x[k])

func([1, 2, 3])


# Python program to find all the Combinations in the list with the given condition

# Input: test_list = [1,2,3]
# Output:
#  [1], [1, 2], [1, 2, 3], [1, 3]
#  [2], [2, 3], [3]



# Python program to get all unique combinations of two Lists

# List_1 = ["a","b"]
# List_2 = [1,2]
# Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]]

def func(x,y):
    main_list=[]
    for i in x:
        for j in y:
            main_list.append([(i,j)])
    return main_list

k= func(["a","b"],[1,2])
print(k)









# Python program to remove all the occurrences of an element from a list

# Input1: 1 1 2 3 4 5 1 2 1
# Output1: 2 3 4 5 2
# Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1.


def func(x):
    main_list=[]
    for i in x:
        if i==1:
            pass
        else:
            main_list.append(i)
    return main_list

k=func([1 ,1 ,2 ,3 ,4 ,5 ,1 ,2 ,1])
print(k)

# Python – Remove Consecutive K element records

# Input : test_list = [(4, 5), (5, 6), (1, 3), (0, 0)] K = 0
# Output : [(4, 5), (5, 6), (1, 3)]

def func(x,y):
    main_list=[]
    for i in x:
        for j in range(len(i)-1):
            if i[j]==y and i[j+1]==y:
                pass
            else:
                main_list.append(i)

    return main_list

k=func([(4, 5), (5, 6), (1, 3), (0, 0)],0)
print(k)


# Python – Replace index elements with elements in Other List

# The original list 1 is : [‘Gfg’, ‘is’, ‘best’]

# The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

# The lists after index elements replacements is :
# [‘Gfg’, ‘is’, ‘best’, ‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’]

def func(x,y):
    main_list =[]
    for i in y:
        for ix,val in enumerate(x):
            if i==ix:
                main_list.append(val)
    return main_list

k=func(['Gfg', 'is', 'best'],[0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0])
print(k)



# Python Program to Retain records with N occurrences of K

# Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2
# Output : [(4, 5, 5, 4)]
def func(x,k,N):
    main_list=[]
    for i in x:
        if i.count(k)==N:
            main_list.append(i)
    return main_list

l = func([(4, 5, 5, 4), (5, 4, 3)], 5, 2)
print(l)







# ****************************************************************** Programs on List of Strings ***********************************************

# Python – Swap elements in String list

# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']




# Python program to reverse All Strings in String List


# The original list is : ['geeks', 'for', 'geeks', 'is', 'best']
# The reversed string list is : ['skeeg', 'rof', 'skeeg', 'si', 'tseb']
out=[]
for i in ['geeks', 'for', 'geeks', 'is', 'best']:
    out.append(i[::-1])
print(out)


# Python program to find the character position of Kth word from a list of strings

# Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 15
# Output : 1
# Explanation : 15th index occurs in “best” and point to “e” which is 1st element of word.


def func(x,y):
    count=-1
    for i in ''.join(x):
        count=count+1
        if count==y:
            return i

k=func(['geekforgeeks', 'is', 'best', 'for', 'geeks'],15)
print(k)






# Python – Extract words starting with K in String List

# Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = l
# Output : [‘learning’, ‘love’]

out=[]
for i in ['Gfg is good for learning', 'Gfg is for geeks', 'I love G4G']:
    for j in i.split(' '):
        if 'l' in j:
            out.append(j)
print(out)



# Python – Prefix frequency in string List

# test_sub = 'gfg'
# The original list is : ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']
# Strings count with matching frequency : 3

def func(x,y):
    count=0
    for i in x:
        if y in i:
            count=count+1
    return count

k=func(['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses'],'gfg')
print(k)




# Python – Split String of list on K character

# The original list is : ['Gfg is best', 'for Geeks', 'Preparing']
# k=''
# The extended list after split strings : ['Gfg', 'is', 'best', 'for', 'Geeks', 'Preparing']

main_lis=[]
for i in ['Gfg is best', 'for Geeks', 'Preparing']:
    for j in i.split(' '):
        main_lis.append(j)
print(main_lis)



# Python – Split Strings on Prefix Occurrence

# Input : test_list = [“geeksforgeeks”, “best”, “geeks”, “and”], pref = “geek”
# Output : [[‘geeksforgeeks’, ‘best’], [‘geeks’, ‘and’]]
# Explanation : At occurrence of string “geeks” split is performed.









# Python program to Replace all Characters of a List Except the given character


# Input : test_list = [‘G’, ‘F’, ‘G’, ‘I’, ‘S’, ‘B’, ‘E’, ‘S’, ‘T’], repl_chr = ‘*’, ret_chr = ‘G’
#Output : [‘G’, ‘*’, ‘G’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’]

test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
Output=[]
for i in test_list:
    if i=='G':
        Output.append(i)
    else:
        Output.append('*')
print(Output)


# Python – Remove words containing list characters

# The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
# The character list is : ['g', 'o']
# The filtered strings are : ['is', 'best']

def func(x, y):
    main_list = []
    test_lis = []
    main_list1 = []
    for i in x:
        for j in y:
            if i in j:
                test_lis.append(j)
            else:
                if j not in main_list:
                    main_list.append(j)
    for p in main_list:
        if p not in test_lis:
            main_list1.append(p)

    return main_list1


k = func(['g', 'o'], ['gfg', 'is', 'best', 'for', 'geeks'])
print(k)




# Python – Ways to remove multiple empty spaces from string List

# The original list is : ['gfg', '   ', ' ', 'is', '            ', 'best']
# List after filtering non-empty strings : ['gfg', 'is', 'best']

lis=[]
for i in ['gfg', '   ', ' ', 'is', '            ', 'best']:
    if i ==' ' or i=='   ' or i=='            ':
        pass
    else:
        lis.append(i)



# Python – Add Space between Potential Words

# Input : test_list = [“ComputerScienceStudentsLoveGfg”]
# Output : [‘Computer Science Students Love Gfg’]



# Python – Filter the List of String whose index in second List contains the given Substring

# Input : test_list1 = [“Gfg”, “is”, “not”, “best”, “and”, “not”, “CS”],
# test_list2 = [“Its ok”, “all ok”, “wrong”, “looks ok”, “ok”, “wrong”, “thats ok”], sub_str = “ok”
# Output : [‘Gfg’, ‘is’, ‘best’, ‘and’, ‘CS’]










