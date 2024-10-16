document.addEventListener('DOMContentLoaded', () => {

    // Deklarasi variabel books untuk menyimpan daftar buku
    let books;

    // Memeriksa apakah sudah ada data buku yang disimpan di localStorage, jika tidak maka simpan array kosong
    if (!localStorage.getItem('books'))
        localStorage.setItem('books', JSON.stringify([]));

    // Mengambil data buku dari localStorage dan menguraikannya menjadi objek JavaScript
    books = JSON.parse(localStorage.getItem('books'));

    // Fungsi untuk memeriksa apakah buku dengan judul tertentu sudah ada dalam daftar buku
    const isDuplicateBook = title => {
        return books.some(book => book.title === title);
    }

    // Fungsi untuk membuat elemen artikel untuk satu buku
    const createArticleBook = book => {
        // Membuat elemen artikel
        const articleEl = document.createElement('article');
        articleEl.className = 'book_item';

        // Membuat elemen judul buku
        const titleEl = document.createElement('h3');
        titleEl.innerHTML = `Title : ${book.title}`;

        // Membuat elemen pengarang buku
        const authorParagraphEL = document.createElement('p');
        authorParagraphEL.innerHTML = `Auhor : ${book.author}`;

        // Membuat elemen tahun terbit buku
        const yearParagraphEl = document.createElement('p');
        yearParagraphEl.innerHTML = `Year : ${book.year}`;

        // Membuat elemen untuk menyimpan tombol aksi (hapus, edit, tandai selesai)
        const actionContainerEl = document.createElement('div');
        actionContainerEl.className = 'action';

        // Membuat tombol untuk menghapus buku
        const deleteBtnEl = document.createElement('button');
        deleteBtnEl.innerHTML = "Hapus buku";
        deleteBtnEl.className = "red";
        deleteBtnEl.addEventListener('click', () => {deleteBook(book.id)});

        // Membuat tombol untuk mengedit buku
        const updateBtnEl = document.createElement('button');
        updateBtnEl.innerHTML = "Edit buku";
        updateBtnEl.className = "blue";
        updateBtnEl.addEventListener('click', () => {updateInfoBook(book.id)});

        // Membuat tombol untuk menandai buku sebagai selesai atau belum selesai dibaca
        const completeBtnEl = document.createElement('button');
        completeBtnEl.addEventListener('click', () => {setToCompleteBook(book.id)});
        if (book.isComplete) {
            completeBtnEl.innerHTML = "Belum selesai dibaca";
            completeBtnEl.className = "yellow";
        } else {
            completeBtnEl.innerHTML = "Selesai dibaca";
            completeBtnEl.className = "green";
        }

        // Menambahkan tombol-tombol ke dalam container aksi
        actionContainerEl.append(deleteBtnEl);
        actionContainerEl.append(updateBtnEl);
        actionContainerEl.append(completeBtnEl);

        // Menambahkan elemen judul, pengarang, tahun terbit, dan container aksi ke dalam elemen artikel
        articleEl.append(titleEl);
        articleEl.append(authorParagraphEL);
        articleEl.append(yearParagraphEl);
        articleEl.append(actionContainerEl);

        // Mengembalikan elemen artikel yang telah dibuat
        return articleEl;
    }

    // Fungsi untuk memperbarui rak buku dengan daftar buku yang diberikan
    const updateBookshelf = listOfBook => {
        // Mendapatkan elemen rak buku yang belum selesai dibaca dan sudah selesai dibaca
        const incompleteBookshelfList = document.getElementById('incompleteBookshelfList');
        const completeBookshelfList = document.getElementById('completeBookshelfList');

        // Mengosongkan isi dari kedua rak buku
        incompleteBookshelfList.innerHTML = '';
        completeBookshelfList.innerHTML = '';

        // Memperbarui rak buku dengan buku-buku dari daftar yang diberikan
        listOfBook.forEach(book => {
            book.isComplete ?
                completeBookshelfList.append(createArticleBook(book))
            :
                incompleteBookshelfList.append(createArticleBook(book));
        });
    }

    // Fungsi untuk menghapus buku dari daftar berdasarkan ID buku yang diberikan
    const deleteBook = id => {
        const index = books.findIndex(book => book.id === id);
        if (index !== -1) {
            // Meminta konfirmasi dari pengguna sebelum menghapus buku
            let userConfirmation = confirm(`Are you sure to delete book : ${books[index].title} (id : ${id})`);
            if (userConfirmation){
                // Menghapus buku dari daftar
                books.splice(index, 1);
                // Menyimpan kembali daftar buku yang telah diperbarui ke dalam localStorage
                localStorage.setItem('books', JSON.stringify(books));
                // Memperbarui rak buku
                updateBookshelf(books);
            }
        }
    }

    // Fungsi untuk menandai buku sebagai selesai atau belum selesai dibaca berdasarkan ID buku yang diberikan
    const setToCompleteBook = id => {
        const index = books.findIndex(book => book.id === id);
        if (index !== -1) {
            // Mengubah status buku (selesai atau belum selesai dibaca)
            books[index].isComplete = !books[index].isComplete;
            // Menyimpan kembali daftar buku yang telah diperbarui ke dalam localStorage
            localStorage.setItem('books', JSON.stringify(books));
            // Memperbarui rak buku
            updateBookshelf(books);
        }
    }

    // Fungsi untuk memperbarui informasi buku berdasarkan ID buku yang diberikan
    const updateInfoBook = id => {
        const index = books.findIndex(book => book.id === id);
        if (index !== -1) {
            // Meminta input pengguna untuk informasi buku yang baru
            const newTitle = prompt(`Masukkan judul baru buku (Judul lama ${books[index].title}) `);
            const newAuthor = prompt(`Masukkan nama pengarang baru (Pengarang lama ${books[index].author})`);
            const newYear = parseInt(prompt(`Masukkan tahun terbit baru (Tahun terbit lama ${books[index].author})`));

            // Memeriksa apakah input yang diberikan valid
            const emptyNewTitle = newTitle.length === 0;
            const emptyNewAuthor = newAuthor.length === 0;
            const invalidNewYear = typeof newYear !== 'number';

            // Jika ada input yang tidak valid, tampilkan pesan kesalahan
            if (emptyNewTitle || emptyNewAuthor || invalidNewYear){
                alert('Pastikan semua informasi buku terisi benar!');
                return;
            }
            
            // Memperbarui informasi buku dengan informasi yang baru
            books[index].title = newTitle;
            books[index].author = newAuthor;
            books[index].year = newYear;
            // Menyimpan kembali daftar buku yang telah diperbarui ke dalam localStorage
            localStorage.setItem('books', JSON.stringify(books));
            // Memperbarui rak buku
            updateBookshelf(books);
            // Menampilkan pesan bahwa informasi buku telah diperbarui
            alert('Update informasi buku selesai.')
        }
    }

    // Fungsi untuk menangani pencarian buku
    const handleSearch = e => {
        e.preventDefault();

        // Mendapatkan query pencarian dari input pengguna
        const query = document.getElementById('searchBookTitle').value.toLowerCase().trim();

        // Mencari buku berdasarkan query pencarian
        const searchResults = books.filter(book =>  (
                book.title.toLowerCase().includes(query) || book.author.toLowerCase().includes(query) || book.year.toString().includes(query)
          ));

        // Jika hasil pencarian tidak kosong, perbarui rak buku dengan hasil pencarian
        if (searchResults.length !== 0)
            updateBookshelf(searchResults);
    }

    // Menambahkan event listener untuk form penambahan buku
    document.getElementById('inputBook').addEventListener('submit', e => {
        e.preventDefault();
        
        // Mendapatkan informasi buku yang akan ditambahkan dari input pengguna
        const bookTitle = document.getElementById('inputBookTitle').value;
        const bookAuthor = document.getElementById('inputBookAuthor').value;
        const bookYear = document.getElementById('inputBookYear').value;
        const bookIsComplete = document.getElementById('inputBookIsComplete').checked;

        // Memeriksa apakah buku dengan judul yang sama sudah ada dalam daftar
        if (isDuplicateBook(bookTitle))
            alert(`Buku dengan judul ${bookTitle} sudah ada dalam daftar.`);
        else {
            // Membuat objek buku baru
            const book = {
                id : new Date().getTime(),
                title: bookTitle.toLowerCase(),
                author: bookAuthor.toLowerCase(),
                year: bookYear,
                isComplete: bookIsComplete
            };

            // Menambahkan buku baru ke dalam daftar buku
            books.push(book);
            // Menyimpan daftar buku yang telah diperbarui ke dalam localStorage
            localStorage.setItem('books', JSON.stringify(books));

            // Memperbarui rak buku
            updateBookshelf(books);
        }

        // Mengosongkan input form setelah buku ditambahkan
        document.getElementById('inputBookTitle').value = '';
        document.getElementById('inputBookAuthor').value = '';
        document.getElementById('inputBookYear').value = '';
        document.getElementById('inputBookIsComplete').checked = false;
    });

    // Menambahkan event listener untuk form pencarian buku
    const searchBook = document.getElementById('searchBook');
    searchBook.addEventListener('submit', handleSearch);
    searchBook.addEventListener('keyup', e => {
        handleSearch(e);
    });

    // Memperbarui rak buku dengan daftar buku yang ada pada saat halaman dimuat
    updateBookshelf(books);
});
