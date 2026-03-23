# Hypergrid Security - OpenSimulator

Hypergrid Security - OpenSimulator

Views

[Page](http://opensimulator.org/wiki/Hypergrid_Security)

[Discussion](http://opensimulator.org/index.php?title=Talk:Hypergrid_Security&action=edit&redlink=1)

[View source](http://opensimulator.org/index.php?title=Hypergrid_Security&action=edit)

[History](http://opensimulator.org/index.php?title=Hypergrid_Security&action=history)

# Hypergrid Security

### From OpenSimulator

Jump to: [navigation](http://opensimulator.org/wiki/Hypergrid_Security#column-one), [search](http://opensimulator.org/wiki/Hypergrid_Security#searchInput) 

**Home** 

**Download** 

**News** 

**Support** 

**Admin** 

**Dev** 

**Screen Shots** 

**Grid List** 

**Bugs**

**Languages:**

**

English**

[Deutsch](http://opensimulator.org/wiki/Hypergrid_Security/de)

[Français](http://opensimulator.org/wiki/Hypergrid_Security/fr)

## Contents

[ [hide](http://opensimulator.org/wiki/Hypergrid_Security)]

[1 Tasks](http://opensimulator.org/wiki/Hypergrid_Security#Tasks)

[1.1 Prevent local users from resolving Hypergrid URLs to foreign destinations](http://opensimulator.org/wiki/Hypergrid_Security#Prevent_local_users_from_resolving_Hypergrid_URLs_to_foreign_destinations)

[1.2 Prevent users at a given UserLevel from travelling to foreign destinations](http://opensimulator.org/wiki/Hypergrid_Security#Prevent_users_at_a_given_UserLevel_from_travelling_to_foreign_destinations)

[1.3 Prevent foreign users from accessing the simulator](http://opensimulator.org/wiki/Hypergrid_Security#Prevent_foreign_users_from_accessing_the_simulator)

[1.4 Ban specific foreign users](http://opensimulator.org/wiki/Hypergrid_Security#Ban_specific_foreign_users)

[2 Discussion](http://opensimulator.org/wiki/Hypergrid_Security#Discussion)

[2.1 Malicious Clients](http://opensimulator.org/wiki/Hypergrid_Security#Malicious_Clients)

[2.1.1 CopyBots](http://opensimulator.org/wiki/Hypergrid_Security#CopyBots)

[2.2 Malicious Hosts](http://opensimulator.org/wiki/Hypergrid_Security#Malicious_Hosts)

[2.2.1 Actively Malicious Hosts](http://opensimulator.org/wiki/Hypergrid_Security#Actively_Malicious_Hosts)

[2.2.2 Piracy](http://opensimulator.org/wiki/Hypergrid_Security#Piracy)

# Tasks

This task text is in development and currently should not be relied upon without direct testing.

## Prevent local users from resolving Hypergrid URLs to foreign destinations

Set

Default is also false.

Both main map search and address bar search use this to resolve region addresses. So setting to false will prevent any attempt to resolve Hypergrid addresses.

This may not prevent users from teleporting via existing hyperlink bookmarks if hypergrid was previously enabled.

This setting should theoretically still allow external users to visit the installation.

## Prevent users at a given UserLevel from travelling to foreign destinations

This is done per user level. For instance, to prevent ordinary (UserLevel 0) local users from going to foreign destinations, set

You can also whitelist certain destinations for users that otherwise cannot travel, or blacklist others for users who can otherwise travel anywhere. See [Hypergrid_Parameters](http://opensimulator.org/wiki/Hypergrid_Parameters) for more details.

## Prevent foreign users from accessing the simulator

Set

This should still allow local users to teleport to foreign climes.

One can also whitelist or blacklist all agents from specific source simulators with the AllowExcept and DisallowExcept parameters. See [Hypergrid_Parameters](http://opensimulator.org/wiki/Hypergrid_Parameters) for more details.

## Ban specific foreign users

See [Banning Foreign Users in Hypergrid](http://opensimulator.org/wiki/Banning_Foreign_Users_in_Hypergrid).

# Discussion

**Please note that this is a historical discussion about content in the Hypergrid rather than about security issues per se.**

There is a wide-spread assumption that open grids such as OSGrid and new forms of grids such as the hypergrid are inherently insecure, and that it will be impossible to develop a "goods-based" economy on top of them; only walled-gardens can be secured. This is both true and false. While it is true with the current state of things, open grids, whatever their form, can be made as secure as the web. The first step towards that is to define exactly what the security threats are, and how they affect (or not) open and closed grids. So, let's spell them out, and face them head-on. This will help put our feet on the ground so that we start developing appropriate solutions.

## Malicious Clients

### CopyBots

Everyone knows about the infamous [CopyBot](http://en.wikipedia.org/wiki/CopyBot). Using libraries such as [LibSL](http://www.libsecondlife.org/wiki/Main_Page) (now known as OpenMetaverse), or by modifying existing viewers, it is possible to develop clients for opensim servers that do unorthodox things such as bypassing the permissions system to copy people's assets. Bots written by griefers can do lots of other nasty things.

Malicious bots are a problem for all opensim administrators, including walled-garden grids. They can be prevented, to a certain extent, by exo-technical solutions such as Terms of Service and real-world lawsuits. Technically speaking, the only way to keep intruders out is to run opensim inside a firewall, pretty much like all other pieces of client/server software out there. If that's an acceptable solution for your case, you should do it.

Unfortunately firewalls also keep the public out, and most opensim operators, even the ones running walled-garden grids, want to reach out to the public. In this case, opensim operators may develop additional technical obstacles for bots, similar to those we see on the Web. For example, make sure agents are being run by real people by giving them a human-challenge during the login/TP process, etc. (This will only deter bots, not modified viewers which are operated by human beings.)

Every obstacle to malicious clients lowers the risk of an intruder attack. However keep this in mind: no matter how many obstacles one builds, a sufficiently skilled and motivated attacker will be able to overcome them to penetrate opensims connected to the public internet. This affects hypergrid nodes as much as walled-garden grids. In fact, it's more pervasive than that: it affects **all** servers (opensim, web, etc.) connected to the public internet. Fighting malicious intruders is a fact of a connected world. Fortunately, those attacks don't happen very often, or the Web would have been dead by now.

## Malicious Hosts

### Actively Malicious Hosts

The new security threat introduced by openness, one that does not exist in closed grids, is the possibility of a user to visit a region that is running malicious code. In the current state of opensim, a malicious host can do serious damage to the user's assets. Let's see how.

Assume you have your assets in your hypergrided-standalone opensim, and you go visit another opensim that happens to be running malicious code. Here is a non-exhaustive list of vulnerabilities that you are exposed to:

The host has your session id, so it can request your inventory items on your behalf and store copies in its local asset server. To add insult to injury, a malicious host could simply wipe out your inventory after having copied it.

Even if the malicious host doesn't access your items by itself, every time you access items in your inventory while you are in that region, those items are cached in the region's local cache, and can be stored persistently by the malicious host.

Malicious hosts can do a lot more damage, but those two are enough to illustrate this new kind of vulnerability affecting open grids. Note that this affects all open grids, i.e. those where arbitrary people can plug-in their opensims, and not just the hypergrid.

Fortunately, there is a family of simple solutions to this problem that can be summarized as "protecting you from yourself." That proposal is described [here](http://opensimulator.org/wiki/Hypergrid_Inventory_Access).

### Piracy

A second new security threat affecting open grids is one pertaining to commerce of virtual goods. Suppose you put something out for sale on your hypergrided opensim. A foreign user comes and buys it. What that really means is that that user will physically get a copy of the assets moved to his/her asset server, which is different from your asset server. The permissions will be whatever you define them to be, and using the regular VW client, that user can only do what you defined he/she should could do with the object, as usual. However, if the user has direct backend access to the asset and inventory servers, that person can simply modify the permissions on his/her copy. This is commonly known as **piracy**. (This is also a problem with programmers who have direct access to the cache that their client keeps; in this case, the only thing that needs to be done to enable piracy is for the user to actually see a texture/animation/in-world object. This does NOT allow scripts to be copied, though, since the script is only interpreted on the server and is never sent for interpretation by the client.)

This situation is the kernel of the belief that open grids are hopeless for a virtual-goods economy. DRM discussion aside, maybe they are hopeless. But then, everyone thought the web was hopeless for selling music, and look at the success of iTunes in spite of all the piracy that still exists out there. Who will be the equivalent of iTunes for virtual hair, skin and clothes?

Retrieved from " [http://opensimulator.org/index.php?title=Hypergrid_Security&oldid=54871](http://opensimulator.org/index.php?title=Hypergrid_Security&oldid=54871)"

[Category](http://opensimulator.org/wiki/Special:Categories):

[Hypergrid](http://opensimulator.org/wiki/Category:Hypergrid) 

Personal tools

[Log in / create account](http://opensimulator.org/index.php?title=Special:UserLogin&returnto=Hypergrid+Security)

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

[What links here](http://opensimulator.org/wiki/Special:WhatLinksHere/Hypergrid_Security)

[Related changes](http://opensimulator.org/wiki/Special:RecentChangesLinked/Hypergrid_Security)

[Special pages](http://opensimulator.org/wiki/Special:SpecialPages)

[Printable version](http://opensimulator.org/index.php?title=Hypergrid_Security&printable=yes)

[Permanent link](http://opensimulator.org/index.php?title=Hypergrid_Security&oldid=54871)

This page was last modified on 8 April 2025, at 13:43.

This page has been accessed 53,239 times.

Content is available under [Attribution-Share Alike 2.5](http://creativecommons.org/licenses/by-sa/2.5/) unless otherwise noted.

[Privacy policy](http://opensimulator.org/wiki/OpenSimulator:Privacy_policy)

[About OpenSimulator](http://opensimulator.org/wiki/OpenSimulator:About)

[Disclaimers](http://opensimulator.org/wiki/OpenSimulator:General_disclaimer)