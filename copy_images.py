import shutil

blue_truck = r"C:\Users\Emon\.gemini\antigravity\brain\ef0dfb9a-cb3a-423a-b856-24c05af7add1\media__1779906145113.png"
fleet_trucks = r"C:\Users\Emon\.gemini\antigravity\brain\ef0dfb9a-cb3a-423a-b856-24c05af7add1\media__1779906186363.jpg"
gn_logo = r"C:\Users\Emon\.gemini\antigravity\brain\ef0dfb9a-cb3a-423a-b856-24c05af7add1\media__1779905510424.jpg"

shutil.copy(blue_truck, r"assets\hero-bg.png")
shutil.copy(fleet_trucks, r"assets\fleet.jpg")
shutil.copy(gn_logo, r"assets\logo.jpg")

print("Copied successfully")
