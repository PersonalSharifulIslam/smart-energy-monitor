# ⚡ Smart Energy Monitor

A simple IoT project that measures **voltage, current, and power** using an ESP32/Arduino and sends data to a **Flask backend**, then displays it on a **web dashboard**.

## 📂 Project Structure
- `hardware/` → ESP32/Arduino firmware code
- `backend/` → Flask API to store & serve data
- `frontend/` → Web dashboard with Chart.js

## 🚀 Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/YOUR-USERNAME/smart-energy-monitor.git
   cd smart-energy-monitor
   ```
2. Install backend requirements:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```
3. Open `frontend/dashboard.html` in your browser.

## 🔧 Hardware
- ESP32 or Arduino with Wi-Fi
- Current Sensor (ACS712 / SCT013)
- Voltage divider for safe measurement

ESP32 sends JSON data:
```json
{
  "voltage": 220,
  "current": 1.5
}
```

## 📊 Features
- Real-time power monitoring
- Data stored in SQLite
- Web dashboard with charts

---

💡 Future improvements: cloud integration, alerts, mobile app.
