// script.js - only JavaScript code as requested
const fileInput = document.getElementById('fileInput');
const inputImg = document.getElementById('inputImg');
const outputImg = document.getElementById('outputImg');
const runBtn = document.getElementById('runBtn');

fileInput.addEventListener('change', (ev) => {
  const file = ev.target.files && ev.target.files[0];
  if (!file) return;
  const url = URL.createObjectURL(file);
  inputImg.src = url;
  outputImg.src = '';
});

// This demo doesn't run a model — it simulates processing by copying the input image to output after a brief delay.
runBtn.addEventListener('click', async () => {
  if (!inputImg.src) return alert('Please choose an input image.');
  runBtn.disabled = true;
  runBtn.textContent = 'Processing...';

  // simulate network / model latency
  await new Promise(r => setTimeout(r, 1200));

  // For demo we just reuse the input image as "dehazed" output
  outputImg.src = inputImg.src;

  runBtn.disabled = false;
  runBtn.textContent = 'Run Dehaze';
});