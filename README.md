<div align="center">

# 📶 WiFi Scanner Pro
### **Alat Pemindai WiFi untuk Termux (Edukasi & Legal)**

![Termux](https://img.shields.io/badge/Termux-000000?style=for-the-badge&logo=termux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-2.0-blue?style=for-the-badge)

*Pemindai jaringan WiFi dengan tampilan visual menarik berbasis Termux API*

[Instalasi](#-instalasi) • [Fitur](#-fitur-utama) • [Demo](#-demo) • [Penggunaan](#-penggunaan) • [Troubleshooting](#-troubleshooting)

</div>

---

## 🎯 Fitur Utama

### 🔍 Pemindaian WiFi
- Scan jaringan WiFi di sekitar secara real-time
- Menampilkan SSID, kekuatan sinyal, dan jenis keamanan
- Visualisasi sinyal dalam bentuk bar

### ⚡ Fitur Visual
- Efek flash LED saat scanning
- Warna terminal menggunakan Colorama
- ASCII Art saat aplikasi dijalankan
- Efek loading & delay

### 🔒 Keamanan & Etika
- Hanya untuk edukasi
- Tidak menyimpan data
- Bukan alat hacking
- Tidak bisa membobol WiFi

---

## 📸 Demo

Contoh output saat dijalankan:

\ \        / ()/ |/ | \ \  /\  / / | || |     __ _ _ __ \ /  / / | |  | |    / ` | ' 
/\  /\  /  | | | | | | | (| | | | /  /  /   ||  ||    _,| |_|

[FLASH BERKEDIP 3x...]

Nama WiFi : Home-WiFi-5G Sinyal    : [||||  ] 4 Keamanan  : WPA2-PSK Password  : ********

Nama WiFi : Cafe_Free Sinyal    : [||    ] 2 Keamanan  : OPEN Password  : ********

---

## 🚀 Instalasi

### Install kebutuhan

pkg update && pkg upgrade -y pkg install python3 git termux-api -y pip install colorama termux-setup-storage

### Clone repository

git clone https://github.com/agusjawirtechid/WifiScan.git cd WifiScan

### Jalankan

python3 app.py

---

## 📖 Penggunaan

Saat program dijalankan:
1. ASCII art muncul
2. Flash LED berkedip
3. Scan WiFi dimulai
4. Data WiFi ditampilkan (SSID, sinyal, keamanan)

Input pemilihan WiFi hanya simulasi edukasi.

---

## 🛠️ Teknologi

- Python 3
- Termux API
- Colorama
- JSON
- Subprocess

---

## 📁 Fitur Kode

termux-wifi-scaninfo termux-torch on/off JSON parsing RSSI to signal bar Colorama output Interactive input

---

## ⚠️ Penting

INI BUKAN TOOLS HACKING

- Tidak bisa hack WiFi
- Tidak bisa crack password
- Tidak mengambil data pribadi
- Hanya untuk edukasi

Pesan humor dari program:

Mana bisa tolol😂😂

---

## 🔧 Troubleshooting

WiFi tidak terdeteksi:

pkg install termux-api -y termux-wifi-scaninfo

Command tidak ditemukan:

pkg update pkg install termux-tools termux-api

---

## 🤝 Kontribusi

Fork → Branch → Commit → Push → Pull Request

---

## 📄 License

MIT License © 2024 Agus Jawir Tech ID

---

## 👤 Author

Agus Jawir Tech ID

---

🌟 Jangan lupa kasih star jika membantu!
