# Window Temp Alert

This is a Python utility that helps you know when it's cool enough outside to open your windows or when it's time to close them in the morning.
Perfect for hot weather, city dwellers, or anyone trying to optimize home ventilation and energy use.

---

## Features

* Automatic weather check using OpenWeatherMap and your zip code.
* Simple, one-time config (location and API key).
* Modular, maintainable code structure.
* Easy to extend: add unit conversions, forecasts, or notifications.
* **Privacy:** No personal data or API keys are shared or collected.

---

## Requirements

* Python 3.8+
* Dependencies listed in `pyproject.toml` (installed by setup scripts)
  > **Note:** This project uses [uv](https://github.com/astral-sh/uv) for fast, reliable virtual environments and dependency management. If you don't have it, install with `pip install uv`.

---

## How to Use

1. **Clone the repo.**

2. **Set up your virtual environment and install dependencies:**

   * **On Linux/macOS:**

     ```bash
     ./project_setup.sh
     ```

   * **On Windows:**

     ```cmd
     project_setup.bat
     ```

      * **Important for Windows/PowerShell users:**

        If you see an error about “execution policy” or `activate.ps1` not loading, run the following command in your PowerShell window **before** activating the virtual environment:

        ```powershell
        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        .venv\Scripts\Activate.ps1
        ```

        This temporarily allows script activation in just this window.  
        Alternatively, use **Command Prompt** (`cmd.exe`) instead of PowerShell, and run:

        ```command prompt
        .venv\Scripts\activate.bat
        ```

        You should see `(.venv)` in your prompt when the virtual environment is active.

   * **Alternatively (cross-platform, Python 3.8+):**

     ```bash
     python project_setup.py
     ```

   This will:

   * Create a `.venv` using uv
   * Install all dependencies from `uv.lock`/`pyproject.toml`

3. **Get a free OpenWeatherMap API key:**

   * Register at [openweathermap.org](https://home.openweathermap.org/) for a *free* account.
   * Retrieve your API key [here](https://home.openweathermap.org/myservices).

4. **First-time setup:**

   * When you run the app for the first time, it will prompt you for your postal code, country, and API key, and store them in a local config file (`config.py`, which is ignored by git).

   *Tip:*
   You can also run the setup utility (`config_utils.py`) directly:

   ```
   python window_temp/config_utils.py
   ```

   This creates or updates your `config.py` without running the main app.

5. **Run the app:**

   ```
   python main.py
   ```

   * Enter your current indoor temperature when prompted.
   * The app will check the outdoor temperature and let you know when it's time to open the windows.
   * The app will pause at the end so you can see the result before closing.

---
**Note:**  
You can safely stop the process at any time with `Ctrl+C` (Windows/Linux) or `Cmd+C` (Mac).

---

## Notes & Limitations

* **API key license:**
  This project uses the free tier of the OpenWeatherMap API.
  You are responsible for following [OpenWeatherMap's terms of use](https://openweathermap.org/themes/openweathermap/assets/docs/Openweather_website_terms_and_conditions_of_use.pdf) and [API licensing](https://openweather.co.uk/privacy-policy) when using your own key.
  *No actual API keys are shared in this repository.*

* **Config safety:**
  Your personal API key and config file are ignored by git (`config.py` is in `.gitignore`).

* **Supported regions:**
  Any country supported by OpenWeatherMap and pgeocode.

* **Time-of-day detection:**
  The app determines morning/evening mode using your device's local system clock, **not** the OpenWeatherMap API.
  If your device's time or timezone is set incorrectly, you may get inaccurate “open/close window” recommendations.

* **Current version:**
  MVP – currently supports Celsius only, with planned support for Fahrenheit, forecast feature, and more.

---

## Project Structure

```
window_temp/
│
├── __init__.py         # Imports and exposes main functions
├── config_utils.py     # Setup and config file handling
├── geolocation.py      # Postal code to latitude/longitude
├── time_utils.py       # Waiting logic for periodic checks
├── weather_api.py      # OpenWeatherMap API calls
main.py                 # App entry point / user interface
[setup files]           # In project root (for venv/deps)
config.py               # created on first run
```

---

## Example Output

```
Input the current temperature inside (°C): 27.5
Current outdoor temperature: 29.0°C. Indoor: 27.5°C.
It is still 1.5 °C warmer outside.
Getting close! Checking again in 15mins.
...
OK, open your window :)
Press Enter to exit...
```

---

Pull requests welcome for new features or fixes!
If you have suggestions, please open an issue.

---

## License

This code is distributed under the MIT License.
You must comply with OpenWeatherMap's API terms for any use of weather data.
No weather data, API keys, or personal information are stored or distributed with this repository.