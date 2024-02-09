def fizzBuzz(n):
    val1 = "fizzBuzz"
    val2 = "buzz"
    val3 = "fizz"
    
    if n%3==0 and n%5==0:
        return val1
        
    elif n%5==0:
        return val2 
    
    elif n%3==0:
        return val3
    else:
        return n

def main():
   print(fizzBuzz(10))

if __name__ == "__main__":
    main()
