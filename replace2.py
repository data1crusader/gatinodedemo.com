import os

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Reveal class
content = content.replace(
    ".reveal { opacity: 0; transform: translateY(40px); transition: all 0.8s var(--ease-out); }",
    ".reveal { opacity: 0; transform: translateY(40px); filter: blur(6px); transition: all 0.8s var(--ease-out); will-change: transform, opacity, filter; }"
)
content = content.replace(
    ".reveal.active { opacity: 1; transform: translateY(0); }",
    ".reveal.active { opacity: 1; transform: translateY(0); filter: blur(0); }"
)

# Shimmer
shimmer_css = """
@keyframes shimmer {
  0% { background-position: -200% center; }
  100% { background-position: 200% center; }
}
"""
if "@keyframes shimmer" not in content:
    content += shimmer_css

content = content.replace(
    ".hero-badge {\n  display: inline-flex;\n  align-items: center;\n  gap: 0.5rem;\n  background: rgba(13, 13, 13, 0.65);\n  border: 1px solid rgba(120, 180, 255, 0.45);\n  padding: 0.5rem 1.25rem;\n  border-radius: var(--radius-full);\n  font-family: var(--font-heading);\n  font-size: 0.8rem;\n  font-weight: 600;\n  letter-spacing: 2px;\n  text-transform: uppercase;\n  color: #d6e8ff;\n  margin-bottom: var(--space-lg);\n  animation: fadeInUp 0.8s var(--ease-out) both;\n}",
    ".hero-badge {\n  display: inline-flex;\n  align-items: center;\n  gap: 0.5rem;\n  background: rgba(13, 13, 13, 0.65);\n  border: 1px solid rgba(120, 180, 255, 0.45);\n  padding: 0.5rem 1.25rem;\n  border-radius: var(--radius-full);\n  font-family: var(--font-heading);\n  font-size: 0.8rem;\n  font-weight: 600;\n  letter-spacing: 2px;\n  text-transform: uppercase;\n  color: #d6e8ff;\n  margin-bottom: var(--space-lg);\n  background-image: linear-gradient(90deg, rgba(30,95,187,0) 0%, rgba(120,180,255,0.2) 50%, rgba(30,95,187,0) 100%);\n  background-size: 200% auto;\n  animation: fadeInUp 0.8s var(--ease-out) both, shimmer 3s infinite linear;\n}"
)

# Service cards
content = content.replace(
    ".service-card {\n  background: var(--clr-white);\n  border-radius: var(--radius-lg);\n  padding: 2rem;\n  transition: all var(--transition-base);\n  position: relative;\n  overflow: hidden;\n  border: 1px solid rgba(0, 0, 0, 0.04);\n}",
    ".service-card {\n  background: var(--clr-white);\n  border-radius: var(--radius-lg);\n  padding: 2rem;\n  transition: all var(--transition-base);\n  position: relative;\n  overflow: hidden;\n  border: 1px solid rgba(0, 0, 0, 0.04);\n  backdrop-filter: blur(4px);\n  box-shadow: 0 0 0 1px rgba(30, 95, 187, 0.1);\n}"
)
content = content.replace(
    ".service-card:hover { transform: translateY(-8px); box-shadow: var(--shadow-lg); }",
    ".service-card:hover { transform: translateY(-8px); box-shadow: 0 8px 32px rgba(30, 95, 187, 0.18), 0 0 0 1px rgba(30, 95, 187, 0.2); }"
)

# Mobile Hero Fix
content = content.replace(
    ".hero-content { padding-top: calc(var(--header-height) + 1.75rem); }",
    ".hero-content { padding-top: calc(var(--header-height) + 4.5rem); }"
)
content = content.replace(
    ".hero-badge {\n    margin-top: 0.25rem;",
    ".hero-badge {\n    margin-top: 1rem;"
)
content = content.replace(
    ".hero-title {\n    font-size: clamp(2.1rem, 9vw, 3.2rem);\n    max-width: 100%;\n  }",
    ".hero-title {\n    font-size: clamp(2.1rem, 9vw, 3.2rem);\n    max-width: 100%;\n    margin-bottom: var(--space-md);\n  }"
)

# Glassmorphism & Polish
content = content.replace(
    "background: rgba(255, 255, 255, 0.95);",
    "background: rgba(6, 11, 24, 0.88);"
)
content = content.replace(
    ".header.scrolled .nav-link { color: var(--clr-dark); }",
    ".header.scrolled .nav-link { color: rgba(255,255,255,0.85); }"
)
content = content.replace(
    ".header.scrolled .nav-link:hover,\n.header.scrolled .nav-link.active { color: var(--clr-primary); }",
    ".header.scrolled .nav-link:hover,\n.header.scrolled .nav-link.active { color: var(--clr-primary-light); }"
)
content = content.replace(
    ".header.scrolled .header-logo-text { color: var(--clr-dark); }",
    ".header.scrolled .header-logo-text { color: var(--clr-white); }"
)
content = content.replace(
    ".header.scrolled .menu-toggle span { background: var(--clr-dark); }",
    ".header.scrolled .menu-toggle span { background: var(--clr-white); }"
)
content = content.replace(
    ".header.scrolled .nav-cta {\n  border-left-color: rgba(0, 0, 0, 0.08);\n}",
    ".header.scrolled .nav-cta {\n  border-left-color: rgba(255, 255, 255, 0.1);\n}"
)

content = content.replace(
    ".why-card {\n  background: rgba(255, 255, 255, 0.03);\n  border: 1px solid rgba(255, 255, 255, 0.06);\n  border-radius: var(--radius-lg);\n  padding: 2rem;\n  transition: all var(--transition-base);\n}",
    ".why-card {\n  background: rgba(255, 255, 255, 0.03);\n  border: 1px solid rgba(255, 255, 255, 0.06);\n  border-radius: var(--radius-lg);\n  padding: 2rem;\n  transition: all var(--transition-base);\n  backdrop-filter: blur(8px);\n}"
)

content = content.replace(
    ".stats {\n  position: relative;\n  background: var(--clr-dark);\n  padding: var(--space-xl) 0;\n  z-index: 5;\n}",
    ".stats {\n  position: relative;\n  background: linear-gradient(135deg, var(--clr-dark) 0%, var(--clr-dark-3) 100%);\n  padding: var(--space-xl) 0;\n  z-index: 5;\n}"
)

content = content.replace(
    ".back-to-top:hover { transform: translateY(-4px); box-shadow: 0 0 40px rgba(30, 95, 187, 0.5); }",
    ".back-to-top:hover { transform: translateY(-4px); box-shadow: 0 0 40px rgba(30, 95, 187, 0.5); }"
)

content = content.replace(
    ".section-padding { padding: var(--space-3xl) 0; }",
    ".section-padding { padding: var(--space-3xl) 0; position: relative; }\n.section-padding::after { content: ''; position: absolute; bottom: 0; left: 10%; right: 10%; height: 1px; background: linear-gradient(90deg, transparent, rgba(30, 95, 187, 0.2), transparent); }"
)

content = content.replace(
    "@supports (backdrop-filter: blur(20px)) {\n  .header.scrolled {\n    background: rgba(255, 255, 255, 0.92);\n  }\n}",
    "@supports (backdrop-filter: blur(20px)) {\n  .header.scrolled {\n    background: rgba(6, 11, 24, 0.88);\n  }\n}"
)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)
