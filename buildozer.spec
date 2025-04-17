[app]
title = Icode
package.name = icode
package.domain = org.example
source.dir = .
source.include_exts = py,kv,json,txt,docx,xlsx,pdf
source.exclude_dirs = __pycache__, .git, .vscode

main.py = Icode/main.py

version = 1.0

requirements = python3,kivy,kivymd,openpyxl,python-docx,reportlab

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET
android.archs = armeabi-v7a, arm64-v8a

android.entrypoint = org.kivy.android.PythonActivity

# ✅ Оставляем только одну строку
android.minapi = 21
android.api = 33

android.sdk = 33
android.ndk = 21b

android.private_storage = True
android.allow_backup = True

# ✅ Стабильная версия Build Tools (важно!)
android.build_tools_version = 33.0.2

# --- Release settings ---
android.release = 1
android.debug = 0

# ❗ Используй безопасные переменные в GitHub Secrets, а не храни пароли в открытом виде!
# Здесь оставить строки пустыми, а секреты передавать через GitHub Actions
android.keystore = my-release-key.keystore
android.keystore_password = 
android.keyalias = my-key-alias
android.keyalias_password = 
