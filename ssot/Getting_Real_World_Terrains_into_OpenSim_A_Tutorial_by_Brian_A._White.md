# Getting Real World Terrains into OpenSim: A Tutorial by Brian A. White

Getting Real World Terrains into OpenSim: A Tutorial by Brian A. White | Be Cunning and Full of Tricks

[Skip to primary content](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#content)

# [Be Cunning and Full of Tricks](https://becunningandfulloftricks.com/)

## Exploring Knowledge Management, Online Communities and Virtual Worlds

Search Search

### Main menu

[Home](https://becunningandfulloftricks.com/)

[About Me and This Blog](https://becunningandfulloftricks.com/about/)

[Hypergrid Safari](https://becunningandfulloftricks.com/2014/07/29/hypergrid-safari-the-evolution-of-exploration-across-the-interconnected-metaverse/)

[My Opensim Grid – Pathlandia](https://becunningandfulloftricks.com/2012/01/09/my-diva-standalone-opensim-grid-pathlandia/)

### Post navigation

[← Previous](https://becunningandfulloftricks.com/2013/09/09/oscc13/) [Next →](https://becunningandfulloftricks.com/2013/09/17/theres-no-humor-like-math-humor/)

# Getting Real World Terrains into OpenSim: A Tutorial by Brian A. White

Posted on [September 14, 2013](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/) by [John "Pathfinder" Lester](https://becunningandfulloftricks.com/author/becunningandfulloftricks/)

**This is recreation of a blog post** by [Brian A. White](http://web.archive.org/web/20120629200309/http://www.virtualwhite.com/?page_id=2). Brian's blog went offline sometime in 2009, and recently [it was suggested that someone republish this useful tutorial](http://lists.berlios.de/pipermail/opensim-users/2013-September/012592.html) to make sure it can be found by search engines and does not someday completely vanish from the Internet. So here it is.

Some of the links in this article are dead and not available in any existing archives. I've left those in but ~~crossed them out.~~ Fortunately these dead links are not critical to the tutorial, and I was able to update the other links that have changed since this article was written. Brian, wherever you are, thank you again for writing this and I hope you are well.

[-John “Pathfinder” Lester](http://about.me/pathfinder)

# Tutorial: Getting Real World Terrains into OpenSim

by [Brian A. White](http://web.archive.org/web/20120629200309/http://www.virtualwhite.com/?page_id=2) – September 9, 2008

I named my first OpenSim region Orcas after a [real world island](http://maps.google.com/maps?f=q&hl=en&geocode=&q=orcas+island&sll=37.0625,-95.677068&sspn=63.647969,112.851563&ie=UTF8&ll=48.592959,-122.858734&spn=0.423268,0.881653&z=10&iwloc=addr). I decided to try and see if I could get the actual Orcas Island terrain into OpenSim to see how it looked and uncover any challanges one might face in bringing RL terrain into OpenSim. This tutorial will walk you through the process I followed and and various software packages required to make this happen (done on Windows). The net, net is I succeeded, but the results were uninspiring.

My thanks to ~~[Petrolia](http://petrolia.pip.verisignlabs.com/)~~ and ~~[this tutorial](http://www.wooblelab.com/command/show/67-3d-height-map-from-usgs)~~ which got me started.

[UPDATE: See Darb Dabney's excellent follow-up post [here](http://blog.simgis.com/2008/09/11/usgs-terrain-in-opensim-a-gis-approach/) which shows how to do this more accurately. He completes a usable Orcas island with 54 OpenSim regions at proper scale! Great work Darb love it!]

**Step 1 – Find Some Terrain**

The US government maintains a great site which while a bit cryptic contains tons of data. Point your web browser here: [http://nationalmap.gov/viewer.html](http://nationalmap.gov/viewer.html). Navigate to “View & Download United States Data”. Make sure to enable pop-ups you'll need them. Google maps it is not, but use the zoom and navigation controls to find a piece of terrain you want to put into OpenSim.

USGS Seamless Server

**Step 2 – Select/Deselect Display Options**

On the right hand side, there is a display panel with several drop downs. Deselect everything (a bit painful) and select “NED Shaded Relief (1/3 arc second)” This relates to the level of detail in the data. 1/3 is the more detailed than the 1 arc sec, but less than 1/9. 1/3 creates fairly large download and you may be able to get by with 1 arc second since this all goes down to 256×256 pixels.

1/3 arc second Elevation Selection

**Step 3 – Select Download Area**

On the right hand side of the display select the “Define Rectangular Download Area” and then drag a selection around the terrain you want to use. The process I describe in this tutorial fits what you select into a square image so the closer to square you select the less distortion you will encounter. Once you finish your selection a pop-up will come up summarizing your request.

**Step 4 – Modify the Data Request**

You want to get a .BIL formatted file, so click at the top of the request summary page on “Modify Data Request”. It looks like a column header but it is a link.

Modify Data RequestScroll down to the 1 selected download size and change from ArcGRID to BIL Change Download Type to .BIL

Now scroll all the way to the bottom and select Save Changes.

Save Changes

Your download should start, although you may have issues as I did with pop-up blocking settings.

**Step 5 – Download and Install MicroDEM (free)**

You now have raw terrain data in a .BIL file. To work with this, you need to convert it from BIL to a height map which is basically a greyscale image where 0 (black) represents the lowest point in the terrain and 255 (white) represents the highest point. The MicroDEM software lets you do this.

Download and install from here:

[http://www.usna.edu/Users/oceano/pguth/website/microdem/microdemdown.htm](http://www.usna.edu/Users/oceano/pguth/website/microdem/microdemdown.htm)

**Step 6 – Open .BIL and Change to Grayscale**

File -> Open DEM (select the .BIL file from your download)

I Needed to create “images” directory under c:\mapdata to get the save BMP to work.

Modify->Elevation->Grayscale

Modify->Grid->Neither

Remove Legend Overlays by right clicking on the image and selecting “Legends/marginalia”

Legends Context Menu

You'll see a dialog like this, deselect all the check boxes and click on “redraw map”.

Remove Legends

Save it to a .BMP with

File->Save

**Step 7 – Crop/Scale in Your Favorite Image Editor**

You now need to scale/crop the image down to 256×256 pixels. For this one I used the freely available GIMP, but Photoshop works well too.

The Gimp

Orcas Sized and Scaled

**Step 12 – Load into OpenSim**

You load the terrain into OpenSim from the OpenSim console with ”terrain load /path/to/file.png”. For SecondLife you can upload a .raw file from the estate tools, but this does not seem to be implemented yet in OpenSim. Converting from a heightmap to an SL raw file is a whole 'nother topic.

My first pass ended up with a very craggy landscape. The black turned into the floor of the sea with steep rises. In short, the terrain scale I picked was far to large for a single region. [I also learned later that you really cannot use the full range of black to white or you will get pretty unusable terrains.]

Craggy from Ground Level

I lowered the water level to zero to get a better perspective and took the following shot from above.

Aerial View With 0 Water Level

**Step 13 – Make Adjustments, Rinse and Repeat**

To get a smoother look, I used Gaussian blur filter in Photoshop and reloaded for the final results. [Reducing the contrast would have helped as well].

Terrain Smoothed with Gaussian Blur

Aerial View of Orcas

At the end of the day, this was not really what I was hoping for. It is not recognizable as Orcas and it is not very practical landscape for an SL Sim.

Here is another post [~~from Emma Nowhere~~](http://emmanowhere.blogspot.com/2007/03/when-i-first-terraformed-nowhere-sim-i.html) which offers more software packages for terraforming OpenSim/SL terrains.

**End of Tutorial**

### Share this:

[Share on X (Opens in new window) X](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?share=twitter&nb=1)

[Share on LinkedIn (Opens in new window) LinkedIn](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?share=linkedin&nb=1)

[Share on Facebook (Opens in new window) Facebook](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?share=facebook&nb=1)

[Share on Pinterest (Opens in new window) Pinterest](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?share=pinterest&nb=1)

[Share on Tumblr (Opens in new window) Tumblr](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?share=tumblr&nb=1)

Like Loading...

### Related

[A Virtual World in my Hands: Running OpenSim and Imprudence on a USB Key](https://becunningandfulloftricks.com/2010/10/07/a-virtual-world-in-my-hands-running-opensim-and-imprudence-on-a-usb-key/) October 7, 2010 In "Education"

[The next 4 meetings of the Hypergrid Adventurers Club will be hosted by Vanish Seriath](https://becunningandfulloftricks.com/2011/01/10/the-next-3-meetings-of-the-hypergrid-adventurers-club-will-be-hosted-by-vanish-seriath/) January 10, 2011 In "Announcements"

[Need a great terrain for your Opensim on a USB key? Here's where to find one and how to set it up.](https://becunningandfulloftricks.com/2010/10/12/need-a-great-terrain-for-your-opensim-on-a-usb-key-here-you-go/) October 12, 2010 In "OpenSim"

This entry was posted in [Announcements](https://becunningandfulloftricks.com/category/announcements/), [Education](https://becunningandfulloftricks.com/category/education-2/), [OpenSim](https://becunningandfulloftricks.com/category/opensim/) and tagged [education](https://becunningandfulloftricks.com/tag/education/), [metaverse](https://becunningandfulloftricks.com/tag/metaverse/), [OpenSim](https://becunningandfulloftricks.com/tag/opensim/), [opensimulator](https://becunningandfulloftricks.com/tag/opensimulator/), [tutorial](https://becunningandfulloftricks.com/tag/tutorial/), [virtual worlds](https://becunningandfulloftricks.com/tag/virtual-worlds-2/) by [John "Pathfinder" Lester](https://becunningandfulloftricks.com/author/becunningandfulloftricks/). Bookmark the [permalink](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/).

## 9 thoughts on “ Getting Real World Terrains into OpenSim: A Tutorial by Brian A. White”

 [Eric Hackathorn](https://www.facebook.com/hackshaven) on [September 14, 2013 at 11:58 am](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#comment-4348) said: You might have better luck spreading the terrain across multiple regions. Alternatively, you could grab the free version of World Machine and manipulate the raw data into something more intended for a virtual environment. Awhile back I wrote up a Unity-focused tutorial: [http://fragileearthstudios.com/2012/09/15/generating-complex-terrains/](http://fragileearthstudios.com/2012/09/15/generating-complex-terrains/) However, this could be adapted for OpenSim by using their “file input device.” [http://www.world-machine.com/learn.php?page=devref#FILI](http://www.world-machine.com/learn.php?page=devref#FILI) [Reply ↓](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?replytocom=4348#respond)

 [John "Pathfinder" Lester](https://becunningandfulloftricks.wordpress.com/) on [September 14, 2013 at 12:02 pm](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#comment-4349) said: Great tutorial, Eric! I know lots of folks (like myself) spend time exploring both Unity and OpenSim, so this is very useful. Thanks so much for sharing it. [Reply ↓](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?replytocom=4349#respond)

 [Eric Hackathorn](https://www.facebook.com/hackshaven) on [September 14, 2013 at 12:16 pm](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#comment-4350) said: If you think there is interest I could probably gin up a tutorial to create something like this: [http://www.flickr.com/photos/hackshaven/7563722762/](http://www.flickr.com/photos/hackshaven/7563722762/) It's 64 regions worth of terrain data and satellite photos. We use this in Unity for volumetric cloud rendering. [http://vimeo.com/72900735#t=2m39s](http://vimeo.com/72900735#t=2m39s) I should probably know this, but does OpenSim allow you to apply a texture across the entire region's terrain?

 [John "Pathfinder" Lester](https://becunningandfulloftricks.wordpress.com/) on [September 14, 2013 at 1:34 pm](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#comment-4351) said: Holy cow, that image is amazing. Yes, please! I think a tutorial on how you created that would be incredibly useful to many people using both Unity and OpenSim. As for how terrain texturing works in Opensim, I believe it works just the same as it does in Second Life. That is, it's really limited and basically sucks. 😛 Perhaps an OpenSim dev someday will move beyond feature parity with SL's terrain texturing options and give Opensim folks some of the powerful terrain texturing flexibility you see in platforms like Unity…

 [Fleep Tuque](http://gravatar.com/fleeep) on [September 14, 2013 at 4:00 pm](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#comment-4354) said: Thanks Path and Eric for the links! Terrain editing in Opensim by hand was very painful until some recent fixes, but it's still pretty limited for recreating RL locations, so these tutorials are super helpful. I'd also be interested in tutorials for Unity and other platforms where you find them, we do a lot of work in multiple worlds! 🙂 [Reply ↓](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?replytocom=4354#respond)

 Fleep Tuque on [September 15, 2013 at 9:16 am](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#comment-4367) said: As an update, in order to follow this tutorial, I actually had to get the map data from this link: [http://www.mrlc.gov/viewerjs/](http://www.mrlc.gov/viewerjs/) And followed the directions at this link to download the data in .BIL format: [http://www.pathloss.com/pwiki/index.php?title=MRLC](http://www.pathloss.com/pwiki/index.php?title=MRLC) So far the rest of the instructions seem to be the same.. [Reply ↓](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?replytocom=4367#respond)

 [John "Pathfinder" Lester](https://becunningandfulloftricks.wordpress.com/) on [September 15, 2013 at 10:13 am](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#comment-4370) said: Thanks Fleep. I'll update the tutorial with those links. [Reply ↓](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?replytocom=4370#respond)

Pingback: [What I'm Reading on 02/23/2014 | Blog | Bob Sutor](http://www.sutor.com/c/2014/02/what-im-reading-on-02232014/)

 [GiMiSa](http://profil.gimisa.ca/) on [May 15, 2014 at 8:21 am](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#comment-8773) said: Hi not sure it would be of interest to you in this post . If not please disregard. About the time you wrote this post I was also playing with RL terrain using USGL database for opensim application. But I use a different approach by creating a MESH terrain instead of applying the texture to the terrain map tool. The intent was to create a tutorial on how to proceed in this way. I created two real terrain map using this method for two of my friends in OSgrid. ( they could be reloaded if you want to experiment with them ). The advantage of MESH terrain is scaling as the mesh size is not limited to 256×256 so rendering a much more detail terrain is possible in a region size. Also an other advantage is that it can be textured with google satellite maps given the proper fit between USGL projection and GOOGLE MAP proprietary one. ( the Technic to do that was a pain to find) Unfortunately there is also a few disadvantageous effect on opensim to use this idea. One of this non important problem is physic. As discussed with Robert Adam father of bullet physic for opensim the mesh physic apply to a large build like a region mesh is not detail enough to follow the landscape properly. The physic box does not allow for the terrain detail. In the case of mesh terrain, the avatar walking over the landscape seem to fly over valleys in a peculiar way. The other disadvantage is the texturing limits applied to opensim. I have tried several work around among which dividing the mesh and using multiple material. The 1MB texture limit cannot provide a detail rendering or the terrain. Prixelisation of the terrain texture as seen from an avatar walking very near (2m) the surface is a killer for this idea. Hope this comment help develop the idea as simulation over real terrain would be of great interest for training or education. With fun in mind… GiMiSa [Reply ↓](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/?replytocom=8773#respond)

### Leave a comment [Cancel reply](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#respond)

Write a comment...

Log in or provide your name and email to leave a comment. [-]

Email me new posts [x] instantly

Instantly [-] daily Daily [-] weekly Weekly [-]

Email me new comments [-]

Save my name, email, and website in this browser for the next time I comment.

Comment

Δ

### Tags

["live music"](https://becunningandfulloftricks.com/tag/live-music/)

[animals](https://becunningandfulloftricks.com/tag/animals/)

[animation](https://becunningandfulloftricks.com/tag/animation/)

[architecture](https://becunningandfulloftricks.com/tag/architecture/)

[art](https://becunningandfulloftricks.com/tag/art-2/)

[artificial intelligence](https://becunningandfulloftricks.com/tag/artificial-intelligence-2/)

[artificial life](https://becunningandfulloftricks.com/tag/artificial-life/)

[augmented reality](https://becunningandfulloftricks.com/tag/augmented-reality/)

[authentic animal conversations](https://becunningandfulloftricks.com/tag/authentic-animal-conversations-2/)

[avatars](https://becunningandfulloftricks.com/tag/avatars-2/)

[business](https://becunningandfulloftricks.com/tag/business/)

[cake](https://becunningandfulloftricks.com/tag/cake/)

[CERN](https://becunningandfulloftricks.com/tag/cern/)

[conference](https://becunningandfulloftricks.com/tag/conference/)

[convention](https://becunningandfulloftricks.com/tag/convention/)

[dogs](https://becunningandfulloftricks.com/tag/dogs/)

[education](https://becunningandfulloftricks.com/tag/education/)

[empathy](https://becunningandfulloftricks.com/tag/empathy/)

[environmental education](https://becunningandfulloftricks.com/tag/environmental-education/)

[finland](https://becunningandfulloftricks.com/tag/finland/)

[francogrid](https://becunningandfulloftricks.com/tag/francogrid/)

[games](https://becunningandfulloftricks.com/tag/games/)

[gaming](https://becunningandfulloftricks.com/tag/gaming/)

[german](https://becunningandfulloftricks.com/tag/german/)

[health](https://becunningandfulloftricks.com/tag/health/)

[healthcare](https://becunningandfulloftricks.com/tag/healthcare/)

[howard phillips lovecraft](https://becunningandfulloftricks.com/tag/howard-phillips-lovecraft/)

[human nature](https://becunningandfulloftricks.com/tag/human-nature/)

[humor](https://becunningandfulloftricks.com/tag/humor/)

[HyperGate](https://becunningandfulloftricks.com/tag/hypergate/)

[HyperGrid](https://becunningandfulloftricks.com/tag/hypergrid/)

[Hypergrid Adventurers Club](https://becunningandfulloftricks.com/tag/hypergrid-adventurers-club/)

[Hypergrid Safari](https://becunningandfulloftricks.com/tag/hypergrid-safari/)

[immersive education](https://becunningandfulloftricks.com/tag/immersive-education/)

[innovation](https://becunningandfulloftricks.com/tag/innovation/)

[itween](https://becunningandfulloftricks.com/tag/itween/)

[Jibe](https://becunningandfulloftricks.com/tag/jibe/)

[jokaydiagrid](https://becunningandfulloftricks.com/tag/jokaydiagrid/)

[leadership](https://becunningandfulloftricks.com/tag/leadership/)

[learning](https://becunningandfulloftricks.com/tag/learning/)

[library](https://becunningandfulloftricks.com/tag/library/)

[life](https://becunningandfulloftricks.com/tag/life/)

[Linden Lab](https://becunningandfulloftricks.com/tag/linden-lab/)

[metaverse](https://becunningandfulloftricks.com/tag/metaverse/)

[metropolis](https://becunningandfulloftricks.com/tag/metropolis/)

[metropolis metaversum](https://becunningandfulloftricks.com/tag/metropolis-metaversum/)

[movie](https://becunningandfulloftricks.com/tag/movie/)

[mp3](https://becunningandfulloftricks.com/tag/mp3/)

[music](https://becunningandfulloftricks.com/tag/music/)

[online communities](https://becunningandfulloftricks.com/tag/online-communities/)

[OpenSim](https://becunningandfulloftricks.com/tag/opensim/)

[opensimulator](https://becunningandfulloftricks.com/tag/opensimulator/)

[osgrid](https://becunningandfulloftricks.com/tag/osgrid/)

[pathlandia](https://becunningandfulloftricks.com/tag/pathlandia/)

[physics](https://becunningandfulloftricks.com/tag/physics/)

[pioneers](https://becunningandfulloftricks.com/tag/pioneers/)

[psychology](https://becunningandfulloftricks.com/tag/psychology-2/)

[ReactionGrid](https://becunningandfulloftricks.com/tag/reactiongrid/)

[second life](https://becunningandfulloftricks.com/tag/second-life/)

[short stories](https://becunningandfulloftricks.com/tag/short-stories-2/)

[snow crash](https://becunningandfulloftricks.com/tag/snow-crash/)

[social signalling](https://becunningandfulloftricks.com/tag/social-signalling/)

[sociology](https://becunningandfulloftricks.com/tag/sociology/)

[squirrel](https://becunningandfulloftricks.com/tag/squirrel/)

[strategy](https://becunningandfulloftricks.com/tag/strategy/)

[TGIB](https://becunningandfulloftricks.com/tag/tgib/)

[tutorial](https://becunningandfulloftricks.com/tag/tutorial/)

[uncanny valley](https://becunningandfulloftricks.com/tag/uncanny-valley/)

[Unity](https://becunningandfulloftricks.com/tag/unity/)

[Unity3d](https://becunningandfulloftricks.com/tag/unity3d/)

[video](https://becunningandfulloftricks.com/tag/video/)

[virtual reality](https://becunningandfulloftricks.com/tag/virtual-reality/)

[virtual worlds](https://becunningandfulloftricks.com/tag/virtual-worlds-2/)

[wiggle planet](https://becunningandfulloftricks.com/tag/wiggle-planet/)

[wiglets](https://becunningandfulloftricks.com/tag/wiglets/)

### Top Posts & Pages

[Gargoyles, Grotesques & Chimeras: Listening to The Anatomy of Melancholy](https://becunningandfulloftricks.com/2012/12/31/gargoyles-grotesques-chimeras-listening-to-the-anatomy-of-melancholy/)

[My Opensim Grid "Pathlandia"](https://becunningandfulloftricks.com/2012/01/09/my-diva-standalone-opensim-grid-pathlandia/)

[The Metaphor of Portals and how to create Instant Hypergates (aka "Blamgates")](https://becunningandfulloftricks.com/2010/10/29/the-metaphor-of-portals/)

[OpenSimulator Community Conference 2013 - My Presentation and My Thanks to Everyone Involved](https://becunningandfulloftricks.com/2013/09/09/oscc13/)

[Hypergrid Safari - The evolution of exploration across the interconnected Metaverse](https://becunningandfulloftricks.com/2014/07/29/hypergrid-safari-the-evolution-of-exploration-across-the-interconnected-metaverse/)

[My old lighthouse in Second Life](https://becunningandfulloftricks.com/2015/03/27/my-old-lighthouse-in-second-life/)

[Hypergrid Adventurers Club on IRC](https://becunningandfulloftricks.com/2010/12/13/hypergrid-adventurers-club-on-irc/)

[Building Immersion through Simple Design: Visit a Meteor Shower in Jibe](https://becunningandfulloftricks.com/2012/09/28/building-immersion-through-simple-design-visit-a-meteor-shower-in-jibe/)

[The beautiful Dawn Chorus intro to WGBH's "Morning Pro Musica" classical music radio show](https://becunningandfulloftricks.com/2012/11/07/the-beautiful-intro-to-wgbhs-morning-pro-musica-classical-music-radio-show/)

### About Me

[John "Pathfinder" Lester](https://gravatar.com/becunningandfulloftricks)

Cypherpunk Capitalist | Crypto | InfoSec | NFT Communities | Metaverse | Culture | Fashion | Art | Identity

[View Full Profile →](https://gravatar.com/becunningandfulloftricks)

[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)

[Comment](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/#comments)

[Reblog](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/)

[Subscribe](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/) [Subscribed](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/)

[Be Cunning and Full of Tricks](https://becunningandfulloftricks.com/) Join 1,480 other subscribers Sign me up

Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fbecunningandfulloftricks.com%252F2013%252F09%252F14%252Fgetting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white%252F)

[Be Cunning and Full of Tricks](https://becunningandfulloftricks.com/)

[Subscribe](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/) [Subscribed](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/)

[Sign up](https://wordpress.com/start/)

[Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fbecunningandfulloftricks.com%252F2013%252F09%252F14%252Fgetting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white%252F)

[Copy shortlink](https://wp.me/p11U98-1dz)

[Report this content](https://wordpress.com/abuse/?report_url=https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/)

[View post in Reader](https://wordpress.com/reader/blogs/15230494/posts/4685)

[Manage subscriptions](https://subscribe.wordpress.com/)

[Collapse this bar](https://becunningandfulloftricks.com/2013/09/14/getting-real-world-terrains-into-opensim-a-tutorial-by-brian-a-white/)

Loading Comments...

Write a Comment...

Email (Required) Name (Required) Website Post Comment

%d  