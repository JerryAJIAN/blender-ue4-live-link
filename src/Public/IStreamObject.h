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
#include "BlenderModel.h"

// Pure Abstract class. Inherit from this to support streaming.
// If you create a new Stream Object then make sure to register it in BlenderLiveLinkStreamObject.h
class IStreamObject
{
public:
    // Interface for modifying and accessing stream parameters
    virtual ~IStreamObject() {}

    virtual const bool ShouldShowInUI() const = 0;

    virtual const FString GetStreamOptions() const = 0;

    virtual FName GetSubjectName() const = 0;

    virtual void UpdateSubjectName(FName NewSubjectName) = 0;

    virtual int GetStreamingMode() const = 0;

    virtual void UpdateStreamingMode(int NewStreamingMode) = 0;

    virtual bool GetActiveStatus() const = 0;

    virtual void UpdateActiveStatus(bool bIsNowActive) = 0;

    virtual bool GetSendAnimatableStatus() const = 0;

    virtual void UpdateSendAnimatableStatus(bool bNewSendAnimatable) = 0;

    virtual const BlenderModel* GetModelPointer() const = 0;

    virtual const FString GetRootName() const = 0;

    virtual bool IsValid() const = 0;

    // Interface for object streaming
    virtual void Refresh() = 0;

    virtual void UpdateSubjectFrame() = 0;
};
