import os
import shutil
import re

# 1. Copy Image
generated_img = r"C:\Users\Emon\.gemini\antigravity\brain\ef0dfb9a-cb3a-423a-b856-24c05af7add1\custom_indian_truck_1779979921596.png"
dest_img = r"assets\hero-bg-custom.png"
if os.path.exists(generated_img):
    shutil.copy(generated_img, dest_img)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace hero-bg and remove truck-cutout
html = html.replace('assets/hero-bg.webp', 'assets/hero-bg-custom.png')
html = re.sub(r'<img src="assets/truck-cutout\.png"[^>]+>', '', html)

# Change hrefs for quote buttons to open modal
html = html.replace('href="#quote"', 'href="#quote" data-modal-target="#quoteModal"')

# Append Modal and Toast HTML before </body>
modal_html = """
  <!-- QUOTE MODAL -->
  <div class="modal-overlay" id="quoteModal">
    <div class="modal-content">
      <button class="modal-close" id="modalClose">&times;</button>
      <h2>Get a Custom Quote</h2>
      <p>Fill out the details below and our team will get back to you within 2 hours.</p>
      <form id="quoteFormModal" class="contact-form">
        <div class="form-group">
          <input type="text" placeholder="Your Name" required />
        </div>
        <div class="form-group">
          <input type="text" placeholder="Pickup Location" required />
        </div>
        <div class="form-group">
          <input type="text" placeholder="Drop Location" required />
        </div>
        <button type="submit" class="btn btn-primary" style="width:100%">Request Quote</button>
      </form>
    </div>
  </div>

  <!-- TOAST CONTAINER -->
  <div id="toastContainer" class="toast-container"></div>
"""

if 'id="quoteModal"' not in html:
    html = html.replace('</body>', modal_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Update styles.css
css_addition = """
/* Modal Styles */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(10, 15, 30, 0.8);
  backdrop-filter: blur(8px);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}
.modal-overlay.active {
  opacity: 1;
  pointer-events: all;
}
.modal-content {
  background: var(--clr-dark);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 2.5rem;
  border-radius: var(--radius-lg);
  width: 90%;
  max-width: 500px;
  transform: translateY(30px);
  transition: transform 0.3s ease;
  position: relative;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
}
.modal-overlay.active .modal-content {
  transform: translateY(0);
}
.modal-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  color: var(--clr-white);
  font-size: 2rem;
  cursor: pointer;
  line-height: 1;
  opacity: 0.7;
  transition: opacity 0.2s;
}
.modal-close:hover { opacity: 1; color: var(--clr-primary-light); }

.modal-content h2 { font-family: var(--font-heading); font-size: 1.8rem; margin-bottom: 0.5rem; color: var(--clr-white); }
.modal-content p { color: rgba(255,255,255,0.7); margin-bottom: 1.5rem; font-size: 0.95rem; }

/* Toast Notification Styles */
.toast-container {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.toast {
  background: #27ae60;
  color: white;
  padding: 1rem 1.5rem;
  border-radius: var(--radius-md);
  box-shadow: 0 10px 20px rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  transform: translateX(120%);
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.toast.show {
  transform: translateX(0);
}
.toast-icon {
  width: 20px; height: 20px;
  border: 2px solid white; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: bold;
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.modal-overlay' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(css_addition)

# 4. Update script.js
js_addition = """
// Modal and Toast Logic
document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('quoteModal');
  const modalClose = document.getElementById('modalClose');
  const modalTriggers = document.querySelectorAll('[data-modal-target="#quoteModal"]');
  
  if (modal) {
    modalTriggers.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        modal.classList.add('active');
      });
    });

    modalClose.addEventListener('click', () => {
      modal.classList.remove('active');
    });

    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.classList.remove('active');
    });
  }

  // Toast Function
  window.showToast = function(message) {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<div class="toast-icon">✓</div> <span>${message}</span>`;
    container.appendChild(toast);
    
    // Animate in
    setTimeout(() => toast.classList.add('show'), 10);
    
    // Remove after 3.5s
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  };

  // Intercept all forms to show success popup
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // If inside modal, close it
      if (modal && modal.classList.contains('active')) {
        modal.classList.remove('active');
      }
      
      showToast('Form submitted successfully! We will contact you soon.');
      form.reset();
    });
  });
});
"""

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

if 'showToast' not in js:
    with open('script.js', 'a', encoding='utf-8') as f:
        f.write(js_addition)

print("Updates applied successfully.")
