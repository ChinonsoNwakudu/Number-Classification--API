from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import math
import requests

app = FastAPI()

#CORS
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

#Fun Fact
def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json", timeout=5)
        response.raise_for_status()
        return response.json().get("text", "no funfact available at the moment.")
    except:
        return "couldn't fetch funfact, try again later."
    
@app.get("/api/classify-number/")    

async def classify_number(number: str = Query(..., description="Number you want to classify")):
    try:
        # validates if input is a number
        try:
            number = int(number)  # Try to convert the number to an integer
        except ValueError:
            # If conversion fails, return a 400 Bad Request response
            return {"number": number, "error": True}

        properties=[]
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 else "even")    

        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": get_fun_fact(number),
        }
    except Exception as e:
        return {"number": number, "error": True, "message": str(e)}


