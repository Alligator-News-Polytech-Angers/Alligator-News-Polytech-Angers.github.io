@echo off

git add .
git status
git commit -m "modification from the batch file"
git push

set /p variable = Appuyez sur une touche pour terminer ...