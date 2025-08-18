from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import json

app = FastAPI()

# Serve static files (e.g., CSS, JS, images) if needed
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

# Home Page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Portfolio Page
@app.get("/portfolio", response_class=HTMLResponse)
def portfolio(request: Request):
    return templates.TemplateResponse("portfolio.html", {"request": request})

# Contact Page
@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# About Page
@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Ask Questions Page
@app.get("/ask", response_class=HTMLResponse)
def ask_page(request: Request):
    return templates.TemplateResponse("ask.html", {"request": request})

# Ask Mistral via Ollama
@app.post("/ask")
def ask_mistral(payload: dict):
    question = payload.get("question")
    if not question:
        return JSONResponse({"error": "No question provided."}, status_code=400)
    ollama_url = "http://192.168.178.31:11434/api/generate"  # or your host IP if needed
    data = {"model": "mistral", "prompt": question}
    try:
        response = requests.post(ollama_url, json=data, stream=True)
        response.raise_for_status()
        full_answer = ""
        for line in response.iter_lines():
            if line:
                print(f"Ollama response line: {line}")  # Debug log
                try:
                    obj = json.loads(line.decode())
                    print(f"Parsed object: {obj}")  # Debug log
                    full_answer += obj.get("response", "")
                except Exception as e:
                    print(f"Error parsing line: {e}")  # Debug log
                    continue
        print(f"Final answer: {full_answer}")  # Debug log
        return {"response": full_answer}
    except Exception as e:
        print(f"Request error: {e}")  # Debug log
        return JSONResponse({"error": str(e)}, status_code=500)
