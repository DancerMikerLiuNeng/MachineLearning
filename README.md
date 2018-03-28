# MachineLearning
learn for fun
# not git venv
git -A .
git reset -- venv

##git local files to github steps

_first step into the destination folder_
>cd destination folder
_run cmd_
>git init
_Add Files_
*you can add one file
    *git add file1
*git current folder all things
    *git add . or git add -A .
*not git one folder
    ** git reset -- folder name**
 _Add comment_
 git commit -m "your comment"
    *git remote add origin https://github.com/xx/text.git
    *git pull --rebase origin master  [pull=fetch+merge]
    *git push -u origin master
 _Remove foler_
 **You could checkout 'master' with both directories;

git rm -r one-of-the-directories
git commit -m "Remove duplicated directory"
git push origin <your-git-branch> (typically 'master', but not always)
Remove directory from git but NOT local
As mentioned in the comments, what you usually want to do is remove this directory from git but not delete it entirely from the filesystem (local)

In that case use:

git rm -r --cached myFolder**
