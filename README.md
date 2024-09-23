## (CC) Click Coffee
Tugas PBP : [Click Your Coffee Here!](http://nashwa-ghania-coffeeshop.pbp.cs.ui.ac.id/)
<br>
<br>


### Tugas 2
#### Langkah Pengimplementasian

1. **Membuat sebuah proyek Django baru.**<br>
   Membuat folder baru kemudian menjalankan virtual environment di dalamnya. Kemudian menginstall beberapa requirements yang dibutuhkan. Selanjutnya menjalankan perintah `django-admin startproject [nama_proyek]` untuk membuat direktori dasar dari proyek Django.

2. **Membuat aplikasi dengan nama main pada proyek tersebut.**<br>
   Menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi main.

3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**<br>
   Menambahkan rute yang diinginkan pada urls.py proyek untuk mengarahkan request ke aplikasi "main". 

4. **Membuat model pada aplikasi main dengan nama Product.**<br>
   Menambahkan model dengan atribut _name, price, description, time_, dan _stock_. Kemudian, memigrasikan model agar setiap perubahan dapat dilacak.

5. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML.**<br>
   Menambahkan fungsi frontpage di views.py untuk merender template HTML dan products yang ada. 

6. **Membuat sebuah routing pada urls.py aplikasi main.**<br>
   Menambahkan rute yang diinginkan pada urls.py main untuk memetakan fungsi yang telah dibuat pada views.py.

7. **Melakukan deployment ke PWS.**<br>
   Membuat proyek baru di PWS kemudian menambahkan URL deployment pada ALLOWED_HOST dalam settings.py. Selanjutnya menjalankan perintah push ke PWS.

8. **Membuat sebuah README.md.**<br>
   Membuat file README.md yang berisi tautan menuju aplikasi PWS dan beberapa jawaban dari pertanyaan.

#### Alur Django
<img width="491" alt="Screenshot 2024-09-10 at 23 05 38" src="https://github.com/user-attachments/assets/6d51b7bd-6f33-412d-8e9a-af292e41a086">

Request client pertama kali diproses oleh **urls.py**, yang mencocokkan URL dengan fungsi view di **views.py**. Di dalam **views.py**, logika dijalankan dan jika data dari database diperlukan, fungsi view memanggil model di **models.py**. Setelah data diperoleh, view menyiapkan template HTML dengan data tersebut, lalu merendernya. Hasilnya berupa halaman web atau respon JSON yang dikirim kembali ke browser client. 

#### Fungsi Git

1. Riwayat Perubahan Lengkap. Git dapat melacak setiap perubahan yang dilakukan pada setiap file, termasuk mencatat siapa yang membuat perubahan dan kapan perubahan itu dilakukan.<br>
2. Branching dan Merging. Dengan git, sebuah proyek dapat dikerjakan dengan banyak orang. Meskipun bekerja sendiri-sendiri, pengguna dapat mengerjakan bagian yang berbeda secara terpisah dengan cara membuat “branch”. Nantinya, pengguna dapat menggabungkan kembali bagian-bagian yang terpisah ini dengan fitur “merge”. <br>
3. Open Source. Git adalah tools yang bersifat open source sehingga dapat digunakan untuk membuat perangkat lunak secara open source. <br>
4. Backup. Git dapat menjadi backup jika terjadi kesalahan atau masalah dalam mengembangkan versi terbaru, Git dapat mengembalikan ke dalam versi sebelumnya. <br>

#### Mengapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django menggunakan arsitektur Model-View-Template (MVT) yang membantu untuk memahami pemisahan logika aplikasi, data, dan tampilan dengan baik. Django juga menyediakan banyak fitur yang dapat digunakan langsung, seperti autentikasi pengguna, URL routing, ORM (Object-Relational Mapping), dan lainnya. Ini memudahkan pemula karena mereka tidak perlu membangun semuanya dari nol.

#### Mengapa model pada Django disebut ORM?

Model Django disebut ORM karena memungkinkan untuk berinteraksi dengan database menggunakan Python, tanpa menulis query SQL langsung. Django ORM secara otomatis mengonversi model Python menjadi tabel database, menjadikan proses pengelolaan data lebih mudah dan mengurangi kemungkinan kesalahan dalam penulisan query SQL manual.


---
### Tugas 3
#### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?<br>
Data delivery sangat diperlukan dalam pengimplementasian sebuah platform karena ia memastikan data yang diperlukan oleh aplikasi dapat dikirim dan diterima dengan tepat dan efisien antara server dan client. Tanpa sistem data delivery yang baik, data dapat rusak atau bahkan hilang. Proses data delivery mencakup pengiriman data secara real-time, pengelolaan bandwidth, serta jaminan keamanan data, sehingga pengguna mendapatkan akses yang stabil dan dapat mendapatkan informasi dan fitur yang mereka butuhkan.

#### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?<br>
Menurut saya, JSON lebih baik dibandingkan XML karena beberapa alasan. JSON menggunakan sintaks yang lebih sederhana untuk menyimpan dan bertukar data, sehingga lebih mudah digunakan. Untuk aplikasi AJAX, JSON lebih cepat dan lebih mudah dikelola daripada XML. Prosesnya juga lebih efisien, di mana JSON dapat diparsing menggunakan `JSON.parse()` dari sebuah string JSON, sedangkan XML memerlukan DOM untuk mengambil nilai dari dokumen XML. Karena kemudahan dan kecepatan JSON ini, ia sering dipilih sebagai alternatif yang lebih baik daripada XML dalam pengembangan aplikasi.

#### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?<br>
Method is_valid() pada form berfungsi untuk memeriksa apakah data yang dikirimkan melalui form sesuai dengan syarat-syarat yang sudah ditentukan. Method ini penting untuk memastikan bahwa data yang diterima aman dan sesuai sebelum diproses lebih lanjut.

#### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?<br>
Peran csrf_token adalah untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Tanpa token ini, form yang dikirimkan dapat dieksploitasi oleh penyerang untuk membuat permintaan berbahaya menggunakan kredensial pengguna yang sah. Token CSRF memastikan bahwa setiap permintaan POST berasal dari sumber yang valid dan bukan dari situs jahat. Tanpa csrf_token, aplikasi menjadi rentan terhadap serangan yang dapat mengubah data atau mengakses informasi pengguna secara tidak sah.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. **Membuat input form untuk menambahkan objek model pada app sebelumnya.**<br>
Membuat file forms.py untuk membuat class ProductEntryForm.Kemudian menambahkan method create_product_entry beserta validasinya di views.py. Lalu membuat file HTML baru yang berisi tampilan untuk form.

2. **Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**<br>
Mengimport HttpResponse dan serializers di views.py dan membuat method show_xml, show_json, show_xml_by_id, dan show_json_by_id. Untuk show by id perlu menggunakan objects.filter(pk=id) agar dapat mengembalikan object sesuai dengan id yang diinginkan.

3. **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**<br>
Menambahkan rute URL pada urls.py. Untuk method show by id perlu tambahan `/<str:id>/` pada path urlpatterns.

#### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.


---
### Tugas 4
#### Apa perbedaan antara HttpResponseRedirect() dan redirect()
HttpResponseRedirect() mengarahkan pengguna ke URL yang spesifik, sedangkan redirect() lebih fleksibel karena dapat menerima URL, nama view, atau objek model dan mengarahkannya secara otomatis.

#### Jelaskan cara kerja penghubungan model Product dengan User!
Model Product biasanya memiliki relasi ForeignKey ke model User. ForeignKey dapat merepresentasikan hubungan Many-to-One. Ini menunjukkan bahwa setiap produk dimiliki oleh satu pengguna, dan pengguna dapat memiliki banyak produk.

#### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses memverifikasi identitas pengguna. Saat login, sistem akan melakukan verifikasi pengguna yang diizinkan untuk masuk ke sistem. Authorization adalah menentukan hak akses pengguna setelah terotentikasi. Django menggunakan fungsi authenticate() untuk memverifikasi identitas pengguna, dan login() untuk mencatat pengguna sebagai terautentikasi.
Django menggunakan izin untuk mengatur otorisasi. Kita bisa menetapkan izin pada model dan memeriksanya di view dengan dekorator seperti @login_required.

#### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django menggunakan sesi dan cookies. Saat pengguna login, ID sesi disimpan di database dan di dalam cookie sessionid. Kegunaan lain dari cookies yaitu dapat menyimpan preferensi pengguna, seperti tema atau bahasa yang dipilih, sebagai penyimpanan data sementara, seperti item dalam keranjang belanja di situs e-commerce, dan juga dapat melacak aktivitas pengguna di situs untuk keperluan analisis. Tidak semua cookies aman digunakan, contohnya Session Hijacking yaitu cookie sesi dicuri sehingga penyerang dapat mengakses akun pengguna tanpa perlu login.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
**Mengimplementasikan fungsi registrasi, login, dan logout.**<br> 
1. Membuat login html dan sign up html dengan form dan methodnya post.
2. Membuat fungsi signup pada views.py yang memanggil UserCreationForm() dan menyimpan form lalu akan pindah ke page login.
3. Membuat fungsi user_login yang memanggil AuthenticationForm(data=request.POST) dan akan men-get user kemudian akan menyimpan cookie dan mengarahkan user ke frontpage.
4. Membuat fungsi logout_user yang akan mengarahkan ke page login dan menghapus cookie sebelumnya.
5. Mengimport semua fungsi views lalu membuat path dari setiap fungsi.

**Membuat dua akun pengguna dengan masing-masing tiga dummy data.**<br>
Melakukan registrasi 2 akun pada page signup/ kemudian login dan menambahkan 3 data pada page create-product-entry/.

**Menghubungkan model Product dengan User**<br>
Menambahkan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` dalam class Product di models.py

**Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**<br>
Membuat context_processor yg mereturn current_user dan last_login untuk passing current_user dan last_login ke base.html yang berada di luar folder main.

**Menjawab beberapa pertanyaan berikut pada README.md**<br>
Memodifikasi README.md yang sudah dibuat sebelumnya.