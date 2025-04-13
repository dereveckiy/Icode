[app]
title = Icode
package.name = icode
package.domain = org.example
source.dir = .
source.include_exts = py,kv,json,txt,docx,xlsx,pdf
source.exclude_dirs = __pycache__, .git, .vscode

# Указание главного файла
main.py = Icode/main.py

version = 1.0

requirements = python3,kivy,kivymd,openpyxl,python-docx,reportlab

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET
android.archs = armeabi-v7a, arm64-v8a

android.entrypoint = org.kivy.android.PythonActivity
android.minapi = 21
android.sdk = 30
android.ndk = 21b
android.private_storage = True
android.allow_backup = True
android.build_tools_version = 34.0.0

# --- Release settings for Google Play ---
android.release = 1
android.debug = 0
android.api = 31

android.keystore = my-release-key.keystore
android.keystore_password = 4256942569iG
android.keyalias = my-key-alias
android.keyalias_password = 4256942569iG
