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
    std::cout << "Destroying FBlenderLiveLink" << std::endl;
};

void FBlenderLiveLink::StartLiveLink()
{
    std::cout << "Called StartLiveLink on FBlenderLiveLink" << std::endl;
};

void FBlenderLiveLink::StopLiveLink()
{
    std::cout << "Called StopLiveLink on FBlenderLiveLink" << std::endl;
};

extern "C"
{
    DLLEXPORT FBlenderLiveLink* BlenderLiveLink_New(){ return new FBlenderLiveLink();}
    DLLEXPORT void BlenderLiveLink_Destroy(FBlenderLiveLink* bll) { bll->~FBlenderLiveLink();}
    DLLEXPORT void BlenderLiveLink_Start(FBlenderLiveLink* bll){ bll->StartLiveLink();}
    DLLEXPORT void BlenderLiveLink_Stop(FBlenderLiveLink* bll){ bll->StopLiveLink();}
}
