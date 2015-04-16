#!/bin/bash

git checkout master
git pull origin master

#activate our virtual env!
. ./yalgaar_env/bin/activate

#generate our frozen site
python freeze.py

#checkout the static site branch 
git checkout gh-pages

#add the built pages
for f in index.html submitted_tweets recent_tweets popular tweets; do
    rm $f
    mv yalgaar/build/$f ./
    git add -r $f
done

#commit!
git commit -m 'New deployment on `date -R`'

#deploy!
git push origin gh-pages

#now back to master!
git checkout master
echo "Done!"
