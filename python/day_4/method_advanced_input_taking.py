#1 string input              => python
a = input()
print(a)



#2 integer input             => 10
#type string, should be converted into integer
a = input()         
a = int(a)
print(a)



#3 float input               => 10.10
#type string, should be converted into float
a = float(input())
print(a)



#4 string splitting          => python for backend
input_arr = input().split()
print(input_arr)

a, b = input().split()
print(a)
print(b)



#5 number splitting          => 10 20 30 40
input_arr = input().split()
input_arr = list(map(int, input_arr))

a, b = map(int, input().split())
print(a)
print(b)



#6 multiple value in single line
'''
4
one two three four
'''
N = int(input())
array = input().split()
print(array)

'''
4
1 2 3 4
'''
N = int(input())
array = list(map(int, input().split()))
print(array)



#7 multi line input
'''
4
one
two
three
four
'''
N = int((input()))
array = []

for i in range(N):
    array.append(input())

print(array)

'''
4
1
2
3
4
'''
N = int(input())
array = []

for i in range(N):
    array.append(int(input()))

print(array)



#8 multiline input with multiple value in single line
'''
4 3
1 2 3 4
5 6 7 8
9 10 11 12
'''
N, no_lines = map(int, input().split())

matrix = []
for i in range(no_lines):
    array = list(map(int, input().split()))
    matrix.append(array)

print(matrix)


'''
3
1 2 3
5 6 7
9 10 11
'''
N = int(input())

matrix = []
for i in range(N):
    array = list(map(int, input().split()))
    matrix.append(array)

print(matrix)



# additional 1              => name 1 2 3 4
string, *array = input().split()
array = list(map(int, array))

print(array)



# additional 2 
'''
2
2
1 2
1 2
3
1 2 3
1 2 3
1 2 3
'''
no_tc = int(input())

all_inputs = []
for i in range(no_tc):
    n = int(input())
    tc = []

    for j in range(n):
        line = list(map(int, input().split()))
        tc.append(line)
    
    all_inputs.append(tc)

print(all_inputs)






