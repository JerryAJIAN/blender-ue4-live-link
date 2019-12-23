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

#include "IStreamObject.h"

struct FLiveLinkSkeletonStaticData;
struct FLiveLinkAnimationFrameData;
struct FLiveLinkTransformStaticData;
struct FLiveLinkTransformFrameData;

class FModelStreamObject : public IStreamObject
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

    // IStreamObject Interface

	virtual const bool ShouldShowInUI() const override;

	virtual const FString GetStreamOptions() const override;

	virtual FName GetSubjectName() const override;
	virtual void UpdateSubjectName(FName NewSubjectName) override;

	virtual int GetStreamingMode() const override;
	virtual void UpdateStreamingMode(int NewStreamingMode) override;

	virtual bool GetActiveStatus() const override;
	virtual void UpdateActiveStatus(bool bIsNowActive) override;

	virtual bool GetSendAnimatableStatus() const override;
	virtual void UpdateSendAnimatableStatus(bool bNewSendAnimatable) override;

	virtual const BlenderModel* GetModelPointer() const override;

	virtual const FString GetRootName() const override;

	virtual bool IsValid() const override;

	virtual void Refresh() override;
	virtual void UpdateSubjectFrame() override;

public:
	static void UpdateBaseStaticData(const BlenderModel* Model, bool bSendAnimatable, FLiveLinkBaseStaticData& InOutBaseFrameData);
	static void UpdateBaseFrameData(const BlenderModel* Model, bool bSendAnimatable, FLiveLinkBaseFrameData& InOutBaseFrameData);
	void UpdateSubjectSkeletalStaticData(FLiveLinkSkeletonStaticData& InOutTransformFrame);
	void UpdateSubjectSkeletalFrameData(FLiveLinkAnimationFrameData& InOutTransformFrame);
	static void UpdateSubjectTransformStaticData(const BlenderModel* Model, bool bSendAnimatable, FLiveLinkTransformStaticData& InOutTransformFrame);
	static void UpdateSubjectTransformFrameData(const BlenderModel* Model, bool bSendAnimatable, FLiveLinkTransformFrameData& InOutTransformFrame);

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
