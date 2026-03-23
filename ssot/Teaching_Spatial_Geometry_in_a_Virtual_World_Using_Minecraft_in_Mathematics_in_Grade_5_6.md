# Teaching Spatial Geometry in a Virtual World: Using Minecraft in Mathematics in Grade 5/6

# Teaching Spatial Geometry in a Virtual World: Using Minecraft in Mathematics in Grade 5/6 

Klaus-Tycho Foerster Aalborg University 

ktfoerster@cs.aau.dk 

Abstract—Spatial geometry is one of the fundamental mathe-matical building blocks of any engineering education. However, it is overshadowed by planar geometry in the curriculum between playful early primary education and later analytical geometry, leaving a multi-year gap where spatial geometry is absent at large. Hence, we investigate the usage of Minecraft as tool to help bridge said gap, as the virtual worlds of Minecraft allow children to create three-dimensional objects in a constructive and algorithmic way. We study two learning scenarios in grade 5/6 with 103 students, reporting on our & the childrens’ experiences. Based on our findings, we believe Minecraft to be a valuable mathematical tool that can be easily used to augment the current curriculum. 

I. INTRODUCTION AND MOTIVATION 

Geometry is one of the cornerstones of mathematics and engineering education, making it relevant for all stages of teaching, from kindergarten to graduate school. In this context, spatial geometry is especially important for designing and understanding real-world phenomena and constructions. As such, it is included in most parts of the K-12 curriculum, with special focus on early primary education and later analytical geometry. In between, it is however absent at large, cf. [1]. Even worse, spatial geometry has often been reduced to calculations [2], mostly ignoring spatial concepts [3]. 

However, students have more experiences with spatial than planar geometry after the first years of primary school, aug-mented by their daily lives [4]. Therefore, a further exploration of spatial geometry should not be delayed until the end of the lower secondary [3], especially as the students’ susceptibility grows significantly around the age of 12, in particular for girls [5]. 

Accordingly, Maier [6] suggests that the concepts of space should be developed by teaching spatial geometry. As the creation of real-world models can be time- and cost-intensive, Luig and Straesser [7] propose to use geometry software in the classroom, backed by Schumann [8]. Especially for spatial geometry, the use of computers allows a transition to digital Pestalozzian ideals, cf. [9], giving more importance to the concepts of solids [2] and allowing traditional learning goals to be reached by new technologies [10]. 

There is no lack [11] of (interactive) 3D geometry soft-ware for use in schools, e.g., Archimedes Geo3D [12], [13], GeoGebra [14], [15], or POV-Ray [16], [17]. 

The listed programs however suffer from the downside that they require the explicit use of a three-dimensional coordinate 

Klaus-Tycho Foerster is supported by the Danish Villum Foundation. 

system, making them harder to grasp than simple planar geometry. According to Kadunz and Straesser, the students even need to mentally construct a numerical image due to the use of coordinates [1]. 

Fig. 1: Spatial constructions in Archimedes Geo3D [12] require the explicit use of three-dimensional coordinates, making it harder to intuitively use in the context of elementary education. 

Elementary spatial geometry programs for children are uncommon, cf. [3]. The only example of educational software that we are aware of in this area is BAUWAS [18], [19], where blocks can be placed in a 10× 10× 10 grid, see Figure 2. 

Fig. 2: Screenshot created with BAUWAS [18]. Blocks can be created/deleted by simply clicking with the left/right mouse button. 

However, we would like to have a program beyond the size restrictions of 10 blocks in every dimension, allowing also for collaborative possibilities and an incentive for the students to use the program in their own free time [24]. As thus, in this article, we investigate the choice of the popular program Minecraft [20] to augment the the teaching of spatial geometry in grades 5/6. In particular, we design and evaluate classroom studies, coming to the conclusion that Minecraft can be used as a valuable tool to augment the concept of space.

(a) Screenshot taken in Minecraft [20]. (b) Uncanny valley effect, from [21]. (c) Screenshot in the CryENGINE 2, from [22]. 

Fig. 3: The uncanny valley hypothesis, first proposed by Mori, cf. [23], states that non-perfect depictions of humans are easily identified by an observer, causing revulsion and feelings of discomfort. On the other hand, clearly artificial scenes such as in Figure 3a are more pleasant than the previously mentioned, as there is no expectation of perfection. Current video games need a high level of modification to bridge the uncanny valley, as attempted in Figure 3c. 

A. Overview of this Article 

In the following Section II we start by covering (related educational work on) Minecraft and its deployment in the classroom. Then, in Section III, we discuss our goals and classroom studies to augment the understanding of spatial ge-ometry in grades 5/6, followed by a qualitative and quantitative assessment in Section IV, also briefly covering a grade 12 trial in Section V. Lastly, we conclude in Section VI with a summary and outlook on future work. 

II. MINECRAFT 

Minecraft is a first-person video game, released in Novem-ber 2011 by the company Mojang, with the main developers being Markus “Notch” Persson and Jen Bergensten [25], [26]. In total, more than 100 million copies of Minecraft were sold worldwide so far [27], with its immense popularity being the reason why Mojang was bought by Microsoft in late 2014 for 2.5 billion dollars [28]. 

Minecraft can be roughly summarized as a (collaborative) sandbox game, where Lego-like blocks can be placed and re-moved. Besides this building mode (coined “creative mode“), there is also a “survival mode” available, where the players start with an empty inventory and have to gather/mine all desired resources, while the world is populated with friendly non-player characters, animals, and hostile monsters. 

Even though Minecraft and its clones might like outdated in terms of today’s video game graphics, its vintage look does not hinder its popularity – it might even have helped popularize it, cf. Figure 3. Furthermore, the procedural world generation allows for all sorts of landscapes in a virtually unlimited environment, as illustrated in Figure 4. 

Fig. 4: Depiction of the maximum size of a Minecraft world, assuming each block having a size of 1m3, from [29]. 

A. Minecraft in Educational Use 

The phenomenon Minecraft1 quickly found its way into education and research as well. Already shortly after its release, articles discussed the classroom use of Minecraft for topics such as biology, ecology, physics, chemistry, and geology and geography, e.g., [30]. In regards to programming, modifications of Minecraft allow for interesting possibilities of visual coding, with methods such as coding blocks [31] in CodeBlocks [32] or turtle coding [33], [34] in ComputerCraft-Edu [35]. We refer to the survey of Nebel et al. [25] for an encompassing literature review, also covering further school subjects. 

Specifically for mathematics, Bos et al. [26] let students (third grade) explore area and perimeter using Minecraft, giving also additional Minecraft mathematical activities for students in elementary education: E.g., reasoning with shapes, geometric measurements, analyzing patterns, or scaling. For the age group 7-9, Al Washmi et al. [36] also consider mathematical activities in a modified version of Minecraft, using a pre-built world with tasks to perform by the students. Kørhsen and Misfeldt [37] perform an ethnomathematical study by monitoring seven 10-year olds in an afterschool Minecraft program, describing their findings in terms of Bishop’s categories [38] and elaborating on the collaborative effect of playing. Related to spatial involvement, Nguyen and Rank [39] present a digital training regimen in Minecraft, where they plan to evaluate mental rotation performance in future work. Lastly, Floyd [40] reasons that “Minecraft clearly promotes the development of spatial abilities”, by comparing the possible actions in Minecraft with related work in spatial reasoning skills development literature. 

B. Deploying Minecraft for Classroom Studies 

The full version of Minecraft is available for most recent versions of Windows/Mac/Linux, and also (at a reduced price) for most gaming consoles and mobile operating systems. However, the single client license cost of ∼26 USD2 is prohibitive for most school budgets. There is also an enhanced 

1From now on, we are going to use Minecraft as a synonym for Minecraft-like software, similar to the use of Google as a verb – unless noted otherwise. 

2At https://minecraft.net/en/store/, price as of November 2016.

education version available, with a more reasonable price of 5 USD3: This version only runs on Windows 10 or macOS, neither being available at the high school in Northern Germany where the teaching took place. 

As we only needed basic building functionalities and es-pecially wanted the students to also being able to continue their work at home, we thus opted for free versions of Minecraft. In the first cross-sectional study we used Minecraft Classic [41] with a browser-based client. As Minecraft Classic was removed in Fall 2015 [41], we then used the free alter-native ClassiCube [42], combined with MCGalaxy [43] as a server. Both ClassiCube and MCGalaxy have low hardware requirements, allowing them to run on dated school hardware (in our case, from ≈ 2010). 

III. SETTING OF THE CLASSROOM STUDIES 

In this section, we will describe our settings/design and goals for our classroom studies, extending our earlier pre-liminary technical report [44]. We chose Minecraft for our classroom studies as we were looking a for software which is 1) available in a free version, 2) which students would use in their own time at home, and 3) where the students can collaborate4. 

We designed two classroom studies, the first one focusing on the transfer between the plane & space [45] and collabo-rative building [37], and the second one for implementing the suggestion of scaling by Bos et al. [26]. 

In total, we evaluated our scenarios with 103 students, 69 for the first setting, and 12 for the second setting, also adding a control group of 22 students. Roughly half of all students were girls. The students were also provided with instructions for Minecraft, see Figure 5. 

Fig. 5: Instructions (in German) for the students on how to use Minecraft. Students in grade 5/6 barely made use of them after a short period, while a few students in grade 12 still consulted them throughout the first hour. 

3At https://education.minecraft.net/, price as of November 2016. 4We refer to the work of Franke [24], who also elaborates on that the 

final products of the students’ geometric work do not need to be graded – an approach we will follow in this article. 

A. Collaboration and Transfer from the Plane to Space 

First, in a cross-sectional study (69 students, 1 class in grade 5/6 each, 1 group of students in grade 5 in extra-curricular activities), we wanted to see if the students could transfer their drawn objects from the plane to the space of the virtual world, if they would have problems with spatial orientation in the first-person view of Minecraft, if already an empty world is enough to spark creativity, and if collaboration at class size is feasible. 

The 4 lectures (2 × 2) were structured as follows: After a short introduction, the students would try working in Minecraft on their own, then work together with a partner on a project designed together, and lastly the whole class together would sketch a project for the remaining 2 lectures: In these, the students would all build on a project collaboratively. The students would also be given the option to play at home in a provided (yet empty) world. In the following week, the students would participate in a questionnaire. 

B. Scaling of Constructions 

Second, in an experiment (12 students from grade 6, with a control group of 22 students in grade 6), we were interested in scaling constructions in Minecraft, and its short-term impact on spatial skills. 

The 2 lectures (2×1) were structured as follows: After a pre-questionnaire, the students would sketch a desired construction and then build it twice, once at normal size, and once at doubled dimensions. In the second lecture the scaling process would be inverted, scaling the dimensions down to half the size, concluded by a post-questionnaire. The control group would be given one questionnaire to compare the two groups. 

IV. EVALUATION OF THE CLASSROOM STUDIES 

In this section, we present our and the students’ experiences during the classroom studies. We begin by describing the details of the first cross-sectional study in Section IV-A, followed by the second experiment in Section IV-B. 

A. First Classroom Cross-Sectional Study 

Construction in Minecraft is performed from a first-person view, i.e., from a higher level of abstraction, as the (avatar’s) viewpoint is inside the to be performed task itself. Notwith-standing, we observed that all students, except for one, had no problems orienting themselves in the virtual world of Minecraft. The students agreed with this observation, cf. Fig-ure 6d. Similarly, the students quickly mastered controlling the avatar, cf. the caption of Figure 5, and were immideately able to construct their first ad-hoc projects alone. 

Afterwards, the students sketched a small project in pairs and built them in Minecraft, see the left four pictures in Figure 9. We observed that the students were able to transfer their two-dimensional sketches to three-dimenstional buildings quite well, performing some minor modifications on the go. The sketches in grade 5 were still very planar (see Figures 7a, 7d), while the sketches in grade 6 were already more spatial (see Figures 7b, 7e).

86% 

14% 

Minecraft Paper 

(a) Would you rather draw on paper or build in Minecraft? 

95% 

5% 

Minecraft Lego 

(b) Would you rather build in Minecraft or Lego/building blocks? 

51% 

49% 

Yes No 

(c) Would you play Minecraft with your parents? 

99% No 

(d) Did you have issues orienting yourself in the world of Minecraft? 

Fig. 6: Evaluation after the cross-sectional study, with n = 69 (rounded %). Regarding the question of playing with their own parents in Fig. 6c, some students answering no noted that their parents would probably not see a relation between Minecraft and mathematics, as something fun cannot be mathematics. 

(a) Sketch of a castle (grade 5). (b) Sketch of a cubic building (grade 6). (c) Outside of the collaboratively built cinema. 

(d) Construction of the castle above. (e) Construction of the cubic building above. (f) Inside the collaboratively built cinema. 

Fig. 7: Examples of constructions from the cross-sectional study. Especially the sketches in grade 6 were already more spatial. 

The results of the following questionnaire are shown in Figures 6 and 10.5 Most students responded that they preferred building in Minecraft to alternatives such as drawing on paper or building with Lego/building blocks, see Figures 6a and 6b. 

For the conclusion of the first two lectures, the students discussed what sort of construction they would like to collab-oratively build in the next two lectures, and set up rules for collaborative building (also for at home). The class in grade 5 built a castle (cf. Figure 8), the class in grade 6 built a park, and the extra-curricular group built a cinema, see Figures 7f and 7c. All groups took great care to collaboratively build without upsetting others, but their building plan was more spontaneously: Students looked where they could help finish-ing building, and then moved their avatar there to continue constructing. We suspect that for larger and more complex projects, we would need to guide the students beforehand to create a (modularized) building plan. 

While the constructions for the castle and the park focused just on the construction, the extra-curricular group decided to also host an event once their cinema was done: They performed a short play on the stage of the cinema (behind the glass in Figure 7f) with some students, while the other students watched from their seats. Especially the collaborative building fascinated the students, which also showed in their 

5Eggeling [46] performed a study with six students, using also the questions in 6 & 10, except for 6c. She notes [46, p. 63] that the students’ answers mostly correspond to ours, drawn from our preliminary technical report [44]. 

interest to build in their free time from home (we did not give the students any “homework”, it was left to them as their own decision). Roughly 80% of the students played on these worlds at least once from home, more than half at least for 6 hours in a two week timespan. We initialized the small worlds to be empty (flat), and noticed that interest in each world went down the “fuller” the worlds became, with interest rising again once we proved new worlds. We suspect that the fascinating part of Minecraft is not so much interacting with an already existing environment, but rather the construction itself: Once the construction is deemed finished, it is not re-iterated or extended later, but rather a new project is started. 

One further observation that surprised us is that we also saw no signs of vandalism in the freely accessible worlds and that we received no complaints from any student that their construction was destroyed. We believe that this effect is rooted in the communal rule-generation, e.g., in Figure 8, and collaborative building in class. We did not perform these steps in grade 12, observing some vandalism, cf. Section V. 

Fig. 8: Notes (in German) from a student regarding collaborative play: First, she noted that she would like to build a castle collaboratively, but that this castle should belong to everyone. Second, she pointed out that everyone should respect the constructions of others.

(a) Collaborative building at home (grade 5). 

(b) Collaborative building at home (grade 6). 

Fig. 9: We provided an empty world for the students to build at home for each group in the cross-sectional study. While the students in grade 5 mostly constructed (independent) buildings next to each other (Fig. 9a), the world in grade 6 was more organized (Fig. 9b). 

Similar to the transfer from paper to space in grades 5 and 6, we observed that the building from home was more structured in grade 6, leading to more organized virtual worlds, see the two exemplary screenshots in Figure 9. 

Lastly, according to the sudents’ opinions, they preferred collaborative building, where they could construct together with the whole class, cf. Figure 10. We believe that this is one of the great strengths and unique opportunities of Minecraft, deserving future investigations: Minecraft allows for an easy setup of building together in large groups, where all students can be immersed into the construction. Without computer use, such a task would be very demanding (money- and time-wise), and might not happen at all in everyday teaching. As such, we believe Minecraft to be a useful additional tool for teaching spatial geometry in grades 5 and 6, which is also used by students in their free time. 

4% 19% 

20% 57% 

alone 

a few friends 

a few classmates 

whole class 

Fig. 10: Would you rather play Minecraft (with) ... ? Question posed to n = 69 students from grade 5/6 after the cross-sectional study. 

B. Second Classroom Experiment 

In our smaller (12 students in grade 6) and shorter (2 lectures) second classroom experiment we focused on the task of scaling, as an interpretation of multiplication in Minecraft, cf. Bos et al. [26]. 

In the first lecture, we started with a pre-questionnaire including one spatial geometry question, cf. Figure 11. Then, the students first sketched a construction, then built it at normal size in 10 minutes, and then tried to build it at doubled scale in 20 minutes. While the volume of a doubled construction (in all dimensions) is increased by 23 = 8, the outer hull block amount just increases by a factor of 22 = 4 (ignoring constructions inside). As thus, the students doubling the constructions in all dimensions were not able to finish their work, see e.g., the crane with missing features in Figure 12b or especially the house in Figure 12c. Only one student was able to completely finish his construction, as he only scaled in two dimensions, needing twice as many blocks in Figure 12d. This lead to discussions why scaling a construction by a factor of two is problematic in twice the construction time. 

One might think that reversing the process in half the time should be easy, but there is the problem that Minecraft has an atomic block size. E.g., if a window has a size of one block, what size should it have when scaling the construction down? The students used two different approaches when scaling was not possible, either ignore the feature such as in Figure 12g or scale the amount of the features as in Figure 12h. Only few students planned a construction that could be properly scaled, as can be seen in Figure 12e. 

We concluded the two lectures with a post-questionnaire of two spatial geometry questions, comparing the results with the same questions asked in a control group of 22 students, and the initial pre-questionnaire. As there was no delay in taking the questions, the effects have to be considered short-term effects. As can be seen in Figure 12, both group behaved roughly the same initially, but the results of the students taking the two lectures improved strongly. We would like to note that we did not perform a classical mathematical lesson plan, but just let the students sketch and build in Minecraft as described. 

We believe that the propaedeutic algorithmic6 tasks per-formed in these two lectures resulted in the better results of the students. We therefore think that the idea of scaling, proposed for Minecraft by Bos et al. [26], is a promising concept for late elementary education, warranting further exploratory studies for its use regarding surface area and volume in the mathematics curriculum. 

V. FURTHER OBSERVATIONS IN GRADE 12 

We also shortly introduced a class in grade 12 to Minecraft for one hour, and offered them as well the option to play at home on a world hosted by us. We defer a detailed overview of this study to a future article. Notwithstanding, there are two observations that we would like to mention: 

6We refer to the article [47] of Schmidt-Thieme for a general overview on the importance of algorithms in (mathematical) education.

(a) Never (4; CG:5) (b) A little (1; CG:5) (c) Few hrs. (1; CG:2) (d) Often (6, CG:10) 

Fig. 11: Results in the second classroom experiment, from the geometry questions in the questionnaire (pre/post, with 4 + 1 + 1 + 6 = 12 students) and the control group (CG, with 5 + 5 + 2 + 10 = 22 students). The captions denote how much the students played Minecraft before, also showing how many students are in each group. Responses in blue are correct, incorrect ones are in orange. The results before the lectures are roughly similar to the control group (except for question #1 in Figure 11a), but have improved to mostly correct results after the two lectures. 

(a) Sketch of the crane in Fig. 12b. (b) Construction of the crane from Fig. 12a, properly scaled. 

(c) Properly scaled house, but too large to complete in time. 

(d) Properly scaled house in two dimensions, but not in height. 

(e) Sketch of the construction in Fig. 12f, each block outline shown. (f) Properly scaled construction. (g) Windows not properly scalable. (h) Another take on scaling. 

Fig. 12: Examples of constructions from the second classroom experiment. The students all chose to build houses in the first lecture (top row), except for one student building a crane in Fig. 12b. In the second lecture, all the students built constructions related to buildings, i.e., merlons (battlements) in Fig. 12f. 

1) Students in grade 12, that did not play Minecraft (or other first-person games) before, had more problems orienting themselves in the virtual world of Minecraft than the corresponding group of students in grade 5/6. They especially lacked the playful behavior of younger children, who accustomized themselves to the new en-vironment quickly. Furthermore, these students in grade 12 also continued to consult the instructions in Figure 5 from time to time, unlike the students in grade 5 and 6. 

2) The students in grade 12 logged in at roughly similar levels from home as the younger children, but their col-laborative behavior was different. Cooperative building was limited, most students built on their own. Further-more, some students actively damaged other buildings when nobody else was logged on – which did not happen in grade 5/6. Two female students noted that they were disappointed by this behavior of their fellow classmates, which they deemed inappropriate for their age. 

We did not study these occurrences in depth, as we did not expect them to happen beforehand. However, we believe that further research in this area would definitely be interesting. 

VI. SUMMARY AND OUTLOOK 

We studied the usage of Minecraft as a tool to teach spatial geometry in virtual worlds in grades 5 and 6. Specifically, we evaluated two classroom studies, focusing on building pre-planned constructions, cooperative building, and scaling three-dimensional constructions. Based on our findings, we believe the appropriate classroom use of Minecraft to be an enriching experience regarding the concept of space at the end of primary education. However, we would like to emphasize that we do not want to advocate for Minecraft replacing parts of the current education curricula. Rather, we see Minecraft as a useful tool to augment teaching in the curriculum: “To be used when appropriate, not to be applied when other tools are more useful, and not taught for its own sake” [48].

The mentioned related work in Section II lists many more possibilities for the further use of Minecraft: We think that especially the usage of programmable agents in this context is promising, as it allows for visual debugging by observing the agents’ actions in a virtual world – a topic we plan to explore further at undergraduate level [34]. 

Another future opportunity is the use of Virtual Reality (VR) for spatial geometry or concepts of space [49], [50], [51], with some research ideas being already over 15 years old [52], [53]. Since recently, Minecraft is also available in a VR version [54], with Azmandian et al. [55] already exploring the possibilites of haptic targeting, e.g., to build a castle [56]. Once the VR hardware7 and appropriate software becomes widely available to schools, we anticipate exciting new directions for augmented learning in the classroom. 

Lastly, we would like to conclude with a statement of a student in Figure 13, with which we wholeheartedly agree. 

Fig. 13: “The whole game consists of math.” – Response from a student in grade 6, when asked about how Minecraft relates to mathematics. 

ACKNOWLEDGEMENTS 

We would like to thank the anonymous reviewers of the 8th IEEE Global Engineering Education Conference (IEEE EDUCON) for their helpful comments on our submission. 

REFERENCES 

[1] G. Kadunz and R. Straesser, Didaktik der Geometrie in der Sekun-darstufe I [Didactics of Geometry in Lower Secondary]. Hildesheim: Franzbecker, 2009. 

[2] M. Ludwig and H.-G. Weigand, Didaktik der Geometrie fuer die Sekun-darstufe I [Didactics of Geometry in Lower Secondary]. Spektrum Heidelberg, 2009, ch. Konstruieren [Constructions], pp. 55–80. 

[3] H.-J. Elschenbroich, Mathematik-Didaktik [Didactics of Mathematics]. Cornelsen Berlin, 2003, ch. Unterrichtsgestaltung mit Computerunter-stuetzung [Creating Teaching with Computer Support], pp. 212–233. 

[4] M. Ludwig, “Vorlesungskapitel: Propaedeutische Geometrie in Klasse 5 und 6 [Lecture Chapter: Propaedeutics of Geometry in Grades 5 and 6],” Available at http://www.math.uni-frankfurt.de/∼ludwig/ vorlesungen/skripten/didgeo/skript didgeo.html, 2007. 

[5] B. Andelfinger, Geometrie [Geometry]. Soest: Landesinstitut fuer Schule und Weiterbildung, 1988. 

[6] P. H. Maier, Raeumliches Vorstellungsvermgen: Ein theoretischer Abriss des Phaenomens raeumliches Vorstellungsvermoegen [Spatial Imagina-tion: A Theoretical Outline of the Phenomenon of Spatial Imagination]. Auer Verlag, 1999. 

[7] K. Luig and R. Straesser, “Foerderung ausgewaehlter Aspekte der Raumvorstellung mit dynamischer Geometriesoftware [Promotion of Selected Aspects of Spatial Representation with Dynamic Geometry Software],” in Beitraege zum Mathematikunterricht, 2009. 

[8] H. Schumann, Raumgeometrie: Unterricht mit Computerwerkzeu-gen[Space Geometry: Teaching with Computer Tools]. Cornelsen Verlag, 2001. 

[9] M. Ludwig, “Raumgeometrie mit Kopf, Herz, Hand und Maus [Space Geometry with Head, Heart, Hand and Mouse],” in Beitraege zum Mathematikunterricht, 2001. 

7Currently ranging from hundreds (Oculus Rift, HTC Vive) to thousands (Microsoft HoloLens) of dollars for a single headset, as of November 2016. A less powerful alternative is to use modern smartphones as a display for virtual reality, e.g., Google Cardboard/Daydream or Samsung Gear VR. 

[10] H.-G. Weigand and T. Weth, Computer im Mathematikunterricht. Neue Wege zu alten Zielen [Computers in Mathematics Teaching. New Ways to Old Goals]. Spektrum Akademischer Verlag, 2002. 

[11] (2016) List of interactive geometry software: 3D Software. [Online]. Available: https://en.wikipedia.org/wiki/List of interactive geometry software#3D Software 

[12] A. Goebel. Archimedes Geo3D. [Online]. Available: http://www. raumgeometrie.de/drupal/en 

[13] ——, Experimentieren im Geometrieunterricht [Experimentation in Geometry Teaching]. Franzbecker, 2006, ch. Dynamische Raumge-ometriesoftware - ein ideales Werkzeug zum Experimentieren in der Geometrie [Dynamic Spatial Geometry Software - an ideal Tool for Experimentation in Geometry], pp. 27–36. 

[14] M. Hohenwarter et al. GeoGebra. [Online]. Available: https://www. geogebra.org/ 

[15] M. Hohenwarter and J. Preiner, “Dynamic mathematics with geogebra,” AMC, vol. 10, p. 12, 2007. 

[16] POV-Ray. [Online]. Available: http://www.povray.org/ [17] POV Team and others, “Persistency of vision ray tracer (pov-ray),” 

Version 1.0, Tech. Rep., 1991. [18] BAUWAS. [Online]. Available: http://www.bics.be.schule.de/son/ 

machmit/sw/bauwas/index.htm [19] H. Meschenmoser, Computergestuetzte Konstruktion und Visualisierung: 

das Konstruktionsprogramm BAUWAS [Computer-Assisted Construction and Visualization: the Construction Program BAUWAS]. Berlin: Machmit-Verlag, 1999. 

[20] M. Persson and J. Bergensten, “Minecraft,” Stockholm, Sweden: Mojang AB., 2011. [Online]. Available: http://minecraft.net 

[21] Smurrayinchester. (2007) Mori Uncanny Valley. CC BY-SA 3.0, https: //creativecommons.org/licenses/by-sa/3.0/legalcode. [Online]. Available: https://commons.wikimedia.org/wiki/File:Mori Uncanny Valley.svg 

[22] inCrysis. (2009) Guide to the game Crysis - Screenshots and ToD art. [Online]. Available: https://aka.ms/incrysis 

[23] M. Mori, K. F. MacDorman, and N. Kageki, “The uncanny valley [from the field],” IEEE Robotics Automation Magazine, vol. 19, no. 2, pp. 98–100, June 2012. [Online]. Available: http://doi.acm.org/110.1109/MRA.2012.2192811 

[24] M. Franke, Didaktik der Geometrie: In der Grundschule [Didactics of Geometry in Primary School]. Spektrum Akademischer Verlag, 2007. 

[25] G. D. R. Steve Nebel, Sascha Schneider, “Mining learning and crafting scientific experiments: A literature review on the use of minecraft in education and research,” Journal of Educational Technology & Society, vol. 19, no. 2, pp. 355–366, 2016. 

[26] B. Bos, L. Wilder, M. Cook, and R. O’Donnell, “Learning mathematics through Minecraft,” Teaching Children Mathematics, vol. 21, no. 1, pp. 56–59, 2014. [Online]. Available: http://dx.doi.org/ 10.5951/teacchilmath.21.1.0056 

[27] O. Hill. (2016, June) We’ve sold Minecraft many, many times! Look! Mojang. [Online]. Available: https://mojang.com/2016/06/ weve-sold-minecraft-many-many-times-look/ 

[28] J. Pagliery. (2014, September) Microsoft buys Minecraft for $2.5 billion. CNN. [Online]. Available: http://money.cnn.com/2014/09/15/ technology/minecraft-microsoft/ 

[29] C. Huang and M. Huang. (2012) The Scale of the Universe 2. [Online]. Available: http://htwins.net/scale2/ 

[30] D. Short, “Teaching scientific concepts using a virtual world -minecraft.” Teaching Science-the Journal of the Australian Science Teachers Association, vol. 58, no. 3, p. 55, 2012. 

[31] C. Zorn, C. A. Wingrave, E. Charbonneau, and J. J. L. Jr., “Exploring minecraft as a conduit for increasing interest in programming,” in Proceedings of the 8th International Conference on the Foundations of Digital Games, FDG 2013, Chania, Crete, Greece, May 14-17, 2013., G. N. Yannakakis, E. Aarseth, K. Jørgensen, and J. C. Lester, Eds. Society for the Advancement of the Science of Digital Games, 2013, pp. 352–359. [Online]. Available: http: //www.fdg2013.org/program/papers/paper46 zorn etal.pdf 

[32] CodeBlocks. (2012). [Online]. Available: https://dev.bukkit.org/ bukkit-plugins/codeblocks/ 

[33] D. Saito, H. Washizaki, and Y. Fukazawa, “Influence of the programming environment on programming education,” in Proceedings of the 2016 ACM Conference on Innovation and Technology in Computer Science Education, ser. ITiCSE ’16. New York, NY, USA: ACM, 2016, pp. 354– 354. [Online]. Available: http://doi.acm.org/10.1145/2899415.2925477

[34] K.-T. Foerster, M. Koenig, and R. Wattenhofer, “A Concept for an Introduction to Parallelization in Java: Multithreading with Programmable Robots in Minecraft,” in Proceedings of the 17th Annual Conference on Information Technology Education, ser. SIGITE ’16, D. Boisvert and S. J. Zilora, Eds. New York, NY, USA: ACM, 2016, p. 169. [Online]. Available: http://doi.acm.org/10.1145/2978192.2978243 

[35] ComputerCraftEdu. (2015). [Online]. Available: http://computercraftedu. com/ 

[36] A. Reem, J. Bana, I. Knight, E. Benson, O. Afolabi, A. Kerr, P. Blanch-field, and G. Hopkins, “Design of a math learning game using a minecraft mod,” in Proceedings of the European Conference on Games Based Learning, 2014. 

[37] K. L. Kørhsen and M. Misfeldt, “An ethnomathematical study of play in minecraft,” in Nordic research in mathematics education: Norma 14, H. Silfverberg, T. Kaerki, and M. Hannula, Eds., 2014, pp. 205–214. 

[38] A. J. Bishop, Mathematical Enculturation: A Cultural Perspective on Mathematics Education. Springer Netherlands, 1991. [Online]. Available: https:/doi.org/10.1007/978-94-009-2657-8 

[39] A. Nguyen and S. Rank, “Studying the impact of spatial involvement on training mental rotation with minecraft,” in Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems, ser. CHI EA ’16. New York, NY, USA: ACM, 2016, pp. 1966– 1972. [Online]. Available: http://doi.acm.org/10.1145/2851581.2892423 

[40] L. Floyd. (2016) Unleashing Math Thinking Power through Minecraft . Hour of Curiosity. [Online]. Available: http://www.hourofcuriosity.com/ minecraft/ 

[41] Minecraft Wiki. (2016, November) Minecraft classic. [Online]. Available: http://minecraft.gamepedia.com/Classic 

[42] ClassiCube. (2016). [Online]. Available: http://www.classicube.net/ [43] MCGalaxy. (2016). [Online]. Available: https://github.com/Hetal728/ 

MCGalaxy/releases [44] K.-T. Förster, “Raumgeometrie mit minecraft,” Beiträge zum Mathe-

matikunterricht 2012, 46. Jahrestagung der Gesellschaft für Didaktik der Mathematik vom 5.3. 2012 bis 9.3. 2012 in Weingarten, 2012. 

[45] B. Schmidt-Thieme and H.-G. Weigand, Didaktik der Geometrie fuer die Sekundarstufe I [Didactics of Geometry in Lower Secondary]. Spektrum Heidelberg, 2009, ch. Symmetrie und Kongruenz [Symmetry and Congruence], pp. 187–214. 

[46] E. Eggeling, “Foerderung ausgewaehlter Aspekte der Raumvostellung mithilfe von Geometrie-Software am Beispiel Minecraft [Promoting selected aspects of spatial reasoning with the help of geometry software, using the example of Minecraft],” B.A. thesis, Humboldt University of Berlin, Germany, December 15, 2016. 

[47] B. Schmidt-Thieme, Strukturieren - Modellieren - Kommunizieren. Leit-bilder mathematischer und informatorischer Aktivitten [Structuring -

Modeling - Communicating. Models of Mathematical and Informatical Activities]. Franzbecker, 2005, ch. Algorithmen faecheruebergreifend und alltagsrelevant? [Algorithms - Interdisciplinary and relevant Every-day?]. 

[48] K.-T. Foerster, “Integrating Programming into the Mathematics Curriculum: Combining Scratch and Geometry in Grades 6 and 7,” in Proceedings of the 17th Annual Conference on Information Technology Education, ser. SIGITE ’16, D. Boisvert and S. J. Zilora, Eds. New York, NY, USA: ACM, 2016, pp. 91–96. [Online]. Available: http://doi.acm.org/10.1145/2978192.2978222 

[49] C. Lai, R. P. McMahan, M. Kitagawa, and I. Connolly, Geometry Explorer: Facilitating Geometry Education with Virtual Reality. Cham: Springer International Publishing, 2016, pp. 702–713. [Online]. Available: http://dx.doi.org/10.1007/978-3-319-39907-2 67 

[50] A. Kovrov and M. Sokolsk, “Using virtual reality for teaching solid geometry: A case study for a cube section,” in Interactive Collaborative Learning (ICL), 2011 14th International Conference on, Sept 2011, pp. 428–433. [Online]. Available: http://dx.doi.org/10.1109/ICL.2011. 6059620 

[51] D. Lai and A. Sourin, “Visual immersive mathematics in 3d web,” in Proceedings of the 10th International Conference on Virtual Reality Continuum and Its Applications in Industry, ser. VRCAI ’11. New York, NY, USA: ACM, 2011, pp. 519–526. [Online]. Available: http://dx.doi.org/10.1145/2087756.2087856 

[52] P. Wilson, Handbook of spatial research paradigms and methodologies 1. Psychology Press, 1997, ch. Use of virtual reality computing in spatial learning research, pp. 181–206. 

[53] H. Kaufmann, D. Schmalstieg, and M. Wagner, “Construct3D: A Virtual Reality Application for Mathematics and Geometry Education,” Education and Information Technologies, vol. 5, no. 4, pp. 263–276, 2000. [Online]. Available: http://dx.doi.org/10.1023/A:1012049406877 

[54] M. Davies. (2016, August) Minecraft VR coming Oculus Rift today! [Online]. Available: https://mojang.com/2016/08/ minecraft-vr-coming-to-oculus-rift-today/ 

[55] M. Azmandian, M. Hancock, H. Benko, E. Ofek, and A. D. Wilson, “Haptic retargeting: Dynamic repurposing of passive haptics for enhanced virtual reality experiences,” in Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, ser. CHI ’16. New York, NY, USA: ACM, 2016, pp. 1968–1979. [Online]. Available: http://doi.acm.org/10.1145/2858036.2858226 

[56] ——. (2016, May) Haptic retargeting: Dynamic repurposing of passive haptics for enhanced virtual reality experiences. Extended video of the best video award at CHI ’16. [Online]. Available: https://www.youtube.com/watch?v=SiH3IHEdmR0