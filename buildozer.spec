[app]
source.dir = .
version = 1.0.0
title = Object Recognition App
package.name = objectrecog
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*
requirements = python3,kivy,opencv-python,tensorflow,numpy
presplash.filename = %(source.dir)s/assets/images/presplash.png
icon.filename = %(source.dir)s/assets/images/icon.png
orientation = portrait
fullscreen = 1
android.permissions = CAMERA, INTERNET

[buildozer]
# (str) Path to the buildozer directory
# buildozer_dir = /path/to/buildozer

# (str) Path to the android sdk
android.sdk_path = C:\Users\Estudiante09\AppData\Local\Android\Sdk

# (str) Path to the android ndk
android.ndk_path = C:\path\to\android-ndk

# (str) Path to the android platform
# android.platform_path = /path/to/android/platform
