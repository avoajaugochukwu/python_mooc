###recursive function to calculate cummulative of a number from 1 

def cummulative_fn1(n):
   if n == 1:
       return 1
   return n + cummulative_fn1(n - 1)

print cummulative_fn1(4)


#iterative function to calculate cummulative of a number from 1
# def cummulative_fn2(n):
#     if n == 1:
#         return 1
#     cummulative_result = 1
#     while n > 1:
#         cummulative_result += n
#         n = n - 1
#     return cummulative_result

# print cummulative_fn1(4)
        
        
    
