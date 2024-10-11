# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

### Permasalahan Bisnis
Meskipun Jaya Jaya Institus mencetak banyak lulusan dengan reputasi sangat baik, banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
Cakupan proyek untuk mengatasi masalah tersebut diantaranya membuat sebuah sistem berbasis machine learning untuk memprediksi apakah siswa akan drop out dari institut atau tidak. Selain itu, proyek ini juga membuat dashboard untuk memantau beberapa faktor yang menyebabkan siswa drop out.

### Persiapan

Sumber data: [Students' Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:
```python
mkdir student_performance_analysis
cd student_performance_analysis
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Business Dashboard
Link dashboard: [dashboard student dropout analysis](https://lookerstudio.google.com/reporting/488e6c7c-4aab-4a37-9356-bbddb3960cec).

Dashboard yang dibuat memiliki 5 visualisasi diantaranya: KPIs, Dropout by Course Categories, Dropout by Tuition fee up to date, Dropout by Displaced, dan Dropout by Scholarship. Tampilan dashboard dapat dilihat sebagai berikut,

![dewi_karimah-dashboard](https://github.com/user-attachments/assets/22ae4e8c-7e16-4756-80a3-7cae4ca501f1)

Gambar 1. Tampilan Dashboard

### KPIs
Visualisasi yang pertama adalah KPIs yang terdiri dari Overall Students (jumlah total siswa), Graduate (jumlah siswa yang telah lulus), Enrolled (jumlah siswa yang terdaftar), Dropout (jumlah siswa yang keluar), 
dan Dropout Rate (siswa yang keluar per keseluruhan siswa). Dari gambar 1. dapat dilihat bahwa jumlah siswa yang keluar atau presentase dropout rate lebih tinggi daripada jumlah siswa yang terdaftar dan belum lulus. Prosentase yang tinggi ini dapat mengakibatkan beberapa hal apabila tidak segera ditangani seperti citra institut yang semakin menurun dan jumlah siswa baru yan menurun di tahun ajaran baru.

### Dropout by Course Categories
Pada bagian ini grafik yang digunakan adalah bar chart yang bertujuan untuk menampilkan perbandingan jumlah siswa yang keluar di setiap kursus yang ada. Hasil visualisai grafik yang ditampilkan pada gambar 1. menunjukkan bahwa kursus manajemen baik yang hanya dihadiri sore hari dan yang biasa memiliki jumlah siswa dropout paling banyak daripada kursus yang lain. Adapun penyebab hal tersebut diantaranya kursus manajemen merupakan kursus dengan peminat yang lebih banyak daripada yang lainnya yang dapat menyebabkan persaingan akademik yang tinggi, ekspektasi siswa yang tidak sesuai dengan bayangan mereka, dan jalur karier kursus manajemen yang luas dan tidak spesifik.

### Dropout by Tuition fee up to date
Pada bagian ini grafik yang digunakan adalah doughnut chart yang bertujuan untuk menampilkan prosentase perbandingan antara siswa dropout yang mengalami pembaruan atas biaya pendidikan mereka dan yang tidak. Dapat dilihat pada gambar 1. jumlah prosentase siswa dropout yang mengalami pembaruan biaya lebih besar daripada yang tidak, hal ini membuktikan banyak siswa yang memilih keluar dikarenakan biaya pendidikan yang lebih tinggi daripada yang sebelumnya.

### Dropout by Displaced
Pada bagian ini grafik yang digunakan juga sama dengan yang sebelumnya yang bertujuan untuk menampilkan prosentase perbandingan antara siswa dropout yang pindah dari tempat asalnya. Hasil grafik pada gambar 1. menunjukkan bahwa jumlah siswa dropout yang pindah lebih banyak daripada yang tidak. Hal ini bisa terjadi kemungkinan karena siswa lebih memilih institut yang lebih dekat dari tempat tinggalnya.

### Dropout by Scholarship
Pada bagian ini grafik yang digunakan juga sama dengan yang sebelumnya yang bertujuan untuk menampilkan prosentase perbandingan antara siswa dropout yang beasiswa dan yang bukan. Hasilnya dapat dilihat pada gambar 1. menunjukkan bahwa jumlah siswa dropout yang bukan beasiswa jauh lebih banyak daripada yang beasiswa. Hal ini menunjukkan bahwa siswa dropout kemungkinan memiliki masalah dengan finansial tetapi tidak mendapatkan beasiswa dan menyebabkan mereka keluar dari institut atau juga bisa siswa keluar karena ada institut lain yang menawarkan biaya yang lebih terjangkau.

## Menjalankan Sistem Machine Learning
Untuk menjalankan streamlit app dapat menjalankan perintah berikut,
```python
streamlit run app.py
```
atau bisa menggunakan link URL streamlit app: [Student Dropout Prediction](https://student-dropout-prediction-31.streamlit.app/).

Cara pengisian dapat dilihat pada video singkat berikut: [Video Tutorial Pengisian](https://www.awesomescreenshot.com/video/32451396?key=ae274d22cb7e9b557765cfc93be79d21)


## Conclusion
Dari dashboard yang telah dibuat dapat disimpulkan bahwa:
- Jumlah siswa yang dropout lebih banyak daripada siswa yang aktif.
- Manajemen merupakan kursus yang memiliki siswa dropout paling banyak.
- Siswa dropout yang mengalami pembaruan biaya lebih banyak daripada yang tidak.
- Siswa dropout yang pindah lebih banyak daripada yang tidak.
- Siswa dropout yang tidak mendapatkan beasiswa lebih banyak daripada yang tidak.

Sedangkan untuk model machine learning yang dibuat mendapatkan akurasi sebesar 76%.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan mereka.
- Dukungan finansial yatau beasiswa yang merata tidak hanya untuk yang berprestasi tetapi yang terkendala finansial.
- Mengadakan bimbingan karier.
- Mengadakan kerja sama dengan perusahaan untuk program magang.
