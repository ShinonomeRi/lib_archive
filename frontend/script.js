async function loadBooks() {
  const response = await fetch("/api/books");
  const books = await response.json();

  const list = document.getElementById("books");
  list.innerHTML = "";

  books.forEach(book => {
    const li = document.createElement("li");
    li.textContent = `${book.id}. ${book.title} — ${book.author}`;
    list.appendChild(li);
  });
}
