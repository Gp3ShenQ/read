
data = []
count = 0
with open('C:/Users/Shen/Desktop/reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        count += 1 
        if count % 1000000 == 0:  #每一千筆  回傳一次進度  % = 取餘數 == 0
            print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')
print(data[0])

sum_len = 0
for d in data:
    sum_len += len(d)

print('留言的平均長度是', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '留言長度小於100')

# good = [d for d in data if 'good' in d] #等同於下面的程式碼

good = []
for d in data:
    if 'good' in d:
        good.append(d)
        
print('一共有', len(good), '留言提到good')

#文字的計數
wc = {} #word_count

count = 1
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 1000000:
        print(word,wc[word])

print(len(wc))

while True:
    word = input('輸入q可以離開\n請問你想找什麼字: ')

    if word == 'q':
        break
    if word in wc:
        print('你查詢的', word , '出現次數', wc[word], '次')
    else:
        print('查無此字')
print('感謝使用此功能')




# sum_len = 0
# for d in data:
#     sum_len += len(d)

# print('留言的平均長度是', sum_len / len(data))

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print('一共有', len(new), '留言長度小於100')

# # good = [d for d in data if 'good' in d] #等同於下面的程式碼

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
        
# print('一共有', len(good), '留言提到good')