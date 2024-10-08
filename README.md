## (CC) Click Coffee
Tugas PBP : [Click Your Coffee Here!](http://nashwa-ghania-coffeeshop.pbp.cs.ui.ac.id/)
<br>
<br>

<details>
<summary>Tugas 2</summary>

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
</details>

<details>
<summary>Tugas 3</summary>

#### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?<br>
Data delivery sangat diperlukan dalam pengimplementasian sebuah platform karena ia memastikan data yang diperlukan oleh aplikasi dapat dikirim dan diterima dengan tepat dan efisien antara server dan client. Tanpa sistem data delivery yang baik, data dapat rusak atau bahkan hilang. Proses data delivery mencakup pengiriman data secara real-time, pengelolaan bandwidth, serta jaminan keamanan data, sehingga pengguna mendapatkan akses yang stabil dan dapat mendapatkan informasi dan fitur yang mereka butuhkan.<br>

#### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?<br>
Menurut saya, JSON lebih baik dibandingkan XML karena beberapa alasan. JSON menggunakan sintaks yang lebih sederhana untuk menyimpan dan bertukar data, sehingga lebih mudah digunakan. Untuk aplikasi AJAX, JSON lebih cepat dan lebih mudah dikelola daripada XML. Prosesnya juga lebih efisien, di mana JSON dapat diparsing menggunakan `JSON.parse()` dari sebuah string JSON, sedangkan XML memerlukan DOM untuk mengambil nilai dari dokumen XML. Karena kemudahan dan kecepatan JSON ini, ia sering dipilih sebagai alternatif yang lebih baik daripada XML dalam pengembangan aplikasi.<br>

#### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?<br>
Method is_valid() pada form berfungsi untuk memeriksa apakah data yang dikirimkan melalui form sesuai dengan syarat-syarat yang sudah ditentukan. Method ini penting untuk memastikan bahwa data yang diterima aman dan sesuai sebelum diproses lebih lanjut.<br>

#### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?<br>
Peran csrf_token adalah untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Tanpa token ini, form yang dikirimkan dapat dieksploitasi oleh penyerang untuk membuat permintaan berbahaya menggunakan kredensial pengguna yang sah. Token CSRF memastikan bahwa setiap permintaan POST berasal dari sumber yang valid dan bukan dari situs jahat. Tanpa csrf_token, aplikasi menjadi rentan terhadap serangan yang dapat mengubah data atau mengakses informasi pengguna secara tidak sah.<br>

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. **Membuat input form untuk menambahkan objek model pada app sebelumnya.**<br>
Membuat file forms.py untuk membuat class ProductEntryForm.Kemudian menambahkan method create_product_entry beserta validasinya di views.py. Lalu membuat file HTML baru yang berisi tampilan untuk form.

2. **Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**<br>
Mengimport HttpResponse dan serializers di views.py dan membuat method show_xml, show_json, show_xml_by_id, dan show_json_by_id. Untuk show by id perlu menggunakan objects.filter(pk=id) agar dapat mengembalikan object sesuai dengan id yang diinginkan.

3. **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**<br>
Menambahkan rute URL pada urls.py. Untuk method show by id perlu tambahan `/<str:id>/` pada path urlpatterns.

#### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
<img width="490" alt="Screenshot 2024-09-15 at 00 22 28" src="https://github.com/user-attachments/assets/d8b8060e-2def-4f1b-af39-11d03f971ec9">
<img width="490" alt="Screenshot 2024-09-15 at 00 22 16" src="https://github.com/user-attachments/assets/27da225f-eb9a-431b-85d5-be525930ff8a">
<img width="490" alt="Screenshot 2024-09-15 at 00 21 53" src="https://github.com/user-attachments/assets/3c644b5b-d83a-4053-ad11-16f154eec32c">
<img width="490" alt="Screenshot 2024-09-15 at 00 21 53" src="https://github.com/user-attachments/assets/af83bcb0-16fe-4d91-af9b-538d697490b3">
</details>

<details>
<summary>Tugas 4</summary>

#### Apa perbedaan antara HttpResponseRedirect() dan redirect()?<br>
HttpResponseRedirect() mengarahkan pengguna ke URL yang spesifik, sedangkan redirect() lebih fleksibel karena dapat menerima URL, nama view, atau objek model dan mengarahkannya secara otomatis.<br>

#### Jelaskan cara kerja penghubungan model Product dengan User!<br>
Untuk menghubungkan model Product dengan User biasanya memakai relasi ForeignKey. ForeignKey dapat merepresentasikan hubungan Many-to-One yang menunjukkan bahwa setiap produk dimiliki oleh satu pengguna, dan pengguna dapat memiliki banyak produk.<br>

#### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.<br>
Authentication adalah proses memverifikasi identitas pengguna. Saat login, sistem akan melakukan verifikasi pengguna yang diizinkan untuk masuk ke sistem. Sedangkan authorization, akan menentukan hak akses pengguna setelah terotentikasi. Django menggunakan fungsi authenticate() untuk memverifikasi identitas pengguna, dan login() untuk mencatat pengguna sebagai terautentikasi. Django juga menggunakan izin untuk mengatur otorisasi. Kita bisa mengatur izin pada model dengan dekorator seperti @login_required.<br>

#### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?<br>
Django menggunakan session ID dan cookies. Saat pengguna login, session ID akan disimpan. Kegunaan lain dari cookies yaitu dapat menyimpan preferensi pengguna, dapat menyimpan data sementara, dan juga dapat melacak aktivitas pengguna di situs untuk keperluan analisis. Tidak semua cookies aman digunakan, ada kasus dimana cookies berisi informasi sensitif seperti password namun tidak dienkripsi sehingga cookies ini memiliki kemungkinan untuk bisa diakses melalui JavaScript oleh pihak ketiga.<br>

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
**Mengimplementasikan fungsi registrasi, login, dan logout.**<br> 
1. Membuat login html dan sign up html dengan form dan methodnya adalah post.
2. Membuat fungsi signup pada views.py yang memanggil UserCreationForm() dan menyimpan form lalu akan pindah ke page login.
3. Membuat fungsi user_login yang memanggil AuthenticationForm(data=request.POST) dan akan men-get user kemudian akan menyimpan cookie dan mengarahkan user ke frontpage.
4. Membuat fungsi logout_user yang akan mengarahkan ke page login dan menghapus cookie sebelumnya.
5. Mengimport semua fungsi views lalu membuat path dari setiap fungsi.

**Membuat dua akun pengguna dengan masing-masing tiga dummy data.**<br>
Melakukan registrasi 2 akun pada page signup/ kemudian login dan menambahkan 3 data pada page create-product-entry/ untuk kedua akun.<br>

**Menghubungkan model Product dengan User.**<br>
Menambahkan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` dalam class Product di models.py<br>

**Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**<br>
Membuat context_processor yg mereturn current_user dan last_login untuk passing current_user dan last_login ke base.html yang berada di luar folder main.<br>

**Menjawab beberapa pertanyaan berikut pada README.md**<br>
Memodifikasi README.md yang sudah dibuat sebelumnya.
</details>

<details>
<summary>Tugas 5</summary>

#### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!<br>
1. Inline styles = CSS ditulis langsung di dalam atribut style pada suatu elemen HTML. contohnya `<p style="color: white;">Tes</p>`.
2. ID selectors = menggunakan tanda # diikuti dengan nilai ID elemen.
3. Classes selector = menggunakan tanda . diikuti dengan nama class. 
4. Element selector = menggunakan nama elemen HTML seperti div, p, atau h1 sebagai selector.

Urutan prioritasnya adalah dari inline styles, ID selectors, classes selector, kemudian element selector.<br>

#### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!<br>
Responsive design penting karena memastikan situs web atau aplikasi bisa terlihat dan berfungsi dengan baik di berbagai perangkat, seperti smartphone, tablet, dan desktop. Ini menjadi konsep yang penting karena banyak orang yang sekarang mengakses internet melalui smartphone. Salah satu contoh aplikasi web yang sudan menerapkan responsive design adalah Google. Google bisa diakses dari perangkat manapun dan tetap nyaman untuk digunakan. Sebaliknya, salah satu contoh aplikasi web yang belum responsive adalah Siak NG.<br>

#### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!<br>
**Margin** adalah ruang kosong di luar elemen yang memisahkannya dari elemen lain dan berfungsi untuk mengontrol jarak antar elemen.
**Border** adalah garis yang mengelilingi elemen di luar padding namun tetap berada di dalam margin dan bisa diatur tebal dan warnanya. 
**Padding** adalah ruang di dalam elemen yang berada di antara konten elemen dan border dan digunakan untuk memberi jarak konten dari tepi elemen. 
Contoh impelementasinya adalah :
```
.element {
  margin: 20px;
  border: 2px solid black;
  padding: 15px;
}
```

#### Jelaskan konsep flex box dan grid layout beserta kegunaannya!<br>
**Flexbox** berfokus pada penyusunan elemen secara linier yaitu secara horizontal atau vertikal. Ini berguna untuk membuat tata letak yang responsif. Contohnya, flexbox sering digunakan untuk mengatur navigasi bar atau card yang fleksibel berdasarkan ukuran layar. 

**Grid Layout** memberikan kontrol untuk mengatur elemen dalam bentuk baris dan kolom. Ini berguna untuk membuat desain yang lebih kompleks, seperti halaman dengan banyak layout seperti feeds IG. Grid membantu kita mengatur elemen-elemen dengan rapi dan terstruktur.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!<br>
**Implementasikan fungsi untuk menghapus dan mengedit product.**<br>
Menambahkan fungsi edit_product dan delete_product berdasarkan id ke dalam views.py. Kemudian, menambahkan path dari kedua fungis tersebut ke dalam urls.py

**Kustomisasi desain pada template HTML.**<br>
1. Menggunakan tailwind untuk memberi style pada login, sigup, addproduct, dan editproduct.

2. Membuat card_product.html yang berisi tampilan card info dari product product yang ada dan juga mempunyai button untuk mengedit dan menghapus product. Lalu memanggil card_product itu di main.html menggunakan include.

3. Membuat folder static/image untuk menyimpan gambar. Kemudian menambahkan image tersebut ke main.html untuk menampilkan gambar jika belum ada data product yang tersimpan.

4. Menambahkan konfigurasi file static dengan cara menambahkan `whitenoise.middleware.WhiteNoiseMiddleware` ke middleware, lalu menambahkan STATICFILES_DIRS dan juga STATIC_ROOT.

5. Membuat responsive navbar pada base.html di folder templates menggunakan tailwind dan mengimplementasikan dropdown untuk pengguna yang sedang login dengan penanganan interaksi menggunakan JavaScript, termasuk menampilkan dan menyembunyikan menu dropdown dan menu mobile. 

**Menjawab beberapa pertanyaan berikut pada README.md**<br>
Memodifikasi README.md yang sudah dibuat sebelumnya.
</details>

<details>
<summary>Tugas 6</summary>

#### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!<br>
JavaScript memiliki peran penting dalam pengembangan aplikasi web modern karena memberikan manfaat seperti interaktivitas, manipulasi DOM, dan pengolahan data. Dengan JavaScript, kita dapat membuat elemen halaman web yang responsif terhadap interaksi pengguna, seperti klik, hover, dan input. JavaScript juga bisa menggunakan fitur fetch sehingga dapat mengambil data dari server tanpa perlu memuat ulang halaman serta bisa melakukan validasi formulir dan mengolah data input pengguna.

#### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?<br>
Keyword await digunakan untuk menunggu response yang dikembalikan oleh fetch() sebelum melanjutkan eksekusi kode selanjutnya sehingga memungkinkan pemanggilan data secara asinkron.

Jika tidak menggunakan await, kode akan terus berjalan tanpa menunggu response dari fetch(). Ini berarti bahwa bagian kode yang bergantung pada hasil dari fetch() mungkin akan dieksekusi sebelum response tersedia sehingga dapat menyebabkan error atau hasil yang tidak diinginkan.

####  Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?<br>
Ketika melakukan permintaan AJAX POST, token CSRF biasanya disertakan dalam header sebagai bagian dari data form. Jika token CSRF tidak disertakan dalam permintaan AJAX, Django secara otomatis akan menolak permintaan tersebut sebagai bagian dari mekanisme keamanannya. 

Alasan kenapa kita memerlukan decorator csrf_exempt adalah karena pada fungsi create-ajax, telah dilakukan autentikasi dan kita yakin bahwa permintaan tersebut valid. Oleh karena itu, kita dapat memutuskan untuk tidak memerlukan token CSRF untuk operasi tersebut. Dekorator `@csrf_exempt` digunakan untuk menonaktifkan pengecekan token CSRF pada view tersebut.

#### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?<br>
Pembersihan data input pengguna juga penting dilakukan di backend karena kita perlu memastikan bahwa semua data yang diterima dari pengguna telah diperiksa dan dibersihkan sebelum disimpan atau diproses lebih lanjut. Ini membantu mencegah serangan seperti Cross-Site Scripting (XSS), yang bisa merusak data atau membahayakan pengguna. Dengan kata lain, pembersihan di backend menambah lapisan perlindungan ekstra untuk aplikasi kita.

Selain itu, pembersihan data di backend memastikan konsistensi dalam penanganan data. Ini mengurangi kemungkinan kesalahan yang mungkin terjadi jika hanya mengandalkan pembersihan di frontend dan memastikan bahwa hanya data yang valid dan aman yang akan diproses oleh sistem.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!<br>
1. **Ubahlah kode cards data product agar dapat mendukung AJAX GET.**<br>
Mengubah kode tampilan product card untuk memungkinkan data diambil secara asinkronus menggunakan AJAX. Dengan ini, data yang ditampilkan pada kartu akan berasal dari permintaan GET AJAX, bukan dari rendering server langsung.

2. **Lakukan pengambilan data product menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.**<br>
Membuat fungsi JavaScript untuk mengirim permintaan AJAX GET dan memfilter data sehingga hanya mengambil product yang dimiliki pengguna yang sedang login.
```
async function getProduct() {
   return fetch("{% url 'main:show_json' %}").then((res) => res.json())
}
```

3. **Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan product.**<br>
Membuat sebuah tombol yang akan membuka modal dialog dengan kode `onclick="showModal();"`. Di dalam modal tersebut, tersedia form untuk memasukkan product baru yang ingin ditambahkan pengguna.

4. **Buatlah fungsi view baru untuk menambahkan product baru ke dalam basis data.**<br>
Membuat fungsi create-ajax yang sudah ada strip tag dengan method POST dan mereturn HttpResponse(status=201) jika berhasil.

5. **Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.**<br>
Menambahkan path /create-ajax/ di urls.py yang akan mengarahkan ke view untuk menambahkan product by ajax.

6. **Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.**<br>
Menambahkan kode ke fungsi addProduct():
```
fetch("{% url 'main:create_ajax' %}", {
   method: "POST",
   body: new FormData(document.querySelector('#productForm')),
})
```

7. **Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar product terbaru tanpa reload halaman utama secara keseluruhan.**<br>
Membuat fungsi refreshProducts() untuk merefresh halaman, lalu fungsi ini dimasukkan ke fungsi addProduct() sehingga setiap kali tombol submit, produk baru ditambahkan dans halaman akan di-refresh secara asinkronus.
</details>