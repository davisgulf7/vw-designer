# Optimization techniques for non densely occluded environments (open worlds) - Reddit

Optimization techniques for non densely occluded environments (open worlds) : r/GraphicsProgramming

[Skip to main content](https://www.reddit.com/r/GraphicsProgramming/comments/tpwx8e/optimization_techniques_for_non_densely_occluded/#main-content) Optimization techniques for non densely occluded environments (open worlds) : r/GraphicsProgramming

Open menu

Open navigation 

Go to Reddit Home

r/GraphicsProgramming

TRENDING TODAY

Get App

Get the Reddit app

[Log In](https://www.reddit.com/login/)

Log in to Reddit

Expand user menu

Open settings menu

[Skip to Navigation](https://www.reddit.com/r/GraphicsProgramming/comments/tpwx8e/optimization_techniques_for_non_densely_occluded/#left-sidebar-container) [Skip to Right Sidebar](https://www.reddit.com/r/GraphicsProgramming/comments/tpwx8e/optimization_techniques_for_non_densely_occluded/#right-sidebar-container)

Back

[Go to GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/)

[r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/)

• 4y ago

[deleted]

Locked post

Stickied post

Archived post

View post in other languages

Report

# Optimization techniques for non densely occluded environments (open worlds)

Other than frustum culling and LOD, what techniques are there for efficiently rendering large open world scenes (for example, elder scrolls, breath of the wild) where you may have lots of details to deal with in a large open space? What fundamental papers are there, books, or other resources I can read?

Read more

8

· 2

# Comments Section

[fgennari](https://www.reddit.com/user/fgennari/)

•

[4y ago](https://www.reddit.com/r/GraphicsProgramming/comments/tpwx8e/comment/i2ehxql/)

There are different optimization techniques for terrain, vegetation, buildings, etc. Maybe you want to comment on which of these you're most interested in?

One of the most important optimizations for large worlds is level of detail. Objects close to the player should be drawn with higher polygon counts than objects further away. You would start with the high detail objects, then reduce the vertex counts of terrain tiles, trees, buildings, player models, etc. by merging nearby faces. Objects that are very far can be drawn as player facing billboard quads with images of the object drawn on them. Anything further out than that can be obscured by fog. Objects smaller than a few pixels in size can either be skipped or merged into nearby small objects as low polygon blobs. But you did say "other than LOD." I'm wondering what types of LOD you considered?

There are also opportunities for occlusion culling. Any hill or object near the player can occlude objects behind it. Some open world games like to place strategic occluders around to block long lines of sight with many objects. Occlusion culling can be done on the CPU with ray cast tests or on the GPU with occlusion queries.

Then there's instancing. Many objects such as vegetation and other props are drawn as many instances of a few base meshes that are translated, rotated, and scaled. Hardware instancing can be used to get a good speedup to rendering.

Then there's the implementation of view frustum culling and distance culling. If you have a large number of objects, you need to put them in a hierarchical data structure so that you can efficiently query the nearby and visible objects. You can use a tree or some type of 2D grid of tiles/blocks.

Finally, you want to optimize the number of draw calls. Rather than making a draw call for each object, they can be batched together into multidraw calls, drawn with instancing, etc. In general you want to combine models that use the same materials/textures and are generally drawn together. For example, all of the decorations made of wood can be a single draw call.

All of this is how I was able to place 18,000 buildings and draw them with a view distance of several miles in my procedural cities project. My blog is here, in case you want some ideas for how to do this: [https://3dworldgen.blogspot.com](https://3dworldgen.blogspot.com/)

2 

[ShakaUVM](https://www.reddit.com/user/ShakaUVM/)

•

[4y ago](https://www.reddit.com/r/GraphicsProgramming/comments/tpwx8e/comment/i2dzddx/)

Level streaming. Divide the world into chunks, load all chunks within X meters of you, where X is your view distance. Unload chunks that move out of range. Add fog beyond X. Boom, you have an Oblivion-Era renderer.

If it's sparsely populated and not heavily occluded, you can do line traces through a chunk by just checking against each object in the chunk, or if that gets too slow use an acceleration structure to hold objects in the chunk.

Customize chunk size to your needs.

1

# Related Answers Section

Related Answers

Top graphics APIs for beginners

Learning graphics programming can be a daunting task, but choosing the right API can make the process much smoother. Here are some of the top graphics APIs recommended for beginners, based on the experiences and opinions of various Redditors:

### OpenGL

OpenGL is often recommended for beginners due to its relative simplicity and extensive learning resources.

**Ease of Learning**: OpenGL is simpler to set up and use compared to Vulkan or DirectX12. ["OpenGL is a really great starting place if you've never done graphics."](https://www.reddit.com/r/GraphicsProgramming/comments/1rmemcm/comment/o8ywese/)

**Rich Learning Resources**: There are countless tutorials, articles, and videos available. ["OpenGL has DECADES of learning material such as tutorials, articles, sample code, YouTube videos, and books."](https://www.reddit.com/r/GraphicsProgramming/comments/1rmemcm/comment/o8z9589/)

**Cross-Platform Compatibility**: OpenGL is highly compatible across different platforms. "It's the most cross-platform option right now."

### Vulkan

Vulkan is a more modern and powerful API, but it comes with a steeper learning curve.

**Low-Level Control**: Vulkan offers unparalleled low-level control over the GPU. ["If you want to understand how GPUs work, learn Vulkan."](https://www.reddit.com/r/gameenginedevs/comments/1rmevki/comment/o8z6d8x/)

**Performance**: Vulkan is known for its high performance, making it suitable for complex 3D applications. ["Vulkan can render scenes with very much complexity."](https://www.reddit.com/r/GraphicsProgramming/comments/1pvzku6/comment/nw08hn2/)

**Complex Setup**: Vulkan requires more boilerplate code and is more complex to set up initially. ["Vulkan is not complicated, it is simple, but too much boilerplate."](https://www.reddit.com/r/gameenginedevs/comments/1rmevki/comment/o901m3b/)

### SDL GPU API

SDL GPU API is a good middle ground, offering a balance between ease of use and low-level control.

**Abstraction**: It provides a higher level of abstraction compared to Vulkan, making it easier to use. ["SDL_GPU is a good abstraction (but harder than OpenGL) and you can ship quickly without all the bloat of Vulkan."](https://www.reddit.com/r/GraphicsProgramming/comments/1rmemcm/comment/o8z6tzy/)

**Cross-Platform**: SDL GPU API is designed to be cross-platform, allowing you to write code once and run it on different operating systems. ["I personally like SDL3 GPU as a good middle ground between ease of use, cross platform, and Vulkan-like flexibility."](https://www.reddit.com/r/gameenginedevs/comments/1rmevki/comment/o8z6ko8/)

**Limited Features**: It may not support all the advanced features found in Vulkan or DirectX12. ["It doesn't support everything you might want: no bindless resource support last I checked, no ray tracing, not all shader types supported."](https://www.reddit.com/r/gameenginedevs/comments/1rmevki/comment/o8z6ko8/)

### WebGPU

WebGPU is a newer API that aims to provide a modern, cross-platform graphics API for the web and native applications.

**Write Once, Run Anywhere**: WebGPU allows you to write code once and run it on different platforms. ["WebGPU happens to be my favourite because it's got a 'write once, run anywhere' type of situation."](https://www.reddit.com/r/GraphicsProgramming/comments/1pvzku6/comment/nvzx4dg/)

**Modern Concepts**: It mirrors concepts from lower-level explicit APIs, making it a good stepping stone to more complex APIs. ["It directly mirrors concepts from lower level explicit apis."](https://www.reddit.com/r/gameenginedevs/comments/1rmevki/comment/o90p9bj/)

**Still Developing**: WebGPU is relatively new, and its specification is still prone to change. ["Only downside is that it's still relatively new and the spec is prone to change."](https://www.reddit.com/r/gameenginedevs/comments/1rmevki/comment/o90p9bj/)

### DirectX12

DirectX12 is a Windows-specific API that offers high performance and low-level control.

**Windows Only**: DirectX12 is limited to Windows, which can be a downside if you need cross-platform compatibility. ["Metal is my favourite but since I dont do mac/ios stuff any more its gotta be dx12."](https://www.reddit.com/r/GraphicsProgramming/comments/1pvzku6/comment/nw07qm8/)

**Performance**: It provides excellent performance on Windows, making it suitable for high-end gaming. ["Else if your focus is not rendering high complexity scenes go for DirectX11 or 12."](https://www.reddit.com/r/GraphicsProgramming/comments/1pvzku6/comment/nw08hn2/)

**Complex Setup**: Like Vulkan, DirectX12 is complex to set up and use. ["Not a big fan of DX12 API."](https://www.reddit.com/r/GraphicsProgramming/comments/1pvzku6/comment/nvzxyrk/)

### Metal

Metal is Apple's graphics API, offering high performance and low-level control on Apple hardware.

**Apple Specific**: Metal is limited to Apple devices, which can be a downside if you need cross-platform compatibility. ["Metal is my favourite but since I dont do mac/ios stuff any more its gotta be dx12."](https://www.reddit.com/r/GraphicsProgramming/comments/1pvzku6/comment/nw07qm8/)

**Ease of Learning**: Metal is considered one of the easiest low-level APIs to learn. ["Metal. One of the easiest to learn, IMHO."](https://www.reddit.com/r/GraphicsProgramming/comments/1pvzku6/comment/nw0dxvb/)

**Performance**: It provides excellent performance on Apple hardware, making it suitable for high-end gaming. ["Metal for me."](https://www.reddit.com/r/GraphicsProgramming/comments/1pvzku6/comment/nw01zc2/)

### Conclusion

Choosing the right graphics API depends on your goals and the level of complexity you are comfortable with. For beginners, OpenGL is often recommended due to its simplicity and extensive learning resources. For those looking for more control and performance, Vulkan or DirectX12 might be better choices, but be prepared for a steeper learning curve. SDL GPU API and WebGPU offer a good balance between ease of use and low-level control, making them suitable for various projects.

### Subreddits for Further Questions

[r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/)

[r/gameenginedevs](https://www.reddit.com/r/gameenginedevs/)

[r/gamedev](https://www.reddit.com/r/gamedev/)

[See Answer](https://www.reddit.com/answers/506495f1-b7fb-45e5-93a9-67d360949782/?q=Top+graphics+APIs+for+beginners&source=PDP)

[Best resources for learning Vulkan](https://www.reddit.com/answers/93cdb276-08b5-4afa-9a88-8f0083f37520/?q=Best+resources+for+learning+Vulkan&source=PDP)

[Common pitfalls in OpenGL programming](https://www.reddit.com/answers/d8c067ee-8504-4532-a697-1a0dd0d4ccd5/?q=Common+pitfalls+in+OpenGL+programming&source=PDP)

[Innovative techniques in real-time rendering](https://www.reddit.com/answers/4a6e2d9a-3c5f-4672-819f-096ff7483b14/?q=Innovative+techniques+in+real-time+rendering&source=PDP)

[How to optimize graphics performance](https://www.reddit.com/answers/1547228f-a0ee-4d4e-95cd-b97eb6313d34/?q=How+to+optimize+graphics+performance&source=PDP)

New to Reddit?

Create your account and connect with a world of communities.

[Continue with Email](https://www.reddit.com/register/)

[Continue With Phone Number](https://www.reddit.com/login/)

By continuing, you agree to our [User Agreement](https://www.redditinc.com/policies/user-agreement) and acknowledge that you understand the [Privacy Policy](https://www.redditinc.com/policies/privacy-policy).

# More posts you may like

[How would you approach an open world 3D terrain and the LOD system for it?](https://www.reddit.com/r/godot/comments/1oxn7ie/how_would_you_approach_an_open_world_3d_terrain/) [r/godot](https://www.reddit.com/r/godot/) • 4mo ago [

### How would you approach an open world 3D terrain and the LOD system for it?

](https://www.reddit.com/r/godot/comments/1oxn7ie/how_would_you_approach_an_open_world_3d_terrain/)  2 281 upvotes · 61 comments

[Any love for ModernGL and creating classic OpenGL rendering techniques?](https://www.reddit.com/r/GraphicsProgramming/comments/1md1y6s/any_love_for_moderngl_and_creating_classic_opengl/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 8mo ago [

### Any love for ModernGL and creating classic OpenGL rendering techniques?

](https://www.reddit.com/r/GraphicsProgramming/comments/1md1y6s/any_love_for_moderngl_and_creating_classic_opengl/)  4 99 upvotes · 9 comments

[I open sourced my infinite procedural world with trees and grass!](https://www.reddit.com/r/godot/comments/1lvjvgr/i_open_sourced_my_infinite_procedural_world_with/) [r/godot](https://www.reddit.com/r/godot/) • 8mo ago [

### I open sourced my infinite procedural world with trees and grass!

](https://www.reddit.com/r/godot/comments/1lvjvgr/i_open_sourced_my_infinite_procedural_world_with/)  280 upvotes · 13 comments

[Progress on Character Rendering in OpenGL](https://www.reddit.com/r/GraphicsProgramming/comments/1qem49p/progress_on_character_rendering_in_opengl/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 2mo ago [

### Progress on Character Rendering in OpenGL

](https://www.reddit.com/r/GraphicsProgramming/comments/1qem49p/progress_on_character_rendering_in_opengl/)  187 upvotes · 13 comments

[Sometimes the smaller parts of gamedev are the most satisfying!](https://www.reddit.com/r/godot/comments/1obylcp/sometimes_the_smaller_parts_of_gamedev_are_the/) [r/godot](https://www.reddit.com/r/godot/) • 5mo ago [

### Sometimes the smaller parts of gamedev are the most satisfying!

](https://www.reddit.com/r/godot/comments/1obylcp/sometimes_the_smaller_parts_of_gamedev_are_the/)  0:52 258 upvotes · 10 comments

[How Computationally Efficient are Compute Shaders Compared to the Other Phases?](https://www.reddit.com/r/GraphicsProgramming/comments/1mgzp6n/how_computationally_efficient_are_compute_shaders/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 8mo ago [

### How Computationally Efficient are Compute Shaders Compared to the Other Phases?

](https://www.reddit.com/r/GraphicsProgramming/comments/1mgzp6n/how_computationally_efficient_are_compute_shaders/) 18 upvotes · 23 comments

[Should I Switch from Vulkan to OpenGL (or DirectX) to Learn Rendering Concepts?](https://www.reddit.com/r/GraphicsProgramming/comments/1lik2rq/should_i_switch_from_vulkan_to_opengl_or_directx/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 9mo ago [

### Should I Switch from Vulkan to OpenGL (or DirectX) to Learn Rendering Concepts?

](https://www.reddit.com/r/GraphicsProgramming/comments/1lik2rq/should_i_switch_from_vulkan_to_opengl_or_directx/) 26 upvotes · 22 comments

[Improving the background environment](https://www.reddit.com/r/godot/comments/1r84eny/improving_the_background_environment/) [r/godot](https://www.reddit.com/r/godot/) • 1mo ago [

### Improving the background environment

](https://www.reddit.com/r/godot/comments/1r84eny/improving_the_background_environment/)  0:37 523 upvotes · 31 comments

[Shot of my OpenGL Engine. Yeah, I like Post Processing.](https://www.reddit.com/r/GraphicsProgramming/comments/1lr0fgi/shot_of_my_opengl_engine_yeah_i_like_post/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 9mo ago [

### Shot of my OpenGL Engine. Yeah, I like Post Processing.

](https://www.reddit.com/r/GraphicsProgramming/comments/1lr0fgi/shot_of_my_opengl_engine_yeah_i_like_post/)  244 upvotes · 18 comments

[Custom GPU implementation Demo ideas](https://www.reddit.com/r/GraphicsProgramming/comments/1rkyuzt/custom_gpu_implementation_demo_ideas/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 15d ago [

### Custom GPU implementation Demo ideas

](https://www.reddit.com/r/GraphicsProgramming/comments/1rkyuzt/custom_gpu_implementation_demo_ideas/)  69 upvotes · 12 comments

[When you screw up your procedural generation algorithm](https://www.reddit.com/r/godot/comments/1rqw6c7/when_you_screw_up_your_procedural_generation/) [r/godot](https://www.reddit.com/r/godot/) • 8d ago [

### When you screw up your procedural generation algorithm

](https://www.reddit.com/r/godot/comments/1rqw6c7/when_you_screw_up_your_procedural_generation/)  816 upvotes · 45 comments

[Screen-Space Indirect Lighting in my OpenGL Project](https://www.reddit.com/r/GraphicsProgramming/comments/1o8x0t5/screenspace_indirect_lighting_in_my_opengl_project/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 5mo ago [

### Screen-Space Indirect Lighting in my OpenGL Project

](https://www.reddit.com/r/GraphicsProgramming/comments/1o8x0t5/screenspace_indirect_lighting_in_my_opengl_project/)  93 upvotes · 7 comments

[Procedural worldbuilding as a 17 year old 3D artist](https://www.reddit.com/r/Houdini/comments/1q0gxcp/procedural_worldbuilding_as_a_17_year_old_3d/) [r/Houdini](https://www.reddit.com/r/Houdini/) • 3mo ago [

### Procedural worldbuilding as a 17 year old 3D artist

](https://www.reddit.com/r/Houdini/comments/1q0gxcp/procedural_worldbuilding_as_a_17_year_old_3d/)  5 119 upvotes · 17 comments

[I made a procedural city generator. Need some feedback!](https://www.reddit.com/r/godot/comments/1jh4u04/i_made_a_procedural_city_generator_need_some/) [r/godot](https://www.reddit.com/r/godot/) • 1y ago [

### I made a procedural city generator. Need some feedback!

](https://www.reddit.com/r/godot/comments/1jh4u04/i_made_a_procedural_city_generator_need_some/)  0:36 389 upvotes · 34 comments

[Got back to working on my renderer. Added camera swapping + keyframes, and fragment shaders](https://www.reddit.com/r/GraphicsProgramming/comments/1o59drh/got_back_to_working_on_my_renderer_added_camera/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 5mo ago [

### Got back to working on my renderer. Added camera swapping + keyframes, and fragment shaders

](https://www.reddit.com/r/GraphicsProgramming/comments/1o59drh/got_back_to_working_on_my_renderer_added_camera/)  89 upvotes · 11 comments

[Self-studying graphics for less than half a year, considering Metal vs Vulkan and PBR vs Ray Tracing, seeking advice](https://www.reddit.com/r/GraphicsProgramming/comments/1lefeok/selfstudying_graphics_for_less_than_half_a_year/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 9mo ago [

### Self-studying graphics for less than half a year, considering Metal vs Vulkan and PBR vs Ray Tracing, seeking advice

](https://www.reddit.com/r/GraphicsProgramming/comments/1lefeok/selfstudying_graphics_for_less_than_half_a_year/) 12 upvotes · 9 comments

[Working on world gen for my game, first time doing procedural generation](https://www.reddit.com/r/Unity2D/comments/1p1x3fc/working_on_world_gen_for_my_game_first_time_doing/) [r/Unity2D](https://www.reddit.com/r/Unity2D/) • 4mo ago [

### Working on world gen for my game, first time doing procedural generation

](https://www.reddit.com/r/Unity2D/comments/1p1x3fc/working_on_world_gen_for_my_game_first_time_doing/)  67 upvotes · 7 comments

[Help for physics engine development](https://www.reddit.com/r/GraphicsProgramming/comments/1oft4ib/help_for_physics_engine_development/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 5mo ago [

### Help for physics engine development

](https://www.reddit.com/r/GraphicsProgramming/comments/1oft4ib/help_for_physics_engine_development/)  53 upvotes · 18 comments

[2 Years of writing a 3D game engine and game (C++, SDL, and OpenGL)](https://www.reddit.com/r/GraphicsProgramming/comments/1nx1hbs/2_years_of_writing_a_3d_game_engine_and_game_c/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 6mo ago [

### 2 Years of writing a 3D game engine and game (C++, SDL, and OpenGL)

](https://www.reddit.com/r/GraphicsProgramming/comments/1nx1hbs/2_years_of_writing_a_3d_game_engine_and_game_c/)  3:10 156 upvotes · 31 comments

[First engine in OpenGL 3.3, what do you think? Which era of graphics programming would this fit?](https://www.reddit.com/r/GraphicsProgramming/comments/1jvglpg/first_engine_in_opengl_33_what_do_you_think_which/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 1y ago [

### First engine in OpenGL 3.3, what do you think? Which era of graphics programming would this fit?

](https://www.reddit.com/r/GraphicsProgramming/comments/1jvglpg/first_engine_in_opengl_33_what_do_you_think_which/)  0:28 109 upvotes · 8 comments

[Update on my game engine so far! Done with the material editor.](https://www.reddit.com/r/GraphicsProgramming/comments/1m20q5w/update_on_my_game_engine_so_far_done_with_the/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 8mo ago [

### Update on my game engine so far! Done with the material editor.

](https://www.reddit.com/r/GraphicsProgramming/comments/1m20q5w/update_on_my_game_engine_so_far_done_with_the/)  76 upvotes · 9 comments

[OpenGL procedural terrain + hydraulic erosion](https://www.reddit.com/r/GraphicsProgramming/comments/1ojcbzc/opengl_procedural_terrain_hydraulic_erosion/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 5mo ago [

### OpenGL procedural terrain + hydraulic erosion

](https://www.reddit.com/r/GraphicsProgramming/comments/1ojcbzc/opengl_procedural_terrain_hydraulic_erosion/)  youtu 101 upvotes · 13 comments

[My C++ OpenGL game engine](https://www.reddit.com/r/GraphicsProgramming/comments/1naehy5/my_c_opengl_game_engine/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 6mo ago [

### My C++ OpenGL game engine

](https://www.reddit.com/r/GraphicsProgramming/comments/1naehy5/my_c_opengl_game_engine/) 157 upvotes · 8 comments

[Are there any tips on creating a GUI interface for a game engine?](https://www.reddit.com/r/GraphicsProgramming/comments/1rte8m2/are_there_any_tips_on_creating_a_gui_interface/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 6d ago [

### Are there any tips on creating a GUI interface for a game engine?

](https://www.reddit.com/r/GraphicsProgramming/comments/1rte8m2/are_there_any_tips_on_creating_a_gui_interface/) 30 upvotes · 21 comments

[14 months of game and graphics programming — building my own tools from scratch](https://www.reddit.com/r/GraphicsProgramming/comments/1re5nei/14_months_of_game_and_graphics_programming/) [r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/) • 23d ago [

### 14 months of game and graphics programming — building my own tools from scratch

](https://www.reddit.com/r/GraphicsProgramming/comments/1re5nei/14_months_of_game_and_graphics_programming/)  92 upvotes · 11 comments

# Community Info Section

[r/GraphicsProgramming](https://www.reddit.com/r/GraphicsProgramming/)

Join

Graphics Programming

A subreddit for everything related to the design and implementation of graphics rendering code.

Show more

Public

Anyone can view, post, and comment to this community

## Top Posts

[Reddit reReddit: Top posts of March 28, 2022](https://www.reddit.com/posts/2022/march-28-1/global/)

[Reddit reReddit: Top posts of March 2022](https://www.reddit.com/posts/2022/march/global/)

[Reddit reReddit: Top posts of 2022](https://www.reddit.com/posts/2022/global/)

[Reddit Rules](https://www.redditinc.com/policies/content-policy) [Privacy Policy](https://www.reddit.com/policies/privacy-policy) [User Agreement](https://www.redditinc.com/policies/user-agreement) [Your Privacy Choices](https://support.reddithelp.com/hc/articles/43980704794004) [Accessibility](https://support.reddithelp.com/hc/sections/38303584022676-Accessibility) [Reddit, Inc. © 2026. All rights reserved.](https://redditinc.com/)

Expand Navigation

Expand Navigation

Collapse Navigation

Collapse Navigation 

0cAFcWeA4XjUaFfeVKL8MkdWAEJdtCVOWSn1Ldty21fDV2t3FjGrovfbe_T4iuFytFXDhx_tyjgon-whlSfsTZduQFL2jhadBaWUDVE6Y_fldR8iERFwTlgiSRJwmnVt9kWASOb2zqFzG4naFMK1WNrVbxwcyU5mKG_BxEStDrP7zZJFSbTvb2BHJ7UYanx7_QT7uXXOxNPQMSz2uch7NY1WjV9SRlRFBB22REkIiSfLxujkpYBMjE02EjozMLnhpilB6NposVtM3wSm9JAfE0ZymBTPSXF3FZh4lpPKKoSieZ5A65Umu6Js568QRaJjrE6lUrL-jbCtovlpq7kYed0_26MmEo66W2ZqKWb8iPnkkAgeR3EsvDKAsugH-A1XQgiFWcyM8zV4xkkBABc54S5TUVlcupvsrVo7Yhm6mgwCsMZACEYyJ7ofielBHx4JHU-zxih5V-YUo3j344s2jTmJY4qUsE4DdwiP_3u1aiD3j-kxvnweRfB7GObm2xLYnzVIYrXQye8u92mrJGTvnTcd-jCNemLHMgcKZTCShgO1ERHSc5ciSGPFhqdtxtvTq26T8tLKbRTKSaZHaImdlqk2l-LZHIKUkQJxZsc12wajdEh7l6a-E22bo2EviQI9h2GAyHG2ouWdvneB_1vb4BuCQHc-Tt7Qg4ttJoxSAmLDqfZKN8fWwedCM1CEjpGsofMXWHdtWe6WTEPOPT9FUQefqU_MHuh53O7wUwitEMVg41h4IBrydHCUM8TWXUYT7YTfsEPQYUCXuFl3TT3XssOG82RQE8-UL32FqfHEJg18AtpgVhPfvjigcOsiowI5XhnpdOuzo1mikagouGP3UEZj0Kcxvm7TbnS-I3xqVbGuVPElBEviDNiZB6SNUBxXLXfghXu8Qb0-vsw2Kicpq1yBgaPZda9vt_FHlfxvP8h4dibCifRtkA-c0clvjFK6DCFflzsVFTpomAmU8HfZKimbTdlhgcKpW0VV483P-4pUJjTtgAMMxtTsIg7HFT-0A4d03kv-mlIUpnm57NMqMYofKZNmlIYW8S8z9cYBylNcwipAVUyb8HvO9zf25c3vXEXEBkrP5YVPPqiBGcAdShKIKhri5tczl9gUxn1D5BCMs9W1GeaHcKj9BO5Khix2I0azPOV_s1b3sW5fTLj5GcJaZhdSWHsosQiDPN5pp1dYMpdxaOJyYfRRCGoE6wGi0blFTa6k_4Ghth-_jxwHmch1VvS5drHiAe467gg8LqraJoGaeyvHTzzj6uZf9PLfh6_b0kuWg_MAkWFIEnwb4ILDzp4Ae0WupSAiFMg7dTgNUx774IjpJFdX88B3bM1JDQY5qgrX4Js47WCVzAO0qH9tljBMIg0iFmb2t7z3FfJThC7lVAQyflGb8FDXjJ91QAB5yEjbHnnioKTBzLbOBno2h-7zQ3kXNW8Tfb6DR7ju_yDGM7ryZxpuX-4oGktLK7fLFj6KSixnUetAKN3OQgCwufzoqBIq6Iyp0ywHUEIkI_gVdXH4rhNn_YnTRNAsxd7rtnPjBrBm7mrFI7NWfGTtt-mGP5FxHaOZ_VauloQ5F2iPwN2xPYfhegJsnHT0vcbJUW6_K6LV61NpfMwHv5bOF7Zffm-1t9xA8DTb2horULEu3e0v2GjoPu5dmvDPCkRIN5MNiyFZ61gnEuI46arXhbKL7K6-l8jMl3zkwp7AZmmdscLO-_vuGOeSo6p5MG7w3D1kTG1Xc1mTIPNrsi8cN-NYKJVL9ap99OHXXqTF4izy50lcI1lZFZEe9yhgETOHVIo3-f0iNBCOQLo0CnN2SBrSsLdWJAvey7E2zgth2W_TND5Wc-2Bb3rwtktl2z7Req3lBFasIIvxDFu5uM9SGMr52bwwG-IjBsZSBfc24w3eSr0vJokElxlcuoA7drowft8eb0BVmEWI1vF596cVLWsTbna7FoKfNPsku-q7J3c3mwnLZxXUJvhqo7a4m4bm-F88jSosFCc2H5sr_FMlPSO5WGbS21lLrzgb363OCHV4ax6pgWYCTaN93bShd-9nsoypuv7m5H-3_dQ3csjtRgYqZUfSHMyh3s5gxUGEHSChzmnUgawLnOLmjwho6tsjZiJJbjz6pou_Ybdzl6Wut23Ob2XMJOYJj3CRuNf909ZJIeGRU3Pqwh5-MpGrhle8B-19Cj8CslvtfpgOv9AdhzTqo46VEppAeY2_RRKPY-Dv1vxYgG95Y737vpVSTUb63zMBYkid1-