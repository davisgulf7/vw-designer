# Configuring LTI Integration with Moodle (Sandbox) - BetterExaminations Documentation

Configuring LTI Integration with Moodle (Sandbox) - BetterExaminations Documentation

### Help & Documentation

## Configuring LTI Integration with Moodle (Sandbox)

Connect your Moodle instance to the BetterExaminations sandbox environment to handle User and course provisioning as well as Grade Syncing

To configure an integration between BetterExaminations and Moodle, you must complete setup steps within BetterExaminations and within Moodle

First, configure the Integration in Moodle, and then complete the setup by adding the Integration in BetterExaminations.

BetterExaminations supports integrating with Moodle 3.9.x and above.

## Configuring the integration in Moodle

**1.** To configure an LTI integration in Moodle, select ' **Site administration**' on the left panel, then select ' **Plugins**' and select ' **External Tool**' ![](https://docs.betterexaminations.com/media/step 1-648x391.png)

**2.** Select ' **Manage tools**' ![](https://docs.betterexaminations.com/media/step 2-648x164.png)

**3.** Select ' **configure a tool manually**' ![](https://docs.betterexaminations.com/media/step 3-647x263.png)

**4.** There are a number of fields to configure. We have provided details of each section below. Please **read this carefully** and make sure to accurately copy and paste any information needed ![](https://docs.betterexaminations.com/media/step 4-648x214.PNG)

**Tool name:** You can input the name of your integration. This can be anything you like. We recommend naming your integration something like 'BetterExaminations Integration' so that its purpose is easily recognised.

**Tool URL:** Please copy and paste the following URL: **https://api.sandbox.betterexaminations.com/lti

Tool description:** This can be anything you like. We recommend providing a description that describes the purpose of your integration. For example: ' This tool is used to integrate Moodle with the BetterExaminations platform' ![](https://docs.betterexaminations.com/media/step 5-648x202.PNG)

**LTI version** - From the dropdown menu, **select LTI 1.3**

**Client ID:** This will be a pre-filled unique value that we will use in BetterExaminations. You can ignore this for now

**Public keyset:** Please copy and paste the following URL: **https://api.sandbox.betterexaminations.com/****.well-known**

**Initiate login URL:** Please copy and paste the following URL: **https://api.sandbox.betterexaminations.com/** **lti/moodle/login**

**Redirection URL(s):** Please copy and paste the following URL: **https://api.sandbox.betterexaminations.com/lti** ![](https://docs.betterexaminations.com/media/step 6-648x276.PNG)

**Custom parameters:** Leave this blank

**Tool configuration usage:** From the dropdown menu, select ' **Show in activity chooser and as a preconfigured tool**'.

**Default launch container:** From the dropdown menu, select ' **New Window**'

**Supports Deep Linking:** Please ensure to **tick 'Support Deep Linking (Content-Item Message)'**

**Content Selection URL**: Leave this blank

**5**. (Optional) Click on ' **Show more**' to reveal the Icon URL. This section allows you to add a BetterExaminations icon to your integration so that it is easy to identify ![](https://docs.betterexaminations.com/media/step 7-648x82.PNG)

**Icon URL:** Please copy and paste the following URL: **https://online.betterexaminations.com/static/media/be-logo-mini.c3fc13d0.svg**

**Secure icon URL:** Please copy and paste the following URL: **https://online.betterexaminations.com/static/media/be-logo-mini.c3fc13d0.svg**

**6**. Select ' **Services**' to open the services options and complete as follows ![](https://docs.betterexaminations.com/media/step 8-647x128.PNG)

**IMS LTI Assignment and Grade Services:** From the dropdown menu, select ' **Use this service for grade sync and column management'**

**IMS LTI Names and Role Provisioning:** From the dropdown menu, select ' **Use this service to retrieve members' information as per privacy settings**'

**Tool Settings:** From the dropdown menu, select ' **Do not use this service**'

**7**. Select ' **Privacy**' to open the privacy options and complete as follows ![](https://docs.betterexaminations.com/media/step 9-648x142.PNG)

**Share launcher's name with tool:** From the dropdown menu, select ' **Always**'

**Share launcher's email with tool:** From the dropdown menu, select ** 'Always'**

**Accept grades from the tool:** From the dropdown menu, select ** 'Always'**

**Force SSL:** Please tick this box

**8**. You do not need to complete the **Miscellaneous** section

**9.** Once you have completed all of the sections above, select ' **Save changes**'

**10.** You should now see your new integration listed under **Tools.** Locate your integration and select the options menu (as shown below) ![](https://docs.betterexaminations.com/media/step 11-281x366.png)

**11**. A popup will open containing **6 important pieces if information**. ![](https://docs.betterexaminations.com/media/step 12-648x258.png)

**Important: This is the information you will need to copy and paste into BetterExaminations during the configuration process.**

You will need this information to hand during the next stage of the process. We recommend you keep this window open and login to BetterExaminations in a new tab. This way you can easily switch between the two tabs and access the information you need.

**To continue**, open a new tab and login to BetterExaminations

## Configuring the integration in BetterExaminations

**1.** To add LTI integration to BetterExaminations, go to the Settings screen and scroll to the "LTI Integrations" section. You'll see a list of existing integrations (if you have any). You can configure a new integration by clicking the "Add integration" button on the right. ![](https://docs.betterexaminations.com/media/step 0-648x106.png)

**2.** Select your Platform from the list and then give your integration a name. This name is what will be shown to users throughout BetterExaminations so make sure to name it something meaningful for your users such as "Moodle" or "QA Moodle" etc. ![](https://docs.betterexaminations.com/media/step 1-648x263.png)

**3.** In the next stage you'll be asked to paste the values provided from Moodle in the first stage of the setup. Once all fields have been added, you can proceed to the next step. ![](https://docs.betterexaminations.com/media/step 2-648x366.PNG)

**4.** In this step you can decide which BetterExaminations User Role should be assigned to any Moodle Administrators when they use the LTI Integration. This step is optional, if you leave it blank Moodle administrators will be treated like standard users within BetterExaminations. ![](https://docs.betterexaminations.com/media/step 3-648x277.PNG)

**5.** The next step allows you to map LTI Context Roles to BetterExaminations Course Roles.

**NOTE:** The roles available for mapping are LTI context roles and NOT your Moodle course roles. This means Moodle is converting your Course roles into LTI context roles and then these context roles are then made available to map to BetterExaminations for mapping to BetterExaminations Course roles. Currently, Moodle converts **all** non-student roles to the LTI context role called "Instructor". Until Moodle supports role mapping ( [MDL-57315](https://tracker.moodle.org/browse/MDL-57315)) BetterExaminations will assign all non-student users the role you choose here. ![](https://docs.betterexaminations.com/media/step 4-648x277.PNG)

**6.** The final screen will display an overview to give you an opportunity to confirm all the options you've selected. Once you're happy, click " **Save changes**". ![](https://docs.betterexaminations.com/media/step 5-648x662.PNG)

That's it! Now BetterExaminations Online and Moodle are configured to use LTI.

On this page

[Configuring the integration in Moodle](https://docs.betterexaminations.com/betterexaminations-online/third-party-integrations/lti-integration/configuring-lti-integration-with-moodle-sandbox/#toc-configuring-the-integration-in-moodle)

[Configuring the integration in BetterExaminations](https://docs.betterexaminations.com/betterexaminations-online/third-party-integrations/lti-integration/configuring-lti-integration-with-moodle-sandbox/#toc-configuring-the-integration-in-betterexaminations)

Related articles

[Configuring LTI Integration with Blackboard](https://docs.betterexaminations.com/betterexaminations-online/third-party-integrations/lti-integration/configuring-lti-integration-with-blackboard/)

[Using the Blackboard LTI Integration](https://docs.betterexaminations.com/betterexaminations-online/third-party-integrations/lti-integration/using-the-blackboard-lti-integration/)

[Configuring LTI Integration with Moodle](https://docs.betterexaminations.com/betterexaminations-online/third-party-integrations/lti-integration/configuring-lti-integration-with-moodle/)

[Using the Moodle LTI Integration](https://docs.betterexaminations.com/betterexaminations-online/third-party-integrations/lti-integration/using-the-moodle-lti-integration/)

[Configuring LTI Integration with Canvas](https://docs.betterexaminations.com/betterexaminations-online/third-party-integrations/lti-integration/configuring-lti-integration-with-canvas/)

[Using the Canvas LTI Integration](https://docs.betterexaminations.com/betterexaminations-online/third-party-integrations/lti-integration/using-the-canvas-lti-integration/)

## BE Feedback Form

Let us know what you think about this article

There are some errors in your form.

Feedback *

Email *

Submit Reset

[Edit this page](https://websites.terminalfour.com/terminalfour/page/section#edit/12601/contents)

© [BetterExaminations](https://www.betterexaminations.com/) 2016-2026. All rights reserved.