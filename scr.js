AOS.init();

const form = document.getElementById('contact-form');
const nameInput = form.name;
const emailInput = form.email;
const messageInput = form.message;
const successMsg = document.getElementById('success-message');

const nameError = document.getElementById('name-error');
const emailError = document.getElementById('email-error');
const messageError = document.getElementById('message-error');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  nameError.textContent = '';
  emailError.textContent = '';
  messageError.textContent = '';
  successMsg.textContent = '';

  let valid = true;

  if (nameInput.value.trim() === '') {
    nameError.textContent = 'Please enter your name';
    valid = false;
  }

  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value.trim())) {
    emailError.textContent = 'Please enter a valid email address';
    valid = false;
  }

  if (messageInput.value.trim() === '') {
    messageError.textContent = 'Please enter a message';
    valid = false;
  }

  if (valid) {
    successMsg.textContent = 'Terima kasih, pesan anda telah terkirim';
    form.reset();
  }
});

// Theme toggle
document.getElementById('theme-toggle').addEventListener('click', () => {
  document.body.classList.toggle('light-mode');
});

// Hamburger menu toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('show');
});