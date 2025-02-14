@echo off
set FILTER_BRANCH_SQUELCH_WARNING=1
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch portfolio_site/settings.py" --prune-empty --tag-name-filter cat -- --all 