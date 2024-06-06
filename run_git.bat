@cls
@echo off
scons --clean
scons pot
git init
git add --all
git commit -m "Versión 2024.06.06-Inicial-1"
git push -u origin master
git tag 2024.06.06
git push --tags
pause
