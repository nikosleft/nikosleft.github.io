import os

# ==========================================
# 🏭 THE WEB FACTORY v2.1
# ==========================================

# --- CONFIGURATION ---
TEMPLATES_DIR = "templates"

# Default Images
IMG_DEFAULT_DRIVING = "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1000&auto=format&fit=crop"
IMG_DEFAULT_GARAGE = "https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?q=80&w=1000&auto=format&fit=crop"

# --- DATA ENTRY ZONE ---
targets = {
    "sxoli-tasos-akis": {
        "type": "driving",
        "name": "Σχολή Οδηγών Τάσος - Άκης",
        "phone": "2310886202",
        "area": "Θεσσαλονίκη (⭐ 4.8/5)", 
        "image": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?q=80&w=1000&auto=format&fit=crop" 
    },

    "garage-aaperformance": {
        "type": "garage",
        "name": "AAPerformance Service",
        "phone": "2314071040",
        "area": "Θεσσαλονίκη (⭐ 4.9/5)",
        "image": "https://images.unsplash.com/photo-1487754180451-c456f719a1fc?q=80&w=1000&auto=format&fit=crop" 
    }
}

# ==========================================
# ⚙️ THE ENGINE
# ==========================================
print("🚀 Starting the Web Factory...")

# Check if templates exist before running
if not os.path.exists(TEMPLATES_DIR):
    print(f"❌ CRITICAL ERROR: The folder '{TEMPLATES_DIR}' does not exist.")
    print("   Please create a folder named 'templates' and put your HTML files inside.")
    exit()

count = 0

for folder, data in targets.items():
    # 1. Extract Data
    site_type = data.get("type", "driving").lower()
    b_name = data.get("name", "Business Name")
    b_phone = data.get("phone", "")
    b_area = data.get("area", "Αθήνα")
    b_image = data.get("image")

    # 2. Logic Switch
    if site_type == "garage":
        template_file = "layout_garage.html"
        if not b_image: b_image = IMG_DEFAULT_GARAGE
        print(f"🔧 Processing GARAGE: {b_name}...")
    else: 
        template_file = "layout_driving.html"
        if not b_image: b_image = IMG_DEFAULT_DRIVING
        print(f"🚗 Processing DRIVING: {b_name}...")

    # 3. Load Template
    template_path = os.path.join(TEMPLATES_DIR, template_file)
    
    if not os.path.exists(template_path):
        print(f"   ⚠️ ERROR: Template '{template_file}' is missing in '{TEMPLATES_DIR}' folder.")
        continue

    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # 4. Inject Data
    html = html_content.replace("{BUSINESS_NAME}", b_name)
    html = html.replace("{PHONE}", b_phone)
    html = html.replace("{AREA}", b_area)
    html = html.replace("{IMAGE_URL}", b_image)

    # 5. Save
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"   ✅ Created: {folder}/index.html")
    count += 1

print(f"\n🎉 DONE! Generated {count} websites.")