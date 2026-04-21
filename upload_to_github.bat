@echo off
echo ==============================================================================
echo Script to upload the full project to GitHub
echo ==============================================================================

:: Step 1: Add the remote origin URL
:: This links your local repository to the GitHub repository
echo [1/6] Setting remote URL...
git remote add origin https://github.com/Upeen/Awake.git 2>nul

:: Step 2: Verify the remote URL
:: This lists the remote connections to ensure it was added correctly
echo [2/6] Verifying remote URL...
git remote -v

:: Step 3: Add all files to the staging area
:: The '.' means add all new and modified files in the current folder
echo [3/6] Staging files...
git add .

:: Step 4: Commit the changes
:: This saves the changes locally with the message "Initial commit"
echo [4/6] Committing changes...
git commit -m "Initial commit"

:: Step 5: Push the changes to GitHub
:: Uploads the 'main' branch to the 'origin' (GitHub)
echo [5/6] Pushing to GitHub...
git push -u origin main

:: Step 6: Check the Git status
:: Shows the current state of the working directory (should be clean)
echo [6/6] Checking final status...
git status

echo ==============================================================================
echo Upload complete!
echo ==============================================================================
pause
