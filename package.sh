#!/bin/bash
VERSION_LINE=$(cat src/__init__.py | grep \"version\" | cut -d : -f 2)
VERSION_MAJOR=$(echo $VERSION_LINE | cut -d : -f 2 | tr -d ',' | tr -d ')' | tr -d '(' | cut -d " " -f 1)
VERSION_MINOR=$(echo $VERSION_LINE | cut -d : -f 2 | tr -d ',' | tr -d ')' | tr -d '(' | cut -d " " -f 2)
VERSION_PATCH=$(echo $VERSION_LINE | cut -d : -f 2 | tr -d ',' | tr -d ')' | tr -d '(' | cut -d " " -f 3)

mkdir UE4LiveLink
cp -R src/LiveLinkWrapper UE4LiveLink
cp -R src/Operators UE4LiveLink
cp -R src/Panels UE4LiveLink
cp -R src/PropertyGroups UE4LiveLink
cp -R src/*.py UE4LiveLink
cp README.md UE4LiveLink/
cp LICENSE UE4LiveLink/
zip -r UE4LiveLink_${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_PATCH}.zip UE4LiveLink
rm -rf UE4LiveLink
