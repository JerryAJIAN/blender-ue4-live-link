#!/bin/bash
cp -R src UE4LiveLink
cp README.md UE4LiveLink/
cp LICENSE UE4LiveLink/
zip -r UE4LiveLink.zip UE4LiveLink
rm -rf UE4LiveLink

