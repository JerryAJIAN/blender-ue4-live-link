
#include "ModelStreamObject.h"

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
    if (bShouldRefresh)
    {
        Refresh();
    }
};

FModelStreamObject::~FModelStreamObject()
{
    Provider->RemoveSubject(SubjectName);
}

int32 FModelStreamObject::GetStreamingMode()
{
    return StreamingMode;
}

void FModelStreamObject::Refresh()
{
    if (GetStreamingMode() == FModelStreamMode::FullHierarchy)
    {
        FLiveLinkStaticDataStruct SkeletonData(FLiveLinkSkeletonStaticData::StaticStruct());
        Provider->UpdateSubjectStaticData(SubjectName, ULiveLinkAnimationRole::StaticClass(), MoveTemp(SkeletonData));
    }
    else
    {
        FLiveLinkStaticDataStruct TransformData(FLiveLinkTransformStaticData::StaticStruct());
        Provider->UpdateSubjectStaticData(SubjectName, ULiveLinkTransformRole::StaticClass(), MoveTemp(TransformData));
    }
}
