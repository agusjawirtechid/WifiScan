```markdown
<div align="center">

# 📶 WiFi Scanner Pro
### **Alat Pemindai WiFi Lengkap dengan Fitur Menarik**

![Termux](https://img.shields.io/badge/Termux-000000?style=for-the-badge&logo=termux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-2.0-blue?style=for-the-badge)

*Pemindai WiFi dengan visual menarik dan fitur unik untuk Termux*

[Instalasi](#-instalasi-sekali-klik) • [Fitur](#-fitur-utama) • [Demo](#-demo) • [Penggunaan](#-penggunaan)

</div>

---

## 🎯 Fitur Utama

### 🔍 **Pemindaian WiFi**
- Deteksi jaringan WiFi terdekat secara real-time
- Tampilkan SSID, kekuatan sinyal, dan jenis keamanan
- Analisis kualitas sinyal dengan indikator visual

### ⚡ **Fitur Spesial**
- **Efek lampu flash** - Flash HP berkedip saat memindai
- **Tampilan ASCII Art** - Logo keren saat program dijalankan
- **Indikator sinyal bar** - Visualisasi kekuatan sinyal
- **Warna terminal** - Interface berwarna dengan Colorama
- **Efek delay** - Animasi loading untuk pengalaman lebih baik

### 🔒 **Keamanan**
- Hanya untuk tujuan edukasi
- Tidak menyimpan data sensitif
- Open source dan transparan

---

## 📸 Demo

**Tampilan saat dijalankan:**
```

---

\ \        / (_)/ |/ |
  \ \  /\  / / | || |     __ _ _ __
   \ \/  \/ / | |  | |    / ` | ' \ 
\  /\  /  | | | | || (| | | | |
\/  \/   |||  \___\_,|| ||

[FLASH BERKEDIP 3x...]

nama wifi: Home-WiFi-5G
PING SINYAL [||||  ] 4
Keamanan wifi [WPA2-PSK]
password : ********

nama wifi: Cafe_Free
PING SINYAL [||    ] 2
Keamanan wifi [OPEN]
password : ********

```

---

## 🚀 Instalasi Sekali Klik

**Salin semua kode di bawah ini dan paste di Termux:**

```bash
# Update & install dependencies
pkg update && pkg upgrade -y
pkg install python3 git -y
pip install colorama

# Install Termux API
pkg install termux-api -y
termux-setup-storage

# Download WiFi Scanner
git clone https://github.com/agusjawirtechid/WifiScan.git
cd WifiScan

# Jalankan program
python3 app.py
```

Atau instal dengan satu command:

```bash
curl -s https://raw.githubusercontent.com/agusjawirtechid/WifiScan/main/install.sh | bash
```

---

📖 Penggunaan

Menjalankan Program

```bash
cd WifiScan
python3 app.py
```

Apa yang Terjadi?

1. ✅ Logo ASCII ditampilkan
2. ⚡ Flash HP berkedip 3x sebagai indikator
3. 📡 Pemindaian WiFi dimulai
4. 📊 Hasil ditampilkan dengan:
   · Nama WiFi (SSID)
   · Kekuatan sinyal (bar visual)
   · Jenis keamanan
   · Placeholder password

Fitur Interaktif

Program akan meminta input untuk "memilih WiFi", tetapi ini adalah Easter Egg edukasi yang mengingatkan tentang keamanan jaringan.

---

🛠️ Teknologi yang Digunakan

· Python 3 - Bahasa pemrograman utama
· Termux API - Akses hardware Android
· Colorama - Warna terminal
· JSON - Parsing data WiFi
· Subprocess - Eksekusi command Termux

---

📁 Struktur Kode

```python
# Fitur utama dalam kode:
1. termux-wifi-scaninfo    # Memindai jaringan WiFi
2. termux-torch on/off     # Kontrol flash LED
3. JSON parsing            # Analisis data WiFi
4. RSSI to signal bar      # Konversi sinyal ke visual
5. Colorama formatting     # Warna terminal
6. Interactive input       # Fitur interaktif
```

---

⚠️ Penting!

INI BUKAN HACKING TOOL!

· ❌ Tidak bisa hack password WiFi
· ❌ Tidak bisa crack jaringan
· ❌ Tidak menyimpan data pribadi
· ✅ Hanya alat pemindai legal
· ✅ Untuk edukasi keamanan jaringan
· ✅ Belajar Python & Termux API

Pesan dari program:

```
"Mana bisa tolol😂😂"
```

← Ini adalah pengingat humor bahwa keamanan WiFi itu serius dan tidak bisa dibobol semudah itu!

---

🔧 Troubleshooting

Masalah: "Wifi tidak ditemukan"

```bash
# Solusi 1: Install Termux API
pkg install termux-api -y

# Solusi 2: Beri izin
termux-wifi-scaninfo

# Solusi 3: Restart Termux
exit
# Buka Termux lagi
```

Masalah: "Command not found"

```bash
pkg update
pkg install termux-tools termux-api
```

---

🤝 Kontribusi

Ingin menambah fitur?

1. Fork repository
2. Buat branch baru
3. Commit perubahan
4. Push ke branch
5. Buat Pull Request

---

📄 License

MIT License © 2024 Agus Jawir Tech ID

---

👤 Author

Agus Jawir Tech ID

---

<div align="center">

🌟 Jangan lupa kasih star jika project ini membantu!

🔔 Pantau untuk update fitur baru!

</div>
```
