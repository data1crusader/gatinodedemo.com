import os

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Add highlight-gold and hero-truck
custom_css = """
/* Hero Custom Updates */
.highlight-gold {
  color: #F1C40F; /* Golden yellow */
  font-style: italic;
  font-family: var(--font-heading);
  display: inline-block;
}

.hero-truck {
  position: absolute;
  bottom: 0;
  right: -5%;
  height: 95%;
  object-fit: contain;
  z-index: 2;
  pointer-events: none; /* so it doesn't block clicks */
}

@media (max-width: 1024px) {
  .hero-truck { right: -15%; height: 80%; }
}

@media (max-width: 768px) {
  .hero-truck { right: -25%; height: 60%; opacity: 0.8; }
}

.btn-secondary.btn-outline-hero {
  background: rgba(255, 255, 255, 0.1);
  color: var(--clr-white);
  border: 1px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
}
.btn-secondary.btn-outline-hero:hover {
  background: rgba(255, 255, 255, 0.2);
}

.btn-primary {
  background: linear-gradient(135deg, #3169d5 0%, #1e5fbb 100%);
  border: none;
}
.btn-primary:hover {
  background: linear-gradient(135deg, #427ce8 0%, #266dd1 100%);
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(custom_css)

print("CSS appended successfully.")
