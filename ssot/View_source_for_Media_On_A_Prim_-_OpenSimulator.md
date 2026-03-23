# View source for Media On A Prim - OpenSimulator

View source for Media On A Prim - OpenSimulator

Views

[Page](http://opensimulator.org/wiki/Media_On_A_Prim)

[Discussion](http://opensimulator.org/index.php?title=Talk:Media_On_A_Prim&action=edit&redlink=1)

[View source](http://opensimulator.org/index.php?title=Media_On_A_Prim&action=edit)

[History](http://opensimulator.org/index.php?title=Media_On_A_Prim&action=history)

# View source for Media On A Prim

### From OpenSimulator

← [Media On A Prim](http://opensimulator.org/wiki/Media_On_A_Prim)

Jump to: [navigation](http://opensimulator.org/index.php?title=Media_On_A_Prim&action=edit#column-one), [search](http://opensimulator.org/index.php?title=Media_On_A_Prim&action=edit#searchInput)

You do not have permission to edit this page, for the following reason:

The action you have requested is limited to users in the group: emailconfirmed.

You can view and copy the source of this page:

=Introduction= Media on a prim was implemented in OpenSimulator as of 0.7.1. This facility allows you to display and navigate web pages from the surface/texture of a prim. =Architecture= Like voice, media on a prim is largely implemented as a direction connection from a prim surface configured for MOAP directly to a website. It looks a little like this. [[image:Arch.png]] # The viewer starts by requesting media on a prim information (ObjectMediaRequest HTTP capability message) for a particular prim (here with ID 123) from OpenSimulator. # OpenSimulator responds with an ObjectMediaResponse with the shared media information for each face. Here, face 0 is currently pointing at www.google.com # The viewer fetches this page directly from google.com and all subsequent interactions with that website go directly to it. OpenSimulator is not involved in any further data exchanges, unless the viewer changes the page URL (in which case that goes back to OpenSimulator and is sent out to any other viewers that are interested in that prim. This is why you can see people changing webpages on these surfaces but you can't see their interactions with that particular page unless the website itself takes steps to mirror it to all browsers pointing at that page. For instance, each viewer can play a movie on a YouTube page that a MOAP surface points to but they are all playing that movie independently. If one user pauses the movie this won't be seen by any other viewer. =Limits= Media on a prim is quite heavyweight. Viewers will very probably place a limit on the number of MOAP surfaces that can be shown at once. Typically, the current limit is 5 surfaces. =References= * For instructions on how to set up MOAP surfaces in a viewer, see [http://community.secondlife.com/t5/English-Knowledge-Base/Shared-Media/ta-p/700145 Media on a prim/Shared Media]

Return to [Media On A Prim](http://opensimulator.org/wiki/Media_On_A_Prim).

Retrieved from " [http://opensimulator.org/wiki/Media_On_A_Prim](http://opensimulator.org/wiki/Media_On_A_Prim)" 

Personal tools

[Log in / create account](http://opensimulator.org/index.php?title=Special:UserLogin&returnto=Media+On+A+Prim&returntoquery=action%3Dedit)

General

[Main Page](http://opensimulator.org/wiki/Main_Page)

[News](http://opensimulator.org/wiki/News)

For Administrators

[Admin Home](http://opensimulator.org/wiki/User_Documentation)

[download](http://opensimulator.org/wiki/Download)

[Running](http://opensimulator.org/wiki/Dependencies)

[Configuration](http://opensimulator.org/wiki/Configuration)

[Building](http://opensimulator.org/wiki/Build_Instructions)

[FAQ](http://opensimulator.org/wiki/FAQ)

[Related Software](http://opensimulator.org/wiki/Related_Software)

[Support](http://opensimulator.org/wiki/Support)

[Report a Bug](http://opensimulator.org/mantis)

For Developers

[Dev Home](http://opensimulator.org/wiki/Development)

[Contributions Policy](http://opensimulator.org/wiki/Contributions_Policy)

[Bug Tracking](http://opensimulator.org/mantis)

For Creators

[Content Creation](http://opensimulator.org/wiki/Artist_Home)

[Scripting](http://opensimulator.org/wiki/Scripting_Documentation)

For Grid Users

[Connecting](http://opensimulator.org/wiki/Connecting)

[Grid List](http://opensimulator.org/wiki/Grid_List)

[Screenshots](http://opensimulator.org/wiki/Screenshots)

Related Links

[Related Software](http://opensimulator.org/wiki/Related_Software)

[Black Duck](https://www.openhub.net/p/opensimulator)

About This Wiki

[Recent changes](http://opensimulator.org/wiki/Special:RecentChanges)

Search

Go Search

Tools

[What links here](http://opensimulator.org/wiki/Special:WhatLinksHere/Media_On_A_Prim)

[Related changes](http://opensimulator.org/wiki/Special:RecentChangesLinked/Media_On_A_Prim)

[Special pages](http://opensimulator.org/wiki/Special:SpecialPages)

[Privacy policy](http://opensimulator.org/wiki/OpenSimulator:Privacy_policy)

[About OpenSimulator](http://opensimulator.org/wiki/OpenSimulator:About)

[Disclaimers](http://opensimulator.org/wiki/OpenSimulator:General_disclaimer)