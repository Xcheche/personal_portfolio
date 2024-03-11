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