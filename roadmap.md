# Project Roadmap

## MVP (Current Features)

* [x] One-time config for API key and location
* [x] Automatic geolocation from postal code
* [x] Regular outdoor temperature checks using OpenWeatherMap
* [x] User input for current indoor temperature (°C)
* [x] Wait logic adjusts based on how close the temps are
* [x] Safe exit via Ctrl+C/Cmd+C at any time
* [x] Modular code—easy to maintain or extend

---

## Planned Features / Improvements

* [ ] **Forecast Crossover:**
  Check the 3-hour OpenWeatherMap forecast and tell the user when the temperature is *expected* to fall below indoor temp.
  *Status: To be added (likely in `weather_api.py`).*

* [ ] **Fahrenheit Support:**
  Allow user input/output in °F as well as °C, with proper conversion.
  *Status: To be added (possibly as `units.py`).*

* [ ] **Morning/Evening Logic:**
  Optional: Add functionality to suggest best window times, e.g. “Close before it gets too hot in the morning.”
  *Status: Idea stage (may go in `time_utils.py`).*

* [ ] **User Notifications:**
  Optionally add desktop notifications (pop-ups) in addition to console print.
  *Status: Future feature.*

* [ ] **Enhanced Input Validation:**
  More robust checking for all user input (temp, zip code, etc.)

* [ ] **Improved Error Handling:**
  Clearer messages for API/network failures, etc.

* [ ] **Sample Output & Screenshots:**
  For README and documentation polish.

---

## Stretch Ideas

* [ ] GUI version (Tkinter, PyQt, etc.)
* [ ] Mobile app version (Flutter, Kivy, etc.)
* [ ] Configurable check intervals and notification thresholds
* [ ] Dockerized setup for advanced users

---

### **Want to contribute or suggest ideas?**

Open an issue or pull request!
