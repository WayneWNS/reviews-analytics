# github 限制每個檔案上傳最多150MB
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # 求餘數；當餘數等於0，表示該數值為其倍數
			print(len(data)) # 程式運行上，print 是很花時間的
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均長度為', sum_len/len(data))