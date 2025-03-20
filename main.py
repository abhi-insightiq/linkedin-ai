from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    openapi_url="/openapi.json",
    servers=[{"url": "https://linkedin-ai-production.up.railway.app", "description": "Production Server"}]
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# Define input and output model
class InputData(BaseModel):
    input_text: str

class OutputData(BaseModel):
    output_text: str

# Sample computation function (Replace with your actual logic)
def process_text(input_text: str) -> str:
    return input_text[::-1].upper()  # Example: Reverses the string

@app.post("/process", response_model=OutputData)
def process_input(data: InputData):
    result = process_text(data.input_text)
    return OutputData(output_text=result)
