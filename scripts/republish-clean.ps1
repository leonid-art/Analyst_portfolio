# Republish portfolio with a single clean commit (no co-author).
# Run from Windows Terminal or PowerShell OUTSIDE Cursor if possible.

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..

$env:GIT_AUTHOR_NAME = "Leonid Fomin"
$env:GIT_AUTHOR_EMAIL = "fla.21@uni-dubna.ru"
$env:GIT_COMMITTER_NAME = "Leonid Fomin"
$env:GIT_COMMITTER_EMAIL = "fla.21@uni-dubna.ru"

git checkout main 2>$null
git checkout --orphan republish-temp
git add -A

$tree = git write-tree
if ($tree -eq "4b825dc642cb6eb9a060e54bf8d69288fbee4904") {
    throw "Empty tree - files not staged. Aborting."
}

$commit = git commit-tree $tree -m "Portfolio: SQL, Python, Power BI, Tableau, Excel"
git update-ref refs/heads/main $commit
git checkout main
git reset --mixed HEAD

git reflog expire --expire=now --all
git gc --prune=now --aggressive

Write-Host "Done. New commit: $commit"
Write-Host "Run: git push --force origin main"
