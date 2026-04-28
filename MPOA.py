
def maximumProfit(arr):
	arr.sort()
	m_p=0
	n=len(arr)
	for i in range(n):
		price=arr[i]
		m=n-i
		profit=price*m
		if profit >m_p:
			m_p=profit
		
	return m_p
	pass

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)