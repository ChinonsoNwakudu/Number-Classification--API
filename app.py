from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# checking for prime numbers
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return False
  
    return True

# Perfect Number
def is_perfect(n):
    return n == sum( i for i in range(1, n) if n % i == 0 )

#Armstrong
def is_armstrong(n):
    num = str(n) # convert each number to a string because we need the digits to be string to know its length
    power = len(num) # the length of the number is need to calculate the power
    return n == sum(int(i) ** power for i in num)

