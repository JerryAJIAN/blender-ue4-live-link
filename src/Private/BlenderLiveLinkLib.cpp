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
    DLLEXPORT BlenderLiveLinkLib* BlenderLiveLinkLib_new(){ return new BlenderLiveLinkLib();}
    DLLEXPORT void BlenderLiveLinkLib_destroy(BlenderLiveLinkLib* blll){ blll->~BlenderLiveLinkLib();}
    DLLEXPORT bool BlenderLiveLinkLib_Init(BlenderLiveLinkLib* blll){ return blll->LibInit();}
    DLLEXPORT bool BlenderLiveLinkLib_Open(BlenderLiveLinkLib* blll){ return blll->LibOpen();}
    DLLEXPORT bool BlenderLiveLinkLib_Ready(BlenderLiveLinkLib* blll){ return blll->LibReady();}
    DLLEXPORT bool BlenderLiveLinkLib_Close(BlenderLiveLinkLib* blll){ return blll->LibClose();}
    DLLEXPORT bool BlenderLiveLinkLib_Release(BlenderLiveLinkLib* blll){ return blll->LibRelease();}
}
