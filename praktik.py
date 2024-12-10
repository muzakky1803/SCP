import streamlit as st
from typing import List

# Data penyakit dan gejala
penyakit = {
    "P1": "Diabetes",
    "P2": "Ginjal kronis",
    "P3": "Sindrom nefrotik",
    "P4": "Infeksi saluran kemih",
    "P5": "Obstruksi saluran kemih",
    "P6": "Pielonefritis/infeksi ginjal",
    "P7": "Sistitis",
    "P8": "Nefropati diabetik",
}

gejala = {
    "G1": "Buang air kecil lebih dari 5 sampai 8 kali sehari",
    "G2": "Perasaan urine tidak sepenuhnya keluar setelah buang air kecil",
    "G3": "Bau urine yang tidak seperti biasa",
    "G4": "Sensasi terbakar atau perih saat buang air kecil",
    "G5": "Urin berwarna merah",
    "G6": "Rasa selalu ingin buang air kecil dan tidak bisa ditahan",
    "G7": "Frekuensi buang air kecil sering tapi jumlah urin yang sedikit",
    "G8": "Disfungsi ereksi pada pria",
    "G9": "Nyeri saat buang air",
    "G10": "Rasa sakit atau sensasi terbakar pada perut bagian bawah",
    "G11": "Kandung kemih membesar terkadang terasa di bagian bawah perut tepat di atas tulang kemaluan",
    "G12": "Perut bagian samping (pinggul) mengalami rasa sakit",
    "G13": "Seperti ada tertekan pada panggul",
    "G14": "Nyeri pada perut",
    "G15": "Nyeri punggung",
    "G16": "Kram otot",
    "G17": "Sesak nafas",
    "G18": "Cegukan berlebih",
    "G19": "Pernafasan lebih dari 12 sampai 20 kali per menit",
    "G20": "Nyeri pada dada",
    "G21": "Susah tidur",
    "G22": "Mendengkur saat tidur",
    "G23": "Kehilangan kesadaran",
    "G24": "Sakit kepala",
    "G25": "Lemas",
    "G26": "Tubuh mudah merasa lelah",
    "G27": "Sering merasa haus",
    "G28": "Selalu merasa lapar",
    "G29": "Kehilangan nafsu makan",
    "G30": "Berat badan menurun atau bertambah lebih dari 1,5 sampai 2,5 kg per minggu",
    "G31": "Mual",
    "G32": "Muntah",
    "G33": "Pembengkakan pada pergelangan kaki, kaki atau tangan",
    "G34": "Pembengkakan sekitar mata",
    "G35": "Suhu badan di atas 38 derajat Celcius",
    "G36": "Tubuh kadang dingin atau menggigil",
    "G37": "Tekanan darah di atas 140/90 mm Hg",
    "G38": "Penglihatan kabur",
    "G39": "Kurang konsentrasi",
    "G40": "Kulit terasa gatal",
    "G41": "Kulit luka lebih dari 7 sampai 21 hari",
    "G42": "Berat badan menurun atau bertambah secara drastis",
    "G43": "Luka sulit sembuh",
    "G44": "Nafas lebih cepat",
    "G45": "Urin terdapat darah",
    "G46": "Tekanan darah tinggi",
    "G47": "Menurun ketajaman mental",
    "G48": "Demam tinggi",
    "G49": "Sering buang air kecil",
}

# Aturan (rules)
aturan = [
    {"gejala": ["G1", "G49"], "penyakit": "P1"},
    {"gejala": ["G19", "G44"], "penyakit": "P2"},
    {"gejala": ["G30", "G42"], "penyakit": "P3"},
    {"gejala": ["G41", "G43"], "penyakit": "P4"},
    {"gejala": ["G35", "G5"], "penyakit": "P5"},
    {"gejala": ["G23"], "penyakit": "P6"},
    {"gejala": ["G24", "G37", "G38"], "penyakit": "P7"},
    {"gejala": ["G1", "G19", "G27", "G28", "G30", "G41"], "penyakit": "P8"},
    {"gejala": ["G5", "G8", "G16", "G17", "G18", "G20", "G23", "G26", "G29", "G31", "G32", "G33", "G40"], "penyakit": "P9"},
    {"gejala": ["G24", "G33", "G34", "G37", "G38"], "penyakit": "P10"},
    {"gejala": ["G1", "G2", "G5", "G7", "G11", "G12", "G14", "G31", "G32", "G35"], "penyakit": "P11"},
    {"gejala": ["G3", "G5", "G14", "G15", "G25", "G29", "G31", "G32", "G35", "G36"], "penyakit": "P12"},
    {"gejala": ["G1", "G3", "G4", "G5", "G7", "G9", "G10"], "penyakit": "P13"},
    {"gejala": ["G1", "G16", "G21", "G22", "G29", "G30", "G31", "G32", "G33", "G34", "G39", "G40"], "penyakit": "P14"}
]

# Fungsi untuk mendeteksi penyakit berdasarkan gejala
def deteksi_penyakit(input_gejala: List[str]) -> List[str]:
    hasil = []
    for rule in aturan:
        if all(gejala in input_gejala for gejala in rule["gejala"]):
            hasil.append(rule["penyakit"])  # Menyimpan kode penyakit
    return hasil

# Streamlit interface
st.title("Sistem Pakar Deteksi Penyakit Ginjal")
st.write("Pilih gejala yang Anda alami:")

# Menggunakan session_state untuk menyimpan gejala yang dipilih
if 'selected_gejala' not in st.session_state:
    st.session_state.selected_gejala = []

# Pilihan gejala oleh pengguna
for kode, nama in gejala.items():
    if st.checkbox(f"{kode}: {nama}", value=(kode in st.session_state.selected_gejala)):
        if kode not in st.session_state.selected_gejala:
            st.session_state.selected_gejala.append(kode)
    else:
        if kode in st.session_state.selected_gejala:
            st.session_state.selected_gejala.remove(kode)

# Deteksi penyakit
if st.button("Deteksi Penyakit"):
    penyakit_terdeteksi = deteksi_penyakit(st.session_state.selected_gejala)
    
    # Menampilkan hasil
    if penyakit_terdeteksi:
        st.write("\nPenyakit yang terdeteksi berdasarkan gejala Anda:")
        for p in penyakit_terdeteksi:
            # Menampilkan nama penyakit berdasarkan kode
            st.write(f"- {penyakit[p]}")
    else:
        st.write("\nTidak ada penyakit yang terdeteksi berdasarkan gejala yang Anda masukkan.")
    
    # Tombol reset untuk menghapus pilihan gejala
    if st.button("Reset Pilihan Gejala"):
        # Reset gejala yang dipilih
        st.session_state.selected_gejala = []  
        st.experimental_rerun()  # Mereload aplikasi untuk reset checkbox
