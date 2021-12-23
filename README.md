# Capstone Project Tim CSD-186 Program SIB Machine Learning dan Front-End Web

## DM : [Sistem Klasifikasi Harga Smartphone Berdasarkan Spesifikasi dan Ekspansinya] 

<p align="center" style="text-align:center;">
    <img alt="DM logo" src="https://github.com/danielrymeds/dataset1/blob/main/dicoding/log_caps.png?raw=true" width="300" />
</p>

## Application Summary:
DM app atau DepotMobile app merupakan sebuah sistem berbasis machine learning yang bertujuan untuk mengklasifikasi sebuah spesifikasi mobile phone atau telepon genggam, yang kemudian juga akan memberikan rekomendasi handphone brand tertentu dengan jangkauan harga dan spesifikasi yang serupa dengan input user.

Aplikasi ini berbasis web dan mudah, serta cukup ringan untuk digunakan. Aplikasi ini dapat digunakan di berbagai browser dan platform seperti dekstop, mobile, dan lainnya, namun penggunaan pada dekstop web lebih direkomendasikan untuk mendapatkan pengalaman terbaik selama menggunakan aplikasi ini. 


## How To Use:
1. ### Navigasi
    Halaman web aplikasi dapat diakses melalui link berikut: [MP App](https://priceclassification.herokuapp.com/). Web dapat diakses melalui browser apapun dan elemen yang dapat   dilihat pertama kali adalah bagian navigasi web yang terdiri dari:
        <p align="center" style="text-align:center;">
            <img alt="navigation" src="https://github.com/danielrymeds/dataset1/blob/main/dicoding/nav.png?raw=true" width="300" />
        </p>
    - Home : Mengarahkan user ke bagian halaman depan web jika ditekan
    - Start(Predict) : Mengarahkan user ke bagian model prediksi dan rekomendasi mobile phone berdasarkan inputan spesifikasi
    - About : Mengarahkan user ke bagian profil anggota tim developer web

2. ### Prediksi
    Setelah user scroll ke bawah atau menekan tombol navigasi 'Start', user diarahkan ke bagian model prediksi dan rekomendasi mobile phone berdasarkan inputan spesifikasi. Tampilan model prediksi pada web adalah seperti berikut:
        <p align="center" style="text-align:center;">
            <img alt="navigation" src="https://github.com/danielrymeds/dataset1/blob/main/dicoding/predict.png?raw=true" width="800" />
        </p>
    Pada bagan prediksi, terdapat tujuh kolom input yang dapat diisi oleh user. Ketujuh kolom input tersebut harus diisi oleh user agar tidak menghasilkan error. Ketujuh data spesifikasi input tersebut antara lain:
    - Weight : Data numerik yang menyatakan berat keseluruhan handphone dalam satuan gram
    - Width : Data numerik yang menyatakan resolusi lebar layar handphone dalam satuan pixel(px)
    - Height : Data numerik yang menyatakan resolusi tinggi/panjang layar handphone dalam satuan pixel(px)
    - ROM : Data numerik yang menyatakan kapasitas internal memori handphone dalam besaran megabyte (Mb)
    - RAM : Data numerik yang menyatakan memori RAM handphone dalam besaran megabyte (Mb)
    - Battery Capacity : Data numerik yang menyatakan kapasitas baterai handphone dalam besaran MAh
    - Brand : Data kelas yang menyatakan merk handphone dari lima merk yang tersedia, yaitu samsung, oppo, vivo, realme, dan xiaomi

3. ### Price Range
    Setelah semua data diinputkan oleh user dan kemudian ditekan tombol predict, maka akan muncul dua output. Output yang pertama adalah price range yang diklasifikasikan oleh sistem.
        <p align="center" style="text-align:center;">
            <img alt="navigation" src="https://github.com/danielrymeds/dataset1/blob/main/dicoding/price.png?raw=true" width="800" />
        </p>
    Output jangkauan harga terdiri dari empat kelas, antara lain:
    - Kelas pertama : < 100 USD
    - Kelas kedua : 100 - 200 USD
    - Kelas ketiga : 200 - 400 USD
    - Kelas keempat : >= 400 USD

4. ### Rekomendasi
    Output ke dua adalah tiga handphone yang direkomendasikan oleh sistem berdasarkan price range dan spesifikasi yang diinputkan oleh user. Contoh tampilan hasil rekomendasi pada web saat dilakukan prediksi adalah seperti berikut:
        <p align="center" style="text-align:center;">
            <img alt="navigation" src="https://github.com/danielrymeds/dataset1/blob/main/dicoding/recommendation.png?raw=true" width="800" />
        </p>
    Namun terdapat beberapa saat dimana sistem tidak dapat menemukan hasil rekomendasi yang memiliki spesifikasi yang mirip dengan inputan user dan brand yang dipilih user. Jika hal tersebut terjadi, maka akan muncul hasil seperti berikut:
        <p align="center" style="text-align:center;">
            <img alt="navigation" src="https://github.com/danielrymeds/dataset1/blob/main/dicoding/notfound.png?raw=true" width="800" />
        </p>
    Jika didapatkan hasil seperti di atas, maka user disarankan untuk menginputkan kembali data spesifikasi yang berbeda atau memilih brand handphone yang berbeda. Setelah itu, user dapat menekan kembali tombol predict dan mendapatkan hasil rekomendasi yang baru.
