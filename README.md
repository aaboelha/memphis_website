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

## Project Structure
```
main.py                # FastAPI app entry point
static/                # Static files (CSS, images)
templates/             # Jinja2 HTML templates
run_website.sh         # Shell script to start the server
```

## License
MIT
