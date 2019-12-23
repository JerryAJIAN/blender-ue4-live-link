#include "BlenderLiveLinkUtilities.h"

// Get all the things that are Animatable and are of a type we can stream
TArray<FName> BlenderUtilities::GetAllAnimatableCurveNames(BlenderModel* BlModel, const FString& Prefix)
{
    TArray<FName> LiveLinkCurves;
    return LiveLinkCurves;
};

TArray<float> BlenderUtilities::GetAllAnimatableCurveValues(BlenderModel* BlModel)
{
    // int PropertyCount = BlenderModel->PropertyList.GetCount();

    TArray<float> LiveLinkCurves;
    // Reserve enough memory for worst case
    // LiveLinkCurves.Reserve(PropertyCount);
    return LiveLinkCurves;
};

FFrameRate BlenderUtilities::TimeModeToFrameRate(int32 TimeMode)
{
    return FFrameRate(24, 1);
}

FQualifiedFrameTime BlenderUtilities::GetSceneTimecode()
{
    int32 LocalTime = 100;
    int32 Fps = 60;
    FFrameTime FrameTime(LocalTime);
    FFrameRate FrameRate = TimeModeToFrameRate(Fps);
    return FQualifiedFrameTime(FrameTime, FrameRate);
}