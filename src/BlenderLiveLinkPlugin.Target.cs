// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;
using System.Collections.Generic;

[SupportedPlatforms(UnrealPlatformClass.Desktop)]
public class BlenderLiveLinkPluginTarget : TargetRules
{
	public BlenderLiveLinkPluginTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Program;

		bShouldCompileAsDLL = false;
		LinkType = TargetLinkType.Monolithic;
		SolutionDirectory = "Programs/LiveLink";
		LaunchModuleName = "BlenderLiveLinkPlugin";


		// We only need minimal use of the engine for this plugin
		bBuildDeveloperTools = false;
		bUseMallocProfiler = false;
		bBuildWithEditorOnlyData = true;
		bCompileAgainstEngine = false;
		bCompileAgainstCoreUObject = true;
		bCompileICU = false;
		bHasExports = true;

		bBuildInSolutionByDefault = false;
	}
}
