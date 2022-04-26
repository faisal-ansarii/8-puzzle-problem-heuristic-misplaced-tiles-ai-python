def move(ar,p,st):
	rh=999999
	store_st= st.copy()	#making state copy to store the state

	for i in range(len(ar)):
		dupl_st= st.copy()

		temp = dupl_st[p]
		dupl_st[p] = dupl_st[arr[i]]
		dupl_st[arr[i]] = temp

		temp_rh = count(dupl_st)
		if temp_rh < rh:
			rh = temp_rh
			store_st = dupl_st.copy()
	return store_st,rh

def print_in_format(matrix):
	for i in range(9):
		if i%3 == 0 and i > 0:
			print("")
		print(str(matrix[i])+" ",end = "")

def count(s):
	c=0
	ideal = [1,2,3,
			4,5,6,
			7,8,0]
	for i in range(9):
		if s[i] != 0 and s[i]!=ideal[i]: # we dont check if zero occur
			c+=1						 # we only check for the example s[1]=1 then  
	return c							# S[1]=ideal[1] it matches so it will 
										# not count the misplaced tile 
										# if its not equal then count
										# we will not consider zero as it has 
										# to come on end of puzzle 

state = [ 1,2,3,0,4,6,7,5,8]
h = count(state)
Level = 1

print("\n-----------Lever "+str(Level)+"---------------")
print_in_format(state)
print("\nHeuristic Value (Misplaced) : "+str(h))

while h > 0:
	pos = int(state.index(0))
	Level+=1
	if pos == 0:				# here we check for possible moves 
								# where t he empty puzzle can go
		arr=[1,3]
		state, h = move (arr,pos,state)
	elif pos == 1:
		arr=[0,2,4]
		state, h = move (arr,pos,state)
	elif pos == 2:
		arr=[1,5]
		state, h = move (arr,pos,state)
	elif pos == 3:
		arr=[0,4,6]
		state, h = move (arr,pos,state)
	elif pos == 4:
		arr=[1,3,5,7]
		state, h = move (arr,pos,state)
	elif pos == 5:
		arr=[2,4,8]
		state, h = move (arr,pos,state)
	elif pos == 6:
		arr=[3,7]
		state, h = move (arr,pos,state)
	elif pos == 7:
		arr=[4,6,8]
		state, h = move (arr,pos,state)
	elif pos == 8:
		arr=[5,7]
		state, h = move (arr,pos,state)
	
	print("\n-----------Lever "+str(Level)+"---------------")
	print_in_format(state)
	print("\nHeuristic Value (Misplaced) : "+str(h))