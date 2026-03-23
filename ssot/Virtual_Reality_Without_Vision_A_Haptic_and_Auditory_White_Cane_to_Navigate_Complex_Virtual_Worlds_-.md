# Virtual Reality Without Vision: A Haptic and Auditory White Cane to Navigate Complex Virtual Worlds - Microsoft

### Virtual Reality Without Vision: A Haptic and Auditory White Cane to Navigate Complex Virtual Worlds 

Alexa F. Siu 

Stanford University 

Stanford, USA 

afsiu@stanford.edu 

Mike Sinclair 

Microsoft Research 

Redmond, USA 

sinclair@microsoft.com 

Eyal Ofek 

Microsoft Research 

Redmond, USA 

eyalofek@microsoft.com 

Christian Holz 

Microsoft Research 

Redmond, USA 

cholz@microsoft.com 

Robert Kovacs 

Hasso Plattner Institute 

Potsdam, Germany 

robert.kovacs@hpi.de 

Edward Cutrell 

Microsoft Research 

Redmond, USA 

cutrell@microsoft.com 

ABSTRACT 

Current Virtual Reality (VR) technologies focus on render-

ing visuospatial effects, and thus are inaccessible for blind 

or low vision users. We examine the use of a novel white 

cane controller that enables navigation without vision of 

large virtual environments with complex architecture, such 

as winding paths and occluding walls and doors. The cane 

controller employs a lightweight three-axis brake mecha-

nism to provide large-scale shape of virtual objects. The 

multiple degrees-of-freedom enables users to adapt the 

controller to their preferred techniques and grip. In addition, 

surface textures are rendered with a voice coil actuator 

based on contact vibrations; and spatialized audio is deter-

mined based on the progression of sound through the ge-

ometry around the user. We design a scavenger hunt game 

that demonstrates how our device enables blind users to 

navigate a complex virtual environment. Seven out of eight 

users were able to successfully navigate the virtual room 

(6x6m) to locate targets while avoiding collisions. We con-

clude with design consideration on creating immersive non-

visual VR experiences based on user preferences for cane 

techniques, and cane material properties. 

Author Keywords 

Virtual reality; white cane; blindness; visual impairments; 

haptic feedback; auditory feedback; mobility, 3D audio 

CSS Concepts 

 Human-centered computing~Human computer inter-

action (HCI); Haptic devices 

INTRODUCTION In recent years, virtual reality (VR) technologies have pro-

liferated into the mainstream market with the promise of 

applications across industries; from entertainment, to 

healthcare and education. At the crossroads of applications, 

researchers have also begun introducing accessibility to VR 

content for people who are blind or low vision [5], [19], 

[21], [24], [39], [56], opening up VR applications to the 

quarter billion users that have currently limited to no ac-

cess. Unlike interacting with stationary and mobile devices, 

VR often requires the user to move and orient for exploring 

and navigating a virtual environment.  

To navigate during day-to-day activities in the real world, 

blind individuals typically use mobility aids, such as the 

white cane (also called a long cane). The cane conveys 

environmental information in the direct path of travel [7] by 

creating a three-dimensional spatial window. Navigating 

with the cane provides three sources of information: detec-

tion of obstacles, surface topography (e.g., textures and 

elevation), and foot-placement preview [3]. For navigation 

tasks, users may employ a variety of cane techniques as 

well as cane tips. Equally important to haptics is the sound 

feedback; often, users use echolocation cues resulting from 

their cane use or footstep sounds to determine the position 

and distance of objects [7]. 

In direct analogy, the use of a virtual white cane has previ-

ously been investigated for enabling blind users to interact 

in VR [5], [24], [27], [39], [56]. For example, Canetroller 

[56] implements a belt-mounted VR cane controller for 

blind users to perceive tapping feedback from virtual ob-

jects. Canetroller is built around a one degree-of-freedom 

magnetic particle brake that can stop horizontal cane swings 

in place combined with vibrotactile and auditory feedback, 

which showed the feasibility of supervised VR interaction 

for blind users in two sparse VR scenes. 

Permission to make digital or hard copies of all or part of this work for personal or 

classroom use is granted without fee provided that copies are not made or distributed 

for profit or commercial advantage and that copies bear this notice and the full 

citation on the first page. Copyrights for components of this work owned by others 

than the author(s) must be honored. Abstracting with credit is permitted. To copy 

otherwise, or republish, to post on servers or to redistribute to lists, requires prior 

specific permission and/or a fee. Request permissions from Permissions@acm.org. 

CHI '20, April 25–30, 2020, Honolulu, HI, USA 

© 2020 Copyright is held by the owner/author(s). Publication rights licensed to 

ACM. 

ACM 978-1-4503-6708-0/20/04…$15.00  

https://doi.org/10.1145/3313831.3376353 

Figure 1. A) A participant navigates through the experimental 

game using the prototype haptic controller. B) Rendered first-

person view of virtual environment (VE). C) Overhead map of 

VE with participant and cane (blue sphere with line). 

Figure 2. Components of our navigation cane controller. The controller renders force feedback in three orthogonal axes of mo-

tion, tactile feedback through a voice coil actuator, and spatialized audio effects through stereo headphones. 6-DOF trackers on 

the headphones and cane localize the user in virtual space and the belt fastens our controller to the body. 

In this work, we venture into larger spaces and examine the 

ability of blind users to independently navigate and explore 

large 6𝑚 × 6𝑚 virtual environments (VE) as shown in 

Figure 1. We enable this through our novel wearable cane 

controller that renders haptic feedback of surface shape, 

impact collisions, and textures, as well as spatialized audio 

based on the progression of sound through the geometry 

around the user. The multiple degrees-of-freedom enables 

users to adapt the controller to their preferred technique and 

grip style. Our VEs include walls and rooms, winding 

paths, and doorways, giving users ample freedom for mov-

ing around and exploring an unknown environment. 

The controller renders two types of haptic feedback: 1) 

kinesthetic forces using a novel lightweight three degree-of-

freedom brake mechanism. This allows users to interact 

with virtual objects to understand their shape; 2) tactile 

feedback using a voice coil actuator that conveys infor-

mation about an object’s surface properties (e.g., texture 

and perceptual hardness) or kinesthetic feedback that is too 

high in frequency for the brake mechanism to simulate. To 

produce audio feedback, we integrate a wave-based acous-

tic simulation to render geometry-aware sound effects. This 

enables users to sense effects such as occlusion of the audio 

source around a corner or get a sense of the dimensions for 

the surrounding space. We demonstrate its use with spatial 

audio beacons that represent landmarks that users managed 

to navigate to even when outside the direct line of hearing. 

To evaluate the performance of our system for conveying 

diverse non-visual information, we created a VR scavenger 

hunt game. Targets were distributed across the indoor envi-

ronment, where some of the targets had no direct line of 

audio to participants’ initial location. Participants walked 

the indoor architecture while forming their understanding of 

the VE. Seven out of eight users were able to successfully 

navigate the VE to locate all five targets while avoiding 

collisions. Moreover, users’ navigation performance in-

creased with repeated play. 

We make three specific contributions in this paper: 

1. A wearable cane controller that renders human-scale 

force feedback corresponding to a virtual environment  

using a novel three-axis brake mechanism along with 

rendering surface textures during tapping and sweeping. 

2. A simulation of virtual environments that renders physi-

cally-realistic audio effects modeled on the properties of 

the space, including geometries and materials. 

3. An evaluation that demonstrates that blind participants 

were able to integrate the various feedback modalities to 

navigate and explore a virtual environment using their 

skills from navigating the real world with a white cane. 

RELATED WORK 

Several works have investigated ways of making VR appli-

cations accessible for the blind and visually impaired. 

These have employed a combination of multimodal feed-

back through audio and haptics, as well as augmentative 

sensory substitution approaches. We review several of these 

approaches in the following sections. 

Acoustic Virtual Environments 

Several prior work has explored using acoustics to enable 

non-visual navigation in VEs. In particular, much work has 

focused on the creation of accessible auditory desktop 

games [4], [31], [32], [41], [48]. These approaches approx-

imate footsteps in the real world through keyboard naviga-

tion, and use text to speech to provide heading information, 

and distance estimation to obstacles. 

Another line of work has focused on applications for navi-

gation training with algorithms to render realistic sound 

effects. Maidenbaum et al. simulated a white cane that 

blindfolded sighted participants controlled with a mouse to 

obtain a single-point depth information (through sound) of 

the VE [26]. González-Mora et al. extended this to provide 

more information by also capturing the form and volume of 

the space in direct line of sight of the user [8]. Seki and 

Sato created a system where they could model sound reflec-

tions to convey the location of obstacles [51]. While these 

systems allowed users to navigate the VE by avoiding colli- 

sions, the information is limited. Acoustics alone cannot 

convey the shape of the virtual geometry or the material 

properties; and more importantly for navigation, users lack 

feedback from their proprioceptive senses. 

Recent advances in the gaming industry, have proposed 

efficient GPU algorithms that enable wave-based simula-

tion of sound through virtual geometry with the purpose of 

increase game immersiveness and realism [30], [40]. Com-

pared to traditional ray-based spatialized audio methods, 

wave-based acoustics is capable of capturing physics-

effects such as occlusion, reverberation, and portaling; all 

of which are important cues for echo location [7].  

Vibrotactile & Force Feedback Approaches 

Prior work has complemented audio effects with various 

modalities of haptic feedback for increasing the immersive-

ness VEs. Several approaches have used traditional VR 

controllers with vibrotactile feedback to support interaction 

with virtual elements [14], [20]. These approaches offer 

users no distinction between surfaces and thus are limited in 

only being able to convey architectural geometry (i.e. walls 

and floor). Other work has extended the use of haptics to 

also convey kinesthetic forces using a variety of haptic 

devices [49], [56]. For example, Schloerb et al. used a 

Phantom haptic device to control the position of the user’s 

avatar in the VE and provide force feedback from collisions 

with room walls [49].  

Virtual Cane Controllers to Explore VEs 

Other researchers have explored providing more intuitive 

navigation by creating simulations of a white cane [5], [19], 

[21], [24], [39], [56] used haptic systems that were ground-

ed and did not allow users to physically move and explore 

the space. On the other hand, [56], [53] used mobile weara-

ble systems. The work by Tzovaras et al. used a hand-worn 

exoskeleton that simulated contact forces from holding a 

cane. While large-scale force feedback was provided, the 

system was not able to render surface properties or realistic 

audio effects. Zhao et al. used a wearable cane (Canetroller) 

and is the closest solution to this work [57]. Canetroller 

only provides kinesthetic haptic feedback in one axis (i.e. 

stopping horizontal motion). Thus, Canetroller cannot pro-

vide meaningful feedback when holding the cane in differ-

ent styles and support the techniques necessary to success-

fully navigate more complex spaces. This constrained ap-

plications to identifications tasks. Moreover, the approaches 

presented above made use of non-directional brakes that 

needed to be released to enable the user retraction of the 

cane, generating a sense of ‘stickiness’ of the obstacles.  

We address these limitations by presenting a novel brake 

mechanism capable of rendering collision forces from the 

cane interactions in all axis. We demonstrate how these 

multidimensional cues complemented with physics-based 

audio rendering enables blind users to independently navi-

gate large spaces. 

DESIGN RATIONALE 

Several factors can vary in the use of the white cane for 

navigation: the techniques used to interrogate the environ-

ment, and the material properties of the cane shaft and tip 

and the position of the hand holding the cane grip. We re-

view the differences in these factors and how they reveal 

important design choices in creating an adaptable cane 

controller for navigation in VR. 

Cane Techniques 

Different cane techniques are used to interrogate the envi-

ronment depending on the situation [47], [56]. Two primary 

techniques most commonly used by blind travelers are the 

two-point touch technique (swinging the cane side to side, 

tapping either side in an arc) and the constant contact tech-

nique (sweeping the cane side to side while keeping the 

cane tip in constant contact with the walking surface) [13]. 

In both cases, the cane motion is within an arc slightly 

wider than one’s shoulder length. This range of motion can 

be spanned by three orthogonal axes (polar coordinates) i.e. 

motion horizontally, vertically and radially where the cane 

collisions are contact constraints which occur as large in-

stantaneous forces opposing the motion. Thus, a three-axis 

brake mechanism may be suitable to physically render vir-

tual contact constraints. 

Material Properties & Tip Styles 

Cane tips tend to fall into five categories: pencil, marshmal-

low, ball, roller, and metal glide [1], [12]. The motion of the 

cane tip over a surface transmits sound and vibration from 

its tip to the hand that is holding the grip. As such, the 

cane’s shaft and tip material properties both affect the hap-

tic sensations felt and the audio effects transmitted [44], 

[36]. For example, a metal tip may amplify both the audito-

ry and tactile high frequency vibrations felt by the user 

compared to a roller or pencil tip [12]. These properties are 

important to consider in rendering high fidelity tactile feed-

back and audio effects. 

Grip & Hand Position 

White cane users often vary the position of the hand hold-

ing the cane in relation to the midline of the body. Three 

common positions exist when holding the white cane: 1) 

held centered out in front of the body above the waist (cen-

tered high), 2) held below the waist (centered low), and 3) 

held to the side (off-center) [9],[16]. In addition, three grip 

styles are commonly used [36] (Figure 3): 1) standard grip 

where the grip is lightly held with the thumb and all other 

fingers except the index which lays flat across the grip; 2) 

pencil grip where the grip is held like a pencil; and 3) tradi-

 Figure 3. A) Traditional cane grip centered-high, B) pencil 

cane grip centered-low, C) standard cane grip centered-low. 

tional grip where the grip is held with the four fingers ex-

cept the thumb, which lays flat across the grip. Depending 

on the navigation task, users will transition between posi-

tions and grips. These indicate the need for versatility in the 

controller’s degrees-of-freedom such that various positions 

and grip styles are allowed.  

 Cane Length and Weight 

A user’s cane length is determined a priori based on the 

user’s stride, walking speed, and reflexes [17]; typically 

ranging from 115 to 165 cm [13]. An appropriate cane 

length not only provides safety but also helps in distance 

estimation. As such maintaining consistency with a user’s 

real-world cane is important to support virtual navigation. 

A cane must also be lightweight with its center of mass not 

too far from the grip, as differences in weight distribution 

can affect its use and increase user fatigue over time [44]. 

Typically, a cane’s weight is in the range of 112-200g [13]. 

SYSTEM IMPLEMENTATION 

Hardware 

Based on the design rationale, we created a virtual cane 

controller prototype. An overview of the controller proto-

type and its components is shown in Figure 2. To interact in 

VR, the user wears our controller using the waist belt that 

mounts all components and puts on a pair of stereo head-

phones. The user holds and moves the controller at the grip 

much like an actual white cane. Our prototype provides 

three primary forms of sensory feedback: 1) large-scale 

shapes of virtual objects through a three-axis brake mecha-

nism that renders kinesthetic feedback, 2) surface textures 

through a voice coil actuator that renders tactile feedback of 

contact vibrations, and 3) high-fidelity first echo and rever-

berations of sound in virtual geometries through a wave-

based acoustics simulation.  

Three-Axis Brake Design to Sustain Human-Scale Forces 

The controller grip is connected to the belt-mounted proto-

type through a guide rail and a two-axis gimbal, such that 

the user can freely slide and rotate the cane when none of 

the brakes are engaged. Figure 3 shows the versatility in 

grip and cane positions afforded by this mechanism. A 

Teensy 3.2 microcomputer with a 32-bit ARM Cortex-M4 

microcontroller drives the hardware electronics (Figure 4). 

The three-axis brake is instrumented on the guide rail to 

prevent movement of the cane grip and thus provide force 

and torque feedback to the user. The horizontal and vertical 

brake mechanisms are rigidly mounted at the base of the 

belt on a ¼" Delrin plate, while the radial brake slides with 

the cane grip (Figure 2). The guide rail is made of a square 

carbon fiber rod to prevent bending and twisting.  

To measure minimum and maximum brake torques and 

forces, the mechanism was rigidly mounted to an 80-20 

aluminum frame. Each brake was then selectively actuated, 

and the resulting force was measured 30 cm away from the 

pivot point for torques and directly on the moving brake for 

linear force using a force gauge (Extech 475044). 

Vertical Axis Brake. Figure 5 shows a close-up view of the 

vertical axis, binary and bi-directional, brake mechanism. 

The mechanism consists of a ratchet with 80 teeth per revo-

lution and two spring-loaded pawls that can be selectively 

engaged to restrict rotation of the ratchet in one direction at 

Figure 4. System Diagram of the controller electronics. 

Figure 5. Vertical Axis Brake; a binary and bi-directional 

brake. Arrow shows the axis of motion. This mechanism con-

sists of a ratchet with two pawls that can be selectively en-

gaged to select a brake direction.  

otion. This mechanism consists of a ratc et with two pawls 

that can be selectively engaged to select a brake direction. 

Figure 6. Horizontal Axis Brake. Arrow shows the axis of 

motion. This mechanism consists of a capstan with a helix-

wound cord that when either side of the cord is tensioned, 

high output forces can be rendered bi-directionally.  

Figure 7. Schematic of the capstan brake mechanism. Two 

solenoid-actuated “shoes” exert a small friction to the cord 

against the capstan to prevent rotation. 

Counter-clockwise solenoid 

Clockwise solenoid 

Low tension counter-clockwise cord brake 

Low tension clockwise 

cord brake 

Delrin helical capstan brake, 

bidirectional To PWM driver 

To PWM driver 

Vectran cord

a time. The ratchet in turn is coupled to the controller guide 

rail to restrict the user’s motion. A micro servo (HI-TEC 

HS-40) actuates a CAM to engage and disengage either of 

the two spring-loaded pawls. This brake mechanism is 

asymmetric, and the user feels minimal resistance when the 

brake is disengaged (0.024 Nm). When either pawl is en-

gaged, the user only feels resistance in one direction (great-

er than 6.01 Nm) but is free to move in the opposing direc-

tion (0.028 Nm). Table 1 shows the measured braking tor-

ques. The total range of motion is 130 

Horizontal Axis Brake. Figure 6 shows an overview of the 

horizontal axis, bi-directional, brake mechanism and Figure 

7 shows a schematic of its working principle. This design is 

based on an extension of the brake used by [53] in a hand-

held VR controller but with a variation to fit our application 

needs of a highly asymmetric brake behavior.  

A capstan brake creates high output forces through an ex-

ponential gain increase of low input forces. The output 

braking force of a capstan+cord is governed by: 

OutputCordTension = InputCordTension * e(µ * Θ)    (1) 

Where µ is the mutual friction between capstan and cord 

and Θ is the number of cord turns (radians). This braking 

device depends on the friction between a rotating capstan 

drum and fixed ends of the spiral-wound Vectran cord. The 

3” diameter x 1” tall drum is made of acetal plastic (Delrin). 

125 lb. Vectran cord and Delrin for the capstan were chosen 

for their mutual friction (static and dynamic with a very low 

stick-slip transition). This allows the brake to exert a low to 

high braking force and any force in between.  

The capstan drum is also mounted to the vertical brake 

mechanism and the two rotate together. There is a 7.5 turn 

helix milled into the outside surface of the drum to retain 

the cord. The two ends of the cord are rigidly mounted to 

the belt plate including approximately 2mm of slack. This 

slack enables the capstan to rotate with very low friction 

when the brake is not actuated. At the two cord entrances of 

the capstan are small solenoid actuated “shoes” that exert a 

small friction of the cord against the capstan (Figure 7). As 

one solenoid is actuated, this small friction resistive force of 

the cord against the capstan is exponentially increased by 

Equation (1) and causes the other end of the cord to resist 

movement with a much higher force (tension). Since the 

end of the cord opposite the solenoid brake is attached to 

the belt, the capstan drum is difficult to rotate in that direc-

tion but easy to move in the other direction. This asymmet-

ric or unidirectional brake behavior is desired, especially 

when the cane hits a barrier. The solenoid operation is near-

ly instantaneous, making the brake very fast acting. Table 1 

summarizes the braking torques. CW and CCW braking 

forces are asymmetric due to the solenoid actuating the drag 

levers being located at different offsets from the pivot point 

and undesired flexion in the levers. 

A capstan brake was chosen as opposed to the ratchet 

mechanism due to its fast actuation speed and brake force 

that can be modulated by varying the PWM signal used to 

actuate the solenoids. This flexibility is advantageous in the 

horizontal axis for generating different floor textures and 

geometry; for example, tactile domes in pavement cross-

roads, and crevices in the floor.  

Radial Axis Brake. Figure 8 shows a close view of the radi-

al axis, binary and unidirectional, brake mechanism and its 

components. The mechanism consists of a cantilevered 

rubber pad actuated by a solenoid (Uxcell a14092600 

ux0438). When the solenoid is engaged, the rubber comes 

in close contact with the guide rail and generates enough 

friction to engage and amplify the braking force to restrict 

sliding of the grip cane in the distal direction. The total 

range of motion is 610mm. Table 1 summarizes the braking 

forces. Compared to the vertical and horizontal axis brakes, 

the radial brake can only restrict motion in one direction. 

For our system, this is adequate since there are rare scenari-

os where preventing motion of the cane in the direction 

towards the user is necessary.  

Weight Distribution. The entire device weighs 1.87 kg. To 

reduce the load on the belt, users wear a shoulder harness 

which helps distribute the weight to the shoulders (Figure 

2). However, due to the multiple components instrumented 

along the cane handle, the weight distribution of the cane is 

Brake Axis Object Location Action Torque [Nm] 

Horizontal 

Disengaged 0.072 

Counter-

Clockwise 

Collision > 4.504 

Moving Away 0.082 

Clockwise Collision > 2.655 

Moving Away 0.082 

Vertical Disengaged 0.024 

Top/Bottom Collision > 6.01 

Moving Away 0.028  Force [N] 

Radial Disengaged 0.405 

Front Collision > 15 

Moving Away 0.81 

Table 1. Unidirectional brake forces in the direction of the 

braking force and in the opposing direction. All measurements 

were taken 30 cm away from the pivot point. 

. 

 Figure 8. Radial axis brake; a binary and unidirectional 

brake. Arrow shows the axis of motion. This mechanism has 

an actuated friction pad that when in contact with the rail 

generates enough friction to engage and amplify the force to 

restrict sliding of the grip. 

offset from the grip. Thus, we included a constant force 

spring (6.3N) attached between the guide rail and the waist-

mounted belt to reduce the device’s apparent weight. The 

controller with the voice coil, radial brake, and VIVE track-

er together weigh 378 g. With the constant force spring, the 

perceived weight can be adjusted by moving the spring 

further or closer to the pivot point.  

Power Consumption. A battery pack (TalentCell 

YB1206000) mounted to the belt is used to power the 

hardware electronics. The battery pack has two outputs: 1) 

5V USB, 12000 mAh and 2) 12V, 6000mAh. The 5V USB 

output is used to power the servo motor; while the 12V 

output is used to power the solenoids for the remaining 

brakes and amplifier for the voice coil actuator. Table 2 

summarizes power consumption requirements based on 

active components. A typical scenario with two axes en-

gaged and texture rendering consumes 0.6A. 

Position Tracking 

To track the position of the user in the virtual environment 

as well as the cane movements, we use an HTC VIVE 

Lighthouse system [10]. Two VIVE tracker v2.0 units are 

used, one attached to the stereo headphones worn by the 

user and another attached to the cane controller. The use of 

a head mounted display (HMD) for visual feedback is diag-

nostic and is optional. 

Software 

We developed an application developed in Unity 2019.2.0 

to interface with the VIVE trackers and render the appro-

priate haptic and auditory feedback to the user based on 

their position and that of the cane. Brakes are selectively 

engaged depending on the dominant axis of the collision. 

Audio and textures are also played dependent on the impact 

velocity, and material properties of the colliding object. 

Texture Rendering 

Our three-axis brake mechanism described above profi-

ciently portrays large-scale forces for shape discrimination 

but lacks the capability for rendering the high-frequency 

accelerations that occur upon contact collisions and sweep-

ing of fine surface textures. Rendering impact forces has 

been shown be a better predictor of perceptual hardness 

compared to stiffness [14]. To address this, we connect an 

amplifier (DROK TDA7297W) to a voice coil actuator 

(Dayton Audio DAEX25FHE-4) capable of rendering a 

broad spectrum of acceleration frequencies [6], [23], [45]. 

The impact vibration and texture frequencies rendered to 

the user were modeled based on data recorded in the real 

world of different sample surfaces (e.g., concrete, metal, 

plastic, hardwood, and carpet); samples are shown in Figure 

9.  For all recordings, we use a carbon fiber cane with a 

metal glide tip distributed by the National Federation for 

the Blind (NFB) [35]. We mount a triple-axis accelerometer 

to the end of a white cane shaft (ADXL335) and record 

tapping and sweeping motions on the sample materials [46]. 

We then converted the voltage to acceleration data using 

calibration constants. To generate a compatible audio sig-

nal, we reduced the three-axis signal to one using principal 

component analysis (PCA) to determine the axis with the 

largest signal energy [14]. Although more recent methods 

have been proposed for generating data-driven texture 

models that make use of vibrations in all three-axes [45], 

we chose this one for its simplicity and good fidelity [46].  

Each virtual object is then tagged with a recorded tapping 

texture and sweeping texture. When the virtual cane moves 

across the surface of a virtual object, the tapping texture is 

played back through the voice coil actuator with its ampli-

tude adjusted proportional to the impact velocity. In addi-

tion, if the cane sweeps on the object, the sweeping texture 

playback rate is rendered and modulated based on the speed 

of the cane tip. If the non-moving cane is simply in static 

contact with an object, we should expect and get no texture. 

Sounds Effects and Wave-Based Acoustics Simulation  

For sound effects generated from collisions and the sweep-

ing motion of the virtual cane, we also recorded data from 

real-world material samples (Figure 9). The same NFB 

carbon fiber cane with a metal glide that was used for re-

cording textures was used for recording the sound effects. 

Tapping and sweeping sounds were recorded with a micro-

phone in an outdoor environment to mitigate sources of 

acoustic reflection. The recordings are then filtered to re-

duce background noise and clipped to retain only the rele-

vant sound signal. For sound clips of sweeping motion, the 

ends of the sample are manually adjusted with a synthesizer 

to achieve smooth playback when looping. 

 Figure 9. Sample material tiles used to record texture models 

and sound. A) Concrete, B) metal (aluminum), C) hardwood 

tile, and D) short carpet. 

Brake States Current [mA] 

None engaged 45.0 One brake engaged 323.5 

Typical use (2 axes engaged + 

voice coil actuator rendering tex-

ture) 

600.0 

Voice coil with highest frequencies 

texture (concrete)  

100.0 

Table 2. Prototype power consumption. 

We integrated Project Acoustics [38] as the primary acous-

tics engine to render high-fidelity spatialized audio. This 

engine models sound wave effects (e.g., occlusion, rever-

beration, portaling) in complex room geometry [40]. The 

simulation is baked a priori with respect to the scene geom-

etry. To accomplish this, all geometry in the virtual scene is 

first assigned absorption coefficients based on the desired 

material properties. The scene is then voxelized and the 

simulation is computed at discrete listener probes in the 3D 

space. The results are registered to the scene and at runtime 

interpolated based on the user’s location and the nearest 

probe locations [40]. In addition to the spatialized audio, 

the volume is also modulated proportional to the impact 

velocity of the cane with collisions. The same workflow 

used for rendering textures is used in this case for determin-

ing which sounds effects are played. 

Surface Foot Preview 

With the components described above, we are only able to 

provide feedback to the user when they’re in contact with 

the cane grip. No feedback is provided relative to the user’s 

body. This means that a user lacks feedback from foot 

placement, for both texture and elevation changes. While 

the cane brake may be engaged to indicate the presence of 

an obstacle, the user is still able to move their body. 

USER EVALUATION 

To evaluate the fidelity of the cane simulation, we designed 

a scavenger hunt game in VR. Participants navigated the 

virtual environment using the cane simulation with two 

tasks in mind: 1) to collect targets, and 2) to avoid walking 

over hazards and virtual walls. Targets gave participants 

structure to navigate the virtual environment; and hazards 

and walls encouraged careful and intentional navigation. 

Evaluation goals 

Through our evaluation, we wanted to understand if and 

how participants could explore the virtual world using our 

non-visual rendering. We were interested in two questions:  

1) Does the simulation provide sufficient sensory infor-

mation through both haptic and auditory channels to enable 

users to independently navigate and understand the space? 

In visual VR experiences, increased realism has been linked 

with improved acquisition of spatial knowledge [31]. We 

hypothesized that the multisensory feedback provided in the 

simulation could simultaneously give the environment 

semantic value and thus help users navigate. In particular, 

we wanted to understand if the wave-based acoustics simu-

lation enabled participants to directly navigate towards 

audio beacons even if such beacons were outside a direct 

line of hearing; and if together with the haptic cues, partici-

pants would be able to understand both global geometry 

and local surface properties.  

2) Can participants apply the same knowledge and skills in 

using their (physical) white cane to effectively navigate the 

VE using our virtual cane? Does our simulation provide 

enough realism (haptic, audio, grip, feel, etc.) for partici-

pants to employ the same techniques they use with a real 

cane to navigate the architectural landmarks in the game? 

Game Mechanics 

The virtual scavenger hunt was set in a virtual building with 

a walking area of 6.1𝑚 × 6.1𝑚 (Figure 10) and two distinct 

spaces: 1) a small carpeted room of 3.9𝑚 × 2.1𝑚 with a 

doorway and a radio playing a podcast, which we included 

to introduce an additional distinct localization cue; 2) an 

open outdoor area with a winding concrete sidewalk lead-

ing into the small room. Participants were told that the 

concrete sidewalk was a “safe zone” where they would not 

encounter hazards, although targets could appear anywhere. 

All walls were rendered as drywall material.  

Participants’ primary task in the game was to collect all five 

targets. Targets appeared sequentially once the previous 

target was collected. Figure 10 shows the location of each 

target numbered in the order in which they appeared. Tar-

gets emitted a distinct sound of techno music that acted as 

an audio beacon which participants could orient to. In addi-

tion, all targets were rendered as cubes (355.6mm per side) 

and sounded like drums when tapped. To collect a target, 

participants had to walk over it. 

Participants were also told to avoid walking over hazards 

and colliding with virtual walls. Unlike targets, hazards did 

not emit beacon sounds. However, they did have a distinct 

shape and material that could be detected by the cane. Haz-

ards were rendered as metal cubes (255mm per side). Tap-

ping or sweeping against them resulted in a metallic clink-

ing sound and texture rendering.  

In addition to the sound effects from the cane tapping or 

sweeping across the various game elements, feedback was 

provided when a participant collected a target or collided 

with walls or hazards. Collecting a target played a reward 

sound of collecting coins. Colliding with a wall played a 

mild explosion sound. Colliding with a hazard played a 

more alarming cartoon-like explosion sound. 

 Figure10. Dimensioned game room drawing (in meters). 

Because the cane’s brake was grounded to the participant’s 

torso, it was not uncommon for the cane to pass into walls 

or other objects as participants walked or pivoted their 

bodies. To help resolve the confusion this could generate, 

whenever the cane was “inside” a virtual object or wall, our 

cane would “lock up” by activating all three brakes until the 

cane was outside the obstacle (usually achieved by physi-

cally walking or turning back). This helped participants to 

verify the location and solidity of objects and gave them an 

additional means of testing their environment with the cane.  

Rationale 

We conducted our evaluation as a scavenger hunt, as it left 

participants’ exploration strategies mostly unconstrained, 

while game elements provided some degree of structure. 

Games have been used in virtual environments for implicit 

learning before [31],[26] as they lead to more immersive 

exploration. In designing the game layout, we included 

game elements based on the four APH mobility training 

techniques [47]: 1) detection (locating targets), 2) shorelin-

ing (avoiding virtual environment walls and following the 

sidewalk), 3) negotiating doors & stairs (navigating be-

tween rooms in the virtual environment), 4) negotiating 

obstacles and reorientation (avoiding obstacles). 

Participants 

Eight legally blind users (4 female, 4 male) were recruited 

for participation through mailing lists. Five participants 

were totally blind and three reported some light and shadow 

perception. Ages ranged from 25 to 70 with an average of 

44.9 years. Only one participant had previously interacted 

with a VR system. All participants had received formal 

O&M training and used a white cane as their preferred 

navigation aid (with at least 5 years of experience). One 

participant used both a cane and a guide dog depending on 

the task. Four participants (P1, P2, P5, P6) used an NFB 

carbon fiber cane with a metal glide tip and the other four 

(P3, P4, P7, P8) used a folding aluminum cane with a Ny-

lon pencil tip. Participants average cane length was 

1.57𝑚 (𝑆𝐷 = 0.2). 

Procedure 

After arrival at the experimental location, participants re-

ceived an overview of the session’s activities and provided 

consent in accordance with our IRB. Following a brief pre-

survey to gather demographic and other details related to 

cane use and VR experience, participants were fitted with 

our controller prototype and the length of the virtual cane 

was set to the same length as their real cane. We then 

walked participants through a brief orientation of the sys-

tem by placing them in the training room VE (Figure 11). 

Participants started inside the corridor (bottom left) where 

they could feel the walls on either side, and we demonstrat-

ed the experience of tapping and dragging against different 

surfaces and what happens when they passed through a wall 

with the cane or their body. They were then encouraged to 

walk along the corridor and find the doorway. After this, 

participants explored the different ground textures (concrete 

vs. wood) and we demonstrated the different sounds and 

textures associated with game elements (targets and haz-

ards). Participants explored the training room until they 

were comfortable with the basic elements of the experience. 

After training, the experimenter led participants to the start 

point of he game room. During the game, the first target 

was placed directly in front of the starting point to give 

participants some immediate feedback (Figure 10). After 

this, targets appeared sequentially and players navigated the 

VE to find them, attempting to navigate around walls and 

avoid hazards. The game concluded once participants ac-

quired the fifth target. If time remained, we asked partici-

pants if they would like to play again. We recorded the 

position and orientation of participants’ headsets and the 

cane, as well as all geometry they collided with. 

At the end of the session, we removed the controller proto-

type and proceeded to a post-survey. We asked participants 

about their understanding of the VE, how they used the 

provided feedback, what things they needed to adapt to in 

contrast to using their real cane, and their overall experi-

ence with the system. The study lasted 1.5 hours. 

Results Overall Game Statistics 

Seven out of the eight participants (excluding P3) were able 

to successfully find all five of the targets in the game. The 

experimenter suspended P3’s game play after locating Tar-

get 4 due to time constraints in keeping the study within the 

allotted time. The average time to complete the game for 

the first trial was 572.3𝑠 (𝑆𝐷 = 287) and to find each 

target 106.0𝑠 (𝑆𝐷 = 119.9). Four participants (P1, P5, P6, 

P8) repeated the game for a second trial. Other participants 

were not able to complete a second trial due to time con-

straints. The average time to complete the game in the sec-

ond trial was 218.2𝑠 (𝑆𝐷 = 51.1) and to find each target 

43.6𝑠 (𝑆𝐷 = 30.3) (Figure 13). 

Figure 12a shows a 2D histogram of position data points 

from trial 1 of all participants. Each point contributes 

1/sampling rate to a histogram bin value such that the total 

value approximates the accumulated time spent in seconds. 

This plot reveals areas where participants spent more time, 

for example at the hallway corner and doorway. Figure 12b 

and Figure 12c show a comparison of the trajectories be-

tween trials. Users were faster and collided with fewer 

hazards and walls the second trial. For the trial 1, users hit 

 Figure 11. User study training and game virtual rooms. 

on average 3.5 hazards (𝑆𝐷 = 2.8), and 12.4 walls 

(𝑆𝐷 = 7.2) (Figure 13). For trial 2, users hit on average 1 

hazard (𝑆𝐷 = 0.8), and 6.2 walls (𝑆𝐷 = 2.6)  (Figure 14).  

Audio Provides Spatial Information and Realism 

All participants had positive comments on the spatialized 

audio rendering engine. Participants commented how its 

realism immersed them in the space, “The audio was super 

real that’s why I thought there were people around me.” 

(P6). It also provided information on participants’ orienta-

tion, distances, and occlusions, “From the target audio cue, 

I could know which direction to go and approximately how 

far I had to go” (P8). “The volume, depending on where 

you were helped a lot; because that’s what I usually use [in 

the real world]” (P5).  

Metal Tip Users Perceive Greater Realism of the VE 

Glide metal tip users performed better in all measures than 

plastic pencil tip users (Figure 13). All metal tip users (P1, 

P2, P5, P6) noted similarities of the vibrations and audio to 

sensations they were familiar with in the real world. “What 

really set out was the tactile. It seemed so real, specially 

outdoors…The cement was spot on…” (P2). “Seems to me 

as much reality based as you can get” (P5). “The sweeping 

was very real. Audio was very real, it helped me locate 

where things might be...” (P6). “[vibrotactile feedback] 

changed in intensity depending on indoor vs outdoor. Like 

the outdoors on pavement the vibrations are harder…” 

(P1). We return to this finding in the discussion.  

Force Feedback Helped to Identify Architectural Geometry 

When asked about their use of the force feedback generated 

by our three-axis brake, most participants (P1,P2,P5–P8) 

commented on its use for: 1) understanding the architectural 

geometry, and 2) finding open spaces to walk in (and know-

ing where NOT to walk). “[It helped me detect] where 

barriers were, depending on the barrier type… How high 

does it go and how far across does it go. Is it straight up 

and down? Getting shape of things mostly” (P1). “I felt the 

clear entries where I didn’t encounter walls” (P5). “When I 

couldn’t move the cane I knew I was somewhere I wasn't 

supposed to be, compared to when it moved freely” (P8). 

Variety of Grips Employed with Some Adaptations Needed 

Most users used the traditional grip with cane held off-

center and some occasionally transitioned to holding the 

cane high above the waist. “I did feel like it was pretty darn 

[close to a real cane]” (P7). P1 and P2 preferred a pencil 

grip and commented on some of the difficulties in using this 

grip. P1 commented that it was not as easy to transition 

between grips and positions due to the brake apparatus. P2 

and P3 also noted their grip’s being quite similar to a real 

cane but having to adjust their hand slightly higher.  

Constant Contact and Two-Point Touch 

All participants commented on using either constant contact 

or two-point touch for general navigation in the open spac-

es. “When I use my cane, I don’t glide, I usually do my tap 

motions. And that’s what I did in the game, but I did glide a 

bit just to see. So, I did a little bit of both and they were 

both spot on” (P2). “Two-point touch I tried but I some-

times got lazy, so I ended up conveying that some in my 

cane technique by the end of it all” (P6).  

The Game was Fun, Interesting, and Challenging 

Participants commented on their enjoyment while playing. 

“It was challenging, and I enjoyed it. The 2nd time I en-

joyed it even more. I wasn't a mad man on a mission” (P6). 

“It was dope!” (P1). Users found the game relatable and 

challenging enough, “It wasn’t easy because I haven't had 

that experience, but it was in a way you could relate to it 

because it’s a total body experience.” (P5).  

DISCUSSION 

Overall, the results of our evaluation show that our system 

provides a compelling VR experience for blind users 

through multimodal haptic cues and auditory feedback. As 

hypothesized, participants primarily used the kinesthetic 

force feedback to understand the architectural geometry of 

Figure 13. Overall game statistics grouped by cane material. 

Error bars represent 95% confidence intervals.   

Figure 14. Overall game statistics grouped by trial. Error 

bars represent 95% confidence intervals. 

Figure 12. A) 2D histogram of position data points from trial 1 

of all participants. Values represent time [seconds] spent at 

each bin. B) Trial 1 trajectories for users that completed two 

trials (P1, P5, P6, P8). C) Trial 2 trajectories for users that 

completed two trials (P1, P5, P6, P8). 

the VE, while the tactile feedback complemented with spa-

tial audio conveyed more information about the local sur-

face properties and geometry of materials.  

An unanticipated effect was the sharp difference in perfor-

mance between users of metal and plastic cane tips. Plastic 

tip participants had more trouble understanding the mean-

ing of the tactile feedback, and generally performed worse. 

We assume this difference is largely due to the fact that we 

recorded sound effects and tactile feedback using a metal-

tipped carbon fiber cane, so the simulation was unfamiliar 

to users of plastic-tipped canes. One participant comment-

ed, “The cane was vibrating a lot for reasons I don’t know”. 

Surprisingly, P4 (a plastic tip user) commented, “The sensa-

tions are a little different. To me. It almost felt I had like 

one of those, I don’t know if you’ve seen, the NFB canes 

that are really flexible.” On the other hand, participants 

accustomed to using a metal tip in the real world found 

greater familiarity with the virtual cane and described the 

feedback as being “spot on” without much needed explana-

tion. These insights highlight the importance of adherence 

to user preferences in cane styles and how they impact the 

amount of training or familiarization needed with a system. 

While we modelled only one type of cane, creating a library 

of different cane styles and material properties is certainly 

possible such that user preferences can be loaded at runtime 

in the same manner that the cane length is adjusted per user. 

Similar to navigating the real world, we found that partici-

pants had more difficulty navigating narrow spaces, such as 

corners and doorways, especially when they were first get-

ting used to the system (Figure 12). However, during sub-

sequent times that they passed the doorway, they were able 

to navigate more efficiently. Differences were even more 

apparent for the second trial where participants were much 

quicker at finding all targets and reduced the number of 

collisions with the wall geometry and hazards. 

An additional confounding variable was the time given to 

participants to navigate the game VE. Many participants 

mentioned their sole focus on finding the targets and less so 

in freely exploring. Linberg et al. showed that acquiring a 

survey representation requires a conscious effort from the 

user [25], one must be motivated to do so [34]. In our study, 

a high reward was placed on finding the targets but less so 

on exploration. This might have provided some bias for 

participants to not focus on forming a mental map of the 

space. This would be in line with Siegel and White’s [52] 

survey knowledge theory where users first form knowledge 

of the content without structure, followed by route 

knowledge (egocentric), and last but less certain, a survey 

knowledge (allocentric). The decrease in navigation time 

and number of collisions provides evidence for participants’ 

understanding of the VE structure and success in route tasks 

but not necessarily acquiring a survey representation. 

LIMITATIONS & FUTURE WORK 

In this work, we approximate the region of interaction of a 

white cane as three orthogonal spanning vectors and create 

a wearable brake system grounded to the user’s body. 

While several benefits arise (i.e., high asymmetric force 

brakes and a mobile system), there are also limitations. The 

controller cannot stop the user’s body motion, so that when 

feedback passes undetected users may still walk into virtual 

objects. We mitigated this by providing audio feedback 

when users collided with the walls. We are also not current-

ly able to render feedback to users’ feet, which would con-

vey cues such as elevation changes and ground textures. 

Our prototype models one particular type of cane, carbon 

fiber with a metal glide tip, as we recorded audio and tex-

tures from real-world materials. Our results show the need 

for expanding this library. In addition, our prototype cannot 

adjust texture and impact feedback depending on where 

along the cane a collision has occurred. A collision at the 

tip generates a different vibration profile compared to im-

pact higher up the cane. One approach towards this could 

be the use of multiple synchronized voice coil actuators. 

Participants navigated the game VE by physically walking 

with a mapping of 1:1 between the real and the virtual. 

However, an interesting question arises on how we might 

enable even larger-scale navigation (e.g., of cities where a 

1:1 mapping is likely not feasible) using established tech-

niques in visual applications such as teleportation and walk-

ing speed gains [1]. Finally, given that users are navigating 

in VR, interesting augmentations could be explored to en-

hance not just realism but user presence [50].   

Prior work has shown survey knowledge can be attained 

through exploration of VEs [37], [20]. Our study provides 

evidence of participants’ understanding of the VE structure 

and acquisition of a route representation. In future work, we 

would like to study survey knowledge acquisition by com-

paring training in a VE and subsequent navigation and 

assessment of standard O&M metrics in an equivalent real-

world environment. 

CONCLUSION 

We described a prototype experience for enabling non-

visual exploration of large VEs. This experience comprises 

a wearable controller simulating a white cane commonly 

used by people who are blind or have low vision. Our con-

troller renders human-scale force feedback using a novel 

three-axis brake alongside surface texture associated with 

tapping and sweeping. Our controller plugs into a VE where 

we render physically realistic audio effects that are modeled 

on the geometry and material properties of the VE. We 

evaluated this experience through a user study in which 

eight blind participants used our system to navigate and 

explore a virtual game using only their senses of hearing, 

touch, and O&M skills. Our work extends the state of the 

art in haptic simulations for VR and is particularly promis-

ing for opening up further research on the accessibility of 

VR for people who are blind or have low vision. 

REFERENCES 

[1] Parastoo Abtahi, Mar Gonzalez-Franco, Eyal Ofek, and 

Anthony Steed. 2019. I’m a Giant: Walking in Large 

Virtual Environments at High Speed Gains. In Pro-

ceedings of the 2019 CHI Conference on Human Fac-

tors in Computing Systems (CHI ’19). Association for 

Computing Machinery, New York, NY, USA, Paper 

522, 1–13. 

DOI:https://doi.org/10.1145/3290605.3300752 

[2] Grace Ambrose-Zaken. 2005. Knowledge of and pref-

erences for long cane components: A qualitative and 

quantitative study. Journal of Visual Impairment & 

Blindness, 99(10), 633-645. 

[3] B. B. Blasch, Steven J. LaGrow, and W. R. De l'Aune. 

1996. Three aspects of coverage provided by the long 

cane: Object, surface, and foot-placement preview. 

Journal of Visual Impairment and Blindness, 90, 295-

301. 

[4] Erin Connors, Elizabeth R. Chrastil, Jaimie Sánchez 

and Ltfi B. Merabet. 2014. Action video game play and 

transfer of navigation and spatial cognition skills in ad-

olescents who are blind. Frontiers in Human Neurosci-

ence, 133.  

[5] Edoardo D'Atri, Carlo Maria Medaglia, Alexandru 

Serbanati, Ugo Biader Ceipidor, Emanuele Panizzi and 

Alessandro D'Atri. 2007. A system to aid blind people 

in the mobility: A usability test and its results. In Sec-

ond International Conference on Systems (ICONS'07) 

(pp. 35-35). IEEE. 

[6] Massimiliano Gabardi, Massimiliano Solazzi, Daniele  

Leonardis and Antonio Frisoli. 2016. A new wearable 

fingertip haptic interface for the rendering of virtual 

shapes and surface features. In 2016 IEEE Haptics 

Symposium (HAPTICS) (pp. 140-146). IEEE. 

[7] Nicholas A. Giudice. (2018). Navigating without vi-

sion: principles of blind spatial cognition. Handbook of 

behavioral and cognitive geography. Edward Elgar 

Publishing.  

[8] José  L. González-Mora, L. Rodriguez-Hernandez, L. 

F. Rodriguez-Ramos, L. Díaz-Saco, and N. Sosa. 1999. 

Development of a new space perception system for 

blind people, based on the creation of a virtual acoustic 

space. In International Work-Conference on Artificial 

Neural Networks. (pp. 321-330). Springer, Berlin, Hei-

delberg. 

[9] William Henry Jacobson. (1993). The art and science 

of teaching orientation and mobility to persons with 

visual impairments. American Foundation for the 

Blind. 

[10] HTC Vive. Retrieved September 13, 2019 from 

https://www.vive.com/us/.  

[11] Dae Shik Kim and Robert Wall Emerson. 2012. Effect 

of cane length on drop-off detection performance. 

Journal of Visual Impairment & Blindness, 106(1), 31-

35. 

[12] Dae Shik Kim, Robert Wall Emerson and Amy B. 

Curtis. 2010. Ergonomic factors related to drop-off de-

tection with the long cane: Effects of cane tips and 

techniques. Human Factors, 52(3), 456-465. 

[13] Dae Shik Kim, Robert Wall Emerson, Kooroosh 

Naghshineh and Alexander Auer. 2017. Drop-off de-

tection with the long cane: Effect of cane shaft weight 

and rigidity on performance. Ergonomics, 60(1), 59-68. 

[14] Julian Kreimeier and Timo Götzelmann. 2019. First 

Steps Towards Walk-In-Place Locomotion and Haptic 

Feedback in Virtual Reality for Visually Impaired. In 

Extended Abstracts of the 2019 CHI Conference on 

Human Factors in Computing Systems (CHI EA ’19). 

Association for Computing Machinery, New York, 

NY, USA, Paper LBW2214, 1–6. 

DOI:https://doi.org/10.1145/3290607.3312944 

[15] Katherine K. Kuchenbecker, Jonathan Fiene and 

Günter Niemeyer. 2006. Improving contact realism 

through event-based haptic feedback. IEEE Transac-

tions on Visualization and Computer Graphics, 12.2, 

219-230. 

[16] Steven J. LaGrow, B. B. Blasch and William De 

l'Aune. 1997. The effect of hand position on detection 

distance for object and surface preview when using the 

long cane for nonvisual travel. RE: view, 28(4), 169. 

[17] Steven J. LaGrow and Marvin J. Weessies. 1994. Ori-

entation and mobility: Techniques for independence. 

Palmerston North, New Zealand: Dunmore Press. 

[18] Orly Lahav and David Mioduser. 2001. Multisensory 

virtual environment for supporting blind persons' ac-

quisition of spatial cognitive mapping–a case study. In 

EdMedia+ Innovate Learning. Association for the Ad-

vancement of Computing in Education (AACE), 1046-

1051. 

[19] Orly Lahav and David Mioduser. 2004. Exploration of 

unknown spaces by people who are blind, using a mul-

tisensory virtual environment (MVE). Journal of Spe-

cial Education Technology, 19, 3, 15-23. 

[20] Orly Lahav and David Mioduser. 2008. Haptic-

feedback support for cognitive mapping of unknown 

spaces by people who are blind. International Journal 

of Human-Computer Studies, 66(1), 23-35. 

[21] Orly Lahav, D Schloerb, S Kummar and M A Sriniva-

san. 2011. A virtual map to support people who are 

blind to navigate through real spaces. Journal of Spe-

cial Education Technology, 26, 4. 

[22] Orly Lahav, David W. Schloerb and Mandayam A. 

Srinivasan. 2015. Virtual environments for people who 

are visually impaired integrated into an orientation and 

mobility program. Journal of Visual Impairment & 

Blindness, 109(1), 5-16. 

[23] Nils Landin, Joseph M. Romano, William McMahan 

and Katherine J. Kuchenbecker. 2010. Dimensional re-

duction of high-frequency accelerations for haptic ren-

dering. In International conference on human haptic 

sensing and touch enabled computer applications, pp. 

79-86. Springer, Berlin, Heidelberg, 2010. 

[24] Anatole Lécuyer, Pascal Mobuchon, Christine Mégard, 

Jérôme Perret, Claude Andriot and J. P. Colinot. 2003. 

HOMERE: a multimodal system for visually impaired 

people to explore virtual environments. In Proceedings 

of IEEE Virtual Reality. IEEE. (pp. 251-258). 

[25] Eric Linberg and Tommy Garling. 1983. Acquisition of 

different types of locational information in cognitive 

maps: Automatic or effortful processing? In Psycho-

logical Research, 45, 19–38.  

[26] Maruricio Lumbreras and Jaime Sánchez. 1999. Inter-

active 3D sound hyperstories for blind children. In 

Proceedings of the SIGCHI conference on Human Fac-

tors in Computing Systems (CHI ’99). Association for 

Computing Machinery, New York, NY, USA, 318– 

325. DOI:https://doi.org/10.1145/302979.303101 

[27] Shachar Maidenbaum, Shelly Levy-Tzedek, Daniel-

Robert Chebat and Amir Amedi. 2013. Increasing ac-

cessibility to the blind of virtual environments, using a 

virtual mobility aid based on the" EyeCane": Feasibil-

ity study. PloS one 8, 8, e72555. 

[28] Shachar Maidenbaum and Amir Amedi. 2015. Non-

visual virtual interaction: Can Sensory Substitution ge-

nerically increase the accessibility of Graphical virtual 

reality to the blind? In 2015 3rd IEEE VR International 

Workshop on Virtual and Augmented Assistive Tech-

nology (VAAT). IEEE. pp. 15-17. 

[29] Mayer L. Max and Jesse R. Gonzalez. 1997. Blind 

persons navigate in virtual reality (VR); hearing and 

feeling communicates reality. Studies in health tech-

nology and informatics. 39, 54-59. 

[30] Ravish Mehra, Nikunj Raghuvanshi, Lauri Savioja, 

Ming C. Lin, and Dinesh Manocha. 2012. An efficient 

GPU-based time domain solver for the acoustic wave 

equation. In Applied Acoustics. 73(2), 83-94. 

[31] Frank Meijer, Branko L. Geudeke, and Egon L. Van 

den Broek. 2009. Navigating through virtual environ-

ments: Visual realism improves spatial cognition. In 

CyberPsychology & Behavior. 12(5), 517-521. 

[32] Lofti B. Merabet, Erin C. Connors, Mark A. Halko and 

Jaime Sanchez. 2012. Teaching the Blind to Find Their 

Way by Playing Video Games. PloS one 7, no. 9 

(2012): e44958. 

[33] Richard Mettler. 1998. Cognitive learning theory and 

cane travel instruction: A new paradigm. DIANE Pub-

lishing. 

[34] Shannon D. Moeser. 1988. Cognitive mapping in a 

complex building. In Environment and Behavior. 20, 

21–49. 

[35] NFB Canes. Retrieved August 9, 2019 from 

https://www.nfb.org/programs-services/free-white-

cane-program. NFB canes. 

[36] Kiyohiko Nunokawa, Y. Seki, Shuichi Ino and K. Doi. 

2014. Judging hardness of an object from the sounds of 

tapping created by a white cane. In 2014 36th Annual 

International Conference of the IEEE Engineering in 

Medicine and Biology Society. IEEE, pp. 5876-5879. 

[37] Makoto Ohuchi, Yukio Iwaya, and Yôiti Suzuki. 2006. 

Cognitive-map forming of the blind in virtual sound 

environment. Georgia Institute of Technology, 2006. 

http://hdl.handle.net/1853/50588. 

[38] Project Acoustics. 2019. (3 March 2019). Retrieved 

September 6, 2019 from https://aka.ms/acoustics. 

[39] Ludek Pokluda and Jiri Sochor. 2003. Spatial haptic 

orientation for visually impaired people. In Eu-

rographics. 

[40] Nikunj Raghuvanshi and John Snyder. 2018. Paramet-

ric directional coding for precomputed sound propaga-

tion. ACM Trans. Graph. 37, 4, Article 108 (July 

2018), 14 pages. 

DOI:https://doi.org/10.1145/3197517.3201339  

[41] Nikunj Raghuvanshi, John Snyder, Ravish Mehra, 

Ming Lin, and Naga Govindaraju. 2010. Precomputed 

wave simulation for real-time sound propagation of 

dynamic sources in complex scenes. ACM Trans. 

Graph. 29, 4, Article 68 (July 2010), 11 pages. 

DOI:https://doi.org/10.1145/1778765.1778805  

[42] Reardon, S. 2011. Playing by ear. Science, 333(6051), 

1816. 

[43] Anthony E. Richardson, Daniel R. Montello and Mary 

Hegarty. 1999. Spatial knowledge acquisition from 

maps and from navigation in real and virtual environ-

ments. Memory & Cognition. 27(4), 741-750. 

[44] Mark D. Rodgers and Robert W. Emerson. 2005. Hu-

man factor analysis of long cane design: Weight and 

length. Journal of Visual Impairment & Blindness. 

99(10), 622-632. 

[45] Joseph M. Romano and Katherine J. Kuchenbecker. 

2011. Creating realistic virtual textures from contact 

acceleration data. In IEEE Transactions on Haptics. 

5(2), 109-119. 

[46] Joseph M. Romano, Takashi Yoshioka and Katherine J. 

Kuchenbecker. 2010. Automatic filter design for syn-

thesis of haptic textures from recorded acceleration da-

ta. In 2010 IEEE International Conference on Robotics 

and Automation. IEEE. pp. 1815-1821.  

[47] Sandra Rosen. Long Cane Techniques: Study Guide. 

Retrieved August 9, 2019 from 

https://tech.aph.org/sbs/04_sbs_lc_study.html#12 

[48] Jaime Sánchez and Mauricio Sáenz. 2010. Metro navi-

gation for the blind. In Computers & Education. 55(3), 

970-981. 

[49] David W. Schloerb, Orly Lahav, Joseph G. Deslogeand 

Mandayam A. Srinivasan. 2010. BlindAid: Virtual en-

vironment system for self-reliant trip planning and ori-

entation and mobility training. In 2010 IEEE Haptics 

Symposium. IEEE. pp. 363-370. 

[50] Martijn J. Schuemie, Peter Van Der Straaten, Merel 

Krijn and Charles A. Van Der Mast.  2001. Research 

on presence in virtual reality: A survey. In CyberPsy-

chology & Behavior. 4(2), 183-201. 

[51] Yoshikazu Seki and Tetsuji Sato, T.  2010. A training 

system of orientation and mobility for blind people us-

ing acoustic virtual reality. IEEE Transactions on neu-

ral systems and rehabilitation engineering. 19(1), 95-

104. 

[52] Alexander W. Siegel and Sheldon H. White. 1975. The 

development of spatial representations of large-scale 

environments. In Advances in Child Development and 

Behavior. New York: Academic Press. Vol. 10, (pp 

10–55). 

[53] Mike Sinclair, Eyal Ofek, Mar Gonzalez-Franco, and 

Christian Holz. 2019. CapstanCrunch: A Haptic VR 

Controller with User-supplied Force Feedback. In Pro-

ceedings of the 32nd Annual ACM Symposium on Us-

er Interface Software and Technology (UIST ’19). As-

sociation for Computing Machinery, New York, NY, 

USA, 815–829. 

DOI:https://doi.org/10.1145/3332165.3347891  

[54] Dimitrios Tzovaras, Georgios Nikolakis, Georgios 

Fergadis, Stratos Malasiotis and Modestos Stavrakis. 

2004. Design and implementation of haptic virtual en-

vironments for the training of the visually impaired. In 

IEEE Transactions on Neural Systems and Rehabilita-

tion Engineering. 12, 2, pp. 266-278. 

[55] David Waller, Earl Hunt and David Knapp. 1998. The 

transfer of spatial knowledge in virtual environment 

training. Presence. 7(2), 129-143. 

[56] Wai Yu and Stephen Brewster. 2002. Multimodal vir-

tual reality versus printed medium in visualization for 

blind people. In Proceedings of the fifth international 

ACM conference on Assistive technologies (As-

sets ’02). Association for Computing Machinery, New 

York, NY, USA, 57–64. 

DOI:https://doi.org/10.1145/638249.638261 

[57] Yuhang Zhao, Cynthia L. Bennett, Hrvoje Benko, 

Edward Cutrell, Christian Holz, Meredith Ringel Mor-

ris, and Mike Sinclair. 2018. Enabling People with 

Visual Impairments to Navigate Virtual Reality with a 

Haptic and Auditory Cane Simulation. In Proceedings 

of the 2018 CHI Conference on Human Factors in 

Computing Systems (CHI ’18). Association for Com-

puting Machinery, New York, NY, USA, Paper 116, 1– 

14. DOI:https://doi.org/10.1145/3173574.3173690 