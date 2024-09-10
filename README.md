## (CC) Click Coffee
Tugas - 2 PBP : [Click Your Coffee Here!](http://nashwa-ghania-coffeeshop.pbp.cs.ui.ac.id/)


### Langkah Pengimplementasian

1. **Membuat sebuah proyek Django baru.**
   Membuat folder baru kemudian menjalankan virtual environment di dalamnya. Kemudian menginstall beberapa requirements yang dibutuhkan. Selanjutnya menjalankan perintah `django-admin startproject [nama_proyek]` untuk membuat direktori dasar dari proyek Django.

2. **Membuat aplikasi dengan nama main pada proyek tersebut.**<br>
   Menjalankan perintah `python manage.py startapp main` untuk membuat aplikan main.

3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**<br>
   Menambahkan rute yang diinginkan pada urls.py proyek untuk
   mengarahkan request ke aplikasi "main". 

4. **Membuat model pada aplikasi main dengan nama Product.**<br>
   Menambahkan model dengan atribut _name, price, description, time_, dan _stock_. Kemudian, memigrasikan model agar setiap perubahan dapat dilacak.

5. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML.**<br>
   Menambahkan fungsi frontpage di views.py untuk merender template HTML dan products yang ada. 

6. **Membuat sebuah routing pada urls.py aplikasi main.**<br>
   Menambahkan rute yang diinginkan pada urls.py main. untuk memetakan fungsi yang telah dibuat pada views.py.

7. **Melakukan deployment ke PWS.**<br>
   Membuat proyek baru di PWS kemudian menambahkan URL deployment pada ALLOWED_HOST dalam settings.py. Selanjutnya menjalankan perintah push ke PWS.

8. **Membuat sebuah README.md.**<br>
   Membuat file README.md yang berisi tautan menuju aplikasi PWS dan beberapa jawaban dari pertanyaan.

### Alur Django
<img width="491" alt="Screenshot 2024-09-10 at 23 05 38" src="https://github.com/user-attachments/assets/6d51b7bd-6f33-412d-8e9a-af292e41a086">

Request client pertama kali diproses oleh **urls.py**, yang mencocokkan URL dengan fungsi view di **views.py**. Di dalam **views.py**, logika dijalankan dan jika data dari database diperlukan, fungsi view memanggil model di **models.py**. Setelah data diperoleh, view menyiapkan template HTML dengan data tersebut, lalu merendernya. Hasilnya berupa halaman web atau respon JSON yang dikirim kembali ke browser client. 

### Fungsi Git

1. Riwayat Perubahan Lengkap. Git dapat melacak setiap perubahan yang dilakukan pada setiap file, termasuk mencatat siapa yang membuat perubahan dan kapan perubahan itu dilakukan.<br>
2. Branching dan Merging. Dengan git, sebuah proyek dapat dikerjakan dengan banyak orang. Meskipun bekerja sendiri-sendiri, pengguna dapat mengerjakan bagian yang berbeda secara terpisah dengan cara membuat “branch”. Nantinya, pengguna dapat menggabungkan kembali bagian-bagian yang terpisah ini dengan fitur “merge”. <br>
3. Open Source. Git adalah tools yang bersifat open source sehingga dapat digunakan untuk membuat perangkat lunak secara open source. <br>
4. Backup. Git dapat menjadi backup jika terjadi kesalahan atau masalah dalam mengembangkan versi terbaru, Git dapat mengembalikan ke dalam versi sebelumnya. <br>

### Mengapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django menggunakan arsitektur Model-View-Template (MVT) yang membantu untuk memahami pemisahan logika aplikasi, data, dan tampilan dengan baik. Django juga menyediakan banyak fitur yang dapat digunakan langsung, seperti autentikasi pengguna, URL routing, ORM (Object-Relational Mapping), dan lainnya. Ini memudahkan pemula karena mereka tidak perlu membangun semuanya dari nol.

### Mengapa model pada Django disebut ORM?

Model Django disebut ORM karena memungkinkan untuk berinteraksi dengan database menggunakan Python, tanpa menulis query SQL langsung. Django ORM secara otomatis mengonversi model Python menjadi tabel database, menjadikan proses pengelolaan data lebih mudah dan mengurangi kemungkinan kesalahan dalam penulisan query SQL manual.
