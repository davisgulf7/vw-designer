# XR Accessibility User Requirements - W3C

# XR Accessibility User Requirements

##  W3C Working Group Note  25 August 2021  

This version:  [https://www.w3.org/TR/2021/NOTE-xaur-20210825/](https://www.w3.org/TR/2021/NOTE-xaur-20210825/)Latest published version:  [https://www.w3.org/TR/xaur/](https://www.w3.org/TR/xaur/)Latest editor's draft:[https://w3c.github.io/apa/xaur/](https://w3c.github.io/apa/xaur/)Previous version:[https://www.w3.org/TR/2020/WD-xaur-20200916/ ](https://www.w3.org/TR/2020/WD-xaur-20200916/)Editors:  [Joshue O'Connor](mailto:joconnor@w3.org) ( W3C ) [Janina Sajka](http://rednote.net/)[Jason White](http://rednote.net/) ( Educational Testing Service ) [Scott Hollier](http://www.hollier.info/)[Michael Cooper](http://www.hollier.info/) ( W3C )  Participate:  [GitHub w3c/apa](https://github.com/w3c/apa/)[File an issue](https://github.com/w3c/apa/)[Commit history](https://github.com/w3c/apa/)[Pull requests](https://github.com/w3c/apa/)[Copyright](https://github.com/w3c/apa/) © 2020-2021 [W3C](https://www.w3.org/)® ([MIT](https://www.csail.mit.edu/), [ERCIM](https://www.ercim.eu/), [Keio](https://www.keio.ac.jp/), [Beihang](https://ev.buaa.edu.cn/)). W3C [liability](https://www.w3.org/Consortium/Legal/ipr-notice#Legal_Disclaimer), [trademark](https://www.w3.org/Consortium/Legal/ipr-notice#W3C_Trademarks) and [permissive document license](https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document) rules apply. 

## Abstract

This document lists user needs and requirements for people with disabilities when using virtual reality or immersive environments, augmented or mixed reality and other related technologies ( XR ). It first introduces a definition of  XR  as used throughout the document, then briefly outlines some uses of  XR . It outlines the complexity of understanding  XR , introduces some technical accessibility challenges such as the need for multi-modal support, synchronization of input and output devices and customization. It then outlines accessibility related user needs for  XR  and suggests subsequent requirements. This is followed by related work that may be helpful understanding the complex technical architecture and processes behind how  XR  environments are built and what may form the basis of a robust accessibility architecture.

This document is most explicitly not a collection of baseline requirements. It is also important to note that some of the requirements may be implemented at a system or platform level, and some may be authoring requirements.

## Status of This Document

This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current  W3C  publications and the latest revision of this technical report can be found in the [W3C  technical reports index](https://www.w3.org/TR/) at https://www.w3.org/TR/.

To comment on this draft [file an issue in the  W3C  APA GitHub repository](https://github.com/w3c/apa/issues/new). If this is not feasible, send email to [public-apa@w3.org](mailto:public-apa@w3.org) ([archives](https://lists.w3.org/Archives/Public/public-apa/)). In-progress updates to the document may be viewed in the [publicly visible editors' draft](https://w3c.github.io/apa/xaur/).

 This document was published by the [Accessible Platform Architectures Working Group](https://www.w3.org/WAI/APA/) as a Working Group Note. 

[GitHub Issues](https://www.w3.org/WAI/APA/) are preferred for discussion of this specification. 

 Publication as a Working Group Note does not imply endorsement by the  W3C  Membership. 

This is a draft document and may be updated, replaced or obsoleted by other documents at any time. It is inappropriate to cite this document as other than work in progress. 

 This document was produced by a group operating under the [W3C  Patent Policy](https://www.w3.org/Consortium/Patent-Policy/). The group does not expect this document to become a  W3C  Recommendation. 

 This document is governed by the [15 September 2020  W3C  Process Document](https://www.w3.org/2020/Process-20200915/). 

## 1.  Introduction

XR  is an acronym used to refer to the spectrum of hardware, applications, and techniques used for virtual reality or immersive environments, augmented or mixed reality and other related technologies. This document is developed as part of a discovery into accessibility related user needs and requirements for  XR . This document does not represent a formal working group position, nor does it currently represent a set of technical requirements that a developer or designer need strictly follow. It aims to outline the diversity of some current accessibility related user needs in  XR  and what potential requirements to meet those needs may be.

### 1.1  What does the term ' XR ' mean?

As with the [WebXR API spec](https://immersive-web.github.io/webxr/) and as indicated in the related [WebXR explainer](https://github.com/immersive-web/webxr/blob/master/explainer.md#what-is-webxr), this document uses the acronym  XR  to refer to the spectrum of hardware, applications, and techniques used for virtual reality or immersive environments, augmented or mixed reality and other related technologies. Examples include, but are not limited to:

Immersive or augmented environments used for education, gaming, multimedia, 360° content and other applications.

Head mounted displays, whether they are opaque, transparent, or utilise video passthrough.

Mobile devices with positional tracking.

Fixed displays with head tracking capabilities.

The important commonality between them being that they all offer some degree of spatial tracking with which to simulate a view of virtual content as well as navigation and interaction with the objects within these environments.

Terms like " XR  Device", " XR  Application", etc. are generally understood to apply to any of the above. Portions of this document that only apply to a subset of these devices will be indicated as appropriate.

### 1.2  Definitions of virtual reality and immersive environments

Virtual reality and immersive environment definitions vary but converge on the notion of immersive computer-mediated experiences. They involve interaction with objects, people and environments using a range of controls. These experiences are often multi-sensory and may be used for educational, therapeutic or entertainment purposes.

### 1.3  Definitions of augmented and mixed reality

Augmented and mixed reality definitions vary but converge on the notion of computer-mediated interactions involving overlays on the real world. These may be informational, or interactive depending on the application.

## 2.  What is  XR  used for?

XR  has a range of purposes from work, education, gaming, multimedia and communication. It is evolving at a fast rate and while not yet mainstream, this will change as computing power increases, hardware becomes cheaper and the quality of the user experience improves.  XR  will be more commonly used for the performance of work tasks, for therapeutic uses, education and for entertainment.

## 3.  Understanding  XR  and Accessibility Challenges

Understanding  XR  itself presents various challenges that are technical. They include issues with a range of hardware, software and authoring tools. To make accessible  XR  experiences there is a need to understand interaction design principles, accessibility semantics and assistive technologies. However, these all represent 'basic' complexities that are in themselves substantial. To add to this, for many designers and authors they may neither know nor have access to people with disabilities for usability testing. Neither may they have a practical way of understanding accessibility related user needs that they can build a solid set of requirements from. In short, they just may not understand what user needs they are trying to meet.

Some of the issues in  XR , for example in gaming, for people with disabilities include:

**Over emphasis on motion controls**. There are many motion controllers that emphasise using your body to control the experience. Some games with  XR  components may lock out traditional control methods when a VR headset is being used, and the user should always be able to use a range of input mechanisms.  Note 3DOF  and  6DOF  may have their own specific mobility issues, for example  3DOF  may have implications for people who have motor impairments that affect the use of one or both arms.  6DOF  may have implications for people who are quadriplegic and for people that use a wheelchair or mobility aid for navigation where there is a need to move directionally in physical space or a higher emphasis on the lower extremity for movement.  

**VR Headsets need the user to be a physical position to play**. The user should not have to be in a particular physical position such as standing or sitting to play a game or perform some action. Or there should be ability to remap these 'physical positions' to other controls (such as using [WalkinVRDriver](https://www.walkinvrdriver.com)).

**Games and hardware being locked to certain manufacturers**. Consoles should allow full button remapping on standard game controllers - to different types of assistive technologies such as switches. These remapping preferences should be mobile, and transportable across a range of hardware devices and software.

**Gamification of VR forces game dynamics on the user**. Some users may wish to just explore an immersive environment without the 'game'.

**Audio design lacks spatial accuracy**. Sound design needs particular attention and can be critical for a good user experience for people with disabilities. The auditory experience of a game or other immersive environment may 'be' the experience [[able-gamers](https://www.w3.org#bib-able-gamers)].

There are a range of disabilities that will need to be considered in making  XR  accessible. It is beyond the scope of this document to describe them all in detail. General categories or types of disabilities are:

Auditory disabilities

Cognitive disabilities

Neurological disabilities

Physical disabilities

Speech disabilities

Visual disabilities

A person may have one of these disabilities or a combination of several. User needs are presented here that may relate to several of these disabilities with a range of requirements that should be met by the author or the platform. For  XR  designers and authors understanding these needs is crucial when making  XR  environments accessible.

Some things designers and authors need to be aware of:

Understanding specific diverse user needs and how they relate to  XR .

Successfully identifying modality needs that are not obvious - but still need to be supported.

Suitable authoring tools that support accessibility requirements in  XR .

Using languages, platforms and engines that support accessibility semantics.

Providing accessible alternatives for content and interaction.

The provision of specific commands within the VR environment (e.g., to go directly to a specified location or to follow another user) which assist with navigation to support different modalities.

The use of virtual assistive technologies (e.g., white cane via a haptic device) to provide non-visual feedback. The research identified that if the same audio cues associated with a real-world infrared white cane were used in immersive environment, users were able to effectively centre themselves in the middle of pathways and walk successfully through virtual doorways based on the same audio feedback as used in the equivalent real-world device [[maidenbaum-amendi](https://www.w3.org#bib-maidenbaum-amendi)]

### 3.1  Immersive Environment challenges

Some of the challenges within immersive environments (and gaming) accessibility include the use of extremely complex input devices, control schemes that require a high degree of precision, timing and simultaneous action; ability to distinguish subtle differences in busy visual and audio information, having to juggle multiple complex goals and objectives [[web-adapt](https://www.w3.org#bib-web-adapt)].

There are also currently very useful accessibility guidelines available that are specific to gaming [[game-a11y](https://www.w3.org#bib-game-a11y)].

### 3.2  XR  and supporting multimodality

Modality relates to modes of sense perception such as sight, hearing, touch and so on. Accessibility can be thought of as supporting multi-modal requirements and the transformation of content or aspects of a user interface from one mode to another that will support various user needs.

Considering various modality requirements in the foundation of  XR  means these platforms will be better able to support accessibility related user needs. There will be many modality aspects for the developer and/or content author to consider.

XR  authors and content designers will also need access to tools that support the multi-modal requirements listed below. 

The following inputs and outputs can be considered modalities that should be supported in  XR  environments.

### 3.3  Various input modalities 

The following are example of some of the diverse input methods used by people with disabilities. In many real-world applications these input methods may be combined.

**Speech** - this is where a user's voice is the main input. Using a range of speech commands, a user should be able to navigate in an  XR  environment, interact with the objects in that environment using their voice alone.

**Keyboard ** - this is where the keyboard alone is the user's main input. A user should be able to navigate in an  XR  environment, interact with the objects in that environment using the keyboard alone.

**Switch ** this is where a since button Switch alone is the user's main input. A user should be able to navigate in an  XR  environment, interact with the objects in that environment using a Switch alone. This switch may be used in conjunction with an assistive technology scanning application within the  XR  environment that allows them to select directions for navigation, macros for communication and interaction.

**Gesture ** - this is where gesture-based controllers are the main input and can be used to navigate in an  XR  environment, interact with the objects in that environment make selections using their voice alone.

**Eye Tracking** - this is where eye tracking applications is the main input. Using a range of commands, a user should be able to navigate in an  XR  environment, interact with the objects in that environment using these eye tracking applications.

### 3.4  Various output modalities 

The following are a list of outputs that can be available to a user to help them understand, interact with and 'sense' feedback from an  XR  application. Some of these are in common use on the Web and other exploratory (such as Olfactory and Gustatory.)

Tactile - this is using the sense of touch, or commonly referred to as haptics.

Visual - this is using the sense of sight, such as 2D and 3D graphics.

Auditory - this is using the sense of sound, such as rich spatial audio, surround sound.

Olfactory - this is the sense of smell.

Gustatory - this is the sense of taste.

### 3.5  XR  controller challenges

As mentioned, there are a range of input devices that may be used. Supporting these controllers requires an understanding of what they are and how they work. There are a variety of alternative gaming controls that may be very useful in  XR  environments and applications. For example, the [Xbox Adaptive Controller](https://www.xbox.com/en-US/xbox-one/accessories/controllers/xbox-adaptive-controller).

While  XR  is the experience, the controller plays a critical part in overcoming some complexity as well as mediating issues that may relate to other challenges around usability and helping the user understand sensory substitution devices. 

Controllers such as the Xbox Adaptive Controller and other switch type inputs allow the user to remap keyboard inputs to control or interact with virtual environments. These powerful customizations allow the user to "do that thing that is difficult" for them with ease. In conjunction with this controller, for example, users with limited mobility they can also simulate actions in the  XR  environment that they would not be able to physically perform. [WalkinVRDriver](https://www.walkinvrdriver.com) is a good example of this where motion range, position and orientation can be set to the user's ability.

### 3.6  Customization of control inputs

Give the user the ability to modify their input preference or use a variety of input devices. The remapping of keys used to control movement or interaction in virtual environments is not currently required by WCAG. It is nevertheless noted in the literature as desirable.

### 3.7   Using multiple diverse inputs simultaneously 

A user with a disability may have several input devices or different assistive technologies. A user may switch 'mode' of interaction, or the tools used without degrading the user experience where they lose focus on a task and cannot return to it, or make unwanted input.

Complexity needs to be managed and co-ordinated between different kinds of assistive technology in immersive environments. There is a platform level requirement to support multiple assistive technologies in a cohesive manner. This would allow combinations to be used in a co-ordinated way e.g. where the users day-to-day AT, can be used with other AT that may be embedded in the environment already for example.

Note

The REQ 5b: Voice activation also indicates potential issues with pairing multiple devices via Bluetooth.

### 3.8  Consistent tracking with multiple inputs 

There may be tracking issues when switching input devices. A tracking issue is where the user may lose their focus or it can be modified in unpredictable or unwanted ways, this can cause loss of focus and potentially push the user to make unwanted inputs or choices.

Outputs sent to multiple devices will need to be synchronised.

### 3.9  Usability and affordances in  XR

An  XR  application should have a high level of usability for someone with a disability using assistive technology. Therefore, communicating affordances successfully is critical and needs to be done in a way that supports multiple modalities. Some related questions are:

How can affordances be successfully translated from one modality to another?

Can affordances be mediated or transformed, as needed by the users own modality preferences?

Should affordances change depending on context of use? What interactions are allowed or not allowed? 

How can we ensure what happens in one modality, is reflected in another? So various modalities are not out of sync e.g. synchronization of captions between real time text transcriptions and other alternatives such as symbols or AAC?

Note

Regarding the discoverability of accessibility features in  XR . It is important for designers of accessible  XR  to understand how to categorize various accessibility features and understand where to place them, in a menu for example. An accessibility related accommodation may have multiple contexts of use that may not be obvious. For example, the suggested use of "mono" in User Need 19 is not just an accessibility feature under a hearing-impaired category, as it is also useful for users with spatial orientation impairments or cognitive and learning disabilities. Care should be taken to ensure these features are categorized in menus correctly and discoverable in multiple contexts.

## 4.  XR  User Needs and Requirements

This document outlines various accessibility related user needs for  XR . These user needs should drive accessibility requirements for  XR  and its related architecture. These come from people with disabilities who use assistive technologies and wish to see the features described available within  XR  enabled applications.

User needs and requirements are often dependent on context of use. The following outline some accessibility user needs and requirements that may be applicable in immersive environments, augmented reality and 360° applications.

These following are neither exhaustive, nor definitive but are presented to help orientate the reader towards understanding some broad user needs and how to meet them. 

### 4.1  Immersive semantics and customization

**User Need 1:** A user of assistive technology wants to navigate, identify locations, objects and interact within an immersive environment.

**REQ 1a:** Navigation mechanisms must be intuitive with robust affordances. Navigation, location and object descriptions must be accurate and identified in a way that is understood by assistive technology. 

**REQ 1b:** Controls need to support alternative mapping, rearranging of position, resizing and sensitivity adjustment.

**REQ 1c:** Objects that are important within any given context of time and place can be identified in a suitable modality.

**REQ 1d:** Allow the user to filter or sort objects and content.

**REQ 1e:** Allow the user to query objects and content for more details.

Note

In an spatialized augmented reality environment a blind user may find a combination of text to speech and sonic symbols helpful. By using a combination of text to speech and sonic symbolism a blind user can do a self-guided tour of a given area using their smartphone. [[spatialized-navigation](https://www.w3.org#bib-spatialized-navigation)]

### 4.2  Motion agnostic interactions

**User Need 2:** A person with a physical disability may want to interact with items in an immersive environment in a way that doesn't require particular bodily movement to perform any given action.

**REQ 2a:** Allow the user performing an action in the environment, in a device independent way, without having to do so physically.

**REQ 2b:** Ensure that all areas of the user interface can be accessed using the same input method.

**REQ 2c:** Allow multiple input methods to be used at the same time.

Note

There are accessibility issues specific to augmented reality. For example, the user may be expected to scan the environment, or scan physical objects, to determine the placement of virtual objects. The user may need to mark a location or an area in space so that the AR application can generate appropriate virtual objects. The user should be able to perform these actions in a motion agnostic way.

### 4.3  Immersive personalization

**User Need 3:** Users with cognitive and learning disabilities may need to personalize the immersive experience in various ways.

**REQ 3a:** Support Symbol sets so they can be used to communicate and layered over objects and items to convey affordances or other needed information in way that can be understood according to user preference.

**REQ 3b:** Allow the user to turn off or 'mute' non-critical environmental content such as animations, visual or audio content, or non-critical messaging.

Note  

Personalization involves tailoring aspects of the user experience to meet the needs and preferences of the individual user.  W3C  are working on various modules for web content that aim to support personalization and are exploring areas such as:

Expanding the accessibility information that may be supplied by the author. [[personalization-semantics](https://www.w3.org#bib-personalization-semantics)]

Facilitating preference driven individual personalization. [[personalization-content](https://www.w3.org#bib-personalization-content)] 

Enabling the author to specify key semantics needed to support users with cognitive impairments. [[personalization-requirements](https://www.w3.org#bib-personalization-requirements)]

### 4.4  Interaction and target customization

**User Need 4:** A user with limited mobility, or users with tunnel or peripheral vision may need a larger 'Target size' for a button or other controls.

**REQ 4a:** Ensure fine motion control is not needed to activate an input.

**REQ 4b:** Ensure hit targets are large enough with suitable spacing around them.

**REQ 4c:** Ensure multiple actions or gestures are not required at the same time to perform any action.

**REQ 4d:** Support 'Sticky Keys' requirements such as serialization for various inputs when the user needs to press multiple buttons.

Note

Users with cognitive and learning disabilities need to understand what items in a visual display are actionable targets and how to interact with them. There is a need for accessibility API's that map custom user interface actions to control types. These actions can then be understood by a broad range of assistive technologies. This would help indicate to users what targets are actionable, and how they can interact with them. By supporting this kind of adaptation and personalization the user can select preferred, familiar options from a set of alternatives. The  W3C  have produced a useful list of these patterns that could help readers understand the user needs of people with cognitive and learning disabilities, as well as in the development of suitable APIs. [[coga-usable](https://www.w3.org#bib-coga-usable)], especially [section 4, the Design Guide](https://www.w3.org/TR/coga-usable/#design_for_everyone).

### 4.5  Voice commands

**User Need 5:** A user with limited mobility may want to be able to use Voice Commands within the immersive environment, to navigate, interact and communicate with others.

**REQ 5a:** Ensure Navigation and interaction can be controlled by Voice Activation.

**REQ 5b:** Voice activation should preferably use native screen readers or voice assistants rather than external devices to eliminate the additional step needed to pair devices.

### 4.6  Color changes

**User Need 6:** Color blind users may need to be able to customise the colors used in the immersive environment. This will help with understanding affordances of various controls or where color is used to signify danger or permission.

**REQ 6a:** Provide customised high contrast skins for the environment to suit luminosity and color contrast requirements.

### 4.7  Magnification context and resetting

**User Need 7:** Screen magnification users may need to be able to check the context of their view in immersive environments.

**REQ 7a:** Allow the screen magnification user to check the context of their view and track/reset focus as needed.

**REQ 7b:** Where it makes sense (such as in menus) interface elements can be enlarged and the menu reflowed to enhance the usability of the interface up to a certain magnification requirement.

Note

There are customisation approaches such as the automatic generation of user interfaces as demonstrated in the SUPPLE project, which adapt to the different challenges the user may face, such as vision, motor control and other user preferences and abilities. A generated UI can make multiple adaptations for different user needs at the same time. This is achieved by generating a UI, or several - after testing a person's ability using an algorithm to learn their preferences. [[supple-project](https://www.w3.org#bib-supple-project)]

### 4.8  Critical messaging and alerts

**User Need 8:** Screen magnification users may need to be made aware of critical messaging and alerts in immersive environments often without losing focus. They may also need to route these messages to a 'second screen' (see **REQ 14** Second Screen).

**REQ 8a:** Ensure that critical messaging, or alerts have priority roles that can be understood and flagged to AT, without moving focus.

### 4.9  Gestural interfaces and interactions

**User Need 9:** A blind user may wish to interact with a gestural interface, such as a virtual menu system.

**REQ 9a:** Support touch screen accessibility gestures (e.g. swipes, flicks and single, double or triple taps with 1, 2 or 3 fingers). See **REQ 14** Second Screen.

**REQ 9b:** Using a virtual menu system - enable a self-voicing option and have each category, or item description, spoken as they receive focus via a gesture or other input. As the blind user gestures to trigger both movement and interaction they may get more detail about items that are closer to them. The user must be allowed to query and interrogate these items and make selections.

**REQ 9c:** Allow for the re-mapping of gestures to associate different actions with different input types or gestures. This may be a virtual switch that can map to new macros on the fly. This will allow the user to change defaults and employ gestures to carry out new actions offered by the immersive environment as required.

### 4.10  Signing videos and text description transformation

**User Need 10:** A deaf or hard of hearing person, for whom a written language may not be their first language, may prefer signing of video for text, objects or item descriptions.

**REQ 10a:** Allow text, objects or item descriptions to be presented to the user via a signing avatar (pre-recorded only).

**REQ 10b:** Any signing videos should be 1/3rd minimum of the original streams signing size. This requirement comes from research of 240 ASL videos intended to be watched by deaf signers, that found that nearly all set signer size to at least one-third the size of the full video. [[raja-asl](https://www.w3.org#bib-raja-asl)]

Note  

 Currently, it is not possible to provide an accurate live interpretation via a signing avatar. In general, animated or digital signing avatars should be avoided as users find them less expressive than recorded video of humans who can convey the natural quality and skill provided by appropriately trained and qualified interpreters and translators. Therefore, uses of signed avatars should rely only on pre-recording of 'real people' who are trained and qualified interpreters and translators. See the concerns expressed by the WFD and WASLI 'Statement on Use of Signing Avatars'. [[wfd-wasli](https://www.w3.org#bib-wfd-wasli)] 

However, we note this is an emerging field and exploration is encouraged to ensure the future development of quality signing avatars. For example, this could be via building a signing avatar that both provides a face with fully functioning muscular variables and can successfully parse the nuances of vocal expression and meaning.

### 4.11  Safe harbour controls

**User Need 11:** People with Cognitive Impairments may be easily overwhelmed in Immersive Environments.

**REQ 11a:** Allow the user to set a 'safe place' - quick key, shortcut or macro.

### 4.12  Immersive time limits

**User Need 12:** Users may be adversely affected by spending too much time in an immersive environment or experience, and may lose track of time. 

**REQ 12a:** Provide a platform integration with tools that support digital wellbeing, allow the user to access alarms for time limits during an immersive session. 

### 4.13  Orientation and navigation

**User Need 13:** A screen magnification user or user with a cognitive and learning disability or spatial orientation impairment needs to maintain focus and understand where they are in immersive environments.

**REQ 13a:** Ensure the user can reset and calibrate their orientation/view in a device independent way.

**REQ 13b:** Ensure field of view in Immersive environments, are appropriate, and can be personalized - so users are not disorientated.

**REQ 13c:** Provide clear visual or audio landmarks.

### 4.14  Second screen devices

**User Need 14:** Users of assistive technology such as a blind, or deaf-blind users communicating via a RTC application in  XR , may have sophisticated 'routing' requirements for various inputs and outputs and the need to manage same. 

**REQ 14a:** Allow the user to route text output, alerts, environment sounds or audio to a braille or other second screen device.

**REQ 14b:** Ensure that the user can manage the flow of critical messaging, or content to display on a second screen.

**REQ 14c:** Support touch screen accessibility gestures (e.g. swipes, flicks and single, double or triple taps with 1, 2 or 3 fingers) on a second screen device to allow the user to navigate menus and interact.

Note

'Second screen' is a term used in this document to denote any another external output device, such as a monitor or sound card, or assistive technology such as braille output. The use of the term is not restricted to just these devices and can refer to any output device a user may choose.

### 4.15  Interaction speed

**User Need 15:** Users with physical disabilities or cognitive and learning disabilities may find some interactions too fast to keep up with or maintain.

**REQ 15a:** Allow users to change the speed they can travel or perform interactions, in an immersive environment.

**REQ 15b:** Allow timings for interactions or critical inputs to be modified or extended.

**REQ 15c:** Provide help for the user with a cognitive or learning disability.

**REQ 15d:** Provide clear start and stop mechanisms.

Note

 The term 'help' for REQ 15c may vary from explanatory information such as textual/symbolic annotations in an application, to human assistance in real time.

### 4.16  Avoiding sickness triggers

**User Need 16:** Users with vestibular disorders, Epilepsy, and photo sensitivity may find some interactions trigger motion sickness and other affects. This may be triggered when doing teleportation or other movements in  XR .

**REQ 16a:** Avoid interactions that trigger epilepsy or motion sickness and provide alternatives.

**REQ 16b:** Ensure flickering images are at a minimum, will not trigger seizures (more than 3 times a second), or can be turned off or reduced.

### 4.17  Spatial audio tracks and alternatives

**User Need 17:** Hard of hearing users may need accommodations to perceive audio.

**REQ 17a:** Provide spatialized audio content to emulate three-dimensional sound forms in immersive environments.

**REQ 17b:** Provide text descriptions of important audio content.

### 4.18  Spatial orientation: Mono audio option

**User Need 18:** Users with spatial orientation impairments, cognitive impairments or hearing loss in just one ear may miss information in a stereo or binaural soundscape.

**REQ 18a:** Allow mono audio sound to be sent to both headphones so that the user can perceive the whole soundscape through either ear. [[mono-ios](https://www.w3.org#bib-mono-ios)].

Note

People with traumatic brain injuries can have a range of impairments. These may be spatial orientation impairments, auditory processing difficulties, visual processing difficulties or a combination. They may miss information in stereo or binaural soundscapes. This can affect orientation while navigating. Even if provided with accurate directions, they may not recognize surroundings, or experience anxiety when navigating. 

### 4.19  Captioning, Subtitling and Text: Support and customization

**User Need 19:** Users may need to customise captions, subtitles and other text in  XR  environments.

**REQ 19a:** Provide support for captioning and subtitling of multimedia content.

**REQ 19b:** Allow customisable context sensitive reflow of captions, subtitles and text content in  XR  environments. The suitable subtitling area may be smaller than what is required currently for television. [[inclusive-seattle](https://www.w3.org#bib-inclusive-seattle)]

Note

The [W3C  Immersive Captions Community Group](https://www.w3.org/community/immersive-captions/) is actively contributing to this emerging accessibility standards work representing a diverse range of user needs.

## 5.  Related Documents

Other documents that relate to this and represent current work in the RQTF/APA are:

[XR  Semantics Module](https://www.w3.org#related-documents) - this document outlines proposed accessibility requirements that may be used in a modular way in immersive, augmented or mixed reality ( XR ). A modular approach may help us to define clear accessibility requirements that support  XR  accessibility user needs, as they relate to the immersive environment, objects, movement, and interaction accessibility. Such a modular approach may help the development of clear semantics, designed to describe specific parts of the immersive eco-system. In immersive environments it is imperative that the user can understand what objects are, understand their purpose, as well as another qualities and properties including interaction affordance, size, form, shape, and other inherent properties or attributes.

[ WebXR Standards and Accessibility Architecture Issues](https://www.w3.org#related-documents) - this document is informative and aims to outline some of the challenges in understanding the complex technical architecture and processes behind how  XR  environments are currently rendered. To make these environments accessible and provide a quality user experience it is important to also understand the nuances and complexity of accessible user interface design and development for the 2D web. Any attempt to make  XR  accessible needs to be based on meeting the practical user needs of people with disabilities.

## A.  Change Log

The following is a list of new requirements and other changes in this document:

**Immersive semantics and customization:** REQ 1c: Objects that are important within any given context of time and place can be identified in a suitable modality.

**Immersive semantics and customization:** REQ 1d: Allow filtering and the ability to query items and content for more details. 

**REQ 1e:** Allow the user to query objects and content for more details.

**Mono audio option:** REQ 19a: Allow mono audio sound to be sent to both headphones so that the user can perceive the whole soundscape through either ear. [[mono-ios](https://www.w3.org#bib-mono-ios)]

**Interaction and target customization:** REQ 4d: Support 'Sticky Keys' requirements such as serialization for various inputs when the user needs to press multiple buttons.

**Gestural interfaces and interactions** REQ 9a: Support touch screen accessibility gestures (e.g. swipes, flicks and single, double or triple taps with 1, 2 or 3 fingers).

**Magnification context and resetting ** REQ 7b: Where it makes sense (such as in menus) interface elements can be enlarged and the menu reflowed to enhance the usability of the interface up to a certain magnification requirement.

**Gestural interfaces and interactions** REQ 9a: Support touch screen accessibility gestures (e.g. swipes, flicks and single, double or triple taps with 1, 2 or 3 fingers) on a second screen device to navigate menus and interact. 

**Gestural interfaces and interactions** REQ 9c: Allow for the re-mapping of gestures to associate different actions with different input types or gestures. This may be a virtual switch that can map to new macros on the fly. This will allow the user to change defaults and employ gestures to carry out new actions offered by the immersive environment as required.

**Signing videos and text description transformation** REQ 10b: Any signing videos should be 1/3rd minimum of the original streams signing size. This requirement comes from research of 240 ASL videos intended to be watched by deaf signers, that found that nearly all set signer size to at least one-third the size of the full video. 

**Orientation and navigation** REQ 13c: Provide clear visual or audio landmarks.

**Second screen devices** REQ 14b: Ensure that the user can manage the flow of critical messaging, or content to display on a second screen.

**Second screen** REQ 14c: Support touch screen accessibility gestures (e.g. swipes, flicks and single, double or triple taps with 1, 2 or 3 fingers) on a second screen device to allow the user to navigate menus and interact.

**Spatial audio tracks and alternatives** REQ 17b: Provide text descriptions of important audio content.

Requirements have been updated based on combined review feedback, discussion and Research Questions Task Force consensus. Other user needs have been edited to better reference related requirements such as with Second screen devices.

Various clarification or reference notes have been added relating to: 

The importance of discoverability relating to accessibility features in  XR .

Specific augmented reality issues when marking locations in a motion agnostic way.

W3C  Personalization semantics and how they can support people with cognitive impairments.

The need for accessibility API's that map custom user interface actions to control types.

The limitations of accurate live interpretation via a digital signing avatar.

The impact of traumatic brain injury on a user's spatial orientation, auditory and visual processing abilities.

## B.  Acknowledgements

### B.1  Participants of the APA working group active in the development of this document

Shadi Abou-Zahra,  W3C

Matthew Tylee Atkinson, The Paciello Group

Judy Brewer,  W3C

Michael Cooper,  W3C

Scott Hollier, Invited Expert

Joshue O'Connor,  W3C

Janina Sajka, Invited Expert

Jason White, Educational Testing Service

### B.2  Previously active participants, commenters, and other contributors

Frances Baum

Nicoló Carpignoli, Chialab 

Wendy Dannels, RIT/NTID Research Center on Culture and Language

David Fazio, Helix Opportunity

Marku Hakkinen, Educational Testing Service

Charles Hall, Invited Expert

Ian Hamilton

John Kirkwood

Raja Kushalnagar, Department of Science, Technology and Mathematics Gallaudet University

Charles LaPierre, Benetech

Thomas Logan, Equal Entry

Melina Möhlne, IRT

Estel·la Oncins Noguer, UAB TransMedia Catalonia

Christopher Patnoe, Google

Devon Persing, Shopify

Sonali Rai, Royal National Institute of the Blind

Ajay Sharma, HCL Technologies

Suzanne Taylor, Things Entertainment

Léonie Watson, TetraLogical

### B.3  Enabling Funders

This work is supported by the [EC-funded WAI-Guide Project](https://www.w3.org/WAI/about/projects/wai-guide/).

## C.  References

### C.1  Informative references

[able-gamers][Thought On Accessibility and VR](https://ablegamers.org/thoughts-on-accessibility-and-vr/). AJ Ryan. March, 2017. URL: [https://ablegamers.org/thoughts-on-accessibility-and-vr/](https://ablegamers.org/thoughts-on-accessibility-and-vr/)[coga-usable][Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/). Lisa Seeman-Horwitz; Rachael Bradley Montgomery; Steve Lee; Ruoxi Ran. W3C. 29 April 2021. W3C Note. URL: [https://www.w3.org/TR/coga-usable/](https://www.w3.org/TR/coga-usable/)[game-a11y][Game Accessibility Guidelines](http://gameaccessibilityguidelines.com). Barrie Ellis; Ian Hamilton; Gareth Ford-Williams; Lynsey Graham; Dimitris Grammenos; Ed Lee; Jake Manion; Thomas Westin. 2019. URL: [http://gameaccessibilityguidelines.com](http://gameaccessibilityguidelines.com)[inclusive-seattle][W3C Workshop on Inclusive XR Seattle](https://www.w3.org/2019/08/inclusive-xr-workshop/). W3C; Pluto VR. W3C. Nov 2019. URL: [https://www.w3.org/2019/08/inclusive-xr-workshop/](https://www.w3.org/2019/08/inclusive-xr-workshop/)[maidenbaum-amendi] Non-visual virtual interaction: Can Sensory Substitution generically increase the accessibility of Graphical virtual reality to the blind? . Maidenbaum, S.; Amedi, A. In Virtual and Augmented Assistive Technology (VAAT), 2015 3rd IEEE VR International Workshop on (pp. 15-17). IEEE. 2015.  [mono-ios][iPhone User Guide](https://support.apple.com/en-gb/guide/iphone/iph3e2e2cdc/ios). Apple. 2020. URL: [https://support.apple.com/en-gb/guide/iphone/iph3e2e2cdc/ios](https://support.apple.com/en-gb/guide/iphone/iph3e2e2cdc/ios)[personalization-content][Personalization Semantics Content Module 1.0](https://www.w3.org/TR/personalization-semantics-content-1.0/). Lisa Seeman; Charles LaPierre; Michael Cooper; Roy Ran; Richard Schwerdtfeger. W3C. 2020. URL: [https://www.w3.org/TR/personalization-semantics-content-1.0/](https://www.w3.org/TR/personalization-semantics-content-1.0/)[personalization-requirements][Requirements for Personalization Semantics](https://www.w3.org/TR/personalization-semantics-requirements-1.0/). Lisa Seeman; Charles LaPierre; Michael Cooper; Roy Ran. W3C. 2020. URL: [https://www.w3.org/TR/personalization-semantics-requirements-1.0/](https://www.w3.org/TR/personalization-semantics-requirements-1.0/)[personalization-semantics][Personalization Semantics Explainer 1.0](https://www.w3.org/TR/personalization-semantics-1.0/). Lisa Seeman; Charles LaPierre; Michael Cooper; Roy Ran; Richard Schwerdtfeger. W3C. 2020. URL: [https://www.w3.org/TR/personalization-semantics-1.0/](https://www.w3.org/TR/personalization-semantics-1.0/)[raja-asl][Legibility of Videos with ASL signers](https://arxiv.org/abs/2105.12928). Cornell UNiversity. 27 May 2021. URL: [https://arxiv.org/abs/2105.12928](https://arxiv.org/abs/2105.12928)[spatialized-navigation][What’s around Me? Spatialized Audio Augmented Reality for Blind Users with a Smartphone](https://link.springer.com/chapter/10.1007/978-3-642-30973-1_5). Blum J.R.; Bouchard M.; Cooperstock J.R. . Springer. 2012. URL: [https://link.springer.com/chapter/10.1007/978-3-642-30973-1_5](https://link.springer.com/chapter/10.1007/978-3-642-30973-1_5)[supple-project][SUPPLE: Automatically Generating Personalized User Interfaces](http://www.eecs.harvard.edu/~kgajos/research/supple/). Krzysztof Gajos et al. Harvard. 2010. URL: [http://www.eecs.harvard.edu/~kgajos/research/supple/](http://www.eecs.harvard.edu/~kgajos/research/supple/)[web-adapt][W3C Workshop on Web Games Position Paper: Adaptive Accessibility](https://www.w3.org/2018/12/games-workshop/papers/web-games-adaptive-accessibility.html). Matthew Tylee Atkinson; Ian Hamilton; Joe Humbert; Kit Wessendorf. W3C. Dec 2018. URL: [https://www.w3.org/2018/12/games-workshop/papers/web-games-adaptive-accessibility.html](https://www.w3.org/2018/12/games-workshop/papers/web-games-adaptive-accessibility.html)[wfd-wasli][WFD and WASLI](https://wfdeaf.org/news/resources/wfd-wasli-statement-use-signing-avatars/). World Federation of the Deaf. 14 March 2081. URL: [https://wfdeaf.org/news/resources/wfd-wasli-statement-use-signing-avatars/](https://wfdeaf.org/news/resources/wfd-wasli-statement-use-signing-avatars/)[↑](https://wfdeaf.org/news/resources/wfd-wasli-statement-use-signing-avatars/)