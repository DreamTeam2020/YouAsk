#!/bin/bash
cd ~/git_hub/YouAsk
git pull
cd ../../public_html/cgi-bin
#Copy the session store and question pages out
rm -r session_store
mkdir session_store
cp -r youask/session_store ../cgi-bin
rm -r question_pages
mkdir question_pages
cp -r youask/question_pages/question* question_pages/
rm -r profile_pages
mkdir profile_pages
cp -r youask/profile_pages/profile* profile_pages/

rm -r youask
mkdir youask
chmod 701 youask
cp -r ../../git_hub/YouAsk/youask ../cgi-bin/

rm -r youask/session_store
cp -r session_store youask/
rm -r youask/question_pages/question_*
cp -r question_pages/question_* youask/question_pages/
rm -r youask/profile_pages/profile_*
cp -r profile_pages/profile_* youask/profile_pages/


find youask -type d -exec chmod 701 {} +
find youask -type f -exec chmod 604 {} +
cd youask
chmod -R 705 *.py
cd controller
chmod 700 *.py
cd ../model
chmod 700 *.py
cd ../session_store
chmod 700 *
cd ../question_pages
chmod 705 *.py
chmod 700 template_question.py
cd  ../profile_pages
chmod 705 *.py
chmod 700 template_profile.py
