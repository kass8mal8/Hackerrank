def is_palindrome (num):
    result,num_remaining = 0,abs(num)
    
    while num_remaining:
        result = result * 10 + num_remaining % 10
        num_remaining //= 10
        
    if num == result :
        return True
    else:
        return False
    
num = 1221
print(is_palindrome(num))