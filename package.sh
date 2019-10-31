#!/bin/bash

# Based on an idea by https://github.com/voutilad/alexa-btvpython

# /!\ You need to make a virtualenv with :
# virtualenv venv
# source venv/bin/activate
# pip install ask-sdk

PACKAGE_NAME="https://github.com/miseaprix/alexa-skill-deal-skill.git"
PROJECT_DIR=$(pwd)
BUILD_DIR="build"
SOURCES="get_hot_deals_skill.py"
VIRTUAL_ENV="venv"
NEEDED_PACKAGES="ask_sdk_core ask_sdk_model requests urllib3 certifi idna chardet pytz"
OTHER_FILES="other_file.txt" # <== TO BE REMOVED IF NOT NEEDED

# clear out existing package
mkdir -p ${BUILD_DIR}
rm -f "$BUILD_DIR/$PACKAGE_NAME.zip"

# package out python module
zip -r9 "$BUILD_DIR/$PACKAGE_NAME.zip" $SOURCES

# package dependencies
cd $VIRTUAL_ENV/lib/python3.7/site-packages
find . \( -name __pycache__ -o -name "*.pyc" \) -delete
zip -r9 "$PROJECT_DIR/$BUILD_DIR/$PACKAGE_NAME.zip" $NEEDED_PACKAGES
cd ${PROJECT_DIR}

# add necessary files
zip -r9 "$PROJECT_DIR/$BUILD_DIR/$PACKAGE_NAME.zip" "$OTHER_FILES" # <== TO BE REMOVED IF NOT NEEDED
