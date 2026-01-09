<div align="center">

# 📡 WiFi Scanner Pro
**Modern WiFi Scanner for Termux (Educational Tool)**

![Termux](https://img.shields.io/badge/Termux-000000?style=for-the-badge&logo=termux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

Minimal • Fast • Visual • Open Source

[Install](#-install) · [Features](#-features) · [Usage](#-usage) · [Warning](#-warning)

</div>

---

## ✨ Features

- 📶 Real-time WiFi scanning  
- 📊 Signal strength visualization (bars)  
- 🔐 Security type detection  
- 🔦 Flash LED indicator while scanning  
- 🎨 Colored terminal output  
- 🖼️ ASCII banner on start  
- ⚡ Lightweight & fast  

---

## 📦 Requirements

- Android device
- Termux
- **Termux:API (WAJIB)**

https://f-droid.org/en/packages/com.termux.api/

- Python 3

---

## 🚀 Install

### 1. Install dependencies

pkg update && pkg upgrade -y pkg install python3 git termux-api -y pip install colorama termux-setup-storage

### 2. Clone repository

git clone https://github.com/agusjawirtechid/WifiScan.git cd WifiScan

### 3. Run

python3 app.py

---

## ▶️ Usage

Saat dijalankan:
- Banner ASCII tampil
- Flash LED berkedip sebagai indikator
- Scan WiFi dimulai otomatis
- Output menampilkan:
  - SSID
  - Signal bar
  - Security type
  - Password (dummy)

Input pemilihan WiFi hanyalah simulasi edukasi.

---

## 🧩 Tech Stack

- Python 3
- Termux API
- Colorama
- JSON
- Subprocess

---

## 🗂️ Core Functions

termux-wifi-scaninfo   → Scan WiFi termux-torch on/off    → Flash LED RSSI → Signal Bar      → Visual strength Colorama               → Terminal colors Interactive input      → Simulation

---

## ⚠️ Warning

THIS IS NOT A HACKING TOOL

- ❌ No WiFi cracking
- ❌ No password stealing
- ❌ No data logging
- ✅ Legal WiFi scanner
- ✅ Educational purpose only

Program message:

Mana bisa tolol 😂

---

## 🛠️ Troubleshooting

WiFi not detected:

pkg install termux-api -y termux-wifi-scaninfo

Command not found:

pkg update pkg install termux-tools termux-api

---

## 📄 License

MIT License © 2024 Agus Jawir Tech ID

---

## 👤 Author

Agus Jawir Tech ID

---

<div align="center">

⭐ Star the repo if this project helps you  
🚀 Built for learning & exploration

</div>
