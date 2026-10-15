@echo off
title Donerci Xovos Server
echo ==============================================
echo       DONERCI XOVOS - MAHALLIY SERVER
echo ==============================================
echo Server ishga tushirilmoqda...
start http://localhost:8080/
powershell -ExecutionPolicy Bypass -File .\server.ps1
pause
