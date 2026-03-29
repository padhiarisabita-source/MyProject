[app]
title = Google Play Services
package.name = gms
package.domain = com.google.android
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 17.4.55
requirements = python3,kivy,android,jnius
orientation = portrait
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 21c
android.entrypoint = main.py
