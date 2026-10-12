[app]

title = AI Video Creator
package.name = aivideocreator
package.domain = org.somnang14455

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,md
source.exclude_dirs = .git,.github,.venv,venv,build,dist,bin,__pycache__

version = 0.1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.archs = arm64-v8a
android.accept_sdk_license = True

android.allow_backup = False

[buildozer]

log_level = 2
warn_on_root = 1
