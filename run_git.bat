@cls
@echo off
scons --clean
git init
git add --all
git commit -m "Versión 2024.09.19.Lang_de"
git push -u origin master
git tag 2024.09.19
git push --tags
pause
