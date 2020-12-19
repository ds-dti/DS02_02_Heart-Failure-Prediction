# Heart Failure Prediction
**Kelompok 2 DS02 (Alva, Erdy, Kushvi, Rafi)**

![Project Poster](/static/images/poster.jpeg "Project Poster")

---

## Daftar Isi
1. [Daftar Isi](#Daftar-Isi)
2. [Project Description](#Project-Description)
3. [Fitur Aplikasi](#Fitur-Aplikasi)
4. [Petunjuk Penggunaan](#Petunjuk-Penggunaan)
    1. [Melakukan Prediksi](#Melakukan-Prediksi)
    2. [Menjalankan Web App di Localhost](#Menjalankan-Web-App-di-Localhost)
5. [Credits](#Credits)

---

## Project Description

Video Penjelasan Proyek: **[YouTube](https://youtu.be/GOGE2-fwA0E)**

Gagal jantung, juga dikenal sebagai gagal jantung kronis, adalah sindrom klinis yang disebabkan oleh disfungsi ventrikel. Gagal jantung adalah manifestasi serius atau tahap akhir dari berbagai penyakit jantung. **Gagal jantung adalah penyakit dengan angka kematian yang tinggi** dan biaya pengobatan yang tinggi. Berdasarkan pedoman *European Society of Cardiology (ESC)*, diseluruh dunia sekitar 26 juta orang dewasa hidup dengan adanya penyakit gagal jantung. [<sup>[1]</sup>](https://ieeexplore.ieee.org/document/8918034)

Faktor-faktor risiko penyakit gagal jantung ada 2 jenis yaitu factor yang dapat dihindari dan yang tidak dapat dihindari. Faktor risiko yang tidak dapat dihindari, antara lain: usia, jenis kelamin, riwayat penyakit keluarga, dan ras. Sedangkan, faktor risiko penyakit yang dapat dihindari, antara lain: hipertensi, profil lipid yang buruk, merokok, kurangnya aktivitas fisik, obesitas, diabetes melitus, konsumsi, makanan berlemak, dan konsumsi alkohol berlebih, dan lain-lain. [<sup>[2]</sup>](https://repository.ubaya.ac.id/37369/)

---

## Fitur Aplikasi
* **Responsive**: mudah dan nyaman dibuka baik di PC, laptop, maupun smartphone.
* **Different use for different needs**: aplikasi menyediakan dua fungsi utama yang dapat digunakan sesuai kebutuhan anda, pemeriksaan mandiri menggunakan fitur basic atau pemeriksaan lanjutan menggunakan fitur advanced.
* **Easy to access database**: semua data yang tersubmit akan tersimpan di Google Sheet yang nantinya data tersebut dapat digunakan untuk meningkatkan performa dari model machine learning.

---

## Petunjuk Penggunaan:
Prototype aplikasi yang sudah berjalan dan online dapat diakses **[disini](https://heart-failure-detection-298811.et.r.appspot.com/)**. Semua data yang disubmit pada prototype aplikasi di link tersebut akan disimpan ke Google Sheet di bawah ini:
* [Heart Failure Prediction New Data (Basic)](https://docs.google.com/spreadsheets/d/1iD2mtSyDw2KVYsgMzfLDO5aV4h_H4BnOQ1ij4dXcT4c/edit?usp=sharing)
* [Heart Failure Prediction New Data (Advanced)](https://docs.google.com/spreadsheets/d/1WkJh3uxwqdOq9Ep6x2CBOeKXlJv-A693Ml1D2M0BI7U/edit?usp=sharing)

### Melakukan Prediksi
1. Buka link web app [disini](https://heart-failure-detection-298811.et.r.appspot.com/).
2. Pilih jenis prediksi yang ingin digunakan (Basic atau Advanced).
3. Masukan data yang diminta aplikasi.
4. Klik tombol "Submit"
5. Tunggu beberapa detik hingga hasil prediksi anda muncul.

### Menjalankan Web App di Localhost
1. Clone repository ke localhost anda
2. Buka command prompt (CMD) pada folder repository
3. *Buat dan jalankan virtual environment Python. Petunjuk pembuatan virtual environment dapat dibaca di [sini](https://www.geeksforgeeks.org/python-virtual-environment/) (opsional)*
4. Ketik `pip install -r requirements.txt` pada CMD untuk menginstall libraries yang dibutuhkan
5. Run web app dengan mengetik `python main.py` pada CMD
6. Buka link yang muncul pada CMD di browser untuk menggunakan aplikasi (default ke 127.0.0.1:5000)
7. Tekan `CTRL+C` pada keyboard untuk menutup aplikasi.
*Notes: jika ingin menjalankan web app di localhost atau server anda sendiri, anda perlu untuk memiliki API untuk akses ke Google Drive dan Google Sheets. Jika anda sudah memiliki API tersebut simpan file JSON yang didpaat dari Google ke file bernama `credentials.json`dan simpan pada root folder aplikasi. Untuk cara mendapatkan API tersebut dapat dibaca [disini](https://medium.com/better-programming/integrating-google-sheets-api-with-python-flask-987d48b7674e)*

---

## Credits:
* [Heart Failure Prediction Dataset (CC BY 4.0)](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)
