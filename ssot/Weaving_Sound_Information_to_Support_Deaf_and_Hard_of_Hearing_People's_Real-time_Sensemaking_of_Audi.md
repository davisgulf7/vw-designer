# Weaving Sound Information to Support Deaf and Hard of Hearing People's Real-time Sensemaking of Auditory Environments

Weaving Sound Information to Support Deaf and Hard of Hearing People’s 1 

Real-time Sensemaking of Auditory Environments: Co-designing with a DHH 2 

User 3 

JEREMY ZHENGQI HUANG 4 

University of Michigan, Computer Science and Engineering, zjhuang@umich.edu 5 

JAYLIN HERSKOVITZ 6 

University of Michigan, Computer Science and Engineering, jayhersk@umich.edu 7 

LIANG-YUAN WU 8 

University of Michigan, Computer Science and Engineering, lyuanwu@umich.edu 9 

CECILY MORRISON 10 

Microsoft Research, cecilym@microsoft.com 11 

DHRUV JAIN 12 

University of Michigan, Computer Science and Engineering, profdj@umich.edu 13 

Current AI sound awareness systems can provide deaf and hard of hearing people with information about sounds, including discrete 14 sources and transcriptions. However, synthesizing AI outputs based on DHH people’s ever-changing intents to facilitate their 15 sensemaking of complex auditory environments remains a challenge. In this paper, we describe the co-design process of SoundWeaver, 16 a sound awareness system prototype that dynamically weaves AI outputs from different AI models based on users’ intents and presents 17 synthesized information through a heads-up display. Adopting a Research through Design perspective, we created SoundWeaver with 18 one DHH co-designer, adapting it to his personal contexts and goals (e.g., cooking at home and chatting in the game store). Through 19 this process, we present design implications for the future of “intent-driven” AI systems for sound accessibility. 20 

CCS CONCEPTS • Human-centered computing • Accessibility • Empirical studies in HCI 21 

Additional Keywords and Phrases: Accessibility, AI, sound awareness, deaf and hard of hearing 22 

 23 

 24 Figure 1: The SoundWeaver’s Prototype’s Three Weaving Modes. SoundWeaver is an AI sound awareness system that 25 dynamically weaves AI outputs based on DHH users’ intents across personal contexts. The prototype contains three 26 modes: Awareness, Action, and Social Mode. Awareness Mode provided general awareness of the environmental sounds 27 through visualization of ambient sounds and optional sound identification. Action Mode facilitates active monitoring of 28 

specific sounds related to a task. Social Mode uses captions and peripheral visualization of ambient sounds to facilitate 29 social interactions. Users can freely switch between modes on the fly based on their real-time information needs.  30 

1 INTRODUCTION 31 

Deaf and hard of hearing (DHH) individuals have limited access to sound information and often seek to enhance their 32 

understanding of their environments through sound awareness [8, 15]. To address this, HCI researchers have leveraged 33 

various AI models to design and develop intelligent sound awareness applications that reduce barriers to accessing 34 

sound information [8, 14, 31, 32]. For example, SoundWatch [32], powered by audio classification models, notifies DHH 35 

users of individual sound events. Speech recognition, invented initially to support captioning for DHH people, has now 36 

also become an inseparable part of audio accessibility for mainstream devices and software [69, 70]. These systems draw 37 

on rapidly advancing models for machine understanding of speech and non-speech sounds, including those for audio 38 

classification [71, 72], acoustic scene understanding [35], and automatic speech recognition [17, 73, 74], which will only 39 

continue to grow and develop more complex capabilities. 40 

However, current AI-based sound awareness applications usually have pre-configured outputs [32]. These outputs 41 

do not have semantic connections to DHH people’s real-time contexts, goals, and information needs. For example, 42 

consider the following scenario of a DHH person (“Sam”) working in a coffee shop (Figure 2): 43 

When a customer approaches her to place an order, Sam turns on the live transcription to understand the customer's 44 

speech. As Sam begins to fulfill the order (e.g., latte), her goal shifts from understanding speech to fulfilling 45 

customer orders by making coffee. She wants to know when the machine is brewing and is done brewing while 46 

watching for new customers walking in. Sam turns on the sound recognition as well. However, because the interface 47 

simply consolidates all the sound information Sam requested (Figure 2; Prior Approaches), she does not know how to 48 

make sense of the information. While making the coffee, Sam leaves the live transcription on because she wants to 49 

know when someone calls her name (i.e., “Sam”) or when her colleagues initiate a conversation. To achieve this, 50 

Sam needs to pay constant attention to the transcription to observe name-calling, distracting her from the tasks at hand.  51 

 52 Figure 2: An illustrative comparison of our system with prior approaches. Prior sound awareness systems assume pre-53 configured outputs (e.g., showing sound events and captions no matter the context). In contrast, SoundWeaver will 54 adapt to users' different intents by allocating and displaying various information. For example, when the user (“Sam”) is 55 making coffee, Action Mode will help her monitor relevant sounds like “boiling” and “blender.” When someone calls 56 Sam, SoundWeaver will show this information on the display, leading Sam to switch to Social Mode, where the system 57 focuses on displaying captions while maintaining some degree of awareness of the environmental sounds. 58 

As the above scenario demonstrates, current sound awareness systems' static and pre-configured nature can fail to 59 

fulfill DHH people’s ever-changing real-world information needs. As AI capabilities continue to develop, so does the 60 

potential for sound awareness systems to adapt their interfaces by shifting from presenting discrete and largely 61 

unprocessed AI output to synthesizing AI-generated information that facilitates DHH people’s real-time sensemaking 62 

and semantic understanding of auditory environments. This work explores two critical aspects of human-AI interaction 63 

design in the context of sound awareness systems for DHH individuals. First, we explore an “intent-driven” AI system 64 

that adapts its behavior based on DHH users’ intents and purposefully weaves together AI outputs to serve DHH people’s 65 

dynamic information needs and support their sensemaking of complex auditory environments. Second, we seek to 66 

understand relationships among AI systems, DHH users, and their environments and observe how this relationship 67 

evolves through interactions. 68 

We present our work from a Research through Design (RtD) perspective [66]. We started by reviewing previously 69 

identified design challenges and opportunities in the human-AI interaction and sound awareness technology space [1, 70 

24, 75]. Our work is also inspired by established theories and models that guide the designs of accessible environments 71 

for DHH individuals, including DeafSpace [48], best captioning practices [37], and broader norms of Deaf Culture. 72 

Grounded in prior knowledge, we then worked closely with Declan1, a Deaf participant, over six months to iteratively 73 

prototype an AI system that supports Declan’s real-time sensemaking of auditory environments. Specifically, we learned 74 

about Declan’s personal contexts (e.g., daily routines and physical environments) and information needs and preferences 75 

across these contexts. We documented and analyzed our findings iteratively following a Grounded Theory approach. 76 

These findings elicited several design goals, including resolving redundant sound information and adapting system 77 

behaviors based on user intents.  78 

Informed by these design goals, we created SoundWeaver, an intent-driven AI system that weaves AI outputs about 79 

sound based on DHH users’ needs and intents, synthesizing relevant sound information through a heads-up display. 80 

SoundWeaver was iteratively developed over multiple co-design sessions with Declan, supplemented by discussions 81 

with our team of mixed hearing abilities. The final SoundWeaver prototype contains three weaving modes: Awareness, 82 

Action, and Social (Figure 1). These modes facilitate distinct user intents and thus display AI-generated sound 83 

information differently: 84 

1. Awareness Mode. Awareness Mode helps DHH users learn about the overall auditory environment and be 85 

aware of intermittent sound events. 86 

2. Action Mode. Action Mode helps DHH users perform more action-intensive tasks by providing more active 87 

and focused monitoring of a selected set of sounds. 88 

3. Social Mode. Social Mode supports social interactions while helping DHH users maintain certain levels of 89 

awareness of the auditory environments. 90 

SoundWeaver allows users to transition between these modes on the fly as their needs and goals change with a 91 

simple click of a button. Additionally, SoundWeaver supports more granular customization (e.g., configuring relevant 92 

sounds for Action Mode). This way, the system allows DHH users to modulate their behaviors and ensure the system 93 

outputs contextually appropriate information. Revisiting Sam’s scenario with SoundWeaver, the Action Mode will 94 

enable Sam to focus on work-related sounds (e.g., blender, water boiling). When SoundWeaver tells Sam that “someone 95 

is calling her name,” Sam seamlessly switches from Action Mode to Social Mode to chat with her colleague. This allows 96 

Sam to seamlessly interact with her environment based on her requirements and complete her tasks (Figure 2; 97 

SoundWeaver).  98 

We deployed and evaluated the SoundWeaver prototype in two of Declan’s routine environments: his home and the 99 

game store he frequently visited. Through these field evaluations, we gained further insights into the design of AI sound 100 

awareness systems for DHH people’s sensemaking of complex auditory information and how introducing novel sound 101 

 1 Declan is a pseudonym for our DHH participant. 

awareness technology can foster new dynamics among DHH users, technology, and the situated environment (e.g., 102 

interactions with a group of friends). 103 

Overall, this work makes the following contributions: 104 

1. We describe the iterative prototyping of SoundWeaver, an intent-driven AI sound awareness system that 105 

facilitates DHH people’s real-time sensemaking. SoundWeaver adapts its information display based on DHH 106 

users’ intents and purposefully weaves AI outputs based on DHH people’s personal contexts. 107 

2. We reflect on the considerations and tensions during the prototyping and field evaluation of SoundWeaver 108 

with a DHH co-designer and present design implications for future AI sound accessibility systems. 109 

2 RELATED WORK 110 

2.1 DHH Culture 111 

The Deaf and hard of hearing community is a diverse group encompassing individuals marked by a wide range of 112 

experiences, backgrounds, and cultural identities. There are three primary models of understanding hearing loss: 113 

medical, social, and cultural-linguistic models [10, 49, 65]. The medical model views hearing loss primarily as a condition 114 

to be diagnosed and treated [76]. The social model shifts the focus from individual hearing loss to societal barriers 115 

limiting participation [47, 76]. The cultural-linguistic model recognizes Deafness as a unique cultural and linguistic 116 

identity rather than simply a disability. This model celebrates Deaf culture, defined by shared values, norms, and 117 

languages like American Sign Language (ASL) [10, 50]. ASL is a developed visual-spatial language with its own syntax, 118 

grammar, and nuances and can convey complex ideas, emotions, and narratives [41, 53, 77]. 119 

Our work draws from established concepts, models, and theories in accessibility for DHH people to guide our co-120 

design process with Declan. For example, DeafSpace, a conceptual framework for creating accessible physical 121 

environments, outlines space design guidelines that provide “full access to communication” and unique considerations 122 

for DHH people’s cognitive, sensory, and emotional experiences [48, 78]. Even though DeafSpace primarily guides space 123 

design, these principles have design implications for AR- or HMD-based sound awareness technologies like 124 

SoundWeaver, where users perceive sound information as part of the physical space. For example, given that Deaf people 125 

perceive their surroundings through subtle visual cues [78], HMD-based sound indicators should communicate the 126 

changes in acoustic environments, such as SoundWeaver’s use of changing colors and waveforms to indicate real-time 127 

ambient noise levels. The caption feature in SoundWeaver also follows established “best practices” to ensure readability 128 

[79], including placing captions at the bottom center of the view, using sans serif fonts with “medium thickness,” and 129 

placing captions in a semi-transparent text box. 130 

2.2 Towards Sound Accessibility with AI 131 

HCI researchers have long studied sound awareness solutions to improve sound accessibility for DHH people. Early 132 

work explored visualizations based on sound characteristics like location, loudness, and pitch [23, 42, 63] and simple 133 

sound classification with shallow learning approaches like support vector machines [36] and decision trees [38]. Driven 134 

by recent advances in deep learning models for sound classification (e.g., Convolutional Neural Networks [21, 52] and 135 

Recurrent Neural Networks [17]), HCI researchers have developed home, mobile, and wearable AI-based sound 136 

recognition systems [8, 31, 32, 60] that process audio signals from the environment and display information about 137 

recognized sound events. For example, SoundWatch [32] informed DHH users of environmental sounds through haptic 138 

feedback and visual notifications containing sound events and loudness. To mitigate AI’s inherent uncertainties (e.g., 139 

recognition errors), more recent mobile sound recognition systems enabled DHH people to teach the system through 140 

audio samples [33] and provide feedback [14]. Besides sound recognition, advances in automatic speech recognition also 141 

led to transcription applications in mobile devices [70, 73, 74]  (e.g., Google Live Transcribe [69]). To fulfill both sound 142 

recognition and transcription needs, Guo et al. proposed an AR prototype that combined sound classification and ASR 143 

outputs in one interface [18]. 144 

Despite the progress, current AI-based sound awareness systems assume discrete, pre-configured outputs, which 145 

struggle to fulfill DHH users’ dynamic and personalized sound information needs across different contexts (e.g., driving 146 

and at work) [24]. While the conglomeration of multiple pieces of sound information [18] partially addresses this need, 147 

current visual representations remain static (e.g., a textual description of sounds) regardless of the user’s needs and 148 

context (e.g., always showing transcriptions of the crowd speech in a coffee shop even though the user wants to focus 149 

on work). In contrast, prior work on non-sound related accessible technologies has explored new human-AI interaction 150 

designs that embodied the concept of “AI extenders,” where AI is closely intertwined with human cognition to enhance 151 

information processing capabilities [20]. Examples of such applications include the scene-weaving concept, an 152 

interaction metaphor that presents information as strands of fabrics that could be “weaved” together into the precepted 153 

scene by individual blind and low-vision (BLV) users [2]. Similarly, Morrison et al. proposed “open-ended AI” as a facility 154 

for BLV children to make sense of social situations based on various spatial audio cues [45].  155 

The current work extends this line of research to the sound awareness technology space. Specifically, we propose an 156 

intent-driven design for AI sound awareness systems, where various kinds of AI-based sound feedback are allocated 157 

purposefully to adapt to DHH people’s real-time contexts and intents and complement DHH people’s trusted ways of 158 

sensemaking of the environment. The scenario of Sam working in a coffee shop, illustrated in Section 1, exemplified the 159 

vision of such systems. 160 

2.3 XR-based Sound Feedback Design 161 

Our decision to implement SoundWeaver as a head-mounted display (HMD) application was informed by prior findings 162 

that, compared to traditional mobile form factors, HMD could provide a diverse set of always-on, easier-to-access sound 163 

information while reducing attention splits and the need to carry the device with hands [16, 29]. Prior work explored 164 

the 3D display of sound information, including captions, localization, sound sources and events, and visualization of 165 

acoustic signals. For example, one pioneering work conducted a design probe of visual feedback for sound information 166 

[28] with a Google Glass-based system. This work elicited user preferences across several dimensions of visual sound 167 

feedback, including arrow-based indicators for directionality, peripheral positioning of indicators, and the inclusion of 168 

loudness data. To address challenges in communication for DHH people, Jain et al. explored HMD-based captions on 169 

HoloLens and suggested designs that adapt to real-world contexts like light conditions and convey this contextual 170 

information (e.g., speaker name and locations). SpeechBubbles [51] focused on the accessibility of group conversations 171 

by probing DHH people’s preferred designs for in- and out-of-view conversations in Mandarin. 172 

Regarding VR environments, researchers explored multimodal sound feedback ranging from visualization [11, 30, 39, 173 

40] to sound modifications [9] and haptics [11, 30, 44]. For example, Jain et al. categorized sounds into dimensions such 174 

as sound source and sound intent and designed corresponding visual and haptic prototypes for VR sound feedback, such 175 

as waveforms for ambient sounds and textual displays for currently playing sounds (e.g., torch crackling) and rhythmic 176 

haptics for critical information. SoundVizVR [39] built on this work and further examined the usability of different 177 

indicator designs for sound types and characteristics. EarVR+ [44] attaches physical LED lights and vibro-motors to 178 

traditional devices to inform DHH users of the localization results. 179 

Building on prior 3D sound feedback designs, we carefully examined these designs by situating them in DHH people’s 180 

personal contexts and preferences. This process allowed us to observe how sound indicators behaved over time and 181 

could produce unexpected results. For example, we found that peripheral arrow indicators, a design suggested by a prior 182 

design probe [28], produced distracting visual flickers during rapid speaker transitions, such as in instances of turn-183 

taking or overlapping dialogue, which impeded users’ ability to focus on the conversation.  184 

3 GENERAL METHODOLOGY 185 

Positionality Statement: Our team comprises five researchers. The first author, Jeremy, is a graduate student at the 186 

University of Michigan who is hearing and has speech-related disabilities. Jeremy is learning ASL and has two years of 187 

experience engaging with the DHH community. Jaylin is a graduate student at the University of Michigan who is hearing 188 

and has five years of experience researching accessible technologies. Liang-Yuan is hearing and has one year of 189 

experience engaging with the DHH community. Cecily has over ten years of research experience working with people 190 

with disabilities. Dhruv identifies as hard of hearing and has over ten years of experience engaging with the DHH 191 

community. Dhruv has a Level 2 fluency in American Sign Language. Our collective experience as a mixed-hearing 192 

ability research team shapes our work, including a deep understanding of DHH culture, the evolution of our design 193 

artifact, the analysis of research data, and in-depth discussions with Declan, our participant. 194 

Our participant “Declan”: Declan is a 22-year-old male who identifies as Deaf. He has profound and non-congenital 195 

hearing loss; he lost hearing in his left ear in childhood and his right ear when he was 20. Declan prefers to communicate 196 

with both DHH and hearing people in sign language; his primary sign language is American Sign Language and Pidgin 197 

Signed English. While he frequently uses sign language, he can also read and communicate in English well. Declan was 198 

a good fit for our study because of three considerations. First, Declan was an early adopter of common accessible 199 

technologies that DHH people use, like Google’s Sound Notification and Live Transcribe, which we presume would 200 

make him comfortable with adopting new technologies and giving critical feedback. Second, identifying as Deaf, Declan 201 

deeply understood the DHH community’s cultural norms and preferences. Third, while being Deaf, Declan conversed 202 

in both speech and ASL and with both hearing and Deaf people, thus offering a unique perspective from the angles of 203 

both hard of hearing and Deaf populations. In our study findings, we describe other details about Declan, such as his 204 

occupation, hobbies, and personal contexts, in our study findings. 205 

Research Methodology: We narrate our six-month co-design process with Declan from the Research through 206 

Design (RtD) [66] perspective. RtD combines design science with scholarly research, where the creation of artifacts is 207 

the research outcome and a means of generating new knowledge about how people use interactive technologies [66]. In 208 

our work, we created the SoundWeaver prototype as a design artifact that embodies intent-driven AI and a medium for 209 

continuous and critical reflections on our design decisions along the journey. 210 

Our co-design process with Declan consisted of three phases. Phase 1 of our study was primarily formative, where 211 

we learned about Declan’s personal contexts and routines and probed Declan’s information needs across these contexts. 212 

In Phase 2, we continuously engaged with Declan through in-person co-design sessions and frequent communications 213 

of design ideas and considerations through text messages, emails, and video calls. During this phase, SoundWeaver 214 

evolved from a “brute-force” prototype [3] based on formative insights and our prior assumptions to a more polished, 215 

carefully designed experience. Phase 3 consisted of the field evaluations of the SoundWeaver prototype and general 216 

reflections on the entire research process. 217 

Throughout the co-design process, we curated five types of data: meeting transcripts, sketches, emails/text messages, 218 

field notes, and video recordings. Our data collection and analysis process was deeply inspired by the Grounded Theory 219 

methods (GTM) [6, 13, 46] to curate and analyze this data. Since the start of our research, we have kept a working 220 

document as the collection of memos using a shared Google Docs file. Initially, this document contained our assumptions 221 

on the “ideal” sound awareness systems based on our prior knowledge. We kept the document updated whenever there 222 

was new data or “quick thoughts.” For example, when we received the meeting transcript for a design session, we 223 

encoded the transcript following open, axial, and selective coding and compared the newly generated codes with the 224 

current ones. The research team regularly jotted down thoughts on existing data through margin comments, particularly 225 

to relate to and compare Declan’s experiences with those of our hard-of-hearing author. By the end of Phase 3, the 226 

number of open codes in our working document expanded significantly from 78 (from Phase 1) to 231. We did not group 227 

these codes into themes; instead, as is common in GTM, we carefully examined the relationship between important 228 

codes and iteratively developed the design goals. The number of these design goals fluctuated as the new data could 229 

reinforce, add to, or invalidate the current goals. 230 

Our decision to engage closely with one DHH participant, Declan, was influenced by several factors. First, as reflected 231 

in Jain’s pioneering autoethnographic work as a DHH traveler [26], getting in-depth longitudinal experiences from 232 

marginalized populations who might be less willing to travel could be challenging. Second, prior studies have 233 

demonstrated that when designing and introducing novel multi-algorithm AI systems, starting with a “deep engagement” 234 

with a single person and community might be the more responsible approach that allows close and critical examination 235 

of that person’s perspective and environments from a more involved standpoint [45, 55].  236 

We proceeded with the study only after obtaining IRB clearance and Declan’s consent with IRB-approved consent 237 

forms. 238 

4 PHASE 1: FORMATIVE STUDY 239 

The goal of Phase 1 was to understand (1) Declan’s personal contexts and routines, (2) Declan’s current approaches to 240 

making sense of the environments, and (3) challenges across his daily routines and tasks due to hearing loss. 241 

4.1 Method 242 

While the general study methodology is detailed in Section 3 above, here we describe the specific procedures for this 243 

study. 244 

4.1.1 Procedure. 245 

We kicked off Phase 1 with a 150-minute meeting with Declan in our research lab on the University of Michigan campus. 246 

Before the session, Declan completed a background questionnaire about his demographic and hearing loss-related 247 

information. We introduced Declan to the logistics of co-design and the goal of creating a sound awareness system that 248 

facilitates his sensemaking of auditory environments. We stressed to Declan that he would be an active co-designer 249 

instead of a participant simply providing feedback to a system. 250 

To understand Declan’s personal contexts, the first author asked Declan about his daily routines on weekdays and 251 

weekends and visualized them on a chart paper with post-it notes (Figure 3). The first author then collaborated with 252 

Declan to examine the visualized routines by breaking them into individual tasks. For example, the “cooking dinner” 253 

routine was broken into tasks such as grabbing ingredients from the fridge, chopping and preparing ingredients, heating 254 

potatoes using microwaves, pan-frying, etc. The tasks were visualized using sketching tools (e.g., colored pens; Figure 255 

3). For each task, the researcher discussed Declan’s challenges due to hearing loss and the existing strategies he applied 256 

to help address the challenges. For instance, in the “cooking dinner” routine, we highlighted the “heating potatoes” task 257 

and asked, “How did your hearing loss make heating potatoes in the microwave difficult?” and “What kind of information 258 

would be helpful?” The researcher repeated this in-depth analysis for each of Declan’s routines. 259 

 260 Figure 3: Sketches from Phase 1’s Formative Study. From left to right: (1) Declan’s personal routines and contexts, (2) 261 Declan sketching the “frames” and corresponding information needs within the routines, and (3) the numerous sketches 262 of Declan’s information needs across personal contexts.  263 

After the session, the first author kept in touch with Declan through text messages and emails. Following the analysis 264 

detailed in the following section, our team scheduled a 45-minute video call with Declan, during which he answered 265 

additional questions that surfaced from the analysis (e.g., the spatial layouts of Declan’s home and workplace). 266 

4.1.2 Analysis. 267 

Phase 1 elicited five types of research data about Declan’s personal contexts, routines, and experiences as a DHH person: 268 

transcripts from meetings and video calls, video recordings, sketches, and text messages and emails. We stored these 269 

data in the same Google Drive folder for convenient cross-referencing. We analyzed the data following the open, axial, 270 

and selective coding methods specified in Section 4. Specifically, the first author walked through the data and generated 271 

57 open descriptive codes in the working document. During the walkthrough, the first author considered all routines 272 

and tasks to gain a holistic understanding of Declan’s personal contexts and sensemaking approaches across contexts. 273 

The second and last author reviewed these open codes and added 21 more. We note that the last author related the open 274 

codes to his experience as a DHH person by commenting on the codes in the document. The research team met four 275 

times to translate open codes into insights that guided the design of the sound awareness system prototype. The team 276 

intermittently added their thoughts to the working document between meetings. The working document at the end of 277 

Phase 1 contained 6593 words. 278 

4.2 Findings 279 

We first highlight the findings that contributed to eliciting design goals and considerations before discussing the latter. 280 

These findings came from our analysis of the raw results to carve out Declan’s information needs across personal 281 

contexts. 282 

4.2.1 Declan’s Personal Contexts. 283 

Declan’s workday routines include cooking, driving to work, and working at the nursing home. At the nursing home, 284 

Declan’s routines consisted of team huddles and one-on-one reports, passing water and linens, taking care of patients 285 

(e.g., getting residents up for activities, wash-ups, working on the IV pumps), charting, and serving dinner. For non-286 

workdays, Declan would drive to the nearby city to play trading card games with his friends at a game store. Declan 287 

would also drive to the local church for the Sunday service and coffee hours. 288 

4.2.2 Varied Information Needs and Sensemaking Intents Across Contexts.  289 

Across personal contexts, Declan had varied sound information needs based on intent:  290 

Awareness of the Environmental Sounds: When entering a new environment, Declan usually “did not know what 291 

to expect.” Therefore, he hoped to get a holistic sense of the new ambient environment: “Let’s say I walk into a room… I 292 

want to immediately know how loud the room is. It’s almost like a vibe check.” Once situated in the environment, Declan 293 

wanted to know the individual sound events. Most of the time, Declan used visual and haptic feedback to make sense of 294 

the events. For example, at home, his partner would stomp on the ground to grab Declan’s attention. At his place of 295 

work (nursing home), Declan used call lights and other visual feedback (e.g., co-workers’ reactions and monitors) to 296 

understand when residents needed his attention. However, sometimes those visual cues were not easily glanceable or 297 

available: “When I am working at the station, I would have to frequently pop my head over and see if there are lights down 298 

in the hallway.” 299 

Declan told us that he was familiar with sound recognition systems (e.g., Google’s Sound Notifications) but was not 300 

impressed by their performance. He used ASL’s description of objects as an analogy [25] for understanding sound events: 301 

“Paint a broad stroke first, then describe details.” Declan first wanted to access more general descriptions of sound events 302 

(e.g., direction and real-time sound level) to incorporate other perceptual abilities (e.g., vision) to make sense of the 303 

information before knowing specific details. “Most of the time, I don’t want to know what it is. I just want to know that it’s 304 

here… If I find interest, then I can be like, ‘What do you think it is?’” He added. In addition to environmental awareness, 305 

Declan also wanted to increase awareness of the sounds he produced (e.g., whether he was making too much noise or 306 

speaking too loudly). 307 

Active sound monitoring: Besides awareness of intermittent sound events, sometimes Declan worked on 308 

specialized tasks requiring more specific, precise, and instant recognition of sounds. We refer to this need as “active 309 

sound monitoring.” There were two general scenarios where Declan needed more active sound monitoring. The first 310 

scenario concerned fault detection – the presence of abnormal sounds and the absence of expected sounds. For example, 311 

Declan described his experience using self-checkout stations: 312 

“Scanner beeping… like the ‘doo’ sounds at the checkout. I cannot tell if I actually scanned the item… like, am I 313 shoplifting right now, or what’s going on?” 314 

The last author, who is hard of hearing, related to this challenge and shared another case of failed fault detection 315 

with the research team, where he could not tell when something “got stuck in the garbage disposal.” Another scenario 316 

category concerned the processes (i.e., sequences of events) with critical acoustic changes that required attention. For 317 

example, Declan could not tell when the pianist started or stopped playing during the church service. Similarly, at work, 318 

he had difficulty knowing the real-time status of the IV pump – standard beeps signaled normal operation, while melodic 319 

chimes indicated potential issues. As a result, he had to “constantly pop his head” to look at the monitor. 320 

Social Interactions: Declan primarily used American Sign Language in Deaf environments or when communicating 321 

with people who used ASL. When interacting with hearing people, Declan used a combination of lipreading and 322 

captioning. During the discussion, Declan highlighted three information challenges: 323 

1. Difficulty locating the speaker in predominantly hearing environments, especially in larger and more scattered 324 

spaces. 325 

2. Increased reliance on captioning when lipreading became difficult (e.g., communicating with people with 326 

“thick facial hair” or facing with his back against him). 327 

3. Difficulty in recognizing people’s calls for attention. 328 

4.2.3 Declan’s Hearing Loss Created New Dynamics, Interactions, and Expressiveness. 329 

In addition to challenges and information needs, we discussed Declan’s existing strategies for understanding the auditory 330 

environment. This conversation surfaced valuable insights on how Declan created access intimacy [4, 67, 68] with social 331 

interactions and used creative expressions as strategies to work and live around hearing loss. These findings sparked 332 

our reflections on how our novel sound awareness system could potentially impact Declan’s relationships with 333 

technology, the environment, and the people around him.  334 

Declan described his experience with the piano music played during the church service:  335 

“Our church pianist, Anita, knows that I can’t hear. So, if she is done playing and I am looking at her, she will look at 336 me and nod her head or take her hands off the keys.” 337 

 Due to his limited access to the music, Declan did not know when the music would start (so he could pay attention). 338 

To address this, the church pianist and Declan turned to gestures (e.g., exaggerating the palm being placed or taken off 339 

the piano gesture) as accessible visual cues to inform Declan of the start and end of the piano music session. However, 340 

there were times when a guest pianist was called to play. “In that case, it would be nice to have someone telling me,” 341 

Declan told us. Future systems should consider these situations and be careful not to forcibly introduce novel 342 

sensemaking processes that might disrupt the current ones. 343 

Declan usually spent his Saturday afternoon playing Magic: The Gathering with his friends at the game store. When 344 

Nathan, Declan’s friend who is Deaf and uses hearing aids, joined him, Declan trusted Nathan as the companion for 345 

achieving collective sound awareness: 346 

“My friend, Nathan, is Deaf and uses ASL. He also has hearing aids. So, I am basically clocked out when hanging out 347 with him. I’m like, OK, I am not going to be on the lookout for anything… if you hear something, you will let me know, 348 because you know I can’t hear anything. Hearing people don’t always remember that.” 349 

In this case, Declan and Nathan’s interdependent relationship was more personal, intimate, and potentially effective 350 

for achieving sound awareness. We took this scenario into account in the design of our artifact by allowing Declan to 351 

stop the system’s sensing behaviors and defer the task to his trusted companions. 352 

To avoid being mistaken as ignoring other people, Declan used T-shirt graphics as a creative means to inform other 353 

people of his Deaf identity: 354 

“A lot of people think I am being rude when I don’t hear them… If I am going out grocery shopping or at the Pride event, 355 I have T-shirts that have the ‘I love you’ ASL sign and says, ‘I am not ignoring you, I’m Deaf.’” 356 

Declan’s graphic T-shirts are a great example of how accessibility solutions can be expressive. Assistive technologies 357 

have traditionally prioritized functions over forms [34]. However, recent studies have found that people with disabilities 358 

consider aesthetics to be an important consideration when choosing ATs [34, 54]. Affirming this finding, we hope it 359 

sparks a new conversation about expressiveness and creativity in the design and use of accessibility tools. 360 

4.2.4 Design Goals and Reflections. 361 

Our mixed-ability research team critically reflected on the Phase 1 findings and used them to shape the design goals of 362 

future sound awareness systems. We emphasize that these design goals are not merely direct products of Declan’s 363 

experiences but a higher-level reflection of what a future sound awareness system should look like inspired by Declan’s 364 

grounded experiences and established knowledge in DHH accessibility (e.g., DeafSpace [48, 78]). We describe the design 365 

goals as well as the specific findings and thoughts that inspired them: 366 

DG1: The display of sound information should adapt to Declan’s ever-changing intents across personal 367 

contexts. Across Declan’s personal contexts, we categorized the intents into three broad categories: awareness of 368 

environmental sounds, active, detailed monitoring of sounds related to specific tasks (e.g., checking out at the grocery 369 

store, cooking, etc.), and social interaction—each intent category called for different kinds of awareness of sound 370 

information, leading to DG1. 371 

DG2: The delivery of sound information should complement Declan’s trusted sensemaking approaches 372 

instead of replacing them. Declan briefed us about his way of processing sound information: “Paint a broad stroke 373 

first, then describe details.” Specifically, he learned the general sound information (e.g., loud noise) first, followed by 374 

specific details (e.g., a loud blender sound) only when necessary. As designers, we should respect DHH people’s trusted 375 

sensemaking approaches, avoid redundant information, and ensure that the system is compatible with them. 376 

DG3: Sound awareness systems should be designed with mindfulness toward their influence on social 377 

dynamics and connections. While prior studies studied how social contexts could impact the acceptability of AI-based 378 

sound awareness systems [15, 24, 31], we bring to attention these systems’ impacts on DHH people’s existing social 379 

dynamics. For example, Declan had established unique access intimacy [67] through “collective access” of sound 380 

information with his friend Nathan and personal cues from the church pianist Anita, an important part of his Deaf 381 

identity. Aligning with DG3, the design of SoundWeaver should support these interactions, not replace them. 382 

DG4: The system should promptly visualize anomalies and other notable changes in the auditory 383 

environments. Across different contexts, Declan has used his perception of visual cues to make sense of the 384 

environments (e.g., using call lights to indicate if residents needed attention), which was consistent with prior theories 385 

in the Deaf Culture [78]. However, these real-world visual cues were not always accessible (e.g., call lights being out of 386 

sight). Sound awareness technologies could reduce this barrier by providing always-on and glanceable visualizations of 387 

the changes or anomalies in the ambient acoustic environments.  388 

4.3 High-Level System Design and Specifications 389 

Based on the design goals and critical reflections on Declan’s personal contexts, we curated an initial system specification 390 

that would potentially inform the design of SoundWeaver. We hypothesized that the system design would be intent-391 

driven, with three modes of weaving sound information to accommodate three broad intents for sound awareness 392 

highlighted in DG1. Users could freely switch among the three modes based on their real-time information needs. We 393 

list the three weaving modes and specify the user intents each mode supports: 394 

Awareness Mode. Awareness mode fulfills DHH people’s needs for awareness of overall auditory 395 

environments and individual sound events specified in Section 4.2. 396 

Action Mode. Action Mode facilitates active sound monitoring. This mode supports more focused tasks 397 

where continuous awareness of a certain set of sounds is required. 398 

Social Mode. Social Mode supports DHH people’s social interactions while maintaining the necessary 399 

awareness of the auditory environments (e.g., knowing the smoke alarm going off when chatting with friends). 400 

The above three modes were directly mapped to the three categories of Declan’s intents across personal contexts. On 401 

a high level, the three modes streamlined different kinds of awareness by weaving AI outputs to fulfill DHH users’ 402 

dynamic information needs. Moreover, switching among the three modes would be an effortless process with minimal 403 

interactions needed. We envisioned the design of each mode to match Declan’s preferred way of processing auditory 404 

information to fulfill the corresponding intent (DG2) and operationalized this vision through a co-design process with 405 

Declan in the following section. 406 

5 PHASE 2: CO-DESIGN OF THE SOUNDWEAVER PROTOTYPE 407 

Phase 2 consisted of a series of co-design activities that led to the creation of the SoundWeaver prototype. 408 

5.1 Initial Prototype 409 

Guided by the high-level system design, we began with an initial prototype that embodied the design goals listed in 410 

Phase 1. The goal of this initial prototype was not to provide a polished design solution but rather to serve as a starting 411 

point for our co-design process. 412 

5.1.1 Design. 413 

The initial SoundWeaver prototype contained three buttons indicating the three modes of weaving sound information: 414 

Awareness, Action, and Social. Users could switch among the modes by pressing any of these buttons, and the 415 

SoundWeaver interface automatically reorganized information to match the new mode without the need for further 416 

customization (DG1).  417 

Awareness Mode: The Awareness Mode contained three types of sound information: sound level, recognized sound 418 

events, and the textual description of the overall acoustic environment. To help DHH people notice changes in acoustic 419 

environments visually (a primary environmental sensemaking approach specified in DeafSpace [78]), we used dynamic, 420 

color-coded tooltip indicators to represent four discrete sound levels: quiet, ambient, loud, and very loud. We also 421 

interfaced with Audio Flamingo [35], an audio language model, to present textual descriptions of auditory environments. 422 

Labels of recognized sound events were hidden by default, but users could manually toggle their display on and off. This 423 

design aligned with DG2, which called for designs that complement Declan’s preferred way of processing sound 424 

information (i.e., “Paint a broad stroke first, then describe details.”) 425 

We present a vignette describing the potential use of this mode: when Declan entered a coffee shop, he noticed the 426 

loudness indicator turning from green (“quiet”) to blue, showing an “ambient” label. To help him know what to expect 427 

in this environment, he asked the system to briefly describe the ambient acoustic scene (e.g., “Multiple people chatting”). 428 

When Declan was fully situated in the context, he used the loudness indicator to help him judge if any event had occurred. 429 

When he noticed the loudness indicator turning from blue (ambient) to orange (loud), he toggled on the display of 430 

recognized sound events and saw a “blender” sound. He looked around and saw that the barista was blending smoothies. 431 

Action Mode: Users could configure the task by assigning relevant sounds to monitor in a companion app. Once 432 

configured, all the selected sound labels would be pinned to the interface. If a sound occurred, the corresponding label 433 

would turn green; otherwise, it stayed gray. For example, Declan programmed the “cooking” task to monitor water 434 

boiling, microwave done, and sizzling sounds. These three sound labels were then pinned. When the microwave was 435 

done heating Declan’s food and elicited a 5-second chime, the “microwave done” label turned green for 5 seconds. 436 

Social Mode: Social Mode facilitated social interactions by providing captions while preserving awareness of 437 

environmental sounds. Informed by prior work on HMD sound visualizations [28], we used arrows as directional 438 

indicators of active speakers. Social Mode also included live transcriptions with medium-bold font and transparent 439 

backgrounds to ensure the visibility of texts (as suggested by best practices for captioning [79]) and the physical space. 440 

Finally, the initial design in Social Mode displayed labels of recognized sound events below the transcription. 441 

5.1.2 Implementation. 442 

The prototype contained two components: the front-end interface and the back-end server. The front-end interface was 443 

implemented as a visionOS application based on an Apple Vision Pro running visionOS 1.2. The back-end server was 444 

based on an iPhone 13 Pro Max running iOS 17.3 and Firebase [80]. Due to the limited sampling range of iPhone and 445 

Vision Pro microphones, the system used an external clip-on microphone (DJI Mic 2). Real-time audio streams collected 446 

by the microphone were transmitted to the iPhone through Bluetooth. The iPhone handled the signal (e.g., calculating 447 

sound levels) and AI (e.g., sound classification) processing locally, except for acoustic scene understanding tasks. 448 

Specifically, we used Apple’s SoundAnalysis framework [72] to achieve real-time sound classification and Apple’s 449 

Speech framework [81] to achieve live captioning. We configured the system to recognize 96 sound classes based on 450 

Declan’s preferences and prior work probing DHH people’s desired sound events [8, 15, 32]. We hosted the Audio 451 

Flamingo model on Google Cloud Platform [82] as an API for acoustic scene understanding tasks. The prototype 452 

interfaced with the Audio Flamingo model by uploading a 5-second audio clip with the prompt “Please provide a 453 

description of the audio.” The output of the model contained a textual description of the audio clip. The four discrete 454 

sound levels in Awareness Mode were: (1) Quiet: less than -50 dBFS, (2) Ambient: -50 dBFS to -30 dBFS, (3) Loud: -30 455 

dBFS to -10 dBFS, and (4) Very Loud: -10 dBFS to 0 dBFS. 456 

Users could configure Action Mode behaviors on the iPhone with a companion iOS application, which transmitted 457 

the configured tasks to Firebase as JSON data. All the real-time data, including sound recognition results, transcriptions, 458 

and sound level, were also relayed to Firebase. We implemented SoundWeaver’s interface as a head-mounted display 459 

(HMD) application because HMD was rated as one of the preferred form factors for mobile sound awareness systems 460 

[15]. Declan reinforced this prior finding, telling us that “having to pull up the phone” was tedious and that having direct 461 

access to sound information “through something like Google Glass” would be “extremely helpful.” However, we 462 

acknowledge that the Vision Pro’s form factor can be cumbersome for daily use and reiterate that our prototype served 463 

primarily as a design artifact for exploration. 464 

5.2 Method 465 

5.2.1 Procedure. 466 

Phase 2 consisted of a series of co-design activities to refine the SoundWeaver prototype iteratively. We invited Declan 467 

to the second 150-minute in-person meeting in our research lab. We first introduced Declan to the state-of-the-art AI 468 

for sound awareness, including sound classification, speech-to-text, and acoustic scene understanding. We discussed the 469 

capabilities, outputs, and limitations of these systems and emphasized that the raw outputs could be adapted based on 470 

his personal contexts and intents – the umbrella goal of the SoundWeaver prototype. 471 

Then, Declan experienced the initial SoundWeaver prototype through a guided demonstration of the Vision Pro 472 

device. The demonstration was not for system evaluation; rather, it primarily focused on introducing the three weaving 473 

modes and the available AI tools (i.e., sound classification, speech-to-text, and acoustic scene understanding) as design 474 

materials for the upcoming co-design activities. We also used this demonstration to familiarize Declan with visionOS 475 

and spatial applications to ensure that Declan could comfortably interact with our prototype in the future. After the 476 

demonstration, we asked Declan, “What are your thoughts on the three modes?” Declan approved this layout, saying: “I 477 

like that you separated it into the three different [modes]. It was getting nebulous with all the [sound information] we talked 478 

about before.” 479 

With Declan’s support on the three-mode design, we dove into the detailed user experience prototyping. Before the 480 

process, we reminded Declan that the goal of our design was not to replace Declan’s perceptual and cognitive abilities. 481 

Instead, we were co-designing a tool for enhancing and complementing his existing ways of sensemaking. We revisited 482 

the sketches about Declan’s personal contexts and routines from Phase 1 and discussed Declan’s preferred sound 483 

information across the routines/frames, suitable modes for the desired information, and how the information should be 484 

presented on the head-mounted display. We used an iPad instead of paper as the canvas for sketching because it allowed 485 

us to use images of environments like living rooms and kitchens to help simulate a first-person view through an AR 486 

display. 487 

Throughout the co-design process, we encountered several instances where the promises of the system's capabilities 488 

conflicted with technical constraints and user experience considerations. Our approach involved transparent 489 

communication about these conflicts, followed by collaborative problem-solving with Declan to develop practical 490 

solutions. For technical challenges, we focused on workable alternatives. For example, upon realizing that ASR 491 

performed poorly in noisy settings, we decided that the system should explicitly inform Declan, allowing him to utilize 492 

lipreading as a “backup option.” Similarly, Declan proposed a feature that pinpoints the direction of the person calling 493 

him. Given that this level of localization was currently difficult to achieve, we decided that using speech recognition to 494 

detect his name would be more reliable. For user experience challenges, the first author carefully stated and visualized 495 

the design limitations and worked with Declan to explore the alternatives. For example, we considered a design that 496 

would position sound events according to their physical directions (e.g., sounds originating from the left would appear 497 

on the left side of the screen). However, we later determined this design would cause visual clutters and unnecessary 498 

distractions. 499 

Following the initial meeting, we maintained ongoing communication with Declan via text messages over two 500 

months while iterating on the SoundWeaver prototype. We also provided regular asynchronous updates on the system’s 501 

development progress and solicited Declan’s feedback during this time. We also presented Declan with multiple design 502 

variations for specific features, asking him to evaluate each option and provide his rationale for any preferences. 503 

5.2.2 Analysis. 504 

Phase 2 data consisted of meeting transcripts, text messages, and digital sketches about SoundWeaver’s potential 505 

interfaces across Declan’s personal contexts and routines. To guide the next iteration of the SoundWeaver prototype, 506 

we followed the same open, axial, and selective coding process on the mixed-format material as in Phase 1. The research 507 

team met weekly to discuss the codes and translate the insights into concrete design decisions for the prototype. This 508 

analysis yielded 91 new open codes. 509 

5.3 Findings 510 

5.3.1 Reflections and Changes in Design Goals. 511 

We present the updates to the design goals based on the two categories of new insights specified above and provide the 512 

rationale behind the changes. 513 

NEW DESIGN GOALS (DG5, DG6): 514 

DG5: Sound awareness systems should inclusively support individuals with intersectional disabilities and 515 

diverse identities. During the co-design session, Declan disclosed that he was neurodivergent. As he explained, “If I 516 

had too much information, I would go into a meltdown,” highlighting how neurodivergent individuals can experience 517 

heightened sensitivity to busy or cluttered visual stimuli [12]. This revelation prompted our critical reflections on the 518 

broader implications for the system design. We recognized that similar considerations should extend to users with 519 

various combinations of disabilities and identities, such as DeafBlind individuals or DHH people with cognitive abilities. 520 

Recently, intersectional disabilities have received increasing attention in accessible technology research. For example, 521 

Harrington et al. advocated race and ethnicity as important constructs for integrating racial equity in accessibility work 522 

[19]. We echo this advocacy through the proposal of DG5 and hope that this work can spark more conversations on this 523 

important topic. 524 

DG6: The system should carefully handle inference-based or interpretive information and not replace 525 

DHH people’s reasoning process by forcefully interpreting outputs. When demonstrating the acoustic scene 526 

understanding feature, we played the dog barking sounds from YouTube. The system presented the output: “I hear an 527 

anxious dog barking.” Declan was unsure about the model’s behavior: “It was attributing reasons to be the sounds… I was 528 

like, okay, the computer has no way of knowing that.” We reflected on this sentiment and agreed that AI sound awareness 529 

systems should not replace DHH people’s reasoning process by forcefully presenting interpretive outputs. This point 530 

was also reflected in the prior work, where ASL interpreters demonstrated that when it comes to interpreting “unknown 531 

sounds,” it was important to “show, not tell. [25]” Several studies in the broader accessibility research argued that 532 

assistive technologies should strive to be a “solution to a sensory problem” rather than the primary source of information 533 

[58, 62], a point echoed by Declan: 534 

“We are using this as an accessibility tool – and it’s not like, ‘we want to know everything about everything.’ Basically, 535 we want access to the same information that hearing people have. And when a hearing person is in another room and 536 hears a crashing sound, they are not going to know what the crash was about. So, I would not want the computer to try 537 to figure out what the crash is about. I will go and investigate it.” 538 

Other findings reinforced our existing design goals. In the initial prototype design, Action Mode used the alternation 539 

of colors to indicate the presence (green) and absence (gray) of sounds. Declan voiced concerns about this design in 540 

Phase 2 because it would alter the existing way Declan processed information: 541 

“It’s a tricky one because that design is a lot… I have a very specific way of processing information, and I don’t think 542 about the sounds that aren’t there because I have never been in a situation where it’s necessary. You are trying to help 543 us, not change us. It’s important to not impose a different way of processing information.” 544 

This feedback reiterated the importance of designing sound awareness systems compatible with DHH people’s 545 

trusted sensemaking approach (DG2). It also illustrated how designers’ preconceptions can lead to “invasive” designs 546 

that are counterintuitive to marginalized communities and interfere with their existing ways of living – a pattern that 547 

resembles “colonization in design [83].” Furthermore, this experience reaffirmed the necessity of engaging in sustained, 548 

iterative co-design processes with target user communities to develop truly beneficial solutions. 549 

5.3.2 Prototype Evolution 550 

Throughout Phase 2, we worked closely with Declan to continuously iterate the SoundWeaver prototype. Here, we 551 

present its design evolution, also visualized in Figure 5. 552 

5.3.2.1 Awareness Mode Evolution. 553 

Sound level indicator: In Awareness Mode, we replaced the discrete, colored-coded sound level indicator with a 554 

waveform that visualizes the sound levels for the most recent five seconds. This design change was based on Declan’s 555 

preferences for symbolic over textual representations: “Pictures are better than words. Deaf people born deaf typically have 556 

a lower rate of being able to read English.” Moreover, we discovered that when sound levels fluctuated near the thresholds, 557 

the indicator colors frequently changed, which could cause considerable discomfort for neurodivergent DHH users. 558 

Displaying sound event labels. In the initial prototype, once the display of sound recognition results was toggled 559 

on, it would remain active until manually deactivated. This design conflicted with Declan’s preference for receiving 560 

“occasional inputs” about the identities of sound events. He felt that the more natural way for him was to have the system 561 

“telling him something is going on” and ask him if he wanted to know the names of the recognized sounds. Based on this 562 

feedback, we implemented a new mechanism: when the system detected a spike in sound level, a prompt “Show Sound 563 

ID?” would appear. Once the system received a “go-ahead” from the user, it displayed sound event labels for five seconds. 564 

Otherwise, the prompt would fade away after five seconds. 565 

Acoustic scene understanding. Based on Declan’s feedback about the system’s overinterpretation of the acoustic 566 

scene (e.g., attributing reasons), we adjusted the prompt to make the information more descriptive rather than analytical 567 

(i.e., “Please provide a neutral description of the audio without any extra details or interpretations in a short sentence.”), 568 

aligning with DG6. We also fixed the output to shorter phrases to reduce the visual clutter and prevent information 569 

overload (DG5). 570 

5.3.2.2 Action Mode Evolution. 571 

The initial Action Mode design displayed all task-related sounds continuously, using green highlights to indicate sound 572 

occurrence. Based on Declan’s feedback specified in Section 6.3, we implemented a more selective approach: users could 573 

designate specific sounds for continuous monitoring by “starring” them, which would pin these sounds to the heads-up 574 

display. Other sound events would only show up when they occurred. The research team debated whether the pinning 575 

system should be removed entirely but decided to keep it as an optional feature because Declan stated that visualizing 576 

the presence and absence of sounds could be helpful in certain situations (e.g., ensuring the water was boiling). 577 

5.3.2.3 Social Mode Evolution. 578 

We omitted the sound recognition results and replaced them with the same sound level visualization waveform used in 579 

the Awareness Mode. This design change was inspired by two realizations. First, Declan emphasized that focusing on 580 

the transcription took precedence over identifying specific sounds in social settings like a game store. Nevertheless, he 581 

still wanted to maintain some degree of environmental awareness during conversations. Second, we recalled from the 582 

formative study that Declan’s trusted friends would inform him of important sounds, a common practice in Deaf 583 

communities [78]. This dynamic effectively addressed Declan’s sound identification needs, making system-generated 584 

recognition results unnecessary. This change aligned with both Declan’s desired sound awareness approach (DG2) and 585 

preserved the access intimacy [67] between him and his trusted companions (DG3).  586 

The caption component initially featured white text on a transparent background, based on our assumption that this 587 

design would minimize visual clutter and maintain Declan’s visual awareness. However, Declan suggested enclosing the 588 

captions in a semi-transparent box to enhance readability while preserving the visibility of “things behind it.” He noted 589 

that other DHH individuals might have different preferences. 590 

Recognizing the automatic speech recognition’s performance limitations in noisy environments, we implemented a 591 

warning system that notified users about potential captioning accuracy issues when it detected elevated ambient noise 592 

levels. This design aligned with established guidelines for human-AI interaction [1, 75] about supporting the “efficient 593 

dismissal” of AI services. 594 

5.3.2.4 Overrides for Critical Sounds 595 

During the co-design, we realized that critical sounds, like emergencies and name-calling, could be overlooked in the 596 

initial prototype due to the lack of explicit alerts. Reflecting on prior work in DHH sound awareness [8, 15, 24, 32], we 597 

concluded that critical and safety-related sound information (e.g., emergency sounds and name-calling) should be 598 

displayed regardless of the current mode and updated the prototype accordingly (Figure 6; 4A and 4B). 599 

6 PHASE 3: FIELD EVALUATION 600 

In Phase 3, we deployed the second iteration of the SoundWeaver prototype to Declan’s routine environments. We 601 

considered field deployment an integral part of the co-prototyping process because AI carried inherent uncertainty in 602 

its capability as a unique design material [61, 64]. Moreover, evaluating SoundWeaver in the field allowed us to probe 603 

two critical questions. First, how could “intent-driven” AI systems fulfill DHH people’s dynamic information needs? 604 

Second, how would the SoundWeaver prototype blend into the intricate social and environmental dynamics across 605 

Declan’s personal contexts? Exploring these questions in the wild allowed us to elicit new design opportunities for 606 

effective human-AI interaction design for sound awareness systems. 607 

6.1 Method 608 

6.1.1 Procedure. 609 

We evaluated the second-iteration SoundWeaver prototype across two distinct personal contexts: Declan’s home and a 610 

game store he frequently visited. We did not evaluate the prototype at Declan’s workplace (i.e., nursing home) due to 611 

the employer’s concerns about the privacy of nursing home residents. We utilized a portable microphone (DJI Mic 2) for 612 

audio capture and transmission to address the audio sampling limitations inherent in Vision Pro and iPhone 613 

microphones. 614 

At home, we first provided a guided demonstration of the SoundWeaver prototype and asked about Declan’s first 615 

impression. Declan then used the system while performing three general tasks: engaging with his partner and pets, 616 

cooking, and participating in conversations. We simulated possible at-home sounds by knocking on the door, playing 617 

smoke alarm sounds through the phone, turning the faucet on and off, dropping books onto the floor, etc. We observed 618 

the interactions by mirroring the Vision Pro screen on an iPad. This session lasted for two hours. 619 

At the game store, Declan used SoundWeaver while playing Magic: The Gathering with his four friends while sitting 620 

around a table. The first author observed the interactions from the side of the table and took field notes. The Vision Pro 621 

screen was mirrored on the first author’s iPad as in the previous session. This session lasted for 2.5 hours. 622 

Following each session, we conducted semi-structured interviews to learn about Declan’s experience using the 623 

system and gather feedback on the sound information’s quantity, presentation, and contextual appropriateness. 624 

 625 Figure 4: Declan uses the SoundWeaver prototype when cooking at home (left) and playing card games with friends 626 (right). 627 

6.1.2 Analysis. 628 

Phase 3 data contained handwritten field notes and transcripts from two field evaluation sessions generated by Google’s 629 

voice recorder app. We again followed Grounded Theory-inspired approaches (i.e., open, axial, and selective coding) to 630 

analyze these materials. Phase 3 elicited 62 new codes. The research team met twice to analyze the open codes and 631 

compare them to the existing data. 632 

6.2 Findings  633 

6.2.1 Notes from Field Evaluation 634 

We present notable snippets of Declan’s interactions with the SoundWeaver prototype at home and the game store that 635 

sparked reflections among the research team and guided the final iteration of the SoundWeaver prototype.  636 

When Declan was petting his cats on the couch using the system, we called Declan’s name to initiate a conversation. 637 

Upon seeing the system message “Someone may have called your name,” Declan looked up and manually activated Social 638 

Mode by tapping the “Social” button, transitioning from Awareness Mode to access the caption feature. In subsequent 639 

feedback, Declan noted that this mode-switching process felt “unnatural” and desired a more seamless transition. He 640 

suggested incorporating the name-calling message into an interactive button that would automatically activate Social 641 

Mode when selected. 642 

When we simulated a visitor by knocking on the door, Declan’s dog started barking. Declan was confused about the 643 

considerable fluctuations in the waveform. Instead of prompting the system to show sound recognition results, Declan 644 

immediately looked around to locate the sound source. When asked about this interaction, Declan explained that looking 645 

around was “much faster” than “tapping a button to know what’s going on.” 646 

In Phase 2, we changed the delivery of sound recognition results from manual toggles to a prompt-based delivery 647 

(i.e., “Show Sound ID?”) triggered by sudden sound level spikes. After extensive usage at home, Declan told us that the 648 

sound recognition results were “much more refined” than he expected, and he “would not mind having it constantly on,” 649 

ultimately favoring the manual toggle-based approach. 650 

During the Magic: The Gathering game, Declan primarily used Social Mode due to the game’s conversational nature. 651 

He noted two main concerns with the interface. First, the fluctuating waveform created a visual distraction that made it 652 

difficult to focus on the active speaker. Second, given the small group size (four players), Declan found the directional 653 

arrows indicating active speakers unnecessary and distracting, particularly during rapid speaker transitions. He 654 

suggested displaying speaker names would be more helpful than directional indicators in small group settings.  655 

Before the game session, the first author anticipated potential caption performance issues in two specific scenarios: 656 

multiple speakers talking at the same time and when the active speaker was positioned at a distance (e.g., sitting 657 

diagonally across the table). These concerns were validated during the session. However, Declan and his companions 658 

devised an effective solution by implementing a “talking stick” approach, passing the portable microphone among 659 

speakers. This method notably enhanced both caption accuracy and reduced latency. 660 

We also worried that inaccurate or incomplete captions might adversely impact Declan’s understanding of the 661 

conversation and raised this concern with Declan. We asked Declan if the system should stop displaying captions to 662 

allow Declan to focus on lipreading when the caption performance became subpar. To our surprise, Declan told us that 663 

even when the caption was inaccurate, it identified some important words he failed to catch with lipreading; thus, he 664 

preferred leaving the caption on regardless of its performance. The session concluded after two hours when Declan 665 

removed the Vision Pro due to fatigue. 666 

 667 Figure 5: The Design Evolution of the SoundWeaver Prototype Across Design Phases. Each color-coded section indicates 668 the design iterations for one of SoundWeaver’s three modes (Awareness in the blue section, Action Mode in green, and 669 Social Mode in yellow). We also use floating tooltips with border colors that match the corresponding mode to highlight 670 changes in the current iteration. For example, in the second iteration of the Social Mode design, we replaced the colored 671 text box with waveforms as indicators for ambient sound level and added a semi-transparent background to the caption. 672 Similarly, in the third iteration of Social Mode, we removed the arrow pointing to speakers and replaced it with speaker 673 names to avoid visual distraction. 674 

6.2.2 Reflections, Design Goal Updates, and Prototype Evolution. 675 

Based on the findings, we made one update to DG1: 676 

DG1: The display of sound information should adapt to DHH people’s ever-changing intents across 677 

personal contexts. Moreover, the adaptation process should require minimal effort from the users. 678 

The change to DG1 was inspired by Declan’s comment that the current method of switching modes and retrieving 679 

sound recognition results felt “unnatural” and required constant manual inputs. This concern was also reflected in prior 680 

work, where DHH users expressed willingness to provide inputs to sound awareness systems but indicated that 681 

repeatedly asking for manual inputs would eventually lead to them “giving up” altogether [24]. 682 

We made three changes to the prototype. First, as Declan suggested, we made the name-calling alert interactive, 683 

enabling an automatic transition to Social Mode when tapped. We applied the same interaction pattern to the “speech” 684 

label in sound recognition results. Second, to address Declan’s concerns about waveform fluctuations creating visual 685 

distractions during conversations, we replaced the waveform-like sound level visualizer with a “sound bubble” 686 

positioned in the corner of the screen. The bubble expands as the sound level increases, providing a more subtle and less 687 

intrusive representation of sound. Third, we reverted Awareness Mode’s sound recognition results to the Phase 1 design, 688 

reinstating the manual toggle feature. Our curated design goals across three co-design phases are presented in Table 1, 689 

while the final SoundWeaver prototype is shown in Figure 6. 690 

Table 1. Our final curated design goals for intent-driven sound awareness systems to support Declan. 691 

CODE DESIGN GOALS 

DG1 The display of sound information should adapt to DHH people’s ever-changing intents across personal contexts. Moreover, the adaptation process should require minimal effort from the users. 

DG2 The delivery of sound information should complement DHH people’s trusted sensemaking approaches instead of replacing them. 

DG3 Sound awareness systems should be designed with mindfulness toward their influence on social dynamics and connections. 

DG4 The system should promptly visualize anomalies and other notable changes in the auditory environments. 

DG5 Sound awareness systems should inclusively support individuals with intersectional disabilities and diverse identities. 

DG6 The system should carefully handle inference-based or interpretive information and not replace DHH people’s reasoning process by forcefully interpreting outputs. 

 692 Figure 6: The Final Design of the SoundWeaver Prototype. In Awareness Mode (Interface 1), the system displays a 693 waveform indicating sound levels by default. Users can tap the sound label toggle (1B) to see the sound labels (1C). 694 Users can also request a textual description of the auditory environment (1D). In Action Mode (Interface 2), the system 695 displays task-related sounds (2A and 2B). Users can pin certain sounds (2A) to monitor them continuously, prompting 696 the interface to reflect their absence and presence. Social Mode (Interface 3) displays the sound level as a pulse-like 697 circular indicator (sound bubble) (3A), along with the speech caption (3B) and speaker name (3C). SoundWeaver will 698 push name-calling alerts (4A) and emergency sound alerts regardless of the current mode. 699 

7 DISCUSSION 700 

Here, we summarize and contextualize key findings in prior research, discuss further implications of our work, and state 701 

study limitations. 702 

7.1 Intent-Driven Design of AI Sound Awareness Systems 703 

Our design artifact, SoundWeaver, demonstrated how AI sound awareness systems can provide different information-704 

presenting interfaces for individual-specific intents (as specified in DG1). The ability to modulate AI system behaviors 705 

based on Declan’s intents encouraged his active and meaningful interactions with AI rather than imposing a predefined 706 

framework for the relevance of auditory information. For example, when we initiated a conversation, Declan’s 707 

information priority shifted from environmental awareness to social interactions. Then, he switched from Awareness to 708 

Social Mode to match this new intent. This approach differs from previous non-personalized systems, where the AI 709 

outputs dictated the information received by DHH users (e.g., [24]) and were agnostic to users’ real-time information 710 

needs. We note that the three modes in the current prototype are tailored to Declan’s individual experiences. Future 711 

work should engage with the wider DHH community to discover more intents requiring different ways of “weaving” 712 

sound information.  713 

In comparison with prior sound awareness systems that have explored end-user customization [8, 32, 33], we argue 714 

that the key difference between this approach and ours lies in the abstraction of AI system behaviors. For example, 715 

ProtoSound [33] provides an interface that enables sound recognition systems to better recognize sounds in users’ 716 

unique personal contexts (e.g., chimes from a DHH user’s microwave). SoundWeaver’s interface, on the other hand, 717 

abstracts away the complexity of customization and maps AI behaviors to Declan’s self-knowledge of tasks to be 718 

accomplished (e.g., to help me with [an intent], AI should do [behavior]). We do not argue for the superiority of either 719 

approach; instead, we encourage future work to envision an accessibility tool with the best of both worlds: how can AI 720 

systems be designed to not only align with user intents but also offer effective mechanisms for users to intervene, correct, 721 

or refine the system’s behaviors? 722 

As human-AI alignment gains traction in HCI research [5, 7, 43, 56], we hope our work inspires new conversations 723 

about developing AI-based accessibility tools that adapt to users’ personal contexts and goals, particularly since AI 724 

systems have traditionally prioritized the majority [57]. However, designing intent-driven systems can be challenging 725 

because intents are “implicit feedback” [57] that can be difficult to observe; as a workaround, our system requires Declan 726 

to remain constantly aware of his real-time intents and assess whether the system aligns with it. The need for manual 727 

mode switching adds another layer of interaction, increasing the cognitive demand. We encourage future work to 728 

examine designs that better capture the implicit feedback and align with user intents without requiring constant 729 

interactions. 730 

Another important consideration throughout the co-design process is the visual design of sound feedback. 731 

Specifically, we asked: What kind of information is necessary and, more importantly, relevant to the Declan’s intents? 732 

How should this information be presented to Declan? These considerations become more important in head-mounted 733 

display (HMD)-based interfaces, as poorly designed visuals can easily lead to distraction, fatigue, and discomfort. 734 

Morrison et al. proposed information density [45] as a key factor in effectively supporting the social sensemaking of a 735 

blind child with HMD-based AI systems, as overly dense information can overwhelm blind and low-vision (BLV) users. 736 

In our case, designing low-density interfaces helped minimize visual distractions and prevent “meltdowns” caused by 737 

information overload for Declan. Additionally, we observed design variability, a term we defined to describe how 738 

SoundWeaver’s sound indicator designs (e.g., waveforms for ambient sound level and arrows indicating active speakers) 739 

respond to unpredictable changes in the acoustic environment. During the field evaluation at the game store, we noticed 740 

that the waveforms indicating ambient sound levels fluctuated drastically – an example of high design variability – 741 

which distracted Declan from focusing on the conversation. To address this, we replaced the waveform visualizer in 742 

Social Mode with a more subtle bubble-shaped visualizer in the peripheral view (see Figure 6-3). Declan also reflected 743 

that in smaller and more intimate settings (e.g., four friends sitting around a table) or situations where speakers 744 

frequently change, he would prefer seeing the speaker’s names in captions instead of directional indicators, as name 745 

changes would be less visually distracting than moving arrows. 746 

7.2 Addressing the Invasiveness of Sound Awareness Technologies 747 

A persistent theme throughout the co-design process was whether the design was “invasive.” Here, we interpret 748 

invasiveness in two critical aspects: 749 

1. Can our design interfere with the current social dynamics in Declan’s circle? 750 

2. Will our design disrupt Declan’s existing sensemaking processes? 751 

Regarding social dynamics, we were concerned that Declan’s usage of the SoundWeaver, which ran on the Apple 752 

Vision Pro headset, would make him self-conscious due to its intrusive form factor, as suggested by prior work [58, 59]. 753 

However, we were pleased to find that Declan felt comfortable using the system around his friends at the game store 754 

and that the friend group supported his system usage (e.g., passing along the microphones to increase the automatic 755 

caption’s accuracy). Declan’s experience aligns with prior findings that DHH people generally feel more comfortable 756 

using sound awareness technologies around closer social circles (e.g., family members) [15, 24]. Moreover, the friend 757 

group’s supportive actions demonstrated how introducing novel assistive technologies can foster new social norms 758 

rooted in interdependence [4]. 759 

Beyond social acceptability, we carefully considered how SoundWeaver could disrupt Declan’s intricate, sometimes 760 

intimate, social fabric based on his hearing loss and Deaf identity. For example, when designing interfaces for the context 761 

of “attending church service,” we pondered whether introducing SoundWeaver would disrupt Declan's personal bond 762 

with Anita, the pianist who accommodates him by signaling the start and end of her music pieces through hand gestures. 763 

Another example of this dilemma arose in our discussion about the name-calling alert. We connected this feature to 764 

Declan wearing a graphic T-shirt that tells other people about his Deafness. While facilitating the recognition of name-765 

calling can be beneficial in social events, this technology may diminish the need for Declan’s existing workarounds, 766 

which are often far more expressive, creative, and social. These concerns, along with careful discussions with Declan, 767 

shaped our decision to only visualize ambient loudness peripherally in Social Mode, deferring most critical sound 768 

awareness tasks to Declan’s trusted companions in the game store. Motivated by these concerns about SoundWeaver’s 769 

impacts on social dynamics, we encourage future researchers to consider two factors when designing AI-based 770 

accessibility tools. First, when the AI works as expected, does its adoption come at the cost of access intimacy [67, 68]? 771 

Second, in the spirit of Amershi et al. [1], who argue that AI systems should “gracefully degrade their services when 772 

encountering errors,” can we design AI systems that, when encountering unexpected results, leverage a broader, 773 

interdependent support system to help users achieve their goals? 774 

The second aspect of invasiveness emerged from the design artifact’s negotiations with Declan’s existing 775 

sensemaking models. Initially, we envisioned SoundWeaver as a “cognitive extender,” [20] anticipating that this AI 776 

application could be tightly integrated and internalized into Declan’s sensemaking process. However, our co-design 777 

sessions revealed a more nuanced perspective. While Declan appreciated the complementary knowledge SoundWeaver 778 

provided (e.g., using captions for filling lipreading gaps), he firmly resisted the idea that the tool should be internalized 779 

or fundamentally alter his way of perceiving the world. This insight prompted us to shift our design approach from 780 

cognitive extensions to augmenting Declan’s sensemaking abilities. The key difference lies in the potential risk when 781 

the system fails or becomes unavailable: the breakdown of extenders can result in a sum loss of the user’s ability [20]. 782 

Our design strategy thus evolved from assumptions about “what is helpful” to a more considered approach that 783 

prioritizes the alignment with Declan’s trusted sensemaking strategies, aligning with DG2. This shift was particularly 784 

evident in the iterative developments of Action Mode, where we offered Declan more agency to selectively monitor 785 

sound events. 786 

Besides the above two aspects, we note that current HMD devices may also be invasive due to their form factors. For 787 

example, our study used Apple Vision Pro, a headset similar in size to ski goggles and weighing about 650 grams. During 788 

the field evaluation, Declan chose to take off the Vision Pro device after two hours of continuous use due to fatigue. 789 

7.3 Reflecting on the Co-Design Process 790 

To our knowledge, this work is the first study that synergizes user experience prototyping with the expertise of a DHH 791 

individual, leveraging their deep understanding of DHH culture, personal contexts, and sound information needs within 792 

a longitudinal co-design process. Here, we present three critical reflections on this process.  793 

First, viewing Declan as an equal contributor to the design artifact allowed us to engage in thoughtful discussions 794 

that led to a system more closely aligned with Declan’s cultural background and sensemaking abilities. During the 795 

formative study, Declan stated that the most important part of sound awareness for him was knowing the presence of 796 

sound. During the analysis, we connected this preference with DeafSpace, which emphasizes how Deaf people rely on 797 

subtle environmental cues to maintain awareness and navigate spaces [48]. This led us to ask, “How can we convey the 798 

presence of sound events through visual cues?” Since Declan identified loudness as a strong indicator of “something 799 

happening,” we initially used color-coded textual indicators (e.g., quiet, ambient, loud) to represent real-time sound levels. 800 

In Phase 2, Declan told us that “pictures are better than words” for him and suggested a waveform-based design to better 801 

convey temporal changes in loudness (e.g., a sudden spike indicating a sound event). 802 

Second, while the above examples demonstrate how an informed user experience prototyping process can help align 803 

AI systems’ behaviors with the user’s sensemaking approaches in accessibility tools, we caution future designers about 804 

the potential discrepancies between how users naturally process information and their interactions with AI. For example, 805 

in our second-iteration prototype, the system prompted Declan to confirm whether he wanted to access sound 806 

classification results whenever a spike in the sound level was detected. The classification results appeared only when 807 

Declan affirmed by tapping the prompt. While this interaction matched Declan’s natural sensemaking process (“Paint a 808 

broad stroke first, then describe details”), during the field evaluation, he found it tedious. Upon realizing that the sound 809 

recognition model was more capable than expected, Declan preferred the manual toggle-based approach employed in 810 

the initial design, which persistently displayed sound event labels but allowed quicker access and dismissal. In this case, 811 

Declan’s increased trust in AI capabilities shifted his priorities from compatibility with his natural sensemaking 812 

approach to a preference for efficiency. We encourage future work to consider this discrepancy, especially in technology 813 

design for marginalized communities, where responsibly balancing cultural norms, values, and usability is crucial. 814 

Third, evaluating the SoundWeaver prototype in Declan’s real-world contexts elicited design insights and challenges 815 

that may be difficult to acquire from lab settings. For example, while our initial design incorporated peripheral arrow 816 

indicators – theoretically supported as effective directional cues [28] – the rapid transitions among active speakers in 817 

group settings created distracting visual effects that impeded Declan’s ability to focus on conversations. 818 

7.4 Limitations and Future Work 819 

While our design goals are deeply informed by the perspectives of one Deaf participant, our hard-of-hearing co-author, 820 

and relevant prior work in DHH culture and accessibility, we do not claim that they are exhaustive or will work as 821 

intended for all DHH people. We present these design goals as starting points for further exploration of intent-driven 822 

systems and eagerly look forward to future work that refines or expands them with feedback from the broader DHH 823 

community. While the SoundWeaver prototype was designed to be generalized beyond our Deaf participant’s use cases, 824 

we recognize that future work needs to evaluate and iterate the prototype through longitudinal studies with diverse 825 

members from the DHH population, further validating its utility and usability and refining its design. Since our work is 826 

primarily qualitative, we did not evaluate the performance of the Audio Flamingo model, which our system used for 827 

generating textual descriptions of the acoustic scene. We encourage future work to assess its performance and explore 828 

how it can involve human-AI interaction to ensure accuracy across diverse contexts.  829 

While acknowledging these limitations, we note that Research through Design with one participant is a powerful 830 

HCI methodology that has been used to elicit rich, situated insights for designing culturally conscious systems that 831 

accommodate diverse needs, particularly in the field of accessibility (e.g., in [27, 45]), where population-wide preferences 832 

vary widely. As Jain et al. [27] argue, such insights are often difficult to obtain through traditional multi-participant 833 

studies. 834 

8 CONCLUSION 835 

Our work presents the co-design process of SoundWeaver, an intent-driven AI sound awareness system prototype that 836 

supports DHH people’s sensemaking of auditory environments, developed in collaboration with a DHH participant. 837 

Reflecting on this design journey, we discuss its implications for the development of future sound awareness systems 838 

and other AI accessibility tools, particularly regarding the alignment of system behaviors with users’ intents and 839 

personal contexts. We also highlight important considerations for designing socially and ethically mindful technologies 840 

to address accessibility challenges. 841 

References 842 

[1] Saleema Amershi, Dan Weld, Mihaela Vorvoreanu, Adam Fourney, Besmira Nushi, Penny Collisson, Jina Suh, Shamsi Iqbal, 843 Paul N. Bennett, Kori Inkpen, Jaime Teevan, Ruth Kikin-Gil, and Eric Horvitz. 2019. Guidelines for Human-AI Interaction. In Proceedings 844 of the 2019 CHI Conference on Human Factors in Computing Systems, May 02, 2019. ACM, Glasgow Scotland Uk, 1–13. 845 https://doi.org/10.1145/3290605.3300233 846 [2] Harshadha Balasubramanian, Cecily Morrison, Martin Grayson, Zhanat Makhataeva, Rita Faia Marques, Thomas Gable, 847 Dalya Perez, and Edward Cutrell. 2023. Enable Blind Users’ Experience in 3D Virtual Environments: The Scene Weaver Prototype. In 848 Extended Abstracts of the 2023 CHI Conference on Human Factors in Computing Systems, April 19, 2023. ACM, Hamburg Germany, 1–4. 849 https://doi.org/10.1145/3544549.3583909 850 [3] Behance. Blog :: The “Brute Force” School of Design: Prototyping over Presentations. Retrieved September 6, 2024 from 851 https://www.behance.net/blog/the-brute-force-school-of-design-prototyping-over-presentations 852 [4] Cynthia L. Bennett, Erin Brady, and Stacy M. Branham. 2018. Interdependence as a Frame for Assistive Technology Research 853 and Design. In Proceedings of the 20th International ACM SIGACCESS Conference on Computers and Accessibility, October 08, 2018. ACM, 854 Galway Ireland, 161–173. https://doi.org/10.1145/3234695.3236348 855 [5] Elfia Bezou-Vrakatseli, Oana Cocarascu, and Sanjay Modgil. 2024. Towards Dialogues for Joint Human-AI Reasoning and 856 Value Alignment. https://doi.org/10.48550/arXiv.2405.18073 857 [6] Melanie Birks and Jane Mills. 2010. Grounded Theory: A Practical Guide. SAGE. 858 [7] Angie Boggust, Benjamin Hoover, Arvind Satyanarayan, and Hendrik Strobelt. 2022. Shared Interest: Measuring Human-AI 859 Alignment to Identify Recurring Patterns in Model Behavior. In Proceedings of the 2022 CHI Conference on Human Factors in Computing 860 Systems (CHI ’22), April 28, 2022. Association for Computing Machinery, New York, NY, USA, 1–17. 861 https://doi.org/10.1145/3491102.3501965 862 [8] Danielle Bragg, Nicholas Huynh, and Richard E. Ladner. 2016. A Personalizable Mobile Sound Detector App Design for Deaf 863 and Hard-of-Hearing Users. In Proceedings of the 18th International ACM SIGACCESS Conference on Computers and Accessibility, October 864 23, 2016. ACM, Reno Nevada USA, 3–13. https://doi.org/10.1145/2982142.2982171 865 

[9] Xinyun Cao and Dhruv Jain. 2024. SoundModVR: Sound Modifications in Virtual Reality to Support People who are Deaf 866 and Hard of Hearing. In Proceedings of the 26th International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS ’24), 867 October 27, 2024. Association for Computing Machinery, New York, NY, USA, 1–15. https://doi.org/10.1145/3663548.3675653 868 [10] Anna Cavender and Richard E. Ladner. 2008. Hearing Impairments. In Web Accessibility: A Foundation for Research, Simon 869 Harper and Yeliz Yesilada (eds.). Springer, London, 25–35. https://doi.org/10.1007/978-1-84800-050-6_3 870 [11] Pratheep Kumar Chelladurai, Ziming Li, Maximilian Weber, Tae Oh, and Roshan L Peiris. 2024. SoundHapticVR: Head-Based 871 Spatial Haptic Feedback for Accessible Sounds in Virtual Reality for Deaf and Hard of Hearing Users. In Proceedings of the 26th 872 International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS ’24), October 27, 2024. Association for Computing 873 Machinery, New York, NY, USA, 1–17. https://doi.org/10.1145/3663548.3675639 874 [12] Seungwon Chung and Jung-Woo Son. 2020. Visual Perception in Autism Spectrum Disorder: A Review of Neuroimaging 875 Studies. Soa Chongsonyon Chongsin Uihak 31, 3 (July 2020), 105–120. https://doi.org/10.5765/jkacap.200018 876 [13] Tom Cole and Marco Gillies. 2022. More than a bit of coding: (un-)Grounded (non-)Theory in HCI. In CHI Conference on 877 Human Factors in Computing Systems Extended Abstracts, April 27, 2022. ACM, New Orleans LA USA, 1–11. 878 https://doi.org/10.1145/3491101.3516392 879 [14] Hang Do, Quan Dang, Jeremy Zhengqi Huang, and Dhruv Jain. 2023. AdaptiveSound: An Interactive Feedback-Loop System 880 to Improve Sound Recognition for Deaf and Hard of Hearing Users. In The 25th International ACM SIGACCESS Conference on Computers 881 and Accessibility, October 22, 2023. ACM, New York NY USA, 1–12. https://doi.org/10.1145/3597638.3608390 882 [15] Leah Findlater, Bonnie Chinh, Dhruv Jain, Jon Froehlich, Raja Kushalnagar, and Angela Carey Lin. 2019. Deaf and Hard-of-883 hearing Individuals’ Preferences for Wearable and Mobile Sound Awareness Technologies. In Proceedings of the 2019 CHI Conference on 884 Human Factors in Computing Systems, May 02, 2019. ACM, Glasgow Scotland Uk, 1–13. https://doi.org/10.1145/3290605.3300276 885 [16] Leah Findlater, Bonnie Chinh, Dhruv Jain, Jon Froehlich, Raja Kushalnagar, and Angela Carey Lin. 2019. Deaf and Hard-of-886 hearing Individuals’ Preferences for Wearable and Mobile Sound Awareness Technologies. In Proceedings of the 2019 CHI Conference on 887 Human Factors in Computing Systems (CHI ’19), May 02, 2019. Association for Computing Machinery, New York, NY, USA, 1–13. 888 https://doi.org/10.1145/3290605.3300276 889 [17] Alex Graves, Abdel-rahman Mohamed, and Geoffrey Hinton. 2013. Speech Recognition with Deep Recurrent Neural 890 Networks. Retrieved July 19, 2024 from http://arxiv.org/abs/1303.5778 891 [18] Ru Guo, Yiru Yang, Johnson Kuang, Xue Bin, Dhruv Jain, Steven Goodman, Leah Findlater, and Jon Froehlich. 2020. 892 HoloSound: Combining Speech and Sound Identification for Deaf or Hard of Hearing Users on a Head-mounted Display. In Proceedings 893 of the 22nd International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS ’20), October 29, 2020. Association for 894 Computing Machinery, New York, NY, USA, 1–4. https://doi.org/10.1145/3373625.3418031 895 [19] Christina N. Harrington, Aashaka Desai, Aaleyah Lewis, Sanika Moharana, Anne Spencer Ross, and Jennifer Mankoff. 2023. 896 Working at the Intersection of Race, Disability and Accessibility. In Proceedings of the 25th International ACM SIGACCESS Conference 897 on Computers and Accessibility (ASSETS ’23), October 22, 2023. Association for Computing Machinery, New York, NY, USA, 1–18. 898 https://doi.org/10.1145/3597638.3608389 899 [20] José Hernández-Orallo and Karina Vold. 2019. AI Extenders: The Ethical and Societal Implications of Humans Cognitively 900 Extended by AI. In Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society, January 27, 2019. ACM, Honolulu HI USA, 901 507–513. https://doi.org/10.1145/3306618.3314238 902 [21] Shawn Hershey, Sourish Chaudhuri, Daniel P. W. Ellis, Jort F. Gemmeke, Aren Jansen, R. Channing Moore, Manoj Plakal, 903 Devin Platt, Rif A. Saurous, Bryan Seybold, Malcolm Slaney, Ron J. Weiss, and Kevin Wilson. 2017. CNN Architectures for Large-Scale 904 Audio Classification. Retrieved July 19, 2024 from http://arxiv.org/abs/1609.09430 905 [22] Jaylin Herskovitz, Andi Xu, Rahaf Alharbi, and Anhong Guo. 2024. ProgramAlly: Creating Custom Visual Access Programs 906 via Multi-Modal End-User Programming. https://doi.org/10.1145/3654777.3676391 907 [23] F Wai-ling Ho-Ching, Jennifer Mankoff, and James A Landay. Can you see what I hear? The Design and Evaluation of a 908 Peripheral Sound Display for the Deaf.  909 

[24] Jeremy Zhengqi Huang, Hriday Chhabria, and Dhruv Jain. 2023. “Not There Yet”: Feasibility and Challenges of Mobile Sound 910 Recognition to Support Deaf and Hard-of-Hearing People. In The 25th International ACM SIGACCESS Conference on Computers and 911 Accessibility, October 22, 2023. ACM, New York NY USA, 1–14. https://doi.org/10.1145/3597638.3608431 912 [25] Jeremy Zhengqi Huang, Reyna Wood, Hriday Chhabria, and Dhruv Jain. 2024. A Human-AI Collaborative Approach for 913 Designing Sound Awareness Systems. In Proceedings of the CHI Conference on Human Factors in Computing Systems, May 11, 2024. 914 ACM, Honolulu HI USA, 1–11. https://doi.org/10.1145/3613904.3642062 915 [26] Dhruv Jain, Audrey Desjardins, Leah Findlater, and Jon E. Froehlich. 2019. Autoethnography of a Hard of Hearing Traveler. 916 In The 21st International ACM SIGACCESS Conference on Computers and Accessibility, October 24, 2019. ACM, Pittsburgh PA USA, 236–917 248. https://doi.org/10.1145/3308561.3353800 918 [27] Dhruv Jain, Audrey Desjardins, Leah Findlater, and Jon E. Froehlich. 2019. Autoethnography of a Hard of Hearing Traveler. 919 In The 21st International ACM SIGACCESS Conference on Computers and Accessibility, October 24, 2019. ACM, Pittsburgh PA USA, 236–920 248. https://doi.org/10.1145/3308561.3353800 921 [28] Dhruv Jain, Leah Findlater, Jamie Gilkeson, Benjamin Holland, Ramani Duraiswami, Dmitry Zotkin, Christian Vogler, and 922 Jon E. Froehlich. 2015. Head-Mounted Display Visualizations to Support Sound Awareness for the Deaf and Hard of Hearing. In 923 Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems (CHI ’15), April 18, 2015. Association for 924 Computing Machinery, New York, NY, USA, 241–250. https://doi.org/10.1145/2702123.2702393 925 [29] Dhruv Jain, Rachel Franz, Leah Findlater, Jackson Cannon, Raja Kushalnagar, and Jon Froehlich. 2018. Towards Accessible 926 Conversations in a Mobile Context for People who are Deaf and Hard of Hearing. In Proceedings of the 20th International ACM 927 SIGACCESS Conference on Computers and Accessibility (ASSETS ’18), October 08, 2018. Association for Computing Machinery, New 928 York, NY, USA, 81–92. https://doi.org/10.1145/3234695.3236362 929 [30] Dhruv Jain, Sasa Junuzovic, Eyal Ofek, Mike Sinclair, John R. Porter, Chris Yoon, Swetha Machanavajhala, and Meredith 930 Ringel Morris. 2021. Towards Sound Accessibility in Virtual Reality. In Proceedings of the 2021 International Conference on Multimodal 931 Interaction (ICMI ’21), October 18, 2021. Association for Computing Machinery, New York, NY, USA, 80–91. 932 https://doi.org/10.1145/3462244.3479946 933 [31] Dhruv Jain, Kelly Mack, Akli Amrous, Matt Wright, Steven Goodman, Leah Findlater, and Jon E. Froehlich. 2020. 934 HomeSound: An Iterative Field Deployment of an In-Home Sound Awareness System for Deaf or Hard of Hearing Users. In Proceedings 935 of the 2020 CHI Conference on Human Factors in Computing Systems, April 21, 2020. ACM, Honolulu HI USA, 1–12. 936 https://doi.org/10.1145/3313831.3376758 937 [32] Dhruv Jain, Hung Ngo, Pratyush Patel, Steven Goodman, Leah Findlater, and Jon Froehlich. 2020. SoundWatch: Exploring 938 Smartwatch-based Deep Learning Approaches to Support Sound Awareness for Deaf and Hard of Hearing Users. In The 22nd 939 International ACM SIGACCESS Conference on Computers and Accessibility, October 26, 2020. ACM, Virtual Event Greece, 1–13. 940 https://doi.org/10.1145/3373625.3416991 941 [33] Dhruv Jain, Khoa Huynh Anh Nguyen, Steven Goodman, Rachel Grossman-Kahn, Hung Ngo, Aditya Kusupati, Ruofei Du, 942 Alex Olwal, Leah Findlater, and Jon E. Froehlich. 2022. ProtoSound: A Personalized and Scalable Sound Recognition System for Deaf 943 and Hard-of-Hearing Users. In CHI Conference on Human Factors in Computing Systems, April 29, 2022. 1–16. 944 https://doi.org/10.1145/3491102.3502020 945 [34] Chloe Kent. 2021. Equipment aesthetics: the companies improving mobility aid design. Medical Device Network. Retrieved 946 September 12, 2024 from https://www.medicaldevice-network.com/features/assistive-device-design/ 947 [35] Zhifeng Kong, Arushi Goel, Rohan Badlani, Wei Ping, Rafael Valle, and Bryan Catanzaro. 2024. Audio Flamingo: A Novel 948 Audio Language Model with Few-Shot Learning and Dialogue Abilities. Retrieved August 13, 2024 from http://arxiv.org/abs/2402.01831 949 [36] R. Shantha Selva Kumari, D. Sugumar, and V. Sadasivam. 2007. Audio Signal Classification Based on Optimal Wavelet and 950 Support Vector Machine. In International Conference on Computational Intelligence and Multimedia Applications (ICCIMA 2007), 951 December 2007. IEEE, Sivakasi, Tamil Nadu, India, 544–548. https://doi.org/10.1109/ICCIMA.2007.370 952 [37] Raja S. Kushalnagar and Christian Vogler. 2020. Teleconference Accessibility and Guidelines for Deaf and Hard of Hearing 953 Users. In Proceedings of the 22nd International ACM SIGACCESS Conference on Computers and Accessibility, October 26, 2020. ACM, 954 Virtual Event Greece, 1–6. https://doi.org/10.1145/3373625.3417299 955 

[38] Yizhar Lavner and Dima Ruinskiy. 2009. A Decision-Tree-Based Algorithm for Speech/Music Classification and 956 Segmentation. EURASIP Journal on Audio, Speech, and Music Processing 2009, (2009), 1–14. https://doi.org/10.1155/2009/239892 957 [39] Ziming Li, Shannon Connell, Wendy Dannels, and Roshan Peiris. 2022. SoundVizVR: Sound Indicators for Accessible Sounds 958 in Virtual Reality for Deaf or Hard-of-Hearing Users. In Proceedings of the 24th International ACM SIGACCESS Conference on Computers 959 and Accessibility (ASSETS ’22), October 22, 2022. Association for Computing Machinery, New York, NY, USA, 1–13. 960 https://doi.org/10.1145/3517428.3544817 961 [40] Ziming Li, Kristen Shinohara, and Roshan L Peiris. 2023. Exploring the Use of the SoundVizVR Plugin with Game Developers 962 in the Development of Sound-Accessible Virtual Reality Games. In Extended Abstracts of the 2023 CHI Conference on Human Factors in 963 Computing Systems (CHI EA ’23), April 19, 2023. Association for Computing Machinery, New York, NY, USA, 1–7. 964 https://doi.org/10.1145/3544549.3585750 965 [41] Scott K. Liddell. 2003. Grammar, Gesture, and Meaning in American Sign Language. Cambridge University Press, Cambridge. 966 https://doi.org/10.1017/CBO9780511615054 967 [42] Tara Matthews, Janette Fong, F. Wai-Ling Ho-Ching, and Jennifer Mankoff. 2006. Evaluating non-speech sound 968 visualizations for the deaf. Behaviour & Information Technology 25, 4 (July 2006), 333–351. https://doi.org/10.1080/01449290600636488 969 [43] Malek Mechergui and Sarath Sreedharan. 2024. Goal Alignment: Re-analyzing Value Alignment Problems Using Human-970 Aware AI. AAAI 38, 9 (March 2024), 10110–10118. https://doi.org/10.1609/aaai.v38i9.28875 971 [44] Mohammadreza Mirzaei, Peter Kán, and Hannes Kaufmann. 2021. Head Up Visualization of Spatial Sound Sources in Virtual 972 Reality for Deaf and Hard-of-Hearing People. In 2021 IEEE Virtual Reality and 3D User Interfaces (VR), March 2021. 582–587. 973 https://doi.org/10.1109/VR50410.2021.00083 974 [45] Cecily Morrison, Edward Cutrell, Martin Grayson, Anja Thieme, Alex Taylor, Geert Roumen, Camilla Longden, Sebastian 975 Tschiatschek, Rita Faia Marques, and Abigail Sellen. 2021. Social Sensemaking with AI: Designing an Open-ended AI Experience with 976 a Blind Child. In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems, May 06, 2021. ACM, Yokohama Japan, 977 1–14. https://doi.org/10.1145/3411764.3445290 978 [46] Michael J Muller and Sandra Kogan. Grounded Theory Method in HCI and CSCW. Grounded Theory. 979 [47] National Research Council (US) Committee on Disability Determination for Individuals with Hearing Impairments. 2004. 980 Hearing Loss: Determining Eligibility for Social Security Benefits. National Academies Press (US), Washington (DC). Retrieved August 11, 981 2024 from http://www.ncbi.nlm.nih.gov/books/NBK207838/ 982 [48] Joan Naturale. InfoGuides: DeafSpace: Principles and Elements of DeafSpace. Retrieved July 5, 2024 from 983 https://infoguides.rit.edu/deafspace/principles 984 [49] Michael Oliver. 1996. Understanding Disability. Macmillan Education UK, London. https://doi.org/10.1007/978-1-349-24269-985 6 986 [50] Carol A. Padden and Tom L. Humphries. 1990. Deaf in America: Voices from a Culture (58896th edition ed.). Harvard 987 University Press. 988 [51] Yi-Hao Peng, Ming-Wei Hsi, Paul Taele, Ting-Yu Lin, Po-En Lai, Leon Hsu, Tzu-chuan Chen, Te-Yen Wu, Yu-An Chen, 989 Hsien-Hui Tang, and Mike Y. Chen. 2018. SpeechBubbles: Enhancing Captioning Experiences for Deaf and Hard-of-Hearing People in 990 Group Conversations. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (CHI ’18), April 21, 2018. 991 Association for Computing Machinery, New York, NY, USA, 1–10. https://doi.org/10.1145/3173574.3173867 992 [52] Karol J. Piczak. 2015. Environmental sound classification with convolutional neural networks. In 2015 IEEE 25th International 993 Workshop on Machine Learning for Signal Processing (MLSP), September 2015. IEEE, Boston, MA, USA, 1–6. 994 https://doi.org/10.1109/MLSP.2015.7324337 995 [53] Wendy Sandler and Diane Lillo-Martin. 2006. Sign Language and Linguistic Universals. Cambridge University Press, 996 Cambridge. https://doi.org/10.1017/CBO9781139163910 997 [54] Aline Darc Piculo dos Santos, Ana Lya Moya Ferrari, Fausto Orsi Medola, and Frode Eika Sandnes. 2022. Aesthetics and the 998 perceived stigma of assistive technology for visual impairment. Disability and Rehabilitation: Assistive Technology 17, 2 (February 2022), 999 152–158. https://doi.org/10.1080/17483107.2020.1768308 1000 

[55] Daniel Schiff, Bogdana Rakova, Aladdin Ayesh, Anat Fanti, and Michael Lennon. 2020. Principles to Practices for Responsible 1001 AI: Closing the Gap. Retrieved September 6, 2024 from http://arxiv.org/abs/2006.04707 1002 [56] Hua Shen, Tiffany Knearem, Reshmi Ghosh, Kenan Alkiek, Kundan Krishna, Yachuan Liu, Ziqiao Ma, Savvas Petridis, Yi-1003 Hao Peng, Li Qiwei, Sushrita Rakshit, Chenglei Si, Yutong Xie, Jeffrey P Bigham, Frank Bentley, Joyce Chai, Zachary Lipton, Qiaozhu 1004 Mei, Rada Mihalcea, Michael Terry, Diyi Yang, Meredith Ringel Morris, Paul Resnick, and David Jurgens. 2024. Towards Bidirectional 1005 Human-AI Alignment: A Systematic Review for Clarifications, Framework, and Future Directions. (2024). 1006 [57] Hua Shen, Tiffany Knearem, Reshmi Ghosh, Kenan Alkiek, Kundan Krishna, Yachuan Liu, Ziqiao Ma, Savvas Petridis, Yi-1007 Hao Peng, Li Qiwei, Sushrita Rakshit, Chenglei Si, Yutong Xie, Jeffrey P. Bigham, Frank Bentley, Joyce Chai, Zachary Lipton, Qiaozhu 1008 Mei, Rada Mihalcea, Michael Terry, Diyi Yang, Meredith Ringel Morris, Paul Resnick, and David Jurgens. 2024. Towards Bidirectional 1009 Human-AI Alignment: A Systematic Review for Clarifications, Framework, and Future Directions. 1010 https://doi.org/10.48550/arXiv.2406.09264 1011 [58] Kristen Shinohara and Jacob O. Wobbrock. 2011. In the shadow of misperception: assistive technology use and social 1012 interactions. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’11), May 07, 2011. Association for 1013 Computing Machinery, New York, NY, USA, 705–714. https://doi.org/10.1145/1978942.1979044 1014 [59] Kristen Shinohara and Jacob O. Wobbrock. 2016. Self-Conscious or Self-Confident? A Diary Study Conceptualizing the Social 1015 Accessibility of Assistive Technology. ACM Trans. Access. Comput. 8, 2 (January 2016), 5:1-5:31. https://doi.org/10.1145/2827857 1016 [60] Liu Sicong, Zhou Zimu, Du Junzhao, Shangguan Longfei, Jun Han, and Xin Wang. 2017. UbiEar: Bringing Location-1017 independent Sound Awareness to the Hard-of-hearing People with Smartphones. Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. 1018 1, 2 (June 2017), 1–21. https://doi.org/10.1145/3090082 1019 [61] Hariharan Subramonyam, Colleen Seifert, and Eytan Adar. 2021. ProtoAI: Model-Informed Prototyping for AI-Powered 1020 Interfaces. In 26th International Conference on Intelligent User Interfaces, April 14, 2021. ACM, College Station TX USA, 48–58. 1021 https://doi.org/10.1145/3397481.3450640 1022 [62] Anja Thieme, Cynthia L. Bennett, Cecily Morrison, Edward Cutrell, and Alex S. Taylor. 2018. “I can do everything but see!”  1023 -- How People with Vision Impairments Negotiate their Abilities in Social Contexts. In Proceedings of the 2018 CHI Conference on Human 1024 Factors in Computing Systems (CHI ’18), April 21, 2018. Association for Computing Machinery, New York, NY, USA, 1–14. 1025 https://doi.org/10.1145/3173574.3173777 1026 [63] M Tomitsch and T Grechenig. DESIGN IMPLICATIONS FOR A UBIQUITOUS AMBIENT SOUND DISPLAY FOR THE DEAF.  1027 [64] Qian Yang, Aaron Steinfeld, Carolyn Rosé, and John Zimmerman. 2020. Re-examining Whether, Why, and How Human-AI 1028 Interaction Is Uniquely Difficult to Design. In Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, April 21, 1029 2020. ACM, Honolulu HI USA, 1–13. https://doi.org/10.1145/3313831.3376301 1030 [65] A. M. Young. 1999. Hearing parents’ adjustment to a deaf child-the impact of a cultural-linguistic model of deafness. Journal 1031 of Social Work Practice 13, 2 (November 1999), 157–176. https://doi.org/10.1080/026505399103386 1032 [66] John Zimmerman, Jodi Forlizzi, and Shelley Evenson. 2007. Research through design as a method for interaction design 1033 research in HCI. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, April 29, 2007. ACM, San Jose 1034 California USA, 493–502. https://doi.org/10.1145/1240624.1240704 1035 [67] 2011. Access Intimacy: The Missing Link. Leaving Evidence. Retrieved July 8, 2024 from 1036 https://leavingevidence.wordpress.com/2011/05/05/access-intimacy-the-missing-link/ 1037 [68] 2017. Access Intimacy, Interdependence and Disability Justice. Leaving Evidence. Retrieved September 7, 2024 from 1038 https://leavingevidence.wordpress.com/2017/04/12/access-intimacy-interdependence-and-disability-justice/ 1039 [69] Live Transcribe | Speech to Text App. Android. Retrieved September 12, 2024 from 1040 https://www.android.com/accessibility/live-transcribe/ 1041 [70] Get live captions of spoken audio on iPhone. Apple Support. Retrieved July 19, 2024 from 1042 https://support.apple.com/guide/iphone/get-live-captions-of-spoken-audio-iphe0990f7bb/ios 1043 [71] Google | yamnet | Kaggle. Retrieved August 1, 2024 from https://www.kaggle.com/models/google/yamnet 1044 [72] MLSoundClassifier. Apple Developer Documentation. Retrieved August 1, 2024 from 1045 https://developer.apple.com/documentation/createml/mlsoundclassifier 1046 

[73] Introducing Whisper. Retrieved July 19, 2024 from https://openai.com/index/whisper/ 1047 [74] Speech-to-Text AI: speech recognition and transcription. Google Cloud. Retrieved July 19, 2024 from 1048 https://cloud.google.com/speech-to-text 1049 [75] People + AI Guidebook. Retrieved July 19, 2024 from https://pair.withgoogle.com/guidebook 1050 [76] Medical and Social Models of Disability | Office of Developmental Primary Care. Retrieved August 11, 2024 from 1051 https://odpc.ucsf.edu/clinical/patient-centered-care/medical-and-social-models-of-disability 1052 [77] Linguistics of American Sign Language, 5th Ed. Retrieved August 11, 2024 from 1053 https://gupress.gallaudet.edu/Books/L/Linguistics-of-American-Sign-Language-5th-Ed 1054 [78] DeafSpace - Campus Design and Planning. Gallaudet University. Retrieved August 12, 2024 from 1055 https://gallaudet.edu/campus-design-facilities/campus-design-and-planning/deafspace/ 1056 [79] Captioning Key. Retrieved August 13, 2024 from https://dcmp.org/learn/captioningkey#3 1057 [80] Firebase | Google’s Mobile and Web App Development Platform. Firebase. Retrieved September 8, 2024 from 1058 https://firebase.google.com/ 1059 [81] Speech. Apple Developer Documentation. Retrieved September 8, 2024 from 1060 https://developer.apple.com/documentation/speech/ 1061 [82] Cloud Computing, Hosting Services, and APIs. Google Cloud. Retrieved September 12, 2024 from 1062 https://cloud.google.com/gcp 1063 [83] Colonized by Design - Industrial Designers Society of America. Retrieved September 8, 2024 from 1064 https://www.idsa.org/innovation_article/colonized-design/ 1065  1066 