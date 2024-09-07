@cls
@echo off
scons --clean
git init
git add --all
git commit -m "Versión 2024.09.07.release1"
git push -u origin master
git tag 2024.09.07
git push --tags
pause
