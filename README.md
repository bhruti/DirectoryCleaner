# 🧹 Directory Cleaner

A simple Python script to automatically **organize files** in a directory by moving them into folders based on their extensions.

## 📌 Features
- Categorizes files into folders based on their **extensions**.
- Automatically **creates folders** if they don’t exist.
- Moves files into appropriate folders **without deletion**.
- **Skips folders** and the script file (`clean.py`) to avoid conflicts.

## 📸 Before & After
### Before Running `clean.py`
![Screenshot (433)](https://github.com/user-attachments/assets/8a5266fb-f1ae-4881-9e46-16ef4447dacb)

### After Running `clean.py`
![Screenshot (434)](https://github.com/user-attachments/assets/736218d5-492d-47ca-8e94-047eedd70904)


## 🛠️ Installation & Usage
1. **Clone the repository**:
   ```sh
   git clone https://github.com/bhruti/DirectoryCleaner
   cd DirectoryCleaner
   ```

2. **Run the script** inside the target directory:
   ```sh
   python clean.py
   ```
   The script will automatically organize files into folders based on their extensions.

## ⚠️ Caution
- If any files have a specific **folder dependency**, manually handle them **before running the script**.
- Ensure you **do not rename important system files**, as this script moves all files except folders and itself (`clean.py`).

Made with ❤️ in Python 🐍

