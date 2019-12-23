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
#include "ModelStreamObject.h"
#include "BlenderLiveLinkUtilities.h"

#include "Roles/LiveLinkAnimationRole.h"
#include "Roles/LiveLinkAnimationTypes.h"
#include "Roles/LiveLinkTransformRole.h"
#include "Roles/LiveLinkTransformTypes.h"

// Creation / Destruction
FModelStreamObject::FModelStreamObject(const BlenderModel* ModelPointer, const TSharedPtr<ILiveLinkProvider> StreamProvider, bool bShouldRefresh)
    : RootModel(ModelPointer)
    , Provider(StreamProvider)
    , bIsActive(true)
    , bSendAnimatable(false)
    , StreamingMode(FModelStreamMode::RootOnly)
{
    // check(ModelPointer)
    FString ModelLongName(ANSI_TO_TCHAR(RootModel->LongName));
    SubjectName = FName(*ModelLongName);

    if (bShouldRefresh)
    {
        Refresh();
    }
};

FModelStreamObject::~FModelStreamObject()
{
    Provider->RemoveSubject(SubjectName);
};

// Stream Object Interface
const bool FModelStreamObject::ShouldShowInUI() const
{
    return true;
};

const FString FModelStreamObject::GetStreamOptions() const
{
    FString MyFooString = TEXT("~");

    const TCHAR* delim = *MyFooString;
    return FString::Join(ModelStreamOptions, delim);
};

FName FModelStreamObject::GetSubjectName() const
{
    return SubjectName;
};

void FModelStreamObject::UpdateSubjectName(FName NewSubjectName)
{
    if (NewSubjectName != SubjectName)
    {
        Provider->RemoveSubject(SubjectName);
        SubjectName = NewSubjectName;
        Refresh();
    }
};

int FModelStreamObject::GetStreamingMode() const
{
    return StreamingMode;
}

void FModelStreamObject::UpdateStreamingMode(int NewStreamingMode)
{
    if (StreamingMode != NewStreamingMode)
    {
        StreamingMode = NewStreamingMode;
        Refresh();
    }
};

bool FModelStreamObject::GetActiveStatus() const
{
    return bIsActive;
};

void FModelStreamObject::UpdateActiveStatus(bool bIsNowActive)
{
    bIsActive = bIsNowActive;
};

bool FModelStreamObject::GetSendAnimatableStatus() const
{
    return bSendAnimatable;
};

void FModelStreamObject::UpdateSendAnimatableStatus(bool bNewSendAnimatable)
{
    if (bSendAnimatable != bNewSendAnimatable)
    {
        bSendAnimatable = bNewSendAnimatable;
        Refresh();
    }
};

const BlenderModel* FModelStreamObject::GetModelPointer() const
{
    return RootModel;
};

const FString FModelStreamObject::GetRootName() const
{
    return FString(RootModel->LongName);
};

bool FModelStreamObject::IsValid() const
{
    // By default, an object is valid if the root model is in the scene
    return true;
};

void FModelStreamObject::Refresh()
{
    if (GetStreamingMode() == FModelStreamMode::FullHierarchy)
    {
        FLiveLinkStaticDataStruct SkeletonData(FLiveLinkSkeletonStaticData::StaticStruct());
        UpdateSubjectSkeletalStaticData(*SkeletonData.Cast<FLiveLinkSkeletonStaticData>());
        Provider->UpdateSubjectStaticData(SubjectName, ULiveLinkAnimationRole::StaticClass(), MoveTemp(SkeletonData));
    }
    else
    {
        FLiveLinkStaticDataStruct TransformData(FLiveLinkTransformStaticData::StaticStruct());
        UpdateSubjectTransformStaticData(RootModel, bSendAnimatable, *TransformData.Cast<FLiveLinkTransformStaticData>());
        Provider->UpdateSubjectStaticData(SubjectName, ULiveLinkTransformRole::StaticClass(), MoveTemp(TransformData));
    }
};

void FModelStreamObject::UpdateSubjectFrame()
{
    if (!bIsActive)
    {
        return;
    }

    if (GetStreamingMode() == FModelStreamMode::FullHierarchy)
    {
        FLiveLinkFrameDataStruct TransformData = (FLiveLinkAnimationFrameData::StaticStruct());
        UpdateSubjectSkeletalFrameData(*TransformData.Cast<FLiveLinkAnimationFrameData>());
        Provider->UpdateSubjectFrameData(SubjectName, MoveTemp(TransformData));
    }
    else
    {
        FLiveLinkFrameDataStruct TransformData = (FLiveLinkTransformFrameData::StaticStruct());
        UpdateSubjectTransformFrameData(RootModel, bSendAnimatable, *TransformData.Cast<FLiveLinkTransformFrameData>());
        Provider->UpdateSubjectFrameData(SubjectName, MoveTemp(TransformData));
    }
};

void FModelStreamObject::UpdateBaseStaticData(const BlenderModel* Model, bool bSendAnimatable, FLiveLinkBaseStaticData& InOutBaseStaticData)
{
    InOutBaseStaticData.PropertyNames = BlenderUtilities::GetAllAnimatableCurveNames(const_cast<BlenderModel*>(Model), FString(ANSI_TO_TCHAR(Model->Name)));
};

void FModelStreamObject::UpdateSubjectTransformStaticData(const BlenderModel* Model, bool bSendAnimatable, FLiveLinkTransformStaticData& InOutTransformStatic)
{
    UpdateBaseStaticData(Model, bSendAnimatable, InOutTransformStatic);
};

void FModelStreamObject::UpdateSubjectSkeletalStaticData(FLiveLinkSkeletonStaticData& InOutAnimationStatic)
{
    UpdateBaseStaticData(RootModel, bSendAnimatable, InOutAnimationStatic);

    InOutAnimationStatic.BoneNames.Reset();
    BoneParents.Reset();
    BoneModels.Reset();

    InOutAnimationStatic.BoneNames.Emplace(RootModel->Name);
    BoneParents.Emplace(-1);
    BoneModels.Emplace(RootModel);

    {
        TArray<TPair<int, BlenderModel*>> SearchList;
        TArray<TPair<int, BlenderModel*>> SearchListNext;

        SearchList.Emplace(0, (BlenderModel*)RootModel);

        while (SearchList.Num() > 0)
        {
            for (const TPair<int, BlenderModel*>& SearchPair : SearchList)
            {
                int ParentIdx = SearchPair.Key;
                BlenderModel* SearchModel = SearchPair.Value;
                int ChildCount = SearchModel->Children.Num();

                for (int ChildIdx = 0; ChildIdx < ChildCount; ++ChildIdx)
                {
                    BlenderModel* ChildModel = SearchModel->Children[ChildIdx];

                    InOutAnimationStatic.BoneNames.Emplace(ChildModel->Name);
                    BoneParents.Emplace(ParentIdx);
                    BoneModels.Emplace(ChildModel);

                    SearchListNext.Emplace(BoneModels.Num() - 1, ChildModel);
                }
            }
        }
        SearchList = SearchListNext;
        SearchListNext.Reset();
    }
    InOutAnimationStatic.BoneParents = BoneParents;

    check(BoneModels.Num() == InOutAnimationStatic.BoneNames.Num());
    if (bSendAnimatable)
    {
        for (int32 BoneIndex = 0; BoneIndex < BoneModels.Num(); ++BoneIndex)
        {
            InOutAnimationStatic.PropertyNames.Append(BlenderUtilities::GetAllAnimatableCurveNames(const_cast<BlenderModel*>(BoneModels[BoneIndex]),
                InOutAnimationStatic.BoneNames[BoneIndex].ToString()));
        }
    }
};

void FModelStreamObject::UpdateBaseFrameData(const BlenderModel* Model, bool bSendAnimatable, FLiveLinkBaseFrameData& InOutBaseFrameData)
{
    InOutBaseFrameData.WorldTime = FPlatformTime::Seconds();
    InOutBaseFrameData.MetaData.SceneTime = BlenderUtilities::GetSceneTimecode();
    if (bSendAnimatable)
    {
        InOutBaseFrameData.PropertyValues = BlenderUtilities::GetAllAnimatableCurveValues(const_cast<BlenderModel*>(Model));
    }
};

void FModelStreamObject::UpdateSubjectSkeletalFrameData(FLiveLinkAnimationFrameData& InOutAnimationFrame)
{
    // UpdateBaseFrameData(RootModel, bSendAnimatable, InOutAnimationFrame);

	// if (BoneParents.Num() != BoneModels.Num())
	// {
	// 	return;
	// }

	// const int32 BoneCount = BoneParents.Num();
	// InOutAnimationFrame.Transforms.SetNum(BoneCount);

	// TArray<FTransform> ParentInverseTransforms;
	// ParentInverseTransforms.SetNum(BoneCount);

	// // loop through children here
	// for (int BoneIndex = 0; BoneIndex < BoneModels.Num(); ++BoneIndex)
	// {
	// 	InOutAnimationFrame.Transforms[BoneIndex] = MobuUtilities::UnrealTransformFromModel(const_cast<FBModel*>(BoneModels[BoneIndex]));
	// 	ParentInverseTransforms[BoneIndex] = InOutAnimationFrame.Transforms[BoneIndex].Inverse();
	// 	if (BoneParents[BoneIndex] != -1)
	// 	{
	// 		InOutAnimationFrame.Transforms[BoneIndex] = InOutAnimationFrame.Transforms[BoneIndex] * ParentInverseTransforms[BoneParents[BoneIndex]];
	// 	}

	// 	if (bSendAnimatable)
	// 	{
	// 		// Stream all parameters of all bones as "<BoneName>:<ParameterName>"
	// 		InOutAnimationFrame.PropertyValues.Append(MobuUtilities::GetAllAnimatableCurveValues(const_cast<FBModel*>(BoneModels[BoneIndex])));
	// 	}
	// }
}

void FModelStreamObject::UpdateSubjectTransformFrameData(const BlenderModel* Model, bool bSendAnimatable, FLiveLinkTransformFrameData& InOutTransformFrame)
{
}
