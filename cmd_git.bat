@echo off

:: Commandes git ↓
git add .
git status
set /p commitMessage = Message du commit :  
git commit -m + %commitMessage%
git push
:: #################

set /p touche = ------------------------- Appuyez sur une touche pour terminer ...