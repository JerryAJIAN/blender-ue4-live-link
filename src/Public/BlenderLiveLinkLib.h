class BlenderLiveLinkLib
{
public:
    BlenderLiveLinkLib();
    ~BlenderLiveLinkLib();
    bool LibInit();
    bool LibOpen();
    bool LibReady();
    bool LibClose();
    bool LibRelease();

    bool bSuccess = true;
};
