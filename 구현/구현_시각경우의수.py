#2020.08.19 작성자: 조수아

count = 0


H = int(input())


for h in range(H+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count += 1

print(count)
            
