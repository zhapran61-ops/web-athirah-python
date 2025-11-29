
articles = [
    {
        "judul": "Hari Pertama Belajar Python",
        "tanggal": "14 Oktober 2025",
        "isi": "Hari ini aku belajar cara bikin web koran pakai HTML dan Python."
    },
    {
        "judul": "Eksperimen HTML",
        "tanggal": "15 Oktober 2025",
        "isi": "Sekarang aku bikin tampilannya lebih profesional pakai CSS kayak koran."
    }
]

template = open("template.html", "r", encoding="utf-8").read()

# Buat bagian isi artikel dari data di atas
content = ""
for a in articles:
    content += f"""
    <div class="article">
      <div class="quote">“{a['judul']}”</div>
      <div class="date">{a['tanggal']}</div>
      <p>{a['isi']}</p>
      <div class="image-placeholder"></div>
    </div>
    """

# Ganti isi artikel lama di template pakai hasil dari Python
html = template.replace(
    '<div class="content">', f'<div class="content">\n{content}\n', 1
)

# Simpan hasilnya jadi file baru
with open("newspaper.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ File 'newspaper.html' berhasil dibuat! Buka di browser aja langsung.")


