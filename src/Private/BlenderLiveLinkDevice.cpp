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
#include "BlenderLiveLinkDevice.h"
#include <iostream>

FBlenderLiveLink::FBlenderLiveLink()
{
    std::cout << "Constructing FBlenderLiveLink" << std::endl;
};

FBlenderLiveLink::~FBlenderLiveLink()
{
    UE_LOG(LogBlenderPlugin, Log, TEXT("Destroying FBlenderLifeLink"));
    // std::cout << "Destroying FBlenderLiveLink" << std::endl;
};

void FBlenderLiveLink::StartLiveLink()
{
    StopLiveLink();

	LiveLinkProvider = ILiveLinkProvider::CreateLiveLinkProvider(GetProviderName());
	
	std::cout << "Live Link Started!" << std::endl;
};

void FBlenderLiveLink::StopLiveLink()
{
    // TickCoreTicker();
	if (LiveLinkProvider.IsValid())
	{
		std::cout << "Provider References: " << LiveLinkProvider.GetSharedReferenceCount() << std::endl;
		LiveLinkProvider = nullptr;
		std::cout << "Deleting Live Link" << std::endl;
	}
	std::cout << "Live Link Stopped!" << std::endl;
};

extern "C"
{
    DLLEXPORT FBlenderLiveLink* BlenderLiveLink_New(){ return new FBlenderLiveLink();}
    DLLEXPORT void BlenderLiveLink_Destroy(FBlenderLiveLink* bll) { bll->~FBlenderLiveLink();}
    DLLEXPORT void BlenderLiveLink_Start(FBlenderLiveLink* bll){ bll->StartLiveLink();}
    DLLEXPORT void BlenderLiveLink_Stop(FBlenderLiveLink* bll){ bll->StopLiveLink();}
}
