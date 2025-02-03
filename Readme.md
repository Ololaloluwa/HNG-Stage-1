# HNG STAGE 1
Public API deployment
## DETAILS
This API  classifies numbers and provides various properties and fun facts about them. It includes endpoints to classify numbers as prime, perfect squares, and more.

## FUCTIONS
- Classify numbers as prime or perfect squares.
- Calculate the sum of digits of a number.
- Checks if the number is an armstrong number.
- Retrieve fun facts about numbers from the Numbers API.
- CORS middleware support.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/Ololaloluwa/HNG-Stage-1.git
cd HNG-Stage-1

```
2. Create and activate a virtual environment:
```sh
python -m venv .venv
source .venv/bin/activate 
```

3. Install the dependencies from
```sh
pip install -r Requirements.txt
```
4.  Run the application:
```sh
uvicorn main:app --reload
```

### ENDPINTS
#### ENDPOINT URL
```sh
https://hng-1-production-e822.up.railway.app/api/classify-number?number=<your number>
```

#### METHOD:
 ```sh
 GET
 ```
#### QUERY PARAMETER:
```sh
'number(str)': The number to classify.
```
#### RESPONSE:
```sh
'number (int)': The input number.
'is_prime (bool)': Whether the number is prime.
'is_perfect (bool)': Whether the number is a perfect square.
'properties (list)': Additional properties of the number.
'digit_sum (int)': The sum of the digits of the number.
'fun_fact (str)': A fun fact about the number.
'error (bool)': Indicates if there was an error with the input.
```
#### EXAMPLE RESPONSE
```sh
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
}
```