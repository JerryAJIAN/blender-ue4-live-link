#pragma once

#include "BlenderLiveLinkCommon.h"

class BlenderUtilities
{
public:
    static TArray<FName> GetAllAnimatableCurveNames(BlenderModel* BlModel, const FString& Prefix = FString());
    static TArray<float> GetAllAnimatableCurveValues(BlenderModel* BlModel);
    static FFrameRate TimeModeToFrameRate(int32 TimeMode);
    static FQualifiedFrameTime GetSceneTimecode();
};
