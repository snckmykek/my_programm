[app]
title = my_programm
package.name = my_programm
package.domain = com.my_programm
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1
requirements = kivy==master,python3crystax==3.5
orientation = all
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
#android.presplash_color = #1d3b3e
android.permissions = WRITE_EXTERNAL_STORAGE
android.api = 19
android.minapi = 13
android.sdk = 23
#private = False
android.ndk_path = /home/kivy/Android/crystax-ndk-10.3.2/
android.arch = armeabi-v7a
p4a.source_dir = /home/kivy/Repos/python-for-android/
[buildozer]
log_level = 2
warn_on_root = 1