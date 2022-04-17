data = []
count = 0
with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        count += 1 
        if count % 1000 == 0:  #每一千筆  回傳一次進度  % = 取餘數 == 0
            print(len(data))
print(len(data))

print(data[0])
print('-------------------------------------'*3)
print(data[1])
 