# Django Weather App

This project is a simple Django application that allows users to enter a city name and view the current weather using a public weather API.

## Features
- Enter a city name to get current weather information
- Uses a public weather API (e.g., OpenWeatherMap)
- Simple, clean UI

## Getting Started

1. **Set up the virtual environment:**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```powershell
   pip install django requests
   ```
3. **Run the server:**
   ```powershell
   python manage.py runserver
   ```
4. **Access the app:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure
- `weather_project/` - Django project settings
- `weather/` - Main weather app

## Customization
- Update the weather API key in the app as needed.

---

This project was generated automatically. For questions, see the code comments or ask Copilot!
