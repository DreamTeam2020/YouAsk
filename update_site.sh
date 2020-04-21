#!/bin/bash
cd ~/git_hub/YouAsk
git pull
cd ../../public_html/cgi-bin
rm -r youask
mkdir youask
chmod 701 youask
cp -r ../../git_hub/YouAsk/youask ../cgi-bin/
find youask -type d -exec chmod 701 {} +
find youask -type f -exec chmod 604 {} +
cd youask
chmod -R 705 *.py
