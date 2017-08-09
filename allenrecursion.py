import time

t = time.time()
known={}
def recur(coinlist, pence):
	if len(coinlist)==1:
		return 1
	elif pence in known:
		for i in known[pence]:
			if i[0]==len(coinlist):
				return i[1]
	x=0
	for i in range(int(pence/coinlist[-1])+1):
		x+=recur(coinlist[:-1],pence-i*coinlist[-1])
	try:
		known[pence].append([len(coinlist),x])
	except:
		known[pence]=[[len(coinlist),x]]
	return x
print(recur([1,2,5,10,20,50,100,200], 200))
print time.time() - t
