# github 限制每個檔案上傳最多150MB
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # 求餘數；當餘數等於0，表示該數值為其倍數
			print(len(data)) # 程式運行上，print 是很花時間的
print(len(data))
print(data[0])
print('-------------------')
print(data[1])