# Memphis Consultancy Website

A modern FastAPI-powered website for Memphis Consultancy, featuring responsive design and dynamic content using Jinja2 templates and Tailwind CSS.

## Features
- FastAPI backend
- Jinja2 templating
- Responsive UI with Tailwind CSS
- Static file serving
- Pages: Home, Portfolio, About, Contact

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd memphis_consultancy
   ```

2. **Create a Python virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required Python libraries**
   ```bash
   pip install fastapi uvicorn jinja2
   ```

## Python Virtual Environment Setup

To prepare and use a Python virtual environment with all required modules:

1. **Create the virtual environment**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**
   ```bash
   source venv/bin/activate
   ```

3. **Install all required modules**
   ```bash
   pip install -r requirements.txt
   ```
   This will install FastAPI, Uvicorn, Jinja2, pytest, and httpx for testing.

4. **Run the website**
   ```bash
   uvicorn main:app --reload
   ```

5. **Run unit tests**
   ```bash
   pytest
   ```
   Test results will be shown in the terminal. You can find and edit tests in `test_main.py`.

## Running the Website

1. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```
   The website will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

2. **(Optional) Run with the provided shell script**
   ```bash
   ./run_website.sh
   ```

## Docker Setup

You can easily deploy this website using Docker:

1. **Build the Docker image**
   ```bash
   docker build -t memphis_website .
   ```

2. **Run the Docker container**
   ```bash
   docker run -d -p 8000:8000 memphis_website
   ```

The website will be available at [http://localhost:8000](http://localhost:8000) on your server.

**Files for Docker deployment:**
- `Dockerfile`: Defines the build steps for the container
- `requirements.txt`: Python dependencies
- `.dockerignore`: Keeps the image clean

## Ollama & Mistral Setup

To enable the "Ask Questions" feature with Mistral:

1. **Install Ollama**
   Follow instructions at https://ollama.com/download

2. **Pull the Mistral model**
   ```bash
   ollama pull mistral
   ```

3. **Start Ollama and make it accessible to other machines/containers**
   ```bash
   OLLAMA_HOST=0.0.0.0:11434 ollama serve
   ```
   This will bind Ollama to all network interfaces so Docker and other machines can connect.

4. **Test Mistral API**
   ```bash
   curl -X POST http://localhost:11434/api/generate -d '{"model": "mistral", "prompt": "Hello"}' -H "Content-Type: application/json"
   ```
   You should see a streaming JSON response from Mistral.

5. **Configure your FastAPI app**
   Make sure your app uses the correct host IP for `ollama_url` (e.g., `http://localhost:11434/api/generate` or your host IP if running in Docker).

## Project Structure
```
main.py                # FastAPI app entry point
static/                # Static files (CSS, images)
templates/             # Jinja2 HTML templates
run_website.sh         # Shell script to start the server
```

## Testing

Unit tests are provided using `pytest` and FastAPI's `TestClient`.

### Run all tests:
```bash
pytest
```

Test file: `test_main.py`

## License
MIT
