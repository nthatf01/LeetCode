class Solution(object):
    def fizzBuzz(n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzbuzz = []
        for i in range (1, n + 1):
            if i % 15 == 0:
                fizzbuzz.append("FizzBuzz")
            elif i % 5 == 0:
                fizzbuzz.append("Buzz")
            elif i % 3 == 0:
                fizzbuzz.append("Fizz")
            else:
                fizzbuzz.append(str(i))
        
        return fizzbuzz


case1 = 3
case2 = 5
case3 = 15

print(sol.fizzBuzz(case1))
print(sol.fizzBuzz(case2))
print(sol.fizzBuzz(case3))
