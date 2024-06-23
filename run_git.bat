@cls
@echo off
scons --clean
git init
git add --all
git commit -m "Versión 2024.06.23.release1"
git push -u origin master
git tag 2024.06.23
git push --tags
pause
