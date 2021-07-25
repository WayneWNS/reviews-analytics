import time
import progressbar

# github 限制每個檔案上傳最多150MB
data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
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
#			   運算			變數        清單           篩選條件
bad = ['bad' in d for d in data] # "'bad' in d" 會判斷True 或False
print(bad)

#  以下為原型
bad = []
for d in data:
	bad.append('bad' in d)


# 文字計數

wc = {} # word_count
start_time = time.time()
for d in data:
	words = d.split() # 如果使用 ' '切割，當內容有連續多個空白鍵，會被切割成多個空字串，所以印出的東西會有空字串，卻有資料。可以用預設括號內不填，他碰到多個空白鍵會自動跳過。
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典

for word in wc:
	if wc[word] > 100:
		print(word, wc[word])

end_time = time.time()
print('總共花費', end_time-start_time, '秒')
print(len(wc))
print(wc['wayne'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字不在字典內')

print('感謝使用本查詢功能')