from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math
import requests

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Prime check function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Perfect number check
def is_perfect(n):
    if n <= 0:  # Ensure that 0 and negative numbers return False
        return False
    return n == sum(i for i in range(1, n) if n % i == 0)

# Armstrong number check
def is_armstrong(n):
    num = str(n)
    power = len(num)
    return n == sum(int(i) ** power for i in num)

# Fun fact retrieval
def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json", timeout=5)
        response.raise_for_status()
        return response.json().get("text", "No fun fact available at the moment.")
    except requests.RequestException:
        return "Couldn't fetch fun fact. Try again later."

@app.get("/api/classify-number/")
async def classify_number(number: str = Query(..., description="Number you want to classify")):
    try:
        # Check if the input is a valid number
        try:
            number = int(number)  # Try to convert the number to an integer
        except ValueError:
            # If conversion fails, return a 400 Bad Request response with the invalid input in the required format
            return {"number": number, "error": True}

        # Handle negative numbers
        if number < 0:
            properties = ["odd" if number % 2 else "even"]  # Only "odd" or "even"
            return {
                "number": number,
                "is_prime": False,
                "is_perfect": False,
                "properties": properties,
                "digit_sum": sum(int(digit) for digit in str(abs(number))),
                "fun_fact": "No fun fact available for negative numbers."
            }

        # Valid positive number logic
        properties = []
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
        # General exception handler (not usually necessary for this case)
        return {"number": number, "error": True, "message": str(e)}
