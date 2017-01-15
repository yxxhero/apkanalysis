#!/usr/bin/env python2.7
#coding:utf-8
import axmlparserpy.apk as apk
ap = apk.APK('_PATH_TO_APK')
print ap.get_package()
print ap.get_androidversion_name()
