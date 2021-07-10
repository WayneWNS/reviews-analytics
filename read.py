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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d) # 括號內的d 的意思是，將留言原封不動的加入good 的隊伍裡。
# # 也可以改成其他的值，例如: 每找到一筆將一個1 數字加入清單。到時print 出來就會有多少筆，就有多少個1
# print('一共有', len(good), '比留言提到good')
# print(good[0])


# good = [d for d in data if 'good' in d] # 第一個d 就是上面append(d) 裡面的數值
# print(good)

# putput = [(number-1) for number in reference if number % 2  == 0]
# 			   運算			變數        清單           篩選條件
bad = ['bad' in d for d in data] # "'bad' in d" 會判斷True 或False
print(bad)

# 以下為原型
bad = []
for d in data:
	bad.append('bad' in d)