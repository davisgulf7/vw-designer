# OSSL vs LSL - OpenSimulator

Views

Page

Discussion

View source

History

# OSSL vs LSL

### From OpenSimulator

Jump to: [navigation](http://opensimulator.org#column-one), [search](http://opensimulator.org#searchInput)LSL and OSSL functions may appear overlapping. Sometimes, they are. This may happen when a OSSL function has been written before it's LL conterpart. Most of the time, they are complementary. 

OSSL implements features not available in LSL (NPCs, Texture Drawing) or extend them, like adressing prims by key, which gives unprecedented flexibility to the scripter. 

This page tries to highlight the differences between OSSL and LSL functions when similar versions exist. 

 llGetLinkPrimitiveParams [osGetLinkPrimitiveParams](http://opensimulator.org/wiki/OsGetLinkPrimitiveParams) Allows for multiple-link constants LINK_SET, LINK_ALL_CHILDREN. Returns a by-side list of properties.   llSetLinkPrimitiveParams   No need for OSSL version since llSetLinkPrimitiveParams accepts all LINK_* flags   llGetPrimitiveParams 
 llSetPrimitiveParams [osGetPrimitiveParams](http://opensimulator.org/wiki/OsGetPrimitiveParams)[osSetPrimitiveParams](http://opensimulator.org/wiki/OsGetPrimitiveParams) Acts on out-of-linkset primitive (uuid instead of linknumber) [osSetProjectionParams](http://opensimulator.org/wiki/OsSetProjectionParams) Same effect can be obtained with llSetLinkPrimitiveParams (linknum, [PRIM_PROJECTOR]) but OSSL version has osSetPrimitiveParams power to work outside linkset.   llCreateLink 
 llBreakLink 
 llBreakAllLinks [osForceCreateLink](http://opensimulator.org/wiki/OsForceCreateLink)[osForceBreakLink](http://opensimulator.org/wiki/OsForceCreateLink)[osForceBreakAllLinks](http://opensimulator.org/wiki/OsForceCreateLink) Does not require PERMISSION_CHANGE_LINKS   llParticleSystem 
 llLinkParticleSystem [osParticleSystem](http://opensimulator.org/wiki/OsParticleSystem)[osLinkParticleSystem](http://opensimulator.org/wiki/OsParticleSystem) llSitTarget 
 llLinkSitTarget [osSetStandTarget](http://opensimulator.org/wiki/OsSetStandTarget)[osSetLinkStandTarget](http://opensimulator.org/wiki/OsSetStandTarget) SitTarget is position when sitting. 
 StandTarget, position when unsitting.   llAvatarOnSitTarget 
 llAvatarOnLinkSitTarget [osGetSittingAvatarsCount](http://opensimulator.org/wiki/OsGetSittingAvatarsCount)() 
[osGetSittingAvatarsCount](http://opensimulator.org/wiki/OsGetSittingAvatarsCount)(uuid)   OSSL function returns the total number of avatars sitting on a linkset. LSL functions apply only to avatars on sittarget (return NULL_KEY if sittarget is not set) and cannot operate outside the linkset. A similar result can be obtained with llGetObjectDetails(uuid, [OBJECT_SIT_COUNT]).   llPlaySound 
 llLoopSound 
 llTriggerSound 
 ... [osPlaySound](http://opensimulator.org/wiki/OsPlaySound)[osLoopSound](http://opensimulator.org/wiki/OsPlaySound)[osTriggerSound](http://opensimulator.org/wiki/OsPlaySound)...   All OSSL sound functions takes a linknumber argument.   llLinkPlaySound   Universal link sound function (SOUND_PLAY, SOUND_LOOP, SOUND_TRIGGER, SOUND_SYNC). Equivalent to resp. osPlaySound, osLoopSound, osTriggerSound, osPlaySoundSlave, osLoopSoundSlave.   llGetNumberOfPrims 
 llGetObjectPrimCount [osGetPrimCount](http://opensimulator.org/wiki/OsGetPrimCount)() 
[osGetPrimCount](http://opensimulator.org/wiki/OsGetPrimCount)(uuid)   OSSL version does not count sitting avatars and does work on attachments   llStartAnimation 
 llStopAnimation [osAvatarPlayAnimation](http://opensimulator.org/wiki/OsAvatarPlayAnimation)[osAvatarStopAnimation](http://opensimulator.org/wiki/OsAvatarPlayAnimation) Does not require PERMISSION_TRIGGER_ANIMATION 
 OSSL can animate multiples avatars, when LSL is bound to the avatar having granted the permission.   llAttachToAvatar 
  llDetachFromAvatar [osForceAttachToAvatar](http://opensimulator.org/wiki/OsForceAttachToAvatar)[osForceDetachFromAvatar](http://opensimulator.org/wiki/OsForceAttachToAvatar) Does not require PERMISSION_ATTACH. 
 Target avatar is implicit. To attach explicitely to a given avatar, use osForceAttachToOtherAvatarFromInventory on the avatar's key.   llGetAgentList [osGetAgents](http://opensimulator.org/wiki/OsGetAgents)[osGetAvatarList](http://opensimulator.org/wiki/OsGetAgents)[osGetNPCList](http://opensimulator.org/wiki/OsGetAgents) llGetAgentList returns a list of agent keys. 
  osGetAgents, a list of agent names. 
 osGetAvatarList, a strided list of agent (key, position, name). 
 osGetNPCList : same as osGetAvatarList, but only NPCs.   llGetInventoryKey 
 llGetInventoryName [osGetInventoryItemKey](http://opensimulator.org/wiki/OsGetInventoryItemKey)[osGetInventoryName](http://opensimulator.org/wiki/OsGetInventoryItemKey) llGetInventoryKey returns item id while osGetInventoryItemKey returns asset id. 
 llGetInventoryName returns name from (index,type) while osGetInventoryName return name fro item id.   llKey2Name [osKey2Name](http://opensimulator.org/wiki/OsKey2Name) llKey2Name works on both avatars and objects. 
 osKey2Name returns an empty string on objects.   Retrieved from "[http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)"  

Personal tools

[Log in / create account](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

General

[Main Page](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[News](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

For Administrators

[Admin Home](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[download](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Running](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Configuration](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Building](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[FAQ](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Related Software](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Support](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Report a Bug](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

For Developers

[Dev Home](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Contributions Policy](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Bug Tracking](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

For Creators

[Content Creation](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Scripting](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

For Grid Users

[Connecting](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Grid List](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Screenshots](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

Related Links

[Related Software](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Black Duck](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

About This Wiki

[Recent changes](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

Tools

[What links here](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Related changes](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Special pages](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Printable version](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

[Permanent link](http://opensimulator.org/index.php?title=OSSL_vs_LSL&oldid=54863)

 This page was last modified on 7 April 2025, at 08:03.

This page has been accessed 10,218 times.

Content is available under [Attribution-Share Alike 2.5 ](http://creativecommons.org/licenses/by-sa/2.5/) unless otherwise noted.

[Privacy policy](http://creativecommons.org/licenses/by-sa/2.5/)

[About OpenSimulator](http://creativecommons.org/licenses/by-sa/2.5/)

[Disclaimers](http://creativecommons.org/licenses/by-sa/2.5/)