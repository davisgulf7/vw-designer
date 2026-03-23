# FAQ: IT Admin Guide - Minecraft Education

FAQ: IT Admin Guide – Minecraft Education

X

## CAPTCHA Security Check

Enter the characters you see.

New | Audio Picture 

Characters

Submit

X

## You are reporting this post or comment!

Are you sure you want to report this?

Please select a reason

Violates posting guidelines

Wrong category or topic

Previously considered suggestion

Duplicate

Child sexual exploitation or abuse

Terrorism or violent extremism

Hate speech

Imminent harm: Threat to harm others

Imminent harm: Self-harm or suicide

Non-consensual intimate imagery

Extreme violence or gore

Nudity or pornography

Harassment or bullying

Defamation, impersonation, false information

Drugs or alcohol

Profanity

Note: 180 character limit

By submitting this report, you confirm that the information you have provided is accurate and complete to the best of your knowledge.

Yes No

[Skip to main content](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide#skip-main-content)

[Minecraft Education Home](https://education.minecraft.net/)

[Support Center](https://edusupport.minecraft.net/hc/en-us)

[Teacher's Lounge](https://aka.ms/mcteacherslounge)

Search

[Sign in](https://edusupport.minecraft.net/hc/en-us/signin?return_to=https%3A%2F%2Fedusupport.minecraft.net%2Fhc%2Fen-us%2Farticles%2F360047118992-FAQ-IT-Admin-Guide) 

Our live chat is temporarily down, and we're working to get it back online as quickly as possible. Find other ways to [contact support](https://edusupport.minecraft.net/hc/en-us/articles/360048662071)! 

[Support Center Home](https://edusupport.minecraft.net/hc/en-us)

[Get Set Up](https://edusupport.minecraft.net/hc/en-us/categories/360003796971-Get-Set-Up)

[Administration](https://edusupport.minecraft.net/hc/en-us/sections/360011448472-Administration)

## Articles in this section

FAQ: IT Admin Guide

## Articles in this section

[Best Practices for Managing Camps and Clubs](https://edusupport.minecraft.net/hc/en-us/articles/4416248488980-Best-Practices-for-Managing-Camps-and-Clubs)

[FAQ: IT Admin Guide](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide)

[URLs Used by Minecraft Education](https://edusupport.minecraft.net/hc/en-us/articles/4404784181524-URLs-Used-by-Minecraft-Education)

[Sign into Minecraft Education with Google account credentials](https://edusupport.minecraft.net/hc/en-us/articles/360051644972-Sign-into-Minecraft-Education-with-Google-account-credentials)

[Location of World Files](https://edusupport.minecraft.net/hc/en-us/articles/4404785703316-Location-of-World-Files)

[Minecraft Education End User License Agreements (EULA)](https://edusupport.minecraft.net/hc/en-us/articles/4405348643092-Minecraft-Education-End-User-License-Agreements-EULA)

# FAQ: IT Admin Guide

[Justin](https://edusupport.minecraft.net/hc/en-us/profiles/415439408432-Justin) Support

4 months ago

Updated

Follow Not yet followed by anyone     

This guide answers many of the common questions IT Administrators have about deploying and managing Minecraft Education in their school(s) such as URLs that need to be allow listed through enterprise firewalls and content filters, ports, minimum required specs, install & update info, and student data.

### Important Links:

[URLs that need to be allow listed](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide#allow)

[Will allowing these URLs open my network to unwanted activity?](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide#unwanted)

[Do I need to forward any Ports for Minecraft Education?](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide#ports)

[What are the minimum required specs for devices to run Minecraft Education?](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide#specs)

[How do I install Minecraft Education?](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide#install)

[How do I update Minecraft Education?](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide#update)

[Does Minecraft Education collect or store student data?](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide#data)

### Why should I allow students to play Minecraft at school?

Minecraft Education is a game-based learning platform that offers educators a transformative way to engage students and ignite their passion for learning. The platform contains controls not found in the Consumer editions of Minecraft - which allow instructors oversight into the activities of their students. Educators in grades K-12 are using Minecraft Education to teach a range of subjects, from history and chemistry to sustainability and foreign languages, and can map lessons directly to specific learning outcomes and curriculum standards. Through these project-based lessons, students build critical 21st century skills like collaboration, creative problem solving and digital citizenship.

### Why do I need to allow network access to URLs?

Minecraft Education is more than just a game—it's a connected platform that uses cloud services to deliver interactive learning tools. To ensure students can access all available features, school IT networks need to allow communication with specific online services. Without this access, key functionality may be blocked.

Here's why network access is essential:

Minecraft Education relies on a services-based architecture, meaning it connects to the internet to access essential features.

External communication is required to enable tools like Immersive Reader (https://edusupport.minecraft.net/hc/en-us/articles/360061503031-Accessibility-Features), lesson content, and coding platforms.

To enable these features, school networks must allow traffic between Minecraft Education and a predefined list of service endpoints.

Allowlisting the below URLs ensures full access to services that are embedded in the Minecraft Education experience.

## List of all URLs used by Minecraft Education

This is the list of all the URLs used by Minecraft Education.

|  |  |

| --- | --- |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

|  |  |

Note that as of v1.21.91, https://www.tynker.com is no long needs to be allow listed as we no longer utilize the services from this URL.

**Additional URLs for Microsoft auth & Azure services:**

[Office 365 URLs and IP address ranges - Microsoft 365 Enterprise | Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide)

See "Microsoft 365 Common and Office Online" section for URLs that relate to the Microsoft login services we use. IDs 56 and 59 in this section are the most relevant to what Minecraft Education uses. Please note however that different organizations may use different URLs. If your network may be blocking our services, you can compare the URLs you're blocking to the list above to see if the URLs are ours.

You will also need to ensure the following processes can run while logging in:

Minecraft.AdalServer.exe (Login)

If you are using SSL Decryption on a **Chromebook** any url that serves up certificates would need to be added to your bypass list. The article from Google has information [here](https://support.google.com/chrome/a/answer/6334001?hl=en&ref_topic=3504941#zippy=%2Chostname-allowlist-for-chrome-devices-using-chrome-extensions-and-apps-chrome-web-store%2Chostname-allowlist-for-chrome-devices-using-android-apps-google-play-store).

### What is the full list of domains that are in the wildcards?

The list of domains can change without notice, and some are CDNs which may be different regionally, so while we will attempt to keep this list up to date and complete, if possible we recommend you use the wildcards (*) above instead of managing specific sub-domains.

|  |  |

| --- | --- |

|  |  |

|  |  |

|  |  |

### Can we reduce the number of “game” related domains in the allow-list?

The Minecraft Education library uses the Microsoft owned services PlayFab and XForge to deliver library content. While we recommend allowing all xboxlive.com subdomains to help protect against future architecture changes such as additional authentication calls or the introduction of new CDNs, it is possible to limit the number of *.xboxlive.com services to just those currently used by XForge:

[https://xforge.xboxlive.com/](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fxforge.xboxlive.com%2F&data=04%7C01%7Cmicahm%40microsoft.com%7Cb2e0de427cc34d821f1108d76880adee%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637092774195972472%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C-1&sdata=0ZBPcUFcpp8WOLuiOWT8VcA96sIF%2Fg7Oz4zBdDH1Wio%3D&reserved=0)

[https://xforgeassets001.xboxlive.com/](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fxforgeassets001.xboxlive.com%2F&data=04%7C01%7Cmicahm%40microsoft.com%7Cb2e0de427cc34d821f1108d76880adee%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637092774195982464%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C-1&sdata=HN34sEANnzvJ2OOAxKOrCOgXxaMDxcPO4vrsCzj1o38%3D&reserved=0)

[https://xforgeassets002.xboxlive.com/](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fxforgeassets002.xboxlive.com%2F&data=04%7C01%7Cmicahm%40microsoft.com%7Cb2e0de427cc34d821f1108d76880adee%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637092774195982464%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C-1&sdata=yMhbmMW3bEZLtrE8%2Fmt9ox6WMtSgT7omEq254aIdVto%3D&reserved=0)

### Will allowing these URLs open my network to unwanted activity?

Minecraft Education only uses services from reputable sources that have been audited for compliance with all relevant security and privacy standards. The communications between Minecraft Education and these service endpoints is limited to data sharing between the application and the service and the services we use are generally not available for web traffic.

The xboxlive.com and playfabapi.com services connect Minecraft Education to our content hosting service which allows for much quicker access to our instructional content. Opening your network to these URLs will allow authenticated communication to all Xbox services hosted on xboxlive.com but does not allow access to public websites like xbox.com. If you are concerned about exposing too many services from xboxlive.com, it is possible to only allow XForge by following the previous questions' instructions.

### Do I need to forward any Ports for Minecraft Education?

Minecraft Education uses a WebRTC signaling service to establish peer-to-peer connections between clients for multiplayer. The establishment of the multiplayer session occurs over web sockets and UDP ports and then the actual peer-to-peer connection occurs over ephemeral ports. Most networks should not need any configuration to support this multiplayer environment but if you do need to configure ports and firewalls, the following information should be helpful:

The signaling connections use wss://signal.franchise.minecraft-services.net

The STUN and TURN connections use turn.azure.com / world.relay.skype.com on the 20.202.0.0 / 16 IP range using remote TCP port 443 and remote UDP ports 3478-3481

The peer-to-peer connections between host and joining client use local ephemeral UDP ports specified by the host client (the local port range is defined by the OS) and sent to the joining client via the signaling service

### What are the minimum required specs for devices to run Minecraft Education?

For the latest information on [system requirements, visit this article.](https://edusupport.minecraft.net/hc/en-us/articles/360047556591)

### How do I install Minecraft Education?

Visit these Help Center pages for information about installation:

The [Minecraft Education download page](https://education.minecraft.net/get-started/download/) contains links to versions for each supported device. See OS specific guides below:

[Windows Installation Guide](https://edusupport.minecraft.net/hc/en-us/articles/13106858087956)

[Chromebook Installation Guide](https://edusupport.minecraft.net/hc/en-us/articles/4404625978516)

[Mac Installation Guide](https://edusupport.minecraft.net/hc/en-us/articles/360047118792)

[iPad Installation Guide](https://edusupport.minecraft.net/hc/en-us/articles/4404623189652)

[Deploying and Updating Minecraft Education](https://edusupport.minecraft.net/hc/en-us/articles/360047118732-Deploying-and-Updating-Minecraft-Education-Edition-apps-all-platforms-) describes how to deploy the application manually or using system management software

You can deploy using **Intune to Macs** with the script located [here.](https://github.com/microsoft/shell-intune-samples/blob/master/Apps/Minecraft%20Education%20Edition/README.md)

Use this link to get the [Minecraft Education installer package](https://aka.ms/meeclientwin10)

### How do I update Minecraft Education?

View our [Update to a New Version of Minecraft Education Edition](https://edusupport.minecraft.net/hc/en-us/articles/360047705032) article for information about how Minecraft Education Edition updates and also how IT Admins can block these updates for greater control.

### Does Minecraft Education collect or store student data?

Minecraft Education uses Office 365 services for authentication, and does not collect or store any personal information within the application. The Office 365 platform is in full compliance with [COPPA, CIPA, and FERPA.](https://edusupport.minecraft.net/hc/en-us/articles/360047118972-COPPA-CIPA-and-FERPA-Information-) View our [User Privacy and Minecraft Education](https://edusupport.minecraft.net/hc/en-us/articles/360047118972) article for more information about.

You can also visit the [Microsoft Trust Center](https://www.microsoft.com/en-us/trust-center) for more information about privacy and security in Microsoft applications.

Was this article helpful?

Yes No

984 out of 1326 found this helpful

Have more questions? [Submit a request](https://edusupport.minecraft.net/hc/en-us/requests/new)

## Related articles

[Troubleshoot the Unable to Connect to World Error](https://edusupport.minecraft.net/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBR9GZ0BBDoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCJAKe9RTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJXL2hjL2VuLXVzL2FydGljbGVzLzQ0MDQ5NzcxNzE3MzItVHJvdWJsZXNob290LXRoZS1VbmFibGUtdG8tQ29ubmVjdC10by1Xb3JsZC1FcnJvcgY7CFQ6CXJhbmtpBg%3D%3D--278f32518890464fa33f8d816ae6857b68bf8c59)

[URLs Used by Minecraft Education](https://edusupport.minecraft.net/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBSxmJEBBDoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCJAKe9RTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJGL2hjL2VuLXVzL2FydGljbGVzLzQ0MDQ3ODQxODE1MjQtVVJMcy1Vc2VkLWJ5LU1pbmVjcmFmdC1FZHVjYXRpb24GOwhUOglyYW5raQc%3D--a892b70017c745f5e621b13e789d539fee971665)

[Troubleshoot the Can't Connect to the Service Error](https://edusupport.minecraft.net/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCJS%2BFZ0BBDoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCJAKe9RTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJZL2hjL2VuLXVzL2FydGljbGVzLzQ0MDQ5NzY5MjYzNTYtVHJvdWJsZXNob290LXRoZS1DYW4tdC1Db25uZWN0LXRvLXRoZS1TZXJ2aWNlLUVycm9yBjsIVDoJcmFua2kI--1f18a8e7056d953f5041f48919aa1490cc7e553b)

[Troubleshoot the Unable to Connect to the Library Error](https://edusupport.minecraft.net/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBR9sZwBBDoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCJAKe9RTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJdL2hjL2VuLXVzL2FydGljbGVzLzQ0MDQ5NzAzNTU5ODgtVHJvdWJsZXNob290LXRoZS1VbmFibGUtdG8tQ29ubmVjdC10by10aGUtTGlicmFyeS1FcnJvcgY7CFQ6CXJhbmtpCQ%3D%3D--b80c42ba4883fd84189a4e214b34f1178a473e69)

[Troubleshoot the Unable to Sign in Error Message](https://edusupport.minecraft.net/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBQlGp0BBDoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCJAKe9RTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJWL2hjL2VuLXVzL2FydGljbGVzLzQ0MDQ5NzcyMTQ3NDAtVHJvdWJsZXNob290LXRoZS1VbmFibGUtdG8tU2lnbi1pbi1FcnJvci1NZXNzYWdlBjsIVDoJcmFua2kK--e4d4fc471f2774c68c6532763a8f13565af6687c)

© 2026 Mojang AB. TM Microsoft Corporation.

[English (US)](https://edusupport.minecraft.net/hc/en-us/articles/360047118992-FAQ-IT-Admin-Guide)

 [Your Privacy Choices](https://aka.ms/YourCaliforniaPrivacyChoices)

[Consumer Health Privacy](https://go.microsoft.com/fwlink/?linkid=2259814)

[Privacy and cookies](http://go.microsoft.com/fwlink/?linkid=521839)

[Terms of use](https://aka.ms/meeterms)

[Trademarks](http://www.microsoft.com/trademarks)

[About our ads](http://choice.microsoft.com/)

[© 2026 Microsoft](https://www.microsoft.com/) 