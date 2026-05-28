import os

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("--clr-primary: #E8611A;", "--clr-primary: #1E5FBB;")
content = content.replace("--clr-primary-light: #FF8C42;", "--clr-primary-light: #4A90E2;")
content = content.replace("--clr-primary-dark: #C74E10;", "--clr-primary-dark: #14408A;")
content = content.replace("--clr-primary-glow: rgba(232, 97, 26, 0.25);", "--clr-primary-glow: rgba(30, 95, 187, 0.25);")
content = content.replace("--clr-dark: #0D0D0D;", "--clr-dark: #060B18;")
content = content.replace("--clr-dark-2: #141414;", "--clr-dark-2: #0A1224;")
content = content.replace("--clr-dark-3: #1A1A1A;", "--clr-dark-3: #0F1A30;")
content = content.replace("--clr-dark-4: #222222;", "--clr-dark-4: #15233D;")
content = content.replace("--clr-dark-5: #2A2A2A;", "--clr-dark-5: #1A2D4D;")
content = content.replace("--shadow-glow: 0 0 30px rgba(232, 97, 26, 0.3);", "--shadow-glow: 0 0 30px rgba(30, 95, 187, 0.3);")
content = content.replace("232, 97, 26", "30, 95, 187")
content = content.replace("255, 180, 120, 0.45", "120, 180, 255, 0.45")
content = content.replace("#ffe8d6", "#d6e8ff")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)
