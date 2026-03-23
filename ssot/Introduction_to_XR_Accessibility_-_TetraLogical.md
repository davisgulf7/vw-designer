# Introduction to XR Accessibility - TetraLogical

Skip to content  Accessibility specialists

# Introduction to XR Accessibility

 Posted on  Wednesday, 11 September 2024  by [Joe Lamyman](https://tetralogical.com/about/team/jlamyman) in [Design and development](https://tetralogical.com/blog/category/design-and-development/)

Extended Reality (XR) provides immersive experiences through detailed visual, audio, and multi-media content. When using these different types of content, we need to consider how we can communicate the same information to people with disabilities in order to make XR accessible to everyone.

In this introduction to the XR accessibility series, we’ll explore key considerations for designing and developing inclusive XR experiences. Whether you’re working with Augmented Reality (AR) or Virtual Reality (VR), and regardless of the hardware, this series will provide guidance to improve usability for people with disabilities.

You can explore other articles in this series including:

[Introduction to XR accessibility](https://tetralogical.com/blog/category/design-and-development/)

[XR Accessibility: for people with seeing disabilities](https://tetralogical.com/blog/category/design-and-development/)

[XR Accessibility: for people with hearing disabilities](https://tetralogical.com/blog/category/design-and-development/)

[XR Accessibility: for people with moving disabilities](https://tetralogical.com/blog/category/design-and-development/)

[XR Accessibility: for people with thinking disabilities](https://tetralogical.com/blog/category/design-and-development/)

You can also watch my [Introduction to XR accessibility talk](https://www.youtube.com/watch?v=5XGwY5PSsb8&list=PLn7dsvRdQEfFompoGO_CE5z-_HjEdgVit) from InclusiveDesign 24 (#ID24).

## Who does this affect?

Before we dive in, there are different [types of disability](https://tetralogical.com/blog/2024/11/18/foundations-types-of-disability/) that might be permanent, temporary, or situational:

**Permanent disabilities**: which are constant and include people with seeing, hearing, moving and thinking disabilities

**Temporary disabilities**: which are periodic and include people who are ill such as experiencing a migraine, or have reduced motion due to wearing a cast or sling

**Situational disabilities**: which are external and dependent on the situation or the environment and include people who are in a loud environment and are unable to hear the related audio, or people who might be multitasking and working under pressure

In order to better understand the needs of people using XR, let's get started by understanding some related standards!

## Standards and starting points

Whether you're starting to design and develop an XR experience, or you're updating an existing project, standards offer a helpful foundation. They allow us to understand what we need to conform to, and for those related to usability, allow us to consider the needs of people using the experience so that we can tailor our design and development to better meet our audience's needs.

### Web Content Accessibility Guidelines

While incredibly useful, it's not always easy to map the [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG22/) to other mediums that are not traditional interfaces such as XR experiences. For example, in some instances, guidelines reference markup and HTML directly, which may not be used at all in an XR product.

WCAG is useful to reference, particularly when creating user interfaces such as menus, which are more similar to content that you would encounter on the web. However, for AR and VR functionality using 3D objects and complex interactions, other standards offer more relevant considerations, specific to the XR medium. For a deeper dive into WCAG, read our [WCAG Primer](https://tetralogical.com/blog/2020/04/10/wcag-primer/).

### XR accessibility user requirements

A good starting point is the W3C's [XR accessibility user requirements](https://www.w3.org/TR/xaur/) (XRAUR). This document includes 19 succinct descriptions of user needs and requirements for people with disabilities. For example:

**User Need 1**: A user of assistive technology wants to navigate, identify locations, objects and interact within an immersive environment.

Each need is then broken down into individual requirements, helping to make them more tangible and actionable.

**REQ 1a**: Navigation mechanisms must be intuitive with robust affordances. Navigation, location and object descriptions must be accurate and identified in a way that is understood by assistive technology.

In addition to this, the requirements aren't restricted to the web, so can be used as a starting point for any XR experience.

Due to the focus on XR, these requirements are more specific to the needs of people, than they would be when attempting to map to WCAG requirements.

In a [workshop exploring the use of XR in learning and education](https://www.cencenelec.eu/media/CEN-CENELEC/CWAs/RI/cwa18006_2023.pdf), the European Committee for Standardisation (CEN) acknowledged that:

In web accessibility, it is plausible to enforce accessibility laws because of existing guidelines, such as Web Content Accessibility Guidelines … The situation is different in XR accessibility.

The section continues with a brief description of the few standards efforts that exist in this space, but ultimately concludes by saying:

…we would especially like to emphasize the XR Accessibility User Requirements from W3C as an appropriate starting point

Therefore, these are the requirements that we would recommend that you use as a basis for designing and developing an XR experience.

It's important to note however, that the authors of the XRAUR document state that:

This document is most explicitly not a collection of baseline requirements.

So while meeting the requirements won't mean that your experience is fully accessible, it will help to ensure that you have a good starting point. As always, considering the specific needs of your audience and the different contexts of use, are critical. Make sure that you carry out [usability testing](https://tetralogical.com/services/agile-usability-testing/) with a range of people with disabilities who will be using your product or service.

### Barriers Browser

Alongside the XRAUR, you can also use the BBC's [Barriers Browser](https://www.bbc.co.uk/accessibility/forproducts/xr/barriers) research, to understand common barriers present in XR experiences, and make sure that these problems are not present in your products.

The barriers identified are the result of research conducted with over 100 research participants, and are presented by disability group, with further information and, where possible, examples and solutions provided for the problems found.

### Inclusive Design Principles

Finally, the [Inclusive Design Principles](https://inclusivedesignprinciples.info/) are also relevant to XR design and development as well. These principles offer clear guidance and help to promote disabled people's needs when designing and developing functionality.

Principles such as, [be consistent](https://inclusivedesignprinciples.info/#be-consistent) and [offer choice](https://inclusivedesignprinciples.info/#offer-choice) are surfaced through techniques such as personalisation, which are vital to creating accessible XR experiences.

## Challenges with controllers

In both the XRAUR and the Barriers Browser research, there are multiple challenges raised in relation to the controllers, which can cause issues for people with different types of disability. In particular, issues relate to Virtual Reality (VR) controllers; typically, two handheld motion-detecting controllers that come with most VR headsets.

Oculus Touch controllers, image from WikiMedia Commons used under the [Creative Commons Attribution-Share Alike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/deed.en)These types of controllers often have a grip with buttons on the back to be used with the index fingers, and on the front are joysticks and buttons which are to be operated using the thumbs. These controllers require a high level of dexterity and motion, plus people need to remember how the controls map to the experience that they are using. This is a high level of complexity when compared to other input methods that people might be using such as head tracking, keyboards, or adaptive controllers.

Handheld controllers require precise input, relying heavily on motion controls and fine motor skills to target and interact with the correct elements or objects. This might not be possible for people who experience tremors or have reduced motion.

## Accessible input methods

Instead of designing and developing solely for a VR headset's motion controllers, you should design and develop for multiple different input methods.

Experiences shouldn't be reliant on motion-only controls. If somebody needs to use a keyboard or an adaptive controller, this should be possible. This relates back to one of the Inclusive Design Principles to [offer choice](https://inclusivedesignprinciples.info/#offer-choice):

Consider providing different ways for people to complete tasks, especially those that are complex or non standard.

By implementing different ways of interacting with the experience, you are allowing people to choose their preferred way of interacting with XR, which might better suit them and allow them to use the experience.

Xbox adaptive controller, image from Rosenfeld Media used under the [Creative Commons Attribution (CC BY 2.0) license](https://creativecommons.org/licenses/by/2.0/)Additionally, we need to carefully consider how people will use these different inputs and design interactions that suit them. Different input methods include keyboard, switches, and adaptive controllers.

In designing for different input methods, ensure that you can support simultaneous input methods too. For example, it might not be possible for someone to use both of the handheld motion controllers that come with a VR headset at the same time. They might be able to hold one motion controller in one hand, but then need to use an adaptive controller with their other hand. People should be given control in order to interact with an experience as they need to, so that they can use it. This relates to the Inclusive Design Principle to [give control](https://inclusivedesignprinciples.info/#give-control):

Ensure people are in control. People should be able to access and interact with content in their preferred way.

Using different input methods allows people to access the experience in the way that works best for them.

Finally, you should also make it possible for people to change the input device that they're using without affecting their experience.

Imagine an experience that requires you to hold motion controls up for a long period of time, which could get tiring for anybody. In this case, being able to switch to a different method of input should be possible. The person using the experience shouldn't have to reset everything, or quit out of the application just to do this, the experience should accept the new method of input seamlessly.

## Provide accessibility settings up front

Make sure accessibility settings are easily available when joining or starting the experience. If it's someone's first time using the experience, display the different options and settings as the first thing that people interact with. Otherwise, if the accessibility settings are hidden in the experience's menus, people might not be able to navigate to them and use your experience!

Using video games as an example for this, The Last of Us: Part 2, provides people with accessibility options the first time they start the game, so that people can ensure that they are using the experience in the way that works best for them. Similarly, Forza Horizon 5 includes an option to access the accessibility options menu from the start screen, and uses a screen reader on the game's menus to allow people to easily understand the different options available.

Accessibility options available from the start screen in Forza Horizon 5  

## Context of use

It's important to remember that design decisions will always be affected by the context of use. For example, visually demonstrating how people should interact with objects to complete an action is something that we might want to make really easy and obvious if we're designing an educational experience or a training experience. However, that's going to differ quite a lot if you're creating an entertainment application such as a virtual escape room.

In cases like this, you may want to subvert interactions slightly and make controls look less obvious so that people can try and discover things themselves. This approach might factor into an education experience as well. As people progress and build their skills and capabilities, you might want to gradually remove affordances to make something more difficult, or less guided, to test how much they've learnt.

Context of use relates to the Inclusive Design Principle to [consider situation](https://inclusivedesignprinciples.info/#consider-situation):

People use your interface in different situations. Make sure your interface delivers a valuable experience to people regardless of their circumstances.

We can think about the context of use when providing context sensitive help, and make sure that people are able to get the right level of support and help that they need to use the experience, without this being overbearing, disruptive, or distracting.

## Summary

The XR Accessibility User Requirements and the Barriers Browser research are great starting points for considering the needs of disabled people when developing XR experiences, as well as some elements of WCAG.

In general, we need to make sure that we:

Support different input methods, so people can choose how they interact with an experience

Provide up front access to accessibility settings when people first use an experience

Now that you're aware of general considerations for accessible XR experiences, you can explore the rest of the posts in this series which cover specific groups of disabilities:

[XR Accessibility: for people with seeing disabilities](https://inclusivedesignprinciples.info/#consider-situation)

[XR Accessibility: for people with thinking disabilities](https://inclusivedesignprinciples.info/#consider-situation)

[XR Accessibility: for people with hearing disabilities](https://inclusivedesignprinciples.info/#consider-situation)

[XR Accessibility: for people with moving disabilities](https://inclusivedesignprinciples.info/#consider-situation)

## More information

[An Illegally Sighted Look at VR Accessibility](https://inclusivedesignprinciples.info/#consider-situation), Jesse Anderson

[Barriers Browser](https://inclusivedesignprinciples.info/#consider-situation), BBC

[Inclusive XR: accessible 3D experiences](https://inclusivedesignprinciples.info/#consider-situation), TetraLogical

[Inclusive XR: accessible augmented reality experiences](https://inclusivedesignprinciples.info/#consider-situation), TetraLogical

[XR accessibility user requirements](https://inclusivedesignprinciples.info/#consider-situation), W3C

## Next steps

If you're currently designing an XR product, our [design review](https://tetralogical.com/services/design-reviews/) service will provide you with our accessibility expertise and guidance to build an accessible experience. If you already have an XR product, our [assessments](https://tetralogical.com/services/assessments/) can help you to understand whether your product meets accessibility standards.

[All categories](https://tetralogical.com/services/assessments/)

[Design and development](https://tetralogical.com/services/assessments/)

[News](https://tetralogical.com/services/assessments/)

[Standards](https://tetralogical.com/services/assessments/)

[Strategy](https://tetralogical.com/services/assessments/)

[Testing](https://tetralogical.com/services/assessments/)

[User experience](https://tetralogical.com/services/assessments/)

[Apps](https://tetralogical.com/services/assessments/)

[Artificial Intelligence](https://tetralogical.com/services/assessments/)

[Assistive Technology](https://tetralogical.com/services/assessments/)

[Code](https://tetralogical.com/services/assessments/)

[Foundations](https://tetralogical.com/services/assessments/)

[Inclusive Design Principles](https://tetralogical.com/services/assessments/)

[Meet the team](https://tetralogical.com/services/assessments/)

[WCAG](https://tetralogical.com/services/assessments/)

## We like to listen

Wherever you are in your accessibility journey, get in touch if you have a project or idea.

[hello@tetralogical.com  ](https://tetralogical.com/services/assessments/)60 Windsor Avenue ,  London ,  SW19 2RR ,  UK   +44 (0)20 8895 6768   hello@tetralogical.com  

© TetraLogical Services Ltd. All Rights Reserved. Company number 12951928.

[Privacy policy](https://tetralogical.com/services/assessments/) - [Accessibility statement](https://tetralogical.com/accessibility-statement/) - [Code of ethics](https://tetralogical.com/code-of-ethics/)