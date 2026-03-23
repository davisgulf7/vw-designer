# How to Create a Moodle Integration - Edlink

Data Integration

Whitepaper

Client Stories

Work With Us

# How to create a Moodle integration  [Back to Edlink](https://twitter.com/edlinkapi)[Moodle](https://twitter.com/edlinkapi)How to create a Moodle integration

Integration with Moodle works a bit differently than some of the other major LMSs (like Canvas, Schoology, and Blackboard). Edtech developers can integrate through 2 main methods. Moodle can integrate through the LTI standard or a Moodle plugin.

## Edlink Team

Written by a team member of Edlink.

[More posts](https://twitter.com/edlinkapi) by Edlink Team.

[Edlink Team](https://twitter.com/edlinkapi)

10 Mar 2025   •  2 min read  

Moodle is an interesting LMS. It's widely used across the education sector by both institutions and individuals who need a learning platform to host courses, share online resources, and grade assessments. Because it's used by such a broad audience, you'll probably receive requests to integrate your app with Moodle if you're an edtech developer.

Moodle integration works a bit different than some of the other major learning management systems, such as Canvas, Schoology, and Blackboard. There are two main methods to integrate with Moodle: through the LTI® standard or through the development and installation of a Moodle plugin. Here is what you need to know to create a Moodle integration.

### LTI Integration for Moodle

[LTI](https://twitter.com/edlinkapi) (or, Learning Tools Interoperability) is a standard from the IMS Global Learning Consortium that several learning platforms have adopted to provide interoperability. Applications that are LTI-compliant can work with any platform that is also LTI-compliant, as long as it's a supported version of LTI.

Moodle supports the most recent releases of the LTI standard: LTI v1.3 and LTI Advantage. Moodle allows users to launch into an LTI app from inside Moodle, itself. Typically, the app appears inside of an iframe in Moodle. Since Moodle supports LTI Advantage, your app can use the improved grade passback and enrollment provisioning services offered by[ LTI Advantage](https://ed.link/community/lti-advantage/).

### Integration With Moodle Plugins

Moodle does allow external applications to also integrate with Moodle environments through[ Moodle's Core APIs](https://docs.moodle.org/dev/Core_APIs). However, if a developer wants to integrate with Moodle through these Core APIs, the developer of the app must create a[ Moodle plugin](https://moodle.com/faq/how-do-i-create-a-moodle-plugin/). This plugin, which must be written in PHP, must be manually installed in a school's Moodle environment by the environment's administrator.

The Core APIs can be used to access different parts of a Moodle environment depending on the role of the user that the plugin authenticates. For example, the plugin can write back to the user's Moodle gradebook, calendar, or profile. It can also be used to gather enrollment information to view a list of courses and roster information for the authenticated user.

### [What Type of Moodle Integration Should I Develop?](https://moodle.com/faq/how-do-i-create-a-moodle-plugin/)

The type of integration that you should build will depend on the needs of your customer. Some schools particularly need LTI integration with their Moodle environments. Others may be looking for a solution that includes features that are better supported by Moodle plugins, such as school or district-wide rostering. Thus, having solutions for both situations can prove to be valuable when trying to work with several schools.

## Read More on Moodle:

Read these other articles we've written on Moodle and integrations.

[The Challenges of Integrating with Moodle](https://moodle.com/faq/how-do-i-create-a-moodle-plugin/)

Edtech Vendors Can Stay Ahead with LMS Integrations

What are API Integrations for LMSs

What is “LTI Integration”?

Rostering Students and Teachers in Your App: What Are Your Options?

## Learn More about Edlink

If you're looking for a partner to guide you through developing Google Classroom integrations, then let us introduce ourselves. We're Edlink!

[Introducing Edlink](https://moodle.com/faq/how-do-i-create-a-moodle-plugin/)

Our Mission at Edlink

[What is the Edlink Unified API?](https://moodle.com/faq/how-do-i-create-a-moodle-plugin/)

### More in  [Moodle](https://ed.link/community/tag/moodle/)

[LMS integrations in 2024 for K12 and higher education: What you need to know](https://ed.link/community/tag/moodle/)

21 Nov 2023  – 1 min read

[Challenges of integrating with Moodle](https://ed.link/community/tag/moodle/)

25 Mar 2021  – 2 min read

[2022's state of the LMS market](https://ed.link/community/tag/moodle/)

19 May 2020  – 4 min read

Brightspace  

## What can I do with the Brightspace (D2L) API?

Brightspace by D2L is a popular LMS in the US and Canada. Many institutions may use Brightspace. So edtech developers need to know how to integrate Brightspace and its features. We'll focus specifically on integration through the Brightspace API and its features.

[Edlink Team](https://ed.link/community/tag/moodle/)14 Mar 2025   •  4 min read  FAQ  

## If I work with Edlink will I automatically be OneRoster/LTI/Clever certified?

No. It is certainly possible for you to get certified by any of the bodies that manage the systems or standards we help edtech developers support. And Edlink would be