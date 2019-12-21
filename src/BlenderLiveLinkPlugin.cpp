
#include "RequiredProgramMainCPPInclude.h"
#include "UObject/Object.h"
#include "Roles/LiveLinkAnimationRole.h"
#include "Roles/LiveLinkAnimationTypes.h"
#include "Roles/LiveLinkCameraRole.h"
#include "Roles/LiveLinkCameraTypes.h"
#include "Roles/LiveLinkLightRole.h"
#include "Roles/LiveLinkLightTypes.h"
#include "Roles/LiveLinkTransformRole.h"
#include "Roles/LiveLinkTransformTypes.h"
#include "LiveLinkProvider.h"
#include "LiveLinkRefSkeleton.h"
#include "LiveLinkTypes.h"

DEFINE_LOG_CATEGORY_STATIC(LogBlenderLiveLinkPlugin, Log, All);

IMPLEMENT_APPLICATION(BlenderLiveLinkPlugin, "BlenderLiveLinkPlugin");

INT32_MAIN_INT32_ARGC_TCHAR_ARGV()
{
	GEngineLoop.PreInit(ArgC, ArgV);
	UE_LOG(LogBlenderLiveLinkPlugin, Display, TEXT("Hello World"));
	return 0;
}

DLLEXPORT double DegToRad(double Deg)
{
	const double E_PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062;
	return Deg * (E_PI / 180.0f);
}
