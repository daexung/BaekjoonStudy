groups = input().split('-')
first_sum = 0


for i in groups[0].split('+'):
    first_sum += int(i)

answer = first_sum
for group in groups[1:]: 
    other_sum = 0
    
    for j in group.split('+'): 
        other_sum += int(j)
    
    answer -= other_sum

print(answer)