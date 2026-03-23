# UV Mapping Tutorial II

printable version In this tutorial I am going to walk you through the process of laying out the UV's and texturing a craps table. Yes this is a follow-up to our previous tutorial where we textured a simple and high resolution die. I thought it would be appropriate to link the tutorials so you can use them together in a scene. 
  This tutorial will be directed more as a step by step process of laying out the UV's of our craps table. This is by no means the only way to do this, but just like everything else in Maya there are hundreds of ways to do the same thing. I am going to use different tools and toolsets to do this to give you a well rounded experience with the different tools you have available to you. In future projects you will be able to use what you learn here and adapt it for what you need.   So PAY ATTENTION to what you are doing! Don't just follow it step by step and then forget what you have done.It will help in the future, I promise.    So, we have received our model from the modeler. How do we go about texturing it? Well, the first step should be gathering reference. Whether that is photos, diagrams, the actual object, the more you can get the better. Unfortunately we don't have a craps table, so we will have to resort to Google for the images. 
  Here are some for you to familiarize yourself with them.   So, looking at these images we can get a descent idea of how things need to be laid out. We are going to need a material for the felt table, a light reddish wood material for the main outer and inner rim of the table, a leather texture and a darker wood texture for the underside and the legs.   Our goal here is not to re-create this specific craps table, but using it as a guide we can get a good idea of how to texture our table to look good. 
  For this tutorial we have some milestones we need to hit in order to call this project complete. 
  Here they are: 


Acquire our model

Layout our models UV's while assigning texture maps.

Render our final textured model.

 Lets get started shall we! 
  First we need to Acquire our model. 


1. Download [crapsTable.zip](https://swardson.com/crapsTable.zip) and save it to your maya projects directory

2. Unzip/Extract the crapsTable.zip file so that you have the crapsTable project folder in your maya projects directory.

3. Open maya and go to file> Project> Set

Navigate to your maya projects directory and choose the crapsTable project.

4. Go to file>Open Scene and choose the crapsTable.ma file

5. Once the file is opened you should see the craps table model sitting on the grid. See image below.

Take this time to familiarize yourself with the model. Rotate around it, zoom in, select the various objects in the scene and check out the topology.   Open the outliner and see what things are named.   Notice the layers on the bottom right, turn them on and off to see how its laid out. 
  Everything is laid out and named and split apart to make the texturing process easier. Any good modeler will do this for you, however, you may get a solid model and have to split it up yourself. Taking a look at your reference imagery you may want to split your model up your model so the areas with different textures are separate. 

Next take a look at the UV's for the model. (Select the top level group, and open the UV Texture editor). 


Yuuuuuuuuuuucccccckkkkkkk!!!!! 
  I know what you are thinking. This is horrible!   Now do you believe me when I told you that the UV's can get nasty when you have been just focusing on modeling your object?

 Milestone 'A' has been reached! We have our model. Let's recap and see what we need to do next. 

Acquire our model

Layout our models UV's while assigning texture maps.

Render our final textured model.

 Milestone B is to Layout our models UV's so that we can go about texturing this thing in a successful manner.  

6. Just as with everything in maya we want to focus on 1 thing at a time. If we look at the whole picture it is virtually impossible to get anything done in a productive manner. We want to layout the UV's for our craps table so keeping with this trend will will take things 1 step at a time by starting with the playing board. 


7. Turn of all of the display layers except for the "playingBoard" layer (see left image).   This will leave the playing board displayed in the persp view (see right image). 


At this point you will want to select this piece of the model and take a look at it alone. Notice the topology and the layout. Specifically notice the small ridge we have going around the whole model. It is always good practice to take notice of what you are working on and start thinking about how you are going to work out what you need to. 
  Lets start laying out our UV's

8. Make the playingTable model is selected and go to the Create UV's > Planer Mapping > [] options menu.   We are going to map our UV's in a planer fashion (think orthographic camera) to the bounding box (will align itself with the width and depth of the model) along the Y-axis (straight down).   9. Make sure your settings match mine in the image above. Then hit the Project button. 

10. Go to your perspective view and take notice of the new manipulator that is displayed above your playingTable model. Also take notice of the options in the channel box. (see images below) 


In the left image we now have our planer projection manipulator active If you accidentally loose this manipulator it can be accessed by choosing the polyPlanerProj1 node in the inputs section of the channel box for the selected object and then choosing the show manipulator tool in the maya toolbar.   To illustrate what's going on here we will want to be looking at both our perspective view and our UV Texture editor.   11. First close your UV Texture editor. Then In your perspective view panel go to the panels menu and choose saved layouts from the drop down,   then choose Persp/UV Texture Editor. This will open the Perspective view in the left panel and the UV Texture editor in the right panel. Split side by side. 
  Notice now that the object looks much better in our UV texture editor. While its better it is not quite where we need it. Thinking about our craps table and our texture map for the playingTable surface we need to adjust the layout of our UV's so that it works how we want. Here is the texture map we will be assigning. 
  Here is our texture map for our playingTable Surface. Notice the orientation of it is horizontal and rectangular. Our current UV layout has the table in a vertical orientation and stretched to a square format. After some simple tweaking we should be able to lay things out correctly. 
  12. First lets actually apply our texture map to the surface, so we know where to align our UV's to make it look right. 
  13. Right click on your object and drop down to Assign New Material. Then Choose Lambert for the material. 
  14. Your attribute Editor should open with the new lambert material. Rename it to playingTableShader and click the checker box next to the color channel. 
  15. Choose File Texture from the menu. 
  16. In the Attribute editor for the file texture click the folder icon next to the image name field. 
  17. If you have your project set correctly you should see a list of texture maps to choose from. Choose the feltTable.jpg file. 
  If you are in texturing mode (6 on the keyboard) you should see your file texture appear on your model both in the perspective view and in the UV Texture editor. It doesn't look correct yet, but we are getting closer and now we have a guide for how to align our UV's to make this part look right. (see image below) 
  18. Select the object and go into the UV texture editor panel. Make sure you can see your channel box. 
  19. In the channel box under the Inputs section click the PolyPlanerProj1 node. This will bring up a series of attributes to adjust. 
  20. Adjust your settings to match the ones in the image below. 
  Your UV Texture editor should now look something like the following: 
  And your perspective view should look something like this: 
  Ok, so we have successfully UV mapped and textured our felt playingTable portion of our craps table model. Good Job! Now we will move on to each of the other pieces of our model and layout their UV's and apply our textures one by one until we are complete. 
  On the road again.... dah dah de de dah.... on the road again!!! 


21. Turn off the playingBoard display layer and turn on the outerWood display layer. 
  22. We are going to be laying out the UV's for and texturing the right and left Ridge pieces. (see below) 
  23. Since both of these pieces are identical to one another (just mirrored) we will layout the UV's for one of them and then replace the other one with the new one. :) Don't worry Ill show you how to do that. We are going to be working on the rightRidge piece. Check the name if you are unsure which is which. 
  24. So this object is a little more complicated (by a little I mean a lot) than our playingTable model we just textured. This object has a many different facing directions, some are linear, some are bent. We have a small ridge running around the side. What are we to do???? 


 Now is a good time to explore a different way to map the UV's aside from the planer mapping technique we have used thus far. AUTOMATIC MAPPING!!!!!!! 
  Automatic mapping may seem like a really nice way to let maya do all the work for you. While this seems extremely appealing and you might be thinking why would I use anything else? Think again!!!!!!! it is often good practice to never let my do anything automatic for you.... Ever!.... because maya has no idea of the art you are trying to create, she only knows what's easy for her. Not good. Before using the automatic mapping function you need to think about your model and decide if it is appropriate.   For our model we need a generic light wood texture on all the various parts of this object. We need it to be linear on the top faces, side faces and the ridge. We don't want stretching or overlapping or pinching. BUT!!!! we don't have to actually have anything specifically placed on this object. By that I mean we don't have any logos, designs, elements that need to show up on a specific area of this object. It just needs to be wood. In this cause Automatic mapping is a descent candidate to layout the UV's for this object. 
 However, we cannot just use the default values for the automatic mapping, this will undoubtedly give us results that are unwanted and nasty. As with everything, different settings will give you sometimes drastically different results.   Lucky for you, I already figured out the best settings for this object. It's ok, you can say it... I Rock!!! ;) 


25. Select the rightRidge object. 
  26. Go to the Create UV's menu and choose Automatic Mapping > [] options box. 
  27. Adjust your settings to match the image below. 
  28. Hit the Project button once you have changed your settings. 
  29. Your UV persp view and UV Texture Editor should now look something like this: 
  Notice in the UV Texture Editor that maya did a descent job of separating out the different sections of the model from one another. We have the outer bent walls separate from the top planer pieces etc. All we have to do now is to optimize the UV space used and move these sections (or shells as they are called) around in the UV space to have a better layout. 
  30. In the UV texture editor select the UV's like the following image. 
  31. And move them to positioned like the following image: 
  32. Next select the following UV's (left image) and move them to be placed like those in the right image. 
  33. Then select the following UV's (left image) and move them to be placed like those in the right image. 
  34. Select the following UV's (left image). MOVE and SCALE them to be placed like those in the right image. 
  35. Finally, SCALE and MOVE all of the UV's to fill the quadrant #2 UV space. (see image below) 
  We now have our UV's nicely laid out for this object. Now lets apply our wood texture map to the model to see how it looks. 
  36. Go into your perspective view and make sure you are in OBJECT MODE and select the rightRidge object. 
  37. Right click on it and choose assign new shader > blinn. 
  38. Rename this shader darkRedWood and attach a file texture node to the color channel. 
  39. In the attribute editor for the file texture node, click the folder icon and choose the file deepRedWood.jpg 


If you are in texturing mode (6 on the keyboard) you should see the wood texture applied nicely to the rightRidge object. Cool huh?! 
  Now for the leftRidge object (since they are identical and only mirrored) we will replace it with a copy of our rightRidge model (so we don't have to do the UV layout process to the leftRidge object as well). 
  40. Select the leftRidge object and delete it. 
  41. Select the rightRidge object and duplicate it. 
  42. In the channel box for the new ridge (rightRidge1) rename it to leftRidge and set the scale in Z to negative 1. 
  43. Then freeze the objects transformations by going to Modify/Freeze Transformations. 
  There you go, leftRidge is now done. How awesome is that?!! 
  Now for the base piece 
  You may notice that this looks a lot like the playingTable object that we laid out earlier. It is in fact a lot like it. However, rather than having to apply a texture that needs specific placement (like the feltTable texture we used before) we can just use a simple planer mapping technique to layout the UV's for this piece. 
  44. with the object selected go to the Create UV's menu and choose Planer Mapping > [] options. 
  45. Make your settings look like the ones in the image below: 
  46. Hit Project. 
  47. Now make sure you are in object mode and your base object is selected. 
  48. right click on the object and choose Assign Existing Material. 
  49. Then choose darkRedWood from the list. (this will assign the same dark red wood shader we have attached to the left and right ridge objects to the base. 
  All we have left to UV layout in this layer is the outerWood Rim Piece 
  This one is going to be a bit trickier but Ill walk you through each step to make it happen. (as if I haven't done that already hahaha) 
  50. go into component mode (faces) and select the following faces: 
  51. Planer map these selected faces with the following options: 
  52. convert your face selection to UV's (control + F12) 
  53. In the UV Texture editor scale the selected UV's in the left image, to look like the right image. 
  54. Now go back to the perspective view, go into object mode, select your object again, then go into component mode (faces) and select the following faces. 
  55. Planer map this piece the same way we did the last one. 
  56. Convert the selection to UV's (control + F12) and move and scale them to go from the way they look in the left image, to the way they look in the right image. 
  57. Go back into the perspective view and get into component mode (faces) and select the following faces. 
  58. Go to the Create UV's menu and choose Cylindrical Mapping.

59. You should get something like the following. 
  Our projection is coming in from the right of this section of the model. we need it to be coming in from the left. 
  60. In the channel box under the inputs selection make sure the polyCylProj1 node is selected and you can see its attributes. 
  61. Adjust yours to match mine. 
  62. Convert your selection to UV's (control + F12) and go into the UV Texture Editor. 
  63. Move and Scale your UV's to go from the image on the left to look like that on the right. 
  64. Go back into the perspective view and go into component mode (faces) and select the following faces. 
  65. Cylindrical Map these faces. 
  66. Convert your selection to UV's (control + F12) and go into the UV Texture Editor.

67. Move and scale these final UV's to go from the left image to look like that of the right image. 
  Now we have all of the UV's flayed out for this object. You may be wondering why we did this in 4 chunks. Well, when you have an elongated surface like this (one that gets wrapped around) You run into stretching and sizing issues when you just cylindrical map the entire thing at once. Since this object is again just a series of wood panels, having some seams will be ok. So by planer mapping the 2 flat edges and 180 degree cylindrical mapping the 2 half circle edges we can layout our UV's much easier, with little to no stretching and utilize more of the texture space. Its a Win, Win, Win .... um Win situation... Moving on. 
  This final piece of the outerWood layer has a golden wood material rather than the darkRedWood shader we have been using. So......... 
  68. Go into the perspective view and into object mode, then select the outerWoodRim object. 
  69. Right click on it and choose assign new material > blinn. 
  70. Name this shader goldWood and attach a file texture node to the color channel. 
  71. Click the folder icon and choose the goldOak.jpg file. 
  If you are in texturing mode your model should now look like the following. 


 That is it for the objects in our outer wood layer. Lets move on to the next one. 
  72. Turn off the outerWood display layer and turn on the innerWood display layer. You should see the following: 
  Notice how this object has a very similiar layout to that of the previous "outerRim" object we just textured. I is not a coincidence and yes we will be using the same methods to lay out the UV's and texture it as we did before. Rather than me walking you through it step by step I will simply lay out the global steps by which you will do it and if you need further assistance, please refer to steps 50 - 72. 
  73. Planer map the following selected faces (left image) and lay them out in the UV Texture editor to look like the right image. 
  74. Planer map the following selected faces (left image) and lay them out in the UV Texture editor to look like the right image. 
  75. Cylindrical map the following selected faces (left image) and lay them out in the UV Texture editor to look like the right image. 
  76. Cylindrical map the following selected faces (left image) and lay them out in the UV Texture editor to look like the right image. 
  77. Now go back into object mode for the innerWood object and apply the goldWood shader to it. right click > assign exsisting material > goldWood. Your perspective view should look like the image below. 
  78. Turn off the innerWood display layer and turn on the woodRails layer. (your perspective view should look like the image below. 


Since these objects are fairly complex in their makeup we are going to go ahead and use the automatic mapping again for these. Actually the settings we used for the left and right ridge pieces earlier will work fine for these objects as well. This is going to be easy! 
  79. Select the longer piece and go to Create UV's > Automatic Mapping. 
  80. Deselect all objects, go back into object mode and re-select the longer piece. Assign the goldWood Shader to this object. 
  81. Select the shorter piece and go to Create UV's > Automatic Mapping. 
  82. Deselect all objects, go back into object mode and re-select the shorter piece. Assign the gold Wood Shader to this object. 
  That's it! Your perspective view should now look like the following: 
  Nice eh! 

Neeeeeeexxxxxxtttttt 
  Turn off the woodRails layer and turn on the chipSets layer. Your perspective view should now look like the following: 
  These are an interesting object set because the one on the right is an instanced duplication of the one on the left. You should remember this concept from the dragon tutorial we started the semester with, as well as any projects you worked on in the beginning class. As with those exercises we did before anything we do to the shape node of one object, the exact same thing will happen to its instances. Therefore, if we layout the UV's on one of these guys, the other will be done simultaneously. Cool, 2 for the price of 1. Lets get going. 
  83. select the one on the left (rightChipSet) and go to Create UV's > Planer mapping > [] options. 
  84. Make sure Bounding Box and Y Axis are checked and hit project. 
  Your perspective view should now look like the following: 
  Notice how the chipSet on the right has an orange border around it like the one on the left. This indicates that the UV's were flayed out for both at the same time. Go into your UV Texture editor and see for yourself if you don't believe me. :) 
  85. Now assign the goldWood shader to both of these objects and we are done with our chipsets. 
  86. Turn off the chipSets layer and turn on the legs layer. 
  87. Select the rightLeg object 
  88. Automatically Map the UV's for this object.

89. Assign the darkRedWood shader to it. 
  90. Select the other leg and do the same thing. 
  You will end up with something like this: 
  91. Turn off the legs layer and turn on the mirrorRim layer. 
  Since this object isn't going to have a texture map applied (its a mirror surface) so it will simply have a procedural highly reflective blinn shader attached, we don't need to be too concerned about the UV's. However, we still should lay them out to ensure we don't get any weird artifacts at render time. 
  92. select the mirrorRim object and automatically map the UV's 
  93. Then assign a new blinn shader to the object.   94. Rename the shader to mirrorShader.

95. Turn the color, specular color and reflective color up to white. 
  96. Turn the reflectivity up to 1. 
  That is it for this bad boy: 
  97. Turn off the mirrorRim layer and turn on the paddedRails layer. 
  Just like with our chipSets the one on the right is an instance of the one on the left. So everything we do to 1 will happen to the other.   98. Select the rightLeatherBumper object. 
  99. Go to Create UV's > Spherical Map 
  100. Adjust the settings in the channel box for polySphProj1 to match the following: 
  101. Attach a new blinn shader to these objects and rename it to leather shader. 
  102. Attach a file texture node to the color channel and choose the leather.jpg image file. 
  If you are in texturing mode Your perspective window should now look something like this: 
  Now, if I am not mistaken, I believe that is all of our pieces. Phheeeewww, that was a lot of work. But its worth it when you are done. Go ahead and turn on all of your display layers to see your fully flayed out and textured model in action. 
  Cool huh?! I think so... 
  Lets take a look at our milestones, shall we. 


 For this tutorial we have some milestones we need to hit in order to call this project complete. 
  Here they are: 


Acquire our model 

Layout our models UV's while assigning texture maps.

Render our final textured model. 
  Lets throw some interesting lighting in there and render ourselves an image. Feel free to include your dice in the render as well. :) 


And here it is............................... 


Acquire our model 

Layout our models UV's while assigning texture maps.

Render our final textured model. 
  Nice work, you now have completed textured a highly complex model. Hopefully you have learned a lot about texturing and model layout and can utilize these techniques in your own projects later on. 
  Tah! 
