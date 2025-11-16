# 🍱 ZidnyCalory App – Calory Object Detection

Capstone Project 4 – Purwadhika AI Engineer  
Nama: **Zidny Alifa Rayhan**

---

## 1. Deskripsi Singkat

ZidnyCalory App adalah aplikasi **object detection untuk makanan** yang bertujuan untuk:
- Mendeteksi berbagai jenis makanan yang ada dalam gambar (telur mata sapi, nasi, tempe, dll).
- Menghitung **jumlah setiap makanan**.
- Dapat Mengkonversi ke **total kalori** berdasarkan informasi kalori per 100 gram / per butir.

Aplikasi dibangun menggunakan:
- Model object detection **YOLO** (fine-tune dari pretrained `yolov12n_general.pt`).
- Training nya dilakukan di **Google Colab** dengan GPU (Tesla T4).
- Aplikasi web ini menggunakan **Streamlit** dan di-deploy ke **Streamlit Community Cloud**.

---

## 2. Dataset

Dataset yang digunakan: **Calory Dataset**  
Isinya adalah gambar makanan dengan anotasi bounding box dalam format YOLO.

Daftar class (contoh):

- Nasi -129 kal per 100gr-
- Ayam Goreng -260 kal per 100 gr-
- Capcay -67 kal per 100gr-
- Sayur bayam -36 kal per 100gr-
- Sayur kangkung -98 kal per 100gr-
- Sayur sop -22 kal per 100gr-
- Tahu -80 kal per 100 gr-
- Telur Dadar -93 kal per 100gr-
- Telur Mata Sapi -110kal1butir-
- Telur Rebus -78kal 1butir-
- Tempe -225 kal per 100 gr-
- Tumis buncis -65 kal per 100gr-
- food-z7P4

Struktur dataset:

```text
calory_dataset/
  data.yaml
  train/
    images/
    labels/
  valid/
    images/
    labels/
  test/
    images/
    labels/
