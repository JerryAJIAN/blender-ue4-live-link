/* This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful, but
   WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program. If not, see <http://www.gnu.org/licenses/>.*/
using UnrealBuildTool;
using System.Collections.Generic;
using System.IO;

public abstract class BlenderLiveLinkPluginTargetBase : TargetRules
{
    public BlenderLiveLinkPluginTargetBase(TargetInfo target, string InBlenderVersionString) : base(target)
    {
        Type =TargetType.Program;

        bShouldCompileAsDLL = true;
        LinkType = TargetLinkType.Monolithic;

        LaunchModuleName = "BlenderLiveLinkPlugin" + InBlenderVersionString;

        // We only need minimal use of the engine for this plugin
        bBuildDeveloperTools = false;
        bUseMallocProfiler = false;
        bBuildWithEditorOnlyData = true;
        bCompileAgainstEngine = false;
        bCompileAgainstCoreUObject = true;
        bCompileICU = false;
        bHasExports = false;
    }
}

public class BlenderLiveLinkPlugin281Target : BlenderLiveLinkPluginTargetBase
{
    public BlenderLiveLinkPlugin281Target(TargetInfo Target) : base(Target, "2.81")
    { }
}
