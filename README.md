# 📊 Number Classification API

## 🚀 Overview  
The **Number Classification API** is a FastAPI-based web service that analyzes numbers and provides interesting mathematical properties along with a fun fact.  

## 🌟 Features  
-  **Prime Number Check** - Determines if a number is prime.  
-  **Perfect Number Check** - Identifies if a number is a perfect number.  
-  **Armstrong Number Check** - Checks if a number is an Armstrong number.  
-  **Digit Sum Calculation** - Returns the sum of the digits.  
-  **Fun Fact Fetcher** - Retrieves an interesting fact about the number from the Numbers API.  
- **CORS Enabled** - Supports Cross-Origin Resource Sharing.  

## 📡 API Endpoint  

### **🔍Classify a Number**  
**Endpoint:**  
```http
GET /api/classify-number?number={your_number}
```
Example Response (200 OK):
```
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
Error Handling (400 Bad Request):

```
{
    "number": "alphabet",
    "error": true,
    "message": "Invalid input. Please enter a valid integer."
}

```
##  Tech Stack
* Programming Language: Python 🐍
* Framework: FastAPI ⚡
* Server: Uvicorn 🌎
* Hosting: Render 🌐
* API for Fun Facts: Numbers API

## Installation & Setup
### Clone the Repository
```
git clone https://github.com/ChinonsoNwakudu/Number-Classification-API.git

cd your-repo
```
### Create a Virtual Environment (Optional but Recommended)
```
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

```
### Install Dependencies
```
pip install -r requirements.txt
```
### Run the API Locally
```
uvicorn app:app --reload
```
API will be available at:
* 👉 http://yourlocalhost/docs (Swagger UI)
* 👉 http://yourlocalhost/redoc (ReDoc UI)

## 🚀 Deployment on Render
1. Push your code to GitHub
```
git add .
git commit -m "Initial commit"
git push origin main
```
2. Go to Render
3. Create a new Web Service
4. Connect your GitHub Repository
5. Set Start Command:
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```
6. Deploy! 🚀

## 🔥 Example Usage
Try accessing the deployed API:

```
curl -X GET "https://your-api-url.com/api/classify-number?number=28"
```
