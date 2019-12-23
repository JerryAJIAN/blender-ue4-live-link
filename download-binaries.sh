#!/bin/bash
mkdir -p Binaries/Linux
curl -o Binaries/Linux/libBlenderLiveLinkPlugin.so https://github.com/tscrypter/blender-ue4-live-link/releases/download/v0.0.1-alpha.2232019/libBlenderLiveLinkPlugin.so
curl -o Binaries/Linux/libBlenderLiveLinkPlugin.debug https://github.com/tscrypter/blender-ue4-live-link/releases/download/v0.0.1-alpha.2232019/libBlenderLiveLinkPlugin.debug
curl -o Binaries/Linux/libBlenderLiveLinkPlugin.sym https://github.com/tscrypter/blender-ue4-live-link/releases/download/v0.0.1-alpha.2232019/libBlenderLiveLinkPlugin.sym
curl -o Binaries/Linux/UE4LiveLink_0.0.1.zip https://github.com/tscrypter/blender-ue4-live-link/releases/download/v0.0.1-alpha.2232019/UE4LiveLink_0.0.1.zip
