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

// Allow ticking of the engine
#include "Containers/Ticker.h"

// Strings
#define BLENDERLIVELINK__CLASS      BLENDERLIVELINK__CLASSNAME
#define BLENDERLIVELINK__NAME       BLENDERLIVELINK_CLASSSTR
#define BLENDERLIVELINK__LABEL      "UE - LiveLink"
#define BLENDERLIVELINK__DESC       "UE - LiveLink"

FBlenderLiveLink::FBlenderLiveLink()
{
    // Set sampling rate to Before Render
    CurrentSampleRate = SampleOptions.Last().Value;
    UpdateSampleRate();

    StartLiveLink();

    SetDirty(false);

    // TSharedPtr<IStreamObject> EditorCamera = MakeShared<FEditorActiveCameraStreamObject>(LiveLinkProvider);
    // EditorCameraObject = EditorCamera;
    // StreamObjects.Emplace(-1, EditorCamera);

    LastEvaluationTime = FPlatformTime::Seconds();
}

FBlenderLiveLink::~FBlenderLiveLink()
{
    StopLiveLink();
}

void FBlenderLiveLink::UpdateSampleRate()
{
    // TODO: Implement
}

void FBlenderLiveLink::SetInformation(const char* NewInformation)
{
    // HardwareVersionInfo.SetString("Version {VERSION_NUMBER}");
    // Information.SetString(NewInformation);
    // Status.SetString("Tom Delaney 2019");
    // TODO: Implement
}

bool FBlenderLiveLink::Init()
{
    SetInformation("Status: Offline");
    return true;
}

bool FBlenderLiveLink::Start()
{
    // Progress - Setting up device && Setting sampling rate

    SetInformation("Status: Online");
    return true;
}

bool FBlenderLiveLink::Stop()
{
    // Progress - Shutting down
    SetInformation("Status: Offline");
    return false;
}

bool FBlenderLiveLink::Done()
{
    return false;
}

bool FBlenderLiveLink::Reset()
{
    Stop();
    return Start();
}

void FBlenderLiveLink::UpdateStream()
{
    TickCoreTicker();

    if (IsDirty())
    {
        UpdateStreamObjects();
    }
    // for (TPair<int32, TSharedPtr<IStreamObject>>& MapPair : StreamObjects)
    // {
    //     const TSharedPtr<IStreamObject>& StreamObject = MapPair.Value;
    //     StreamObject->UpdateSubjectFrame();
    // }
}

int32 FBlenderLiveLink::GetCurrentSampleRateIndex()
{
    int32 CurrentSampleIdx = 0;
    for (int SampleIdx = 0; SampleIdx < SampleOptions.Num(); ++SampleIdx)
    {
        const FFrameRate& TestSampleRate = SampleOptions[SampleIdx].Value;
        if (CurrentSampleRate == TestSampleRate)
        {
            CurrentSampleIdx = SampleIdx;
            break;
        }
    }
    return CurrentSampleIdx;
}

void FBlenderLiveLink::StartLiveLink()
{
    StopLiveLink();

    LiveLinkProvider = ILiveLinkProvider::CreateLiveLinkProvider(GetProviderName());
}

void FBlenderLiveLink::StopLiveLink()
{
    TickCoreTicker();
    if (LiveLinkProvider.IsValid())
    {
        LiveLinkProvider = nullptr;
    }
}

void FBlenderLiveLink::UpdateStreamObjects()
{
    // for (TPair<int32, TSharedPtr<IStreamObject>>& MapPair : StreamObjects)
    // {
    //     const TSharedPtr<IStreamObject>& StreamObject = MapPair.Value;
    //     if (StreamObject->IsValid())
    //     {
    //         StreamObject->Refresh();
    //     }
    //     else
    //     {
    //         StreamObjects.Remove(MapPair.Key);
    //     }
    // }
    SetDirty(false);
    // SetRefreshUI(true);
}

void FBlenderLiveLink::TickCoreTicker()
{
    double CurrentTime = FPlatformTime::Seconds();
    FTicker::GetCoreTicker().Tick(CurrentTime - LastEvaluationTime);
    LastEvaluationTime = CurrentTime;
}

int32 FBlenderLiveLink::GetNextUID()
{
    return NextUID++;
}

bool FBlenderLiveLink::IsEditorCameraStreamed() const
{
    // TSharedPtr<IStreamObject> EditorCameraObjectPin = EditorCameraObject.Pin();
    // if(EditorCameraObjectPin.IsValid())
    // {
    //     return EditorCameraObjectPin->GetActiveStatus();
    // }
    return false;
}

void FBlenderLiveLink::SetEditorCameraStreamed(bool bStream)
{
    // TSharedPtr<IStreamObject> EditorCameraObjectPin = EditorCameraObject.Pin();
    // if (EditorCameraObjectPin.IsValid())
    // {
    //     EditorCameraObjectPin->UpdateActiveStatus(bStream);
    // }
}

void FBlenderLiveLink::SetProviderName(const FString& NewValue)
{
    if (NewValue != GetProviderName())
    {
        CurrentProviderName = NewValue;
        SetDirty(false);
    }
}

//===========================================================================
// External C library calls
//===========================================================================
extern "C" // prevent name mangling so it can be referenced from Python
{
    DLLEXPORT FBlenderLiveLink* BlenderLiveLink_Construct()
    {
        return new FBlenderLiveLink();
    }

    DLLEXPORT void BlenderLiveLink_Destroy(FBlenderLiveLink* BlenderLiveLink)
    {
        BlenderLiveLink->~FBlenderLiveLink();
    }

    DLLEXPORT void BlenderLiveLink_UpdateSampleRate(FBlenderLiveLink* BlenderLiveLink)
    {
        BlenderLiveLink->UpdateSampleRate();
    }

    DLLEXPORT void BlenderLiveLink_SetInformation(FBlenderLiveLink* BlenderLiveLink, const char* NewInformation)
    {
        BlenderLiveLink->SetInformation(NewInformation);
    }
}
