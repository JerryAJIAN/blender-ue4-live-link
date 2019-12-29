/* This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful, but
   WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program. If not, see <http://www.gnu.org/licenses/>.
*/
#include "BlenderLiveLinkLib.h"
#include <iostream>

BlenderLiveLinkLib::BlenderLiveLinkLib()
{
    std::cout << "Constructing BlenderLiveLinkLib" << std::endl;
};

BlenderLiveLinkLib::~BlenderLiveLinkLib()
{
    std::cout << "Destroying BlenderLiveLinkLib" << std::endl;
};

bool BlenderLiveLinkLib::LibInit()
{
    std::cout << "Calling LibInit on BlenderLiveLinkLib" << std::endl;

    GEngineLoop.PreInit(TEXT("BlenderLiveLinkPlugin -Messaging"));

    // ensure target platform manager is referenced early as it must be created on the main thread
    GetTargetPlatformManager();

    ProcessNewlyLoadedUObjects();

    // Tell the module manager that it may now process newly-loaded UObjects when new C++ modules are loaded
    FModuleManager::Get().StartProcessingNewlyLoadedObjects();
    FModuleManager::Get().LoadModule(TEXT("UdpMessaging"));

    std::cout << "BlenderLiveLink Library Initialized" << std::endl;

    return bSuccess;
};

bool BlenderLiveLinkLib::LibOpen()
{
    std::cout << "Calling LibOpen on BlenderLiveLinkLib" << std::endl;
    return bSuccess;
};

bool BlenderLiveLinkLib::LibReady()
{
    std::cout << "Calling LibReady on BlenderLiveLinkLib" << std::endl;
    return bSuccess;
};

bool BlenderLiveLinkLib::LibClose()
{
    std::cout << "Calling LibClose on BlenderLiveLinkLib" << std::endl;
    return bSuccess;
};

bool BlenderLiveLinkLib::LibRelease()
{
    std::cout << "Calling LibRelease on BlenderLiveLinkLib" << std::endl;
    return bSuccess;
};

extern "C"
{
    DLLEXPORT BlenderLiveLinkLib* BlenderLiveLinkLib_New(){ return new BlenderLiveLinkLib();}
    DLLEXPORT void BlenderLiveLinkLib_Destroy(BlenderLiveLinkLib* blll){ blll->~BlenderLiveLinkLib();}
    DLLEXPORT bool BlenderLiveLinkLib_Init(BlenderLiveLinkLib* blll){ return blll->LibInit();}
    DLLEXPORT bool BlenderLiveLinkLib_Open(BlenderLiveLinkLib* blll){ return blll->LibOpen();}
    DLLEXPORT bool BlenderLiveLinkLib_Ready(BlenderLiveLinkLib* blll){ return blll->LibReady();}
    DLLEXPORT bool BlenderLiveLinkLib_Close(BlenderLiveLinkLib* blll){ return blll->LibClose();}
    DLLEXPORT bool BlenderLiveLinkLib_Release(BlenderLiveLinkLib* blll){ return blll->LibRelease();}
}
