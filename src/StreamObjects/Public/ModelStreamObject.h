
#pragma once

#include "IStreamObject.h"

struct FLiveLinkSkeletonStaticData;
struct FLiveLinkAnimationFrameData;
struct FLiveLinkTransformStaticData;
struct FLiveLinkTransformFrameData;

class FModelStreamObject // : public IStreamObject
{
private:
        const TArray<FString> ModelStreamOptions = { TEXT("Root Only"), TEXT("Full Hierarchy")};

        enum FModelStreamMode
        {
            RootOnly,
            FullHierarchy
        };

public:
        // Construct from a BlenderModel*
        FModelStreamObject(const BlenderModel* ModelPointer, const TSharedPtr<ILiveLinkProvider> StreamProvider, bool bShouldRefresh=true);

        virtual ~FModelStreamObject();

        void Refresh();

        int32 GetStreamingMode();

protected:
        // Stream Variables
        const BlenderModel* const RootModel;
        const TSharedPtr<ILiveLinkProvider> Provider;

        FName SubjectName;
        TArray<int32> BoneParents;
        TArray<const BlenderModel*> BoneModels;
        bool bIsActive;
        bool bSendAnimatable;
        int StreamingMode;
};
