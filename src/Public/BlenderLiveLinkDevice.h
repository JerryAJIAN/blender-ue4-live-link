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

# pragma once

//---- Registration defines
#define BLENDERLIVELINK__CLASSNAME      FBlenderLiveLink
#define BLENDERLIVELINK__CLASSSTR       "BlenderLiveLink"

#define IntToChar(input) std::to_string(input).c_str()
#define FStringToChar(input) ((std::string)TCHAR_TO_UTF8(*input)).c_str()
#define CharToFString(input) UTF8_TO_TCHAR(input)

// Class
class FBlenderLiveLink
{
public:
    FBlenderLiveLink();
    ~FBlenderLiveLink();

    void StartLiveLink();
    void StopLiveLink();

    // Initialization/Shutdown
    bool Init();    // Initialize/create
    bool Done();
    bool Reset();
    bool Stop();    // Stop (offline)
    bool Start();   // Start (online)

    void UpdateStreamObjects();

    void SetDirty(bool bNewDirty) { bIsDirty = bNewDirty; }
    bool IsDirty() const { return bIsDirty; }

    const TArray<TPair<FString, FFrameRate>> SampleOptions =
    {
        TPair<FString, FFrameRate>(FString("30hz"), FFrameRate(30,1)),
        TPair<FString, FFrameRate>(FString("50hz"), FFrameRate(50,1)),
		TPair<FString, FFrameRate>(FString("60hz"), FFrameRate(60, 1)),
		TPair<FString, FFrameRate>(FString("100hz"), FFrameRate(100, 1)),
		TPair<FString, FFrameRate>(FString("120hz"), FFrameRate(120, 1)),
		TPair<FString, FFrameRate>(FString("Before Render"), FFrameRate(-1, 1)),        
    };

    FFrameRate CurrentSampleRate;
    void UpdateSampleRate();

    int32 GetNextUID();

    bool IsEditorCameraStreamed() const;
    void SetEditorCameraStreamed(bool bStream);

    const FString& GetProviderName() const { return CurrentProviderName; }
    void SetProviderName(const FString& NewValue);

public:
    // TMap<int32, TSharedPtr<IStreamObject>> StreamObjects;
	TSharedPtr<ILiveLinkProvider> LiveLinkProvider;

public:
    void SetInformation(const char* NewInformation);
    void TickCoreTicker();

private:
    // TWeakPtr<IStreamObject> EditorCameraObject;
    FString CurrentProviderName = "Blender Live Link";

    int32 NextUID = 1;

    void UpdateStream(); // Get latest data and send to unreal

    int32 GetCurrentSampleRateIndex();

    bool bIsDirty;

    double LastEvaluationTime;
};
