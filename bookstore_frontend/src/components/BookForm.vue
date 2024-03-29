<template>
  <div class="book-form">
    <h2>{{ formTitle }}</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="formData.title" required>
      </div>
      <div class="form-group">
        <label for="author">Author:</label>
        <input type="text" id="author" v-model="formData.author" required>
      </div>
      <div class="form-group">
        <label for="year">Year:</label>
        <input type="number" id="year" v-model="formData.year" required>
      </div>
      <button type="submit" class="submit-button">{{ submitButtonText }}</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    book: Object
  },
  data() {
    return {
      formData: {
        title: '',
        author: '',
        year: ''
      }
    };
  },
  computed: {
    formTitle() {
      return this.book ? 'Edit Book' : 'Add New Book';
    },
    submitButtonText() {
      return this.book ? 'Update' : 'Add';
    }
  },
  created() {
    if (this.book) {
      this.formData = { ...this.book };
    }
  },
  methods: {
    submitForm() {
      if (this.book) {
        this.updateBook();
      } else {
        this.addBook();
      }
    },
    addBook() {
      axios.post('http://localhost:8000/api/v1/books/', this.formData)
        .then(response => {
          // Handle successful addition
          console.log('Book added:', response.data);
        })
        .catch(error => {
          console.error('Error adding book:', error);
        });
    },
    updateBook() {
      axios.put(`http://localhost:8000/api/v1/books/${this.book.id}`, this.formData)
        .then(response => {
          // Handle successful update
          console.log('Book updated:', response.data);
        })
        .catch(error => {
          console.error('Error updating book:', error);
        });
    }
  }
}
</script>

<style scoped>
.book-form {
  font-family: 'Arial', sans-serif;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  max-width: 400px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
input[type="number"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.submit-button {
  display: block;
  width: 100%;
  padding: 10px;
  border: none;
  background-color: #007bff;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>
