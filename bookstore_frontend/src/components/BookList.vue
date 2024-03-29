<template>
  <div class="book-list">
    <h2>Book List</h2>
    <ul>
      <li v-for="book in books" :key="book.id" class="book-item">
        <div class="book-details">
          <h3>{{ book.title }}</h3>
          <p class="author">by {{ book.author }}</p>
          <p class="year">Published in {{ book.year }}</p>
        </div>
        <div class="book-actions">
          <button @click="editBook(book)" class="edit-button">Edit</button>
          <button @click="deleteBook(book.id)" class="delete-button">Delete</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: []
    };
  },
  mounted() {
    this.fetchBooks();
  },
  methods: {
    fetchBooks() {
      axios.get('http://localhost:8000/api/v1/books/')
        .then(response => {
          this.books = response.data;
        })
        .catch(error => {
          console.error('Error fetching books:', error);
        });
    },
    editBook() {
      // Implement edit functionality
    },
    deleteBook() {
      // Implement delete functionality
    }
  }
}
</script>

<style scoped>
.book-list {
  font-family: 'Arial', sans-serif;
  padding: 20px;
}

.book-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}

.book-details {
  flex: 1;
}

.author {
  font-style: italic;
  color: #666;
}

.year {
  color: #888;
}

.book-actions {
  display: flex;
  align-items: center;
}

.edit-button, .delete-button {
  padding: 8px 12px;
  margin-left: 10px;
  border: none;
  background-color: #007bff;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.edit-button:hover, .delete-button:hover {
  background-color: #0056b3;
}
</style>
