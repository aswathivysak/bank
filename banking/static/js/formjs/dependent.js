
const btn = document.getElementById('btn');

btn.addEventListener('click', () => {
  const formdisp = document.getElementById('formdisp');

  if (formdisp.style.display === 'none') {
    // 👇️ this SHOWS the form
    formdisp.style.display = 'block';
  }
  else {
     👇️// this HIDES the form
    formdisp.style.display = 'none';
  }
});
