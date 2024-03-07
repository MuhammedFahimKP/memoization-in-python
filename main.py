from functools import lru_cache

@lru_cache
def fibno(number:int) -> int:
    
     if number in [1,2]:
             return 1
         
     if number == 0:
             return 0
         
     return fibno(number - 1) + fibno(number - 2)
 
 
 
for i in range(1,100):
    print(f'{i}  {fibno(i)}') 