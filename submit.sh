python vis.py
git status
read -p "Enter the file(s) to stage: " ff
git add "$ff"
read -p "Enter problem number or complete commit message: " ans
if ! [[ $ans =~ ^[0-9]+$ ]];then
    git commit -m $ans
else
    git commit -m "Complete Problem $ans"
fi
