const scrollToTopBtn = document.getElementById('scroll-to-top');

window.onscroll = function() {
  const scrollTop = (document.body.scrollTop || document.documentElement.scrollTop);

  if (scrollTop > 100) {
    scrollToTopBtn.style.display = 'block';
  } else {
    scrollToTopBtn.style.display = 'none';
  }
};

scrollToTopBtn.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});

// form submision



function submitForm(event) {
  event.preventDefault();

  // Assuming the form submission is successful
  // You can add your own form submission logic here if needed

  // Show the success message
  var successMessage = document.getElementById("success-message");
  successMessage.innerText = "Sent successfully!";
  successMessage.style.display = "block";

  // Set a timeout to hide the success message after 5 seconds
  setTimeout(function () {
    successMessage.style.display = "none";
  }, 5000);

  // Reset the form fields (optional)
  event.target.reset();

  return false;
}