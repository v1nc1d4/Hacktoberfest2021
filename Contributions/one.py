class Solution(object):
   def hammingWeight(self, n):
      """
      :type n: int
      :rtype: int
      """
      v = str(bin(v))
      print(n)
      one_count = 0
      for i in v:
         if i == "1":
            one_count+=1
      return one_count
num = "101010100101010101010"
ob1 = Solution()
print(ob1.hammingWeight(num))
