// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.


#include "BlenderLiveLinkPlugin.h"

#include "RequiredProgramMainCPPInclude.h"

DEFINE_LOG_CATEGORY_STATIC(LogBlenderLiveLinkPlugin, Log, All);

IMPLEMENT_APPLICATION(BlenderLiveLinkPlugin, "BlenderLiveLinkPlugin");

INT32_MAIN_INT32_ARGC_TCHAR_ARGV()
{
	GEngineLoop.PreInit(ArgC, ArgV);
	UE_LOG(LogBlenderLiveLinkPlugin, Display, TEXT("Hello World"));
	return 0;
}
