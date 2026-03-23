# Scaffolding Learning with Mixed Reality

Computers & Graphics 33 (2009) 34–46

Contents lists available at ScienceDirect

Computers & Graphics

0097-84 

 Corr 

E-m 

(S. Lam 

lok@cis

journal homepage: www.elsevier.com/locate/cag

Technical Section

Scaffolded learning with mixed reality

John Quarles a,, Samsun Lampotang b, Ira Fischler c, Paul Fishwick a, Benjamin Lok a 

a Department of Computer & Information Science & Engineering, The University of Florida, E301 CSE Building, P.O. Box 116120, Gainesville, FL 32611, USA b Department of Anesthesiology, The University of Florida, P.O. Box 100254, Gainesville, FL 32610-0254, USA c Department of Psychology, The University of Florida, Psychology Bldg. Room 114, P.O. Box 112250, Gainesville, FL 32611-2250, USA

a r t i c l e i n f o 

Keywords: 

Mixed reality 

Modeling and simulation 

Anesthesiology 

Psychology 

User studies

93/$ - see front matter & 2008 Elsevier Ltd. A 

esponding author. Tel.: +1352 378 2109; fax: 

ail addresses: jpq@cise.ufl.edu (J. Quarles), SL 

potang), ifisch@ufl.edu (I. Fischler), fishwic 

e.ufl.edu (B. Lok).

a b s t r a c t 

Scaffolding is a widely used educational practice in which directed instruction gradually decreases as 

student competence increases—resulting in increased independent learning. This research introduces 

and evaluates an MR-based system for technology-mediated scaffolding in anesthesia education. 

Through merging real and virtual objects, the system addresses a vital problem in merging abstract and 

concrete knowledge. To evaluate the system, a user study was conducted (n ¼ 130). Results suggest that 

MR’s merging of real and virtual spaces can offer (1) a unique level of educational scaffolding, and (2) an 

improved learning-transfer from abstract to concrete domains. 

To classify the presented system, the virtuality continuum is extended to include scaffolding. The 

presented scaffolding-space continuum classifies technology-mediated scaffolding tools along three 

orthogonal continuums: (1) virtuality, (2) information (e.g. abstract, concrete), and (3) interaction. 

Using these 3 orthogonal continuums, effective engineering approaches for technology-mediated 

educational scaffolding are described. 

& 2008 Elsevier Ltd. All rights reserved.

1. Introduction 

This research focuses on how mixed reality (MR) can enable novel scaffolded learning approaches. Scaffolding is an educational process whereby educators gradually decrease directed instruction (e.g. the level of detail of the instruction) as students become more competent at a task. This approach has been shown to promote independent learning, which is an important skill when students encounter new challenges. Although educators have implemented scaffolding for many years [1], recently there has been a need for new technologies that enable scaffolding. This research describes how MR can enable novel scaffolding tools (e.g. gradually decreas-ing the proportion of virtual objects in an MR scene as the user gains competence) that offer students vital learning benefits, such as improved training-transfer to real-world scenarios. 

To investigate how MR impacts scaffolding, this research uses MR to address an educational challenge in anesthesia education. In the anesthesia education process, many students first learn about anesthesia machines by interacting with an abstract simulation of an anesthesia machine—the virtual anesthesia machine (VAM) (Fig. 1). This simulation has been shown to be very effective in teaching students about abstract concepts such as

ll rights reserved. 

+1352 3921220. 

ampotang@anest.ufl.edu 

k@cise.ufl.edu (P. Fishwick),

invisible gas flow [2]. However, anesthesia educators have noted that some students may have difficulty transferring the knowledge from VAM to the real-world anesthesia machine. It was suggested that there was a need for additional scaffolding to facilitate a smoother transition between the VAM and the real machine. 

As a potential solution to this problem, this paper presents an MR-based scaffolding tool—the augmented anesthesia machine (AAM) (Figs. 2 and 3). The AAM combines an anesthesia machine with the widely used VAM—an interactive, web disseminated, abstract simulation of an anesthesia machine. By combining the VAM with an anesthesia machine, the AAM gives anesthesiology students the critical ability to visualize an abstract simulation of the anesthesia machine’s internal dynamic model components and invisible gas flow, while interacting with the real anesthesia machine as a tangible user interface. 

To describe how MR in general can enable scaffolding, we propose to extend the virtuality continuum [3] to scaffolding-space continuum (SSC). The SSC is made up of three orthogonal continuums: (1) the virtuality continuum, which varies from real to virtual, (2) the information continuum, which varies from abstract to concrete (e.g. the VAM is abstract and the real machine is concrete), and (3) the interaction continuum which also varies from abstract to concrete (e.g. the VAM employs 2D, abstract interaction, the real machine employs physical, concrete interac-tion). Within the space of the SSC, an effective scaffolding approach would utilize a set of systems (e.g. VAM, AAM, real anesthesia machine) along a curve or a line (e.g. interpolating between abstract and concrete as the user gains competence).

Fig. 1. The abstract VAM simulation. 

Fig. 2. The AAM visualization. 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–46 35

The research presented in this paper uses the AAM to demonstrate how MR can enable scaffolded learning and improve the overall understanding of a concept. Specifically, this paper describes:

1.

 The application of the augmented anesthesia machine [4].

 2.

 A user study conducted to evaluate the AAM’s scaffolded 

learning benefits.

 3.

 Extending the virtuality continuum to classify technology-

mediated scaffolding, such as the AAM. 

2. Previous work 

This section outlines some of the MR research that has aided in the development of the AAM and has enabled its multiple representations. Specifically, in this section we will briefly over-view: (1) tracking and registration techniques, (2) tangible interfaces, (3) magic lens displays, and (4) integrative modeling. 

2.1. Tracking and registration techniques 

Registration research focuses on solving the problem of accurately aligning virtual objects with real objects so that they appear to exist in the same space [5]. One approach to registration is to affix fiducial markers to the real objects in the scene and track them with a single camera, as implemented by ARToolkit [6]. Another approach consists of using stereo images to track retro-reflective IR markers [7]. To facilitate tracking and registration in the AAM, the system uses IR-based marker tracking for the magic lens. 

2.2. Tangible user interfaces 

A tangible interface [8] is an interface that employs real objects ‘‘as both representations and controls for computational med-ia.’’[9] For example, a classic interface for a computer simulation is a graphical user interface (GUI) in which the user clicks on buttons and slider bars to control the simulation. The main purpose of a GUI is interactive control. Like a GUI, a tangible user interface (TUI) is used for control of the simulation, but the TUI is also an integral part of that simulation—often a part of the phenomenon being simulated. Rather than just being a simulation control, a TUI also represents a virtual object that is part of the simulation. In this way, interacting with the real object (i.e. a real anesthesia machine) facilitates interaction with both the real world and the virtual world at the same time. For example, NASA engineers performed a virtual assembly using real tools in MR [10]. Through interacting with a real tool as a tangible interface, they were able to interact with the virtual objects and complete the assembly. 

2.3. Magic lens display 

Magic lenses were created originally as 2D interfaces [11]. 2D magic lenses are movable, semi-transparent ‘regions of interest’ that show the user a different representation of the information underneath the lens. They were used for such operations as magnification, blur, and previewing various image effects. Each lens represented a specific effect. If the user wanted to combine effects, two lenses could be dragged over the same area, producing a combined effect in the overlapping areas of the lens. The overall purpose of the magic lens was to show underlying data in a different context or representation. This purpose remained when it was extended from 2D into 3D [12]. Instead 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–4636

plane, boxes and spheres were used to give an alternate visualization of volumetric data. 

In mixed and augmented-reality interfaces, these lenses have again been extended to become tangible user interfaces and display devices as in [13]. With an augmented-reality lens, the user can look through a lens and see the real world augmented with virtual information within the lens’ ‘region of interest’ (i.e. defined by an ARToolkit pattern marker or an LCD screen of a Tablet PC-based lens). The lens acts as a filter or a window for the real world and is shown in perspective with the user’s first-person perspective of the real world. Thus, the MR/AR lens is similar to the original 2D magic lens metaphor, but has been implemented as a 6DOF tangible user interface instead of a 2D graphical user interface. 

2.4. Integrative modeling 

Integrative modeling—the concept of linking abstract topolo-gically based dynamic simulation models with geometric models using ‘‘desktop VR’’ is introduced in [14] and is extended in [15,16,17]. Our work with the AAM is a further extension of this concept, using mixed reality to realize the linkage with an effective form of human–machine interaction.

3. Scaffolded learning 

3.1. Definition 

Scaffolding is guided instruction that fades over time as the learner gains competence [1]. The term scaffolding is an analogy to building construction. The building is the learner’s under-standing of a concept and the scaffolding is the support to bring the learner to competency. Just as in construction, the amount of scaffolding is reduced as the learner comes closer to under-standing the concept. This scaffolding approach has been shown to increase learner’s independent learning ability. As the scaffold-ing is decreased, learners naturally take more responsibility in understanding the concepts and rely less on the scaffolding. 

3.2. Technology-mediated scaffolding 

Traditionally, scaffolding refers to teacher interaction with students, but more recently the concept has been applied to technology-mediated scaffolding [1,18] (e.g. MR-based scaffold-ing). Technology-mediated scaffolding involves designing inter-faces and systems that can fade as the user gains more understanding about how to interact with the system and about the concepts being taught. 

For example, in [18], a group of high school students were given scientific modeling software (e.g. software that aided them in creating visual models of weather patterns and fluid dynamics). When the students started using the software, there were scaffolds in the form of pop-ups that would offer to help the user understand how to use the software effectively. Over time and based on user input, these interface hints became less frequent. This scaffolding was shown to be very effective and increased their independent exploration of more advanced features in the software. 

3.3. Scaffolding with abstract and concrete representations 

In the learning process [19,20], it can be beneficial to scaffold learning with both abstract and concrete representations of a concept. Concrete representations (i.e. the anesthesia machine) 

different types of knowledge and provide different kinds of scaffolding. Research in psychology has shown that scaffolding with multiple representations that fade from abstract to concrete is beneficial in learning difficult concepts [19,21–23]. Note that throughout this paper, we are considering real devices, such as an anesthesia machine, to be concrete representations. 

Concrete Representations offer Concrete Experience— 

‘‘tangible, felt qualities of the world, relying on our senses and immersing ourselves in concrete reality.’’[20] For example, the real anesthesia machine, a concrete representation, is effective for teaching procedural concepts and psychomotor skills, such as how to physically interact with a specific anesthesia machine. It also provides tactile feedback such as the feel of the fluted knob for setting oxygen flow. Concrete representations preserve natural spatial and metric skills such as orientation, relative position, shape, and size. 

Abstract Representations offer Abstract Conceptualiza-

tion—‘‘thinking about, analyzing, or systematically planning, rather than using sensation as a guide.’’ [20] For example, the VAM, an abstract representation, teaches students about intangi-ble concepts such as invisible gas flow, which can be applied to many anesthesia machine models. Currently, students train with both the VAM and the real anesthesia machine representations to gain a broader understanding of anesthesia machines. 

The remainder of this section describes the current anesthesia machine learning process and an issue that some anesthesiology educators have experienced. Then, the next section describes how MR can offer multiple representations to scaffold some of the transfer problems with the current learning processes.

3.3.1. The VAM: an abstract representation 

In a study of closed malpractice claims, 75% of anesthesia machine-related operating room incidents resulting in patient death or permanent brain damage were due to user error [24]. The other 25% was due to machine failure. User errors occur because the anesthesia provider does not properly understand the machine, how it functions and how it should be used. In the event of an intra-operative anesthesia machine failure, without adequate knowledge about the anesthesia machine, the anesthe-sia provider may not be able to detect, identify and address the problem before patient injury occurs. For enhanced patient safety, the anesthesia provider must have a good understanding of the internal gas flows, the functions, and the relationships of the internal components within the anesthesia machine. 

To address this problem, anesthesia educators created the now widely used virtual anesthesia machine (VAM). The VAM is an interactive, online, abstract 2D transparent reality [25] simulation of the internal components and invisible gas flows of an anesthesia machine. This transparent reality approach empha-sizes internal processes and structure at the expense of visual fidelity and resulted in enhanced comprehension compared to an opaque, photorealistic instantiation of an identical model of the anesthesia machine [2,26]. Since 1999 the VAM user base has grown to 33,500 registered users and the VAM website (http:// vam.anest.ufl.edu) has 11 million hits per year. 

Since the VAM is essentially a visually labeled directed graph [27], the VAM’s abstract representation offers several major learning benefits over a real anesthesia machine:



 Users can visualize internal components usually hidden from view and track invisible gas flows in the simplified anesthesia machine interconnections.

 

 The anesthesia machine components have been spatially 

reorganized in the VAM to make the gas flow animation more 

Fig. 4. (Left) A real anesthesia machine with the flow meters (A) and the vaporizer (B) highlighted. (Right) The flow meters and vaporizer are spatially reversed in the 

abstract representation of the virtual anesthesia machine (VAM). 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–46 37

different anesthesia machine designs. This type of reorganiza-tion reflects a well-designed manual approach to graph layout.

 

 The VAM is easily disseminated using online web technologies. 

By visualizing and interacting with the VAM’s abstract representation, the user can learn how the gas particles flow between the components of the anesthesia machine. This gas flow cannot be directly observed in a real anesthesia machine. For example, consider Fig. 4. In the real anesthesia machine, there is a hidden pneumatic connection between the flow meters (A) and the vaporizer (B). By observing the real machine, a student could not learn that gas flows from (A) to (B). However, in the VAM, this pneumatic connection is: (1) visualized and (2) simplified due to the spatial reorganization of (A) and (B). The color-coded gas particles flow through the visualized piping to demonstrate the flow between (A) and (B). The VAM visualization scaffolds abstract learning for anesthesiology students—enabling students to better understand the gas flow. This kind of understanding helps anesthesia providers to operate the machine properly and safely and, in the rare event of machine failure, to quickly assess the situation and execute the best course of action for the patient. 

3.3.2. The anesthesia machine: a concrete representation 

The VAM simulation is used in parallel to practice with a real anesthesia machine in the operating room. The anesthesia machine gives students the concrete experience of physically interacting with a real anesthesia machine. They learn to interact with the machine by pressing the buttons, turning the knobs and reading the gas flow meters for example. This gives students the procedural knowledge and psychomotor skills that anesthesia providers need to safely deliver general anesthesia with a real anesthesia machine. 

3.3.3. Problems mapping between concrete and abstract 

representations 

The VAM simplifies and reorganizes physical relationships such as the relative distance, position, and orientation of the anesthesia machine’s components. Not all learners have the same learning style. While VAM helps with conceptual understanding for the majority of learners, this spatial reorganization and abstract representation may make it difficult for a subset of students to orient themselves to the real machine. As an example, 

black box photorealistic simulation, 8 out of 39 (20%) preferred the photorealistic simulation to VAM [26]. 

For example, the gas flow meter controls in the VAM (Fig. 4A) have been spatially reversed. The reason for this is that the VAM is an abstract representation—it simplifies the gas flow path to make the component relationships easier to visualize and under-stand. However, a novice student could oversimplify the concept of the meters in VAM. The student could memorize to turn the left knob CCW to increase the O2. When the student interacts with a real anesthesia machine, he or she might turn the left knob CCW and accidentally increase the N2O instead. This could result in (1) negative training-transfer and (2) setting an incorrect gas mixture. 

4. Using MR as scaffolding to merge concrete and abstract knowledge 

Training that uses only abstract and concrete representations (as in current anesthesia machine training) may be made more effective when there are additional representations that span the 

abstract and the concrete [22]. MR technology can enable these additional representations. For example, consider one of the representations implemented by the AAM in Fig. 2. The VAM components have been spatially reorganized and registered to the corresponding exterior component surfaces of the real machine. Students can visualize the gas flow in the context of the real machine with an MR display device (i.e. a magic lens). Moreover, synchronizing the gas flow simulation to the meters, settings, and gauges of the real machine allows students to interact with the simulation through their natural interaction with the real machine. By allowing users to interact with and visualize the VAM in the context of the real machine, the AAM helps users to better understand the relationships between the abstract VAM simulation and the anesthesia machine. 

Scaffolding over multiple representations (i.e. the VAM, the AAM, and the anesthesia machine) of a concept may improve overall comprehension of the concept [28]. Multiple representa-tions reduce reductive biases—the oversimplification of a concept— which is a common mistake among novice users [23], such as new anesthesiology students. The AAM combines the concrete repre-sentation of the anesthesia machine with the abstract representa-tion of the VAM. This enables multiple representations of the anesthesia machine. These representations may improve training-transfer between the abstract representation and the concrete 

Abstract Representation 

(VAM) 

Concrete Representation 

(Anesthesia Machine) 

Combined Representations 

(AAM) 

Fig. 5. The anesthesia machine learning process augmented with the AAM. The AAM bridges the learning gap between the abstract and concrete representations of the 

VAM and the anesthesia machine. 

Fig. 6. The AAM-abstract visualization shown from the user’s perspective. Inset: a 

user interacts with the real machine while viewing the resulting AAM-abstract 

visualization on an untracked Tablet PC. 

Fig. 7. A user turns a gas knob on the real machine and visualizes how this 

interaction affects the overlaid VAM simulation. 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–4638

4.1. AAM representations 

The AAM augments the current learning process with two new representations: (1) AAM-abstract and (2) AAM-concrete. These representations are intended to offer a smoother transition from the VAM’s abstract representation to the anesthesia machine’s concrete representation. This section describes the AAM’s two new representations in detail.

4.1.1. The AAM-abstract representation 

In the augmented learning process, AAM-abstract is the first representation that begins to integrate the VAM with the real machine. In this representation, users visualize the VAM but interact naturally with the real machine instead of using a mouse and sitting at a desktop computer. Users can walk freely around the real machine, turn the real knobs, and press the real buttons while visualizing the impact of these interactions on the 2D VAM simulation, displayed on an untracked Tablet PC (Fig. 6). This representation allows the user to better understand how to interact with the real machine and how the real machine interaction influences the 2D VAM simulation. This represen-tation relates the concrete and tactile experience of real machine interaction to the abstract concepts learned from the 2D VAM. 

AAM-abstract’s visualization is mostly 2D and almost identical to the VAM. The major difference is the 3D modeled anesthesia machine components that are registered to the VAM components. 

relationship between the VAM components and the anesthesia machine components. Is this AAM-D?

4.1.2. The AAM-concrete representation 

The AAM-concrete representation allows the user to take full advantage of the benefits of the MR technology. The user interacts with the real machine and visualizes the spatially reorganized VAM components registered to the corresponding components of the real machine from a first-person perspective. For the visualization, the user looks through a hand-held magic lens—a tracked 6DOF Tablet PC display. The lens acts as a see-through window into the world of the 3D simulation (Fig. 7). This visualization allows the user to see how the VAM simulation flows in the context of the real machine. 

Conceptually, the VAM components are ‘cut out’ of the VAM and ‘pasted’ over the corresponding parts of the real machine (Fig. 2). The collocation of the VAM components and the real anesthesia machine components demonstrates the relationships between the VAM and the anesthesia machine. By visualizing the collocated components, students may gain a better orientation to the layout, the function and inter-relationships of the real anesthesia machine components.

5. AAM system description 

The AAM consists of an anesthesia machine augmented with MR technology (tracking systems, magic lens). This section will describe the implementation details of the AAM system. Specifi-cally, this section will explain the details of the magic lens display and tracking technology that the AAM uses to (1) register the VAM with the real machine and (2) interact with the machine as a 

Fig. 8. A view of the anesthesia machine vaporizer (top) and the magic lens view of the vaporizer simulation (bottom) shown from the same viewpoint. 

Fig. 9. The magic lens tracking system. 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–46 39

5.1. Magic lens display 

To visualize the AAM-concrete, users look through a magic lens, a 6DOF tracked HP tc1100 Tablet PC (Fig. 8). Students can view the real machine from a first-person perspective with a registered VAM simulation shown in context with the real machine. The anesthesia machine displayed on the lens appears in the same position and orientation as the real anesthesia machine, as if the lens was a transparent window and the user was looking through it. 

However, the lens in the AAM is not actually see-through. There are no cameras mounted on the lens that would allow the user to see through the lens. Instead of visualizing the real machine directly through the lens, the user sees a high-resolution scale 3D model of the machine that is registered to the real anesthesia machine. Using the lens’s position and orientation information along with the pre-computed position of the real machine, the lens can display the 3D model of the machine from a perspective that is consistent with the real machine. Thus, to the user, the lens appears to be see-through. We decided against using true video see-through for two reasons: (1) ergonomics: it would increase the hardware and weight of the lens and (2) registration between the simulation and the machine would be less stable with video see-through. However, in the future we will explore other display options such as a true video see-through magic lens or a head mounted display. 

5.2. Tracking systems 

There are two separate tracking systems used in the AAM. One system tracks the position and orientation of the magic lens, while the other system tracks the settings, meters, and gauges of the real anesthesia machine—Modulus II (Ohmeda, Madison, WI.) These enable the anesthesia machine to be used as a tangible user interface (TUI) for the visualized VAM simulation. 

5.2.1. Tracking the magic lens 

To track the position and orientation of the magic lens, the AAM tracking system uses an outside-looking-in optical tracking technique (Fig. 9). The tracking method is widely used by the VR/MR community [7]. The lens tracking system consists of two stationary webcams (Unibrain Fire-I, 640 480, 30 FPS) with software that calculates the position of retro-reflective markers that are attached to the objects being tracked (i.e. the magic lens). The specifications of the system are as follows: tracking volume: 555 m; accuracy: 1 cm; jitter: 5 mm; latency: 70 ms. 

To maintain the window metaphor, the 3D graphics displayed on the lens must be rendered consistently with the user’s first- 

perspective on the lens, the tracking system tracks the 3D position and orientation of the magic lens display and approximates the user’s head position. 

5.2.2. Tracking the anesthesia machine’s settings, meters, and gauges 

To enable the anesthesia machine as a TUI, the abstract simulation is synchronized to the real machine. To perform this synchronization, the AAM tracking system monitors the settings and output (i.e. gas meters, pressure gauges, knobs, buttons) of the real machine and uses them to drive the simulation. An OpenCV [29]-driven 2D optical tracking system with 3 webcams is employed to detect the states of the machine. State changes of the settings are detectable as changes in 2D position or visible marker area as long as the cameras are close enough to the tracking targets to detect the change in position. For example, to track the machine’s knobs and other input devices, retro-reflective markers are attached and webcams are used to detect the visible area of the markers. The machine’s pressure gauge (bright red needle over black background) and bag are more difficult to track since retro-reflective tape cannot be attached to them. Thus, the gauge and bag tracking system uses color-based tracking (i.e. the 2D position of the bright red pressure gauge needle). 

Many newer electronic anesthesia machines provide a quasi-real time digital output (e.g., RS-232) of their internal states. With these machines, optical tracking of the machine components may not be necessary. This minimizes the hardware and makes the 

Table 1 Layout, display, and interface details for each condition. 

Condition Abstract simulation 

layout 

Display Interface 

VAM Diagram Desktop PC Mouse 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–4640

will likely use one of these newer anesthesia machines and eliminate optical tracking of the anesthesia machine components. This optical system was used for prototyping purposes. Surpris-ingly, we found that the optical system was quite effective and robust, as will be demonstrated by the user study section that follows.

AAM-MR Registered to 

machine 

6DOF magic lens Anesthesia machine 

AAM-D Registered to 3D 

machine model 

Desktop PC Mouse and keyboard 

AM-R Not displayed No display Anesthesia machine 

AM-D Not displayed Desktop PC Mouse and keyboard

6. User study 

A study was conducted to determine if MR’s merging of real and virtual spaces could effectively scaffold the user’s transfer of abstract knowledge to a concrete domain. We conducted a between-subjects user study over a period of two academic semesters with 130 participants. Participants completed a learn-ing session with one of the following: (1) the VAM (VAM group), (2) AAM-concrete (AAM-MR group), (3) a desktop-based version of the AAM (AAM-D group), (4) a desktop simulation of the real anesthesia machine (AM-D group), or (5) the real anesthesia machine itself (AM-R group). In the study, we wanted to investigate how the combined representation of AAM-concrete would scaffold anesthesia machine understanding and transfer to the real machine. 

Hypotheses: 

H1. If the simulations are ordered by level of abstraction (e.g. from highest to lowest—(1) VAM, (2) AAM-D, (3) AAM-MR, and (4) AM-D and AM-R), then they will gradually fade out abstract concepts. This will enable abstract concept learning to be effectively scaffolded (i.e. faded). 

H2. The AAM-concrete will improve transfer to the real machine by enabling the merging of abstract and concrete knowledge. 

6.1. Population and study environment 

There were 130 participants in this study. All the participants were college students in an Introductory Psychology class. Students in this class are required to participate in a number of studies for credit in the course. Thus, all the participants received credit for their participation in the study. The study protocol was approved prior to data collection by the University of Florida IRB (]2007-U-688). The study was conducted in a quiet, air-condi-tioned room. In each study session, there was one participant and one investigator in the room for the duration of the session. 

6.2. Study conditions 

This study was conducted over two academic semesters. Because some additional metrics were added in the second semester, the VAM group and the AAM-MR group conditions were repeated, which is why these conditions include more partici-pants. This section explains the details of each experimental condition and Table 1 shows the details of layout, display, and interface for each condition. Each participant was taught anesthe-sia concepts in one of the following conditions:



 VAM group: The VAM group (n ¼ 38) was trained using the VAM. They visualized and interacted with the VAM’s abstract representation using a desktop computer and a mouse. The details of the VAM are explained in Section 3.3.1.

 

 AAM-MR group: The AAM-MR group (n ¼ 39) was trained using 

AAM-concrete. Participants used a tracked, 6DOF magic lens to visualize an abstract simulation superimposed over a model of the real machine, which was registered to the real machine 

adjusted the real anesthesia machine controls. The details of AAM-concrete are explained in Section 4.

 

 AAM-D group: The AAM-D group (n ¼ 18) was trained using a 

desktop version of AAM-concrete. Participants visualized the same abstract simulation superimposed over a scale machine model, but they viewed it on a desktop computer. Participants used a mouse and keyboard to interact with the abstract simulation and to navigate the 3D space. 2D interaction with the simulation was identical to the VAM but the 3D rendering was identical to the magic lens. The purpose of this condition was to discover the benefits of the magic lens and real machine interaction by comparing this group to AAM-MR.

 

 AM-R group: The AAM-R group (n ¼ 20) was trained using a 

real anesthesia machine with no additional visualizations or simulation. They physically interacted with the controls (e.g. physical knobs and buttons) of the anesthesia machine and observed the meters and gauges. The details of the anesthesia machine can be found in Section 3.3.2.

 

 AM-D group: The AM-D group (n ¼ 15) was trained using a 

desktop-based photorealistic simulation of an anesthesia machine (i.e. the same real anesthesia machine that group AM-R and AAM-MR used). The AM-D simulation is similar to an interactive video. Participants used the mouse to interact with the anesthesia machine simulation from a fixed view-point. The purpose of this condition was to investigate the benefits of haptics in the anesthesia machine and determine if the same benefits exist in the AAM-MR group. 

6.3. Study procedure 

For each participant, the study was conducted over a period of 2 consecutive days to minimize the contribution of superficial and short-term learning to performance. The first day included several spatial cognitive tests and an anesthesia machine training module. The second day included 2 tests on anesthesia machines: a written test and a hands-on test with the real machine. The second day also included several questionnaires about subjective opinions of the learning module and personal information (i.e. computer usage and experience, GPA, etc.). 

Prior to arriving to the study, participants were unaware of all the details of the study (i.e. they did not know it was about anesthesia machine training). When they arrived, they were given an informed consent form that gave them an overview of the study procedure. The procedure is as follows: 

Day 1 (90 min session) 1. Introduction to the anesthesia machine (10 min): Once 

participants finished the informed consent process, they were asked to put on a white lab coat so that they would ‘‘feel more like an anesthesiologist.’’ The lab coat was also used to reduce 

Table 2 Study conditions and metrics used per semester. 

Semester Conditions Metrics used 

Fall AAM-MR (n ¼ 20), VAM 

(n ¼ 20), AM-R (n ¼ 20) 

Time to complete 5 exercises, spatial 

cognition tests, short answer anesthesia 

machine test, multiple choice anesthesia 

machine test, fault test 

Spring AAM-MR (n ¼ 19), VAM 

(n ¼ 18), AAM-D (n ¼ 18), 

AM-D (n ¼ 15) 

Spatial cognition test, machine component 

identification test, machine component 

function test, matching test, short answer 

anesthesia machine test, multiple-choice 

anesthesia machine test, fault test 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–46 41

with the color trackers. Participants were handed a manual which provided them an introduction to the VAM. The manual was used in conjunction with an online interactive tutorial (http://vam.anest. ufl.edu/simulationhelp.html), which highlighted and explained each of the major VAM components and subsystems. 

2. Complete 5 exercises (60 min): Each participant completed the same 5 exercises by following the manual and either interacting with the VAM or AAM-concrete. Each of the exercises focused on a specific anesthesia machine concept (i.e. a particular component or subsystem). This exercise was timed. 

3. Spatial cognition tests: (20 min): Participants were given 3 tests to assess their spatial cognitive ability: (1) the arrow span test, (2) the perspective taking test, and (3) navigation of a virtual environment. Each of these is outlined in [30]. 

Day 2 (60 min session) 

1. Self-evaluation (5 min): Participants were asked to rate their proficiency in overall anesthesia machine understanding that was gained from the previous day. 

2. Machine component identification test (5 min): This was used as a metric for memory retention. 

3. Machine component function test (15 min): This was used as a metric for memory retention and abstract understanding. 

4. Matching tests (5 min): This test was a metric for training-transfer. 

5. Short answer anesthesia machine test (15 min): This was a metric for abstract understanding. 

6. Multiple-choice anesthesia machine test (5 min): This was a metric for abstract understanding. 

7. Hands-on anesthesia machine fault test (10 min): This was a metric for concrete understanding. 

8. Personal/subjective questionnaires (5 min): Participants were asked several personal questions (i.e. computer experience, GPA, etc.). 

6.4. Metrics 

Time to complete the 5 exercises: Participants were timed as they worked through the 5 main exercises. 

Machine component identification test: To assess participant memory retention of the machine components, participants were shown a picture of the simulation they used the previous day (e.g. AAM-MR group saw a screenshot from the magic lens, AM-R saw a picture of the real machine). For the 17 different components of the machine, participants were asked to identify (i.e. write the name of) each letter-labeled component. Each answer was graded out of a maximum of 4 points for a perfect answer. Points were deducted for partial or incorrect answers. 

Machine component function test: To assess participant under-standing and memory retention of the machine components, participants were shown a picture of the simulation they used the previous day (e.g. AAM-MR group saw a screenshot from the magic lens, AM-R saw a picture of the real machine). For the 17 different components of the machine, participants were asked to state the function (i.e. the purpose of each component and how it affected the gas flow). Each answer was graded out of a maximum of 4 points for a perfect answer. Points were deducted for partial or incorrect answers. 

Matching test: To assess learning-transfer to the real machine, participants were shown a picture of the real machine and were asked to match the 17 simulation components to components in the picture or name the components that could not be matched. Note that all components could be matched. Participants were allowed to use the simulation pictures from the previous 

test—for reference. Note that groups AM-R and AM-D did not complete this test because the answers would have been redundant (i.e. we assumed that if participants were shown two of the same picture of the machine, they would be able to perfectly match components between the pictures). Each answer was graded out of a maximum of 4 points for a perfect answer. All points were deducted if the component was incorrectly matched. However, often participants could not identify a match but could identify the real component. Points were awarded in this case. 

Short answer anesthesia machine test: This test consisted of 22 short answer questions, which gave a score of a participant’s abstract knowledge. The tests consisted of short answer and multiple-choice questions from the Anesthesia Patient Safety Foundation anesthesia machine workbook [31]. For example, one question asked, ‘‘Is the inhalation valve bidirectional or unidirec-tional and why?’’ To correctly answer this question, one would need a deep understanding of the flow of invisible gasses in the machine and the function of the valves. Each question was graded out of a maximum of 4 points for a perfect answer and points were deducted for insufficient or incorrect answers. 

Multiple-choice anesthesia machine test: This test consisted of 7 multiple-choice questions, which measured the participant’s abstract knowledge. The tests consisted of multiple-choice questions from the Anesthesia Patient Safety Foundation anesthe-sia machine workbook [31]. For example, one question asked, ‘‘Is the CO2 absorber bidirectional?’’ Each question was worth 1 point for a correct answer and 0 points for an incorrect answer. 

Hands-on anesthesia machine fault test: For this test, partici-pants used only the anesthesia machine without any type of computer simulation. The investigator first caused a problem with the machine (i.e. disabled a component). Then the participant had to find the problem and describe what was happening with the gas flow. Participant performance on this test was assessed on one metric: if the participant was able to identify the problem causing the machine fault. Participants were given as much time as they needed and stopped when they either identified the problem or quit. In the first semester (Table 2), participants were told that there was a fault and that they had to diagnose it. In the second semester, the difficulty of this test was increased by telling the participants that there may or may not be a fault present. In general, this test assessed the participants’ concrete knowledge of the machine.

6.5. Results 

This section presents a meta-analysis of the results because not all conditions were conducted for both semesters and some metrics changed between semesters (Table 2). The matching 

metric was not included during the first semester. Furthermore, the fault test procedure was made significantly more difficult during the second semester (see Section 6.4), which resulted in

Table 3 Univariate ANOVA tests (pair-wise differences shown). 

Conditions 

compared 

Time to 

complete 5 

exercises 

Machine 

component 

identification test 

Machine 

component 

function test 

Matching 

test 

Short answer 

anesthesia 

machine test 

Multiple-choice 

anesthesia 

machine test 

Fault test 

(w2) 

AAM-D–VAM – 0.460 0.074 0.875 0.577 0.229 – 

AM-D–VAM – 0.005 o0.001 – 0.016 0.297 – 

AM-D–AAM-D – 0.036 0.051 – 0.065 0.907 – 

AAM-MR–VAM o0.001 0.147 0.021 0.054 0.077 0.967 0.082 

AAM-MR–AAM-D – 0.499 0.635 – 0.242 0.214 – 

AAM-MR–AM-D – 0.127 0.119 0.037 0.434 0.280 – 

AAM-MR–AM-R 0.002 – – – – – 0.006 

VAM–AM-R 0.324 – – – – – o0.001 

Average Function Understanding 

0 

0.5 

1 

1.5 

2 

2.5 

3 

VAM 

Sc or 

e 

AAM-D AAM-MR AM-D 

Fig. 10. Average function (abstract concept understanding) scores. 

Table 5 Machine component identification test results. 

Group Average score per question St. dev. 

VAM 1.73 0.74 

AAM-D 1.55 0.59 

AAM-MR 1.39 0.58 

AM-D 1.02 0.81 

AM-R – – 

Table 4 Time to complete the 5 training exercises results (first semester). 

Group Average minutes St. dev. 

VAM 21.5 5.49 

AAM-D – – 

AAM-MR 35.6 15.68 

AM-D – – 

AM-R 23.1 4.67 

Table 6 Machine component function test results. 

Group Average score per question St. dev. 

VAM 2.24 0.92 

AAM-D 1.72 0.72 

AAM-MR 1.58 0.83 

AM-D 1.12 0.83 

AM-R – – 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–4642

very few second semester participants correctly diagnosing the fault, regardless of condition. Only the first semester fault test results are presented here. Also, note that the spatial ability test results and personal/subjective questionnaire results are omitted since there were no significant differences between groups with regards to these metrics. Because of these differences, there is no data for certain metrics (depending upon the semester) and some data has yet to be analyzed. A dash denotes that there is no data for that condition and n/a denotes that the data has yet to be analyzed. 

6.5.1. Results of time to complete 5 exercises 

AM-R and VAM groups’ training times were not significantly different. However, VAM Group (compared to AAM-MR: po0.001) and AM-R group (compared to AAM-MR: p ¼ 0.002) performed significantly faster than AAM-MR in completing the 5 training exercises on the first day (Table 4). The VAM’s decreased training time highlights that the VAM is more efficient for teaching abstract concepts, as will be supported by results in Section 6.5.2. The AM is more efficient at teaching procedural concepts as will be shown in Section 6.5.3. However, note that in each of the conditions training time had little correlation to other metrics, such as written tests and fault tests. 

Note that the AAM group had more variance in training time and an increased average time. Some AAM group participants trained for significantly longer times (e.g. two standard deviations higher the average) than the typical AAM group participant. It is possible that some participants were more interested in the AAM interaction and spent more time visualizing the machine with the magic lens. It is also possible that training time increased due to the increased complexity of the visualization. Finally, it is possible that AAM group spent additional time mentally merging the visualization concepts with the real world. However, more work will be needed to determine the cause of increased training times. 

6.5.2. Results of abstract concept understanding metrics: machine 

component identification test, machine component function test, 

short answer anesthesia machine test, multiple-choice anesthesia 

machine test 

There were significant differences between the study groups (Table 3) for measures of abstract concept understanding. These metrics include: machine component identification test (Table 5), machine component function test (Fig. 10, Table 6), short answer anesthesia machine test (Table 7), and multiple-choice anesthesia machine test (Table 8). Note that these tests assessed mostly abstract knowledge. Refer to Section 6.4 for details about each metric. 

The averages of the data suggest that abstract concept understanding decreases with the level of abstraction of the 

Table 7 Short answer anesthesia machine test results. 

Group Average score per question St. dev. 

VAM 1.83 0.73 

AAM-D 1.71 0.57 

AAM-MR 1.45 0.67 

AM-D 1.27 0.47 

AM-R n/a n/a 

Table 8 Multiple-choice anesthesia machine test results—not significant. 

Group Average score per question St. dev. 

VAM 0.39 0.15 

AAM-D 0.30 0.16 

AAM-MR 0.39 0.21 

AM-D 0.31 0.23 

AM-R n/a n/a 

Table 9 Fault test results (first semester). 

Group # Participants correctly diagnosed 

VAM 3 of 20 

AAM-D – 

AAM-MR 9 of 20 

AM-D – 

AM-R 18 of 20 

Table 10 Matching test results. 

Group Average score per question St. dev. 

VAM 2.56 0.95 

AAM-D 2.50 0.99 

AAM-MR 3.12 0.84 

AM-D – – 

AM-R – – 

Average Matching 

0 

0.5 

1 

1.5 

2 

2.5 

3 

3.5 

VAM 

Sc or 

e 

AAM-D AAM-MR 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–46 43

trains abstract concepts the most effectively. The AM-D, a photorealistic simulation, is arguably the least abstract of the four conditions in Fig. 10 and trains abstract concepts the least effectively. A student might progress through the simula-tions in the order of decreasing level of abstraction (i.e. (a) VAM, (b) AAM-D, (c) AAM-MR, and (d) AM-D). Then as the student progresses through using each of the systems, the scaffolds of abstraction are gradually removed. The results support hypothesis (H1)—with decreasing level of abstraction, the simulations fade 

abstract concepts, thereby enabling abstract concept learning to be 

effectively scaffolded. 

It is important to note that among the abstract concept understanding metrics, there are not significant differences between AAM-D and AAM-MR (p ¼ 0.64). This suggests that these two types of systems are mostly interchangeable with respect to abstract concept understanding.

Fig. 11. Average matching (learning-transfer) scores.

6.5.3. Results of fault test results 

The fault test assessed participants’ concrete knowledge of the machine by forcing them to interact with the machine without the use of a simulation. In this test, the participant was first sent outside of the room. The investigator then removed a small, yet vital piece of the inhalation valve (called the leaflet) thereby allowing gas to abnormally flow in both directions through the valve. This simulated an incompetent valve. In a real scenario, this failure would cause the patient to rebreathe carbon dioxide. When participants returned to the room, at first glance the system appeared to be operating normally (i.e. there were no alarms sounding). Participants had to detect and identify that a small piece was missing from the inhalation valve. 

Results show that there was a significant difference (Table 3) between the groups in the performance of the fault test (Table 9). AM-R group found the faults the most frequently. VAM group found faults least frequently. AAM-MR group’s frequency was between that of AM-R and VAM. Results suggest that increased real machine exposure increases fault detection ability. That is, as abstract concepts are ‘‘faded out’’, concrete concepts are also ‘‘faded in,’’ which creates a smooth transition between abstract and concrete. In this case, MR can be used as a training-transfer interface to bridge the gap between the VAM and the real machine. 

Although the VAM may offer improved abstract knowledge, 

concrete anesthesia machine. This is precisely the concern that educators have had with the VAM and other abstract representa-tions. For example, many VAM participants understood the abstract concept of the inhalation valve and they may have correctly answered the written questions regarding the gas flow in the valve (i.e. the example question from Section 6.5.2). However, during the fault test, they could not perform the mental mapping between the abstract representation of the VAM inhalation valve and the concrete representation of the real anesthesia machine inhalation valve. Thus, it was difficult for VAM participants to apply their abstract knowledge to a concrete problem, such as the problem presented in the fault test. 

In contrast to the VAM’s abstract representation, the AAM-MR is a combination of abstract and concrete representations. This combined representation enables the fading out of abstract concepts and the fading in of concrete concepts. This suggests 

that the MR-based scaffolding tools (such as AAM-concrete) may aid 

in the merging of abstract and concrete knowledge.

6.5.4. Results of matching test results 

There were significant differences between the groups in the matching metric—the primary metric learning-transfer (Table 10, Fig. 11). The matching metric directly assessed participants’ ability to map the simulation components to the corresponding real 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–4644

significantly better matching scores than VAM group (p ¼ 0.054). Surprisingly, AAM-MR group also had significantly better match-ing scores than the AAM-D group (p ¼ 0.037). This supports the hypothesis (H2): AAM-concrete significantly improves transfer of 

learning from abstract to concrete domains. 

Because AAM-MR group performed matching significantly better than AAM-D, this suggests that the magic lens and real machine interaction significantly improved learning-transfer. However, it is unclear why there is an improvement. Previous work suggests that MR’s compensation for low spatial cognition [32] may have an impact on this matching ability. In order to visibly highlight each component in the screenshots of AAM-MR and AAM-D (i.e. for the identification and function metrics), the viewing perspective of the OpenGL camera had to be changed. Participants used these images for reference when performing the matching. These changes in perspective may have confused the AAM-D participants with low spatial cognition. In contrast, because AAM-concrete has been shown to compensate for below-average spatial cognition abilities [32], the AAM-MR group likely did not experience this confusion.

6.6. Discussion of proposed usage of simulations for scaffolding 

It is important to note that each of the simulations (e.g. VAM, AAM-MR) used in the study have specific benefits. Each offers a different representation of an anesthesia machine and each representation offers a different type of merged abstract and concrete knowledge. This knowledge is scaffolded through the fading of (1) level of abstraction, (2) level of interaction (e.g. 2D and 3D), and (3) proportion of virtual and real objects. Because each of the simulation types offers different scaffolds, we propose that all of these simulation types should be used progressively in the learning process. 

Although each of these simulation types offers different knowledge types to the user, it is not clear how to order the usage for optimal scaffolding. For example, instead of fading abstraction, concreteness could be faded instead. To fade concreteness, a user might progress through the simulations in the following order: (1) AM-D, (2) AAM-MR, (3) AAM-D, and (4) VAM. However, it is not known what the ordering or frequency of use should be for optimal scaffolding. Likely, the best approach varies from person to person and across disciplines. The important point here is that although we may not know the best way to use these technology-mediated scaffolding tools, each of the tools does offer the user additional levels of scaffolding, which other technologies may not be able to duplicate. For students, this type of scaffolding may create a smoother transition from abstract concepts to real-world scenarios.

6.7. Discussion of the scaffolding benefits of MR 

One of the main purposes of this work was to determine the specific scaffolding benefits of MR-based displays and interfaces (such as magic lenses and tangible interfaces). Critics have suggested that using a desktop-based system (such as AAM-D) may have equivalent learning benefits to an MR-based system (such as AAM-MR). This skepticism is understandable in the case of the AAM because AAM-D group’s desktop renders exactly the same visuals as the magic lens in AAM-concrete. The only differences between the systems are (1) the type of interaction and (2) the context of the rendering. Perhaps the collocated, in-context rendering coupled with collocated physical interaction helps to solidify the spatial and functional relationships between 

There is also a unique aspect of magic lenses that may improve scaffolding. The user can interactively fade the scaffolding in various ways. We have observed users ‘‘zooming out’’ and using the lens to view the whole simulation at once. Other times, users interact with the lens like a magnifying glass—inspecting details of the simulation in-context. For example, the user can observe gas flows of a specific component in the context of the real machine while still experiencing the human field of view (1201). Within the bounds of the lens, a subset of the user’s view visualizes the overlaid abstract simulation. This subset is shown within the context of the surrounding real-world view. Further-more, users can interactively choose to lower the lens and observe only the real machine. These types of behaviors are examples of the interactive fading that the magic lens interface affords. 

We have not yet performed an analysis to quantify how often participants perform these interactive fading behaviors or what effect its frequency has on their performance. However, we have observed many users performing interactive fading quite often. We expect that this interactive fading may be one of the causes for the AAM-MR group’s improved -–transfer.

7. The scaffolding-space continuum: extending the virtuality continuum 

The results of our study suggest that different simulation types offer the user different levels of scaffolding. Together, the simulations can smoothly fade abstract information in support of scaffolding. However, it is important to note that the simulations also enable fading along other continuums as well, such as virtuality and interaction. For example, along the virtuality continuum, AAM-MR would be classified as more ‘real’ than the VAM because AAM-MR has a higher proportion of real to virtual objects. To generalize this, we propose a classification system—scaffolding-space continuum—that extends the virtuality continuum specifically for technology-mediated scaffolded learning environments, such as the AAM. 

7.1. The virtuality continuum 

In 1994 Milgram coined the term mixed reality and proposed the virtuality continuum as a taxonomy of MR systems and displays [3]. The virtuality continuum ranges from real to virtual—loosely referring to the proportion of real and virtual objects in an environment. For example, if there are more real objects than virtual objects in the environment, the corresponding display may be considered an augmented-reality display. In contrast, if there are more virtual objects than real objects, Milgram might classify the corresponding display as augmented virtuality. 

However, the virtuality continuum does not classify all the system aspects of an MR-based scaffolding environment. For example, fading abstraction may be independent of fading virtual objects. By extension of the virtuality continuum, the remainder of this section proposes a classification system for technology-mediated scaffolding environments such as the AAM. 

7.2. The scaffolding-space continuum 

We propose a scaffolding-space continuum to classify technol-ogy-mediated scaffolded learning environments, such as the AAM. The scaffolding-space continuum consists of three continuums of classification (Figs. 12): (X) virtuality—extending from real to virtual, (Y) information—extending from concrete to abstract, and (Z) interaction—also extending from concrete to abstract. Each of the scaffolding systems presented in this paper can be classified 

**Information Continuum **

**AbstractConcrete **

**Interaction Continuum **

**AbstractConcrete **

**Virtuality Continuum **

**VirtualReal **

| (VAM) 

| (VAM) 

| (VAM) 

| (AAM-D) 

| (AAM-D) 

| (AAM-D) 

| (AAM-MR) 

| (AAM-MR) 

| (AAM-MR) 

| (AM-R) 

| (AM-R) 

| (AM-R) 

Fig. 12. The study simulations can be classified by each continuum of the 

scaffolding-space continuum. 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–46 45

The details of the X-axis—the virtuality continuum—have already been described in Section 7.1. The following sections will focus on the other two continuums, how the three continuums are related, and how the scaffolding-space continuum can be applied to scaffolding. 

7.2.1. Information continuum 

The information continuum varies from concrete information to abstract information. We reiterate the definition of abstract conceptualization from Section 3: ‘‘thinking about, analyzing, or systematically planning, rather than using sensation as a guide.’’ [20] Representations that teach these types of skills (e.g. under-standing the internal dynamics of a car engine) would be considered abstract. In contrast, concrete refers to ‘‘tangible, felt qualities of the world, relying on our senses and immersing ourselves in concrete reality’’ [20]. Representations that teach these types of skills (e.g. driving a car) would be considered concrete. A system will be located in a specific place along the continuum based on the proportion of abstract and concrete information being presented by the environment. For example, we might consider the AAM-concrete representation to be slightly more concrete than abstract (Fig. 12 top). 

7.2.2. Interaction continuum 

The interaction continuum varies from concrete to abstract. This continuum refers to the abstractness of the interfaces. Factors such as the interface’s generality (e.g. a mouse is a very general interface) and the dimensionality (e.g. 3D interaction is usually considered more concrete than 2D) can aid in classifying an interface’s level of abstractness or concreteness. For example, the VAM’s mouse interface is considered a very abstract interface, whereas the AAM-concrete’s anesthesia machine is considered a very concrete interface (Fig. 12 middle). 

7.2.3. Differences between continuums 

It may not be obvious that the aforementioned continuums are in fact different continuums. Based on the examples given throughout this paper, one might conclude that concrete is always congruent to real. To understand why this is not the case, consider driving in a virtual car simulation. All objects represented in the 

concrete. Similarly, one could use a mouse (an abstract interface) to interact with either virtual objects or real objects. The latter is rarely encountered but definitely possible. There are many more examples but the main point is that the three continuums differ in the types of systems that can be represented.

7.2.4. Scaffolding by movement along continuums 

One of the main principles of scaffolding is the importance of gradually fading instructional support as the learner demon-strates increased competence. In the scaffolding-space conti-nuum, this fading can be represented as gradual movement along one or more of the continuums. For example, a scaffolding solution that fades abstract concepts might utilize multiple systems classified along the information continuum. Moreover, by classifying two systems with the scaffolding-space continuum, it may become apparent whether there is a lack of scaffolds between the two systems. For example, if the VAM and the machine are classified with the scaffolding-space continuum, it becomes obvious that there are large instructional gaps along all three of the continuums. That is, using the continuums as a visual representation of a scaffolding solution, educators may be able use the scaffolding-space continuum as a guide to determine intermediary systems (e.g. the AAM) that could provide the needed instructional supports to fill the gaps.

8. Conclusions 

The AAM uses MR technology to combine a real anesthesia machine with its corresponding 2D abstract simulation—the VAM. This combination was created to resolve a critical scaffolded learning-transfer problem from the VAM to the real machine. This paper outlined the AAM’s two new representations of the anesthesia machine and presented a user study that evaluated the methods of transfer from abstract to concrete representations. As demonstrated by the study, the AAM’s new machine repre-sentations scaffold the transfer from the abstract VAM to the concrete anesthesia machine. We propose that the AAM be used as an intermediary learning module that bridges VAM training and real anesthesia machine training. 

To generalize the AAM, we proposed a classification system for scaffolding environments such as the AAM. As an extension of the virtuality continuum [3], the proposed scaffolding-space conti-nuum classifies scaffolding systems along 3 continuums: (1) virtuality, (2) information, and (3) interaction. These continuums take into account the various proportions of real to virtual objects, abstract to concrete information, and abstract to concrete interactions, respectively. Using these continuums as visual classification tools, educators may be able to determine where additional scaffolds (e.g. the AAM) should be placed. 

As previously stated, research in psychology has shown that scaffolding with multiple representations that fade from abstract to concrete is beneficial in learning difficult concepts [19,21–23]. The results of our user study with the AAM support this research and suggest that the MR’s merging of real and virtual spaces can offer (1) an additional level of scaffolding and (2) an improved learning-transfer from abstract to concrete domains. The results suggest that MR may be an effective educational scaffolding tool that 

can bridge abstract and concrete knowledge in the learning process.

Acknowledgments 

This research is supported by NSF Grant IIS-0643557. Some of 

J. Quarles et al. / Computers & Graphics 33 (2009) 34–4646

thanks goes to David Lizdas, Cynthia Kaschub, and the study participants. 

References 

[1] Oliver R, Herrington J. Exploring technology-mediated learning from a pedagogical perspective. Interactive Learning Environments 2003;11(2): 111–26. 

[2] Fischler I, Foti S, Lampotang S. Simulation and the cognitive science of learning: assessing the virtual anesthesia machine (VAM). In: Proceedings of the third of partnership in global learning conference on consolidating eLearning experiences, 2005. 

[3] Milgram P, Kishino F. A taxonomy of mixed reality visual displays. IEICE Transactions on Information Systems 1994;77:1321–9. 

[4] Quarles J, Lampotang S, Fischler I, Fishwick P, Lok B. A mixed reality approach for merging abstract and concrete knowledge. IEEE Virtual Reality 2008, Reno, NV, March 8–12, 2008. p. 27–34. 

[5] Azuma RT. A survey of augmented reality. Presence: Teleoperators and Virtual Environments 1997;(1054–7460) 6(4):355–85. 

[6] Kato H, Billinghurst M. Marker tracking and HMD calibration for a video-based augmented reality conferencing system. In: Proceedings of the second IEEE and ACM international workshop on augmented reality 1999; 11:85–94. 

[7] Van Rhijn A, Mulder JD. Optical tracking and calibration of tangible interaction devices. In: Proceedings of the immersive projection technology and virtual environments workshop, 2005. 

[8] Ishii H, Ullmer B. Tangible bits: towards seamless interfaces between people, bits and atoms. In: Proceedings of the SIGCHI conference on human factors in computing systems, 1997. p. 234–41. 

[9] Ullmer B, Ishii H. Emerging frameworks for tangible user interfaces. IBM Systems Journal 2000;39(3):915–31. 

[10] Lok BC. Toward the merging of real and virtual spaces. Communications of the ACM 2005;47(8):48–53. 

[11] Bier EA, Stone MC, Pier K, Buxton W, DeRose TD. Toolglass and magic lenses: the see-through interface. In: Proceedings of the 20th annual conference on computer graphics and interactive techniques 1993. p. 73–80. 

[12] Viega J, Conway MJ, Williams G, Pausch R. 3D magic lenses. in: Proceedings of the ninth annual ACM symposium on user interface software and technology 1996:51–8. 

[13] Looser J, Billinghurst M, Cockburn A. Through the looking glass: the use of lenses as an interface tool for augmented reality interfaces. In: Proceedings of the second international conference on computer graphics and interactive techniques in Australasia and Southe East Asia, 2005. p. 204–11. 

[14] Fishwick PA. Toward an integrative multimodeling interface: a human– computer interface approach to interrelating model structures. SIMULATION 2004;80(9):421. 

[15] Park M, Fishwick PA. An integrated environment blending dynamic and geometry models. AI, Simulation and Planning In High Autonomy Systems 2004;3397:574–84.

[16] Park M, Fishwick PA. Integrating dynamic and geometry model components through ontology-based inference. SIMULATION 2005;81(12):795. 

[17] Shim H and Fishwick PA. Enabling the concept of hyperspace by syntax/ semantics co-location within a localized 3D visualization space. Human– Computer Interaction in Cyberspace: Emerging Technologies and Applica-tions, 2007. 

[18] Jackson SL., Krajcik J, Soloway E. The design of guided learner-adaptable scaffolding in interactive learning environments. In: Proceedings of the SIGCHI conference on human factors in computing systems, 1998. p. 187–94. 

[19] Kolb DA. Experiential learning: experience as the source of learning and development. Englewood Cliffs, NJ: Prentice-Hall; 1984. 

[20] Kolb DA, Boyatzis RE, Mainemelis C. Experiential learning theory: previous research and new directions. Perspectives on Thinking, Learning, and Cognitive Styles: the Educational Psychology Series 2001:227–47. 

[21] Jacobson MJ, Archodidou A. The design of hypermedia tools for learning: fostering conceptual change and transfer of complex scientific knowledge. Journal of Learning Sciences 2000;9(2):145–99. 

[22] Jonassen DH. Instructional design models for well-structured and III-structured problem-solving learning outcomes. Educational Technology Research and Development 1997;45(1):65–94. 

[23] Spiro RJ, Feltovich PJ, Jacobson MJ, Coulson RL. Cognitive flexibility, constructivism, and hypertext: random access instruction for advanced knowledge acquisition in ill-structured domains. Educational Technology 1991;31(5):24–33. 

[24] Caplan RA, Vistica MF, Posner KL, Cheney FW. Adverse anesthetic outcomes arising from gas delivery equipment: a closed claims analysis. Anesthesiology 1997;87:741–8. 

[25] Lampotang S, Lizdas DE, Gravenstein N, Liem EB. Transparent reality, a simulation based on interactive dynamic graphical models emphasizing visualization. Educational Technology 2006;46(1):55–9. 

[26] Fischler I, Kaschub CE, Lizdas DE, Lampotang S. Understanding of anesthesia machine function is enhanced with a transparent reality simulation. Simulation in Health Care 2008;3:26–32. 

[27] Rosen KH. Discrete mathematics and its applications. 4th ed. WCB/McGraw-Hill; 1999. 

[28] Sousa M, Ebert D, Stredney D, Svakhine N. Illustrative visualization for medical training. In: Proceedings of eurographics workshop on computa-tional aesthetics in graphics, visualization and imaging 2005;11:201–9. 

[29] Bradski G. The OpenCV library. Dr. Dobb’s Journal November 2000, Computer Security. 

[30] Hegarty M, Motello DR, Richardson AE, Ishikawa T, Lovelace K. Spatial abilities at different scales: individual differences in aptitude test performance and spatial-layout learning. Intelligence 2006;34:151–76. 

[31] Lampotang S, Lizdas DE, Liem EB, Gravenstein JS. The Anesthesia Patient Safety Foundation Anesthesia Machine Workbook v1.1a. Retrieved December 25, 2007, from University of Florida Department of Anesthesiology Virtual Anesthesia Machine Web site: /http://vam.anest.ufl.edu/members/workbook/ apsf-workbook-english.htmlS. 

[32] Quarles J, Lampotang S, Fischler I, Fishwick P, Lok B. Tangible user interfaces compensate for low spatial cognition. In: IEEE 3D user interfaces 2008, Reno, NV, March 8–9, 2008. p. 11–18.