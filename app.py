import streamlit as st
from ultralytics import YOLO
from PIL import Image
st.set_page_config(page_title="ZidnyCalory App", page_icon="🍱")

@st.cache_resource
def load_model():
    model = YOLO("models/best.pt")  
    return model

model = load_model()

kalori_per_class = {
    "Ayam Goreng -260 kal per 100 gr-": 260,
    "Capcay -67 kal per 100gr-": 67,
    "Nasi -129 kal per 100gr-": 129,
    "Sayur bayam -36 kal per 100gr-": 36,
    "Sayur kangkung -98 kal per 100gr-": 98,
    "Sayur sop -22 kal per 100gr-": 22,
    "Tahu -80 kal per 100 gr-": 80,
    "Telur Dadar -93 kal per 100gr-": 93,
    "Telur Mata Sapi -110kal1butir-": 110,
    "Telur Rebus -78kal 1butir-": 78,
    "Tempe -225 kal per 100 gr-": 225,
    "Tumis buncis -65 kal per 100gr-": 65,
    "food-z7P4": 0
}

st.title("🍱 ZidnyCalory App")
st.write("Deteksi makanan dan hitung total kalori nya secara otomatis dari gambar yang kamu upload.")

uploaded_file = st.file_uploader("Upload gambar makanan", type=["jpg", "jpeg", "png"])
conf_thres = st.slider("Confidence threshold", 0.1, 0.9, 0.5, 0.05)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Gambar Input", use_column_width=True)

    results = model.predict(image, conf=conf_thres)
    res = results[0]

    plotted = res.plot()
    plotted_rgb = plotted[:, :, ::-1]
    st.image(plotted_rgb, caption="Hasil Deteksi", use_column_width=True)

    if res.boxes is None or res.boxes.cls is None:
        st.warning("Tidak ada objek makanan terdeteksi.")
    else:
        class_ids = res.boxes.cls.cpu().numpy().astype(int)
        class_names = [model.names[cid] for cid in class_ids]

        counts = {}
        total_cal = 0

        for name in class_names:
            counts[name] = counts.get(name, 0) + 1

        st.subheader("🍽 Rincian Deteksi Makanan")
        for name, count in counts.items():
            cal = kalori_per_class.get(name, 0) * count
            total_cal += cal
            st.write(f"- **{name}** : {count}x → {cal} kcal")

        st.markdown("---")
        st.subheader(f"🔥 Total Kalori: **{total_cal} kcal**")

        if total_cal < 300:
            st.info("Kategori: **Rendah Kalori** (baik untuk makanan ringan atau jika sedang diet).")
        elif total_cal <= 700:
            st.info("Kategori: **Sedang** (untuk 1 porsi makan normal).")
        else:
            st.warning("Kategori: **Tinggi** (dibatasi jika sedang diet).")
