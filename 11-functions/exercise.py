# Return th highest even Number

# mEthod 1
def highest_even(li):
   ans = [1]
   for no in li:
      if(no%2 == 0):
         if(no not in ans and no>ans[0]):
            ans.insert(0, no)
   return ans[0]

print(highest_even([1,2,3,4,5,6,7,100,200])) 


# Method 2
def highest_even1(li1):
   ans1 = []
   for no in li1:
      if(no%2==0):
         ans1.append(no)
   return max(ans1)

print(highest_even1([1,2,3,4,5,6,7,8]))