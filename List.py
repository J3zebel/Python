list1 = ["flight","flower","flag"]
def longestCommonPrefix(list1):
       list1.sort()

       x = list1[0]  
       y = list[-1]
       ans = "" 
       for i in range(min(len(x),len(y))):   
              if x[i] != y[i]:
                     return ans
              ans += x[i]
       