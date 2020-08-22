<<<<<<< HEAD
# 2020.08.19 작성자: 조수아


#int(ord(input_data[0])) - int(ord('a')) + 1

N = input()
count =0
data = [ (-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

row = int(N[1])
c= ('0x'+N[0])
column = int(c, 16)
column -= 9
a = (row, column)


for n in data:

    if n[0] + a[0] >= 1 and n[1] + a[1] >= 1 and n[0] + a[0] <= 8 and n[1]+a[1] <=8:
        count += 1  

print(count)
=======
# 2020.08.19 작성자: 조수아


#int(ord(input_data[0])) - int(ord('a')) + 1

N = input()
count =0
data = [ (-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

row = int(N[1])
c= ('0x'+N[0])
column = int(c, 16)
column -= 9
a = (row, column)


for n in data:

    if n[0] + a[0] >= 1 and n[1] + a[1] >= 1 and n[0] + a[0] <= 8 and n[1]+a[1] <=8:
        count += 1  

print(count)
>>>>>>> 5ca76d22337ab9895a85cd2a769d498a09968ef0
