data = []
count = 0
with open('C:/Users/Shen/Desktop/reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        count += 1 
        if count % 1000000 == 0:  #每一千筆  回傳一次進度  % = 取餘數 == 0
            print(len(data))

# print('檔案讀取完了,總共有', len(data), '筆資料')


sum_len = 0
for d in data:
    sum_len += len(d)

print('留言的平均長度是', sum_len / len(data))
