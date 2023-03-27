#Write a function, maxValue, that takes in array of numbers as an argument. The function should return the largest number in the array.
#Solve without using any built-in array methods.
#Assume that the array is non-empty.

def max_value(nums: list):
  max = float('-inf')
  
  for num in nums:
    if num > max:
      max = num
      
  return max
    