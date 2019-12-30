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
#pragma once

#include "BlenderLiveLinkCommon.h"
#include "IStreamObject.h"
#include "Misc/CommandLine.h"
#include "Async/TaskGraphInterfaces.h"
#include "Modules/ModuleManager.h"
#include "UObject/Object.h"
#include "Misc/ConfigCacheIni.h"
#include "Misc/OutputDevice.h"

// Simple input device
class FBlenderLiveLink
{
public:
    FBlenderLiveLink();
    ~FBlenderLiveLink();
    void StartLiveLink();
    void StopLiveLink();
	const FString& GetProviderName() const { return CurrentProviderName; }

    TSharedPtr<ILiveLinkProvider> LiveLinkProvider;

private:
	FString CurrentProviderName = "Blender Live Link";
};
