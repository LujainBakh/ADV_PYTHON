[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
ios.codesign.allowed = false


[buildozer]
ios.p4a_deploy = False
ios.kivy_ios_url = https://github.com/kivy/kivy-ios

[ios]
xcode_deploy = 1
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
