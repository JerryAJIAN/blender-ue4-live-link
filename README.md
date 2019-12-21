# blender-ue4-live-link  
[![Build Status](https://travis-ci.org/tscrypter/blender-ue4-live-link.svg?branch=master)](https://travis-ci.org/tscrypter/blender-ue4-live-link)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=tscrypter_blender-ue4-live-link&metric=alert_status)](https://sonarcloud.io/dashboard?id=tscrypter_blender-ue4-live-link)  
Blender (2.8) plugin to provide Live Link integration with Unreal Engine 4

## Steps to get library compiling on linux properly
```
cp Engine/Source/ThirdParty/SDL2/SDL-gui-backend/lib/Linux/x86_64-unknown-linux-gnu/libSDL2.a Engine/Source/ThirdParty/SDL2/SDL-gui-backend/lib/Linux/x86_64-unknown-linux-gnu/libSDL2.a_bak  

cp Engine/Source/ThirdParty/SDL2/SDL-gui-backend/lib/Linux/x86_64-unknown-linux-gnu/libSDL2_fPIC.a libSDL2.a

cp Engine/Source/ThirdParty/jemalloc/lib/Linux/x86_64-unknown-linux-gnu/libjemalloc.a Engine/Source/ThirdParty/jemalloc/lib/Linux/x86_64-unknown-linux-gnu/libjemalloc.a_bak  

cp Engine/Source/ThirdParty/jemalloc/lib/Linux/x86_64-unknown-linux-gnu/libjemalloc_pic.a libjemalloc.a  

cp Engine/Source/ThirdParty/zlib/zlib-1.2.5/Lib/Linux/x86_64-unknown-linux-gnu/libz.a Engine/Source/ThirdParty/zlib/zlib-1.2.5/Lib/Linux/x86_64-unknown-linux-gnu/libz.a_bak  

cp Engine/Source/ThirdParty/zlib/zlib-1.2.5/Lib/Linux/x86_64-unknown-linux-gnu/libz_fPIC.a libz.a
```