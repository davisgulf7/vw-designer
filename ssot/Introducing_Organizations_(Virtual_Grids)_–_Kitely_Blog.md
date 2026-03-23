# Introducing Organizations (Virtual Grids) – Kitely Blog

 Skip to content Kitely Blog

## Recent Posts

## Recent Comments

## Archives

## Meta

# Introducing Organizations (Virtual Grids)

We’re excited to introduce the biggest addition to Kitely since Kitely Market: **Organizations**. Organizations are a way to create a virtual grid inside Kitely. Use our new offering to take advantage of Kitely’s robustness and advanced management tools and avoid having to deal with the technical complexity of running a standalone grid.

Organizations enable you to create and manage your own users, with precise control over which worlds they can visit and what they can do in-world. They provide administrative capabilities that enable you to manage groups of users and worlds with unprecedented ease.

Kitely’s Organizations are designed for companies, educators, roleplaying groups, and any other collection of people that has its own members and needs to control what they can do in-world.

### Types of Organizations

We offer three types of organizations:

**Starter Organizations** – can have up to 100 users and 10 worlds, for $49.95/month.

**Standard Organizations** – can have up to 400 users and 40 worlds, for $99.95/month. This type of organization can use advanced features that aren’t available to Starter Organizations.

**Custom Organizations** – contact us to discuss your needs if they aren’t met by our Standard Organizations. This option can include custom features.

The prices listed above include the Organization and its users, but not the worlds that you manage using the Organization. Those have to be paid for separately.

Some organizations (e.g., schools) aren’t active year-round. To save on costs, we allow Organizations to be **Stored**. A Stored Organization is disabled, and its price is reduced by 50%. This reduced price is paid daily, using KC, until the account is switched back to active mode.

### How to Create an Organization

The [Settings](https://www.kitely.com/settings) page has a new section called “Organizations (Virtual Grids)”. This section lets you create an Organization. 

An Organization has a **Name** and a **Short Name.** The Short Name is used in the Organization’s domain names: its Admin Console and Grid URI.

For example, here’s how to create an Organization called “Durion School of Wizardry”:

The Kitely user that creates the Organization becomes its **owner**. The owner pays for the Organization, and if the owner’s account is deleted then the Organization is also deleted. Therefore, if you’re creating an Organization that matches a real-world organization such as a school or a company then consider creating a special Kitely user just to own the Organization. This way, if you leave the real-world organization then you can transfer control of this Kitely user to a co-worker.

### Admin Console And Private Virtual Grid

Each Organization gets the following:

**Admin Console** – a website where the Organization’s administrators can manage the Organization: its users, worlds, permissions, etc. (This is not a public website for the Organization’s regular users: it’s only used by the Admins.)

**Private Virtual Grid** – a private grid that runs inside Kitely. This is a “Virtual” grid because it uses the same servers as the main Kitely grid. But it has its own Grid URI, and the Admins can control who may visit the grid’s (Organization’s) worlds.

For example, suppose you created an Organization whose Short Name is **durion**. Then the organization’s URLs would be:

**Admin Console** – https://**durion**.kitely.org

**Grid URI** – grid.**durion**.kitely.org:8002

This is what the Admin Console looks like (this is the Dashboard):

This is what the grid looks like in Firestorm:

### Adding Users

Organizations can have two types of users:

**Managed Users** – users that are created by the Organization. The Organization Admins have full control over these users. Managed Users can’t login to the main Kitely website.

**Independent Users** – regular Kitely users who have agreed to join the Organization. The Admins only control what Independent Users do when they’re visiting the Organization’s worlds. However, the Admins can’t control what Independent Users do outside the Organization.

Typically, an Organization will have only a handful of Independent Users, and many Managed Users. An Organization probably has a list of students/employees that should be given access to the Organization, and one of the Admins will create accounts for all of these users. To make this process easier, you can create multiple Managed Users at once by uploading their details in a CSV file. This process is called [Batch Create Users](https://kitely.atlassian.net/wiki/spaces/doc/pages/600866826/Batch+Create+Users).

Admins have full control over **Managed Users**. Admins can:

Create and delete Managed Users

Choose which avatars they can use (their appearance) 

Control which worlds they can visit

View the worlds that they visited

Prevent them from uploading assets into the system

To add **Independent Users**, Admins send them an invitation by email. If the invited user clicks on the link in the invitation then they become a member of the Organization. Independent Users can be members of an unlimited number of Organizations, and they can cancel those memberships from the Settings page in their Kitely account.

You can manage the Organization’s users in the Users page of the Admin Console:

You can view and edit all of the properties of Managed Users:

### Adding Worlds

All worlds must be owned by an Independent User that is a member of the Organization. The user **assigns** a world to the Organization in the world’s Manage World dialog:

Since the world owner is an Independent User, they can remove the world from the Organization at any time. So make sure that the Organization’s most important worlds are owned by yourself, by the Kitely account in which you created the Organization, or by someone you trust…

When a world is assigned to an Organization, any Estate Managers it had are removed and the Organization’s Admins become Estate Managers in the world. This gives the Admins extensive permissions in the world. When a world is removed from an Organization, the Organization’s Admins stop being its Estate Managers.

 You can manage worlds in the Worlds page of the Admin Console: 

You can optionally set one of the Organization’s worlds as the **Default World**. This world should be open to visits from all of the users in the Organization. When users login to your Organization’s virtual grid for the first time (without specifying which world they want to visit), they enter the Default World. Users also enter the Default World if they try to visit a world that has been deleted, or that they don’t have permission to visit.

In addition, anyone that tries to teleport to your Organization’s Grid URI without specifying a world will enter the Default World (assuming they have permission to visit it, of course).

### Managing Permissions Using Groups

Users and worlds belong to **Groups**. Permissions are assigned to User Groups. These permissions determine which worlds the users can visit, and whether they’re allowed to upload assets.

For example, consider a school called the “Durion School of Wizardry”. The school offers three courses: Divination, Enchantment and Potions. Only students that are enrolled in a course are allowed to visit the course’s classrooms (virtual worlds).

You can implement this scheme in your Organization as follows:

Create three **User Groups**: Divination, Enchantment and Potions. Add the users that are enrolled in each course to the corresponding User Group.

Create three **World Groups**, also called Divination, Enchantment and Potions. The World Groups contain the worlds that are used to teach each of the courses.

Give each User Group permission to visit the corresponding World Group.

Here’s what the Users Groups hierarchy looks like (we’ve included some other groups, too):

The number in parentheses after each User Group is the number of users in that Group.

And here’s what the World Groups hierarchy looks like:

The number in parentheses after each World Group is the number of worlds in that Group.

Here are the permissions that were set on one of the User Groups:

The permissions in this screenshot show that users that belong to the “Divination” User Group are allowed to visit worlds in the “Divination” World Group. However, they’re not allowed to upload assets.

What about teachers? We want them to be allowed to visit any classroom (even if it’s not their own). So the Teachers User Group gets permission to visit the top-level group “Classrooms”. This automatically allows them to visit the worlds that are included in the World Groups below “Classrooms” in the World Groups hierarchy. In addition, teachers are allowed to upload assets:

If you view the permissions tab of a World Group then you can see the reverse permissions, i.e. which User Groups are allowed to visit that World Group:

If you want to verify that you’ve set the permissions correctly then choose any user and view their permissions. This shows you which worlds they can visit. You can also click on the “i” icon to see an explanation of why they have (or don’t have) the specified permission.

### External Users and Worlds

Because Organizations are Virtual Grids inside Kitely, external users (users that don’t belong to the Organization) can visit the Organization’s worlds directly (without having to use the Hypergrid). However, you control which worlds (if any) external users can visit. You do this by giving (or withholding) permission for the “External Users” group to visit your worlds.

Likewise, your Managed Users can visit external worlds in Kitely without having to use the Hypergrid. But again, you choose whether to allow this, by giving (or withholding) permission for your users to visit worlds in the “External Worlds” group. Note that if you do allow your users to visit External Worlds then they can visit any external world: you can’t control precisely which external worlds they can visit.

Finally, you can choose to allow (or prevent) Hypergrid users to visit your Organization, and/or for your Managed Users to visit worlds in the Hypergrid.

### World Visits

You can view every world visit made in your Organization in the Visits page. This includes visits made to your Organization’s worlds (even visits by external users), and all visits made by your Managed Users (even visits to external worlds in Kitely, but not visits to Hypergrid regions outside Kitely). Visits that are currently active are highlighted.

### History

You can view a detailed list of changes that were made to the Organization in the History page. Many of the history events can be clicked to get additional information.

If your Organization has multiple Admins then there will likely be times when you’ll want to know who made changes to your Organization. This information is shown in the “Requested By” column.

You can export the History table to a CSV file.

### Avatars

You can choose which initial avatars your Managed Users can use. A new Organization gets two sets of default avatars:

7 avatars that are identical to the default Kitely avatars. These avatars can change all of their clothes, including their underwear.

6 avatars that have a similar visual style to the Kitely avatars, but have underwear that is part of their skin layer (so they can’t get fully naked by taking off all their clothes).

You’ll probably only want to use one of these sets, but not both. For example, the Durion School of Wizardry has chosen to use only the non-naked avatars, so they’re the only ones that are enabled in the screenshot below. (You can delete avatars that you don’t need, but you might want to just disable them, as this gives you the option of enabling them in the future.)

The picture button lets you upload an image for the avatar: this is the image that your users see when they choose their avatar. The arrow buttons change the order in which the avatars appear. 

You can add your own custom avatars to this list by copying the current appearance of your own avatar, or that of any of the Organization’s Managed Users. You can’t copy the appearance of any Independent User, however (except yourself).

### The Setup Kitely Program

**Setup Kitely** is a program whose purpose is to help the Organization’s users, who might never have heard of OpenSim, visit the Organization’s worlds for the first time.

Setup Kitely runs on Windows and Mac computers. It helps the users download the correct version of Firestorm for their computer; add your Organization’s Virtual Grid to Firestorm; choose their avatar; and enter one of the Organization’s worlds.

For example, here’s the avatar selection page of Setup Kitely:

Setup Kitely’s ability to add your Virtual Grid to Firestorm is particularly useful, because adding grids is a highly technical operation that many people, especially ones new to OpenSim, encounter problems with.

Learn more about Setup Kitely here.

Regular Kitely users (that don’t belong to an Organization) can also run Setup Kitely, but its only benefit is to change their avatar to one of the default avatars that we offer.

### Kitely Market

Since Organizations are Virtual Grids inside Kitely, you can use non-exportable items from Kitely Market in the Organization’s worlds and avatars.

Managed Users can’t use Kitely Market because they can’t login to the main Kitely website. So if you want a Managed User to get items from Kitely Market then one of the organization’s Independent Users will have to buy the items themselves, and deliver them to the Managed User from Kitely Market as a gift.

### This is Just the Beginning

While Kitely Organizations already provide you with many advanced tools for managing a virtual grid, this is just the initial launch of the service. We consider this new offering to be an important part of our future business and will continue adding many features to it in the foreseeable future.

Some of our features are considered **Advanced Features**, and are only available to Standard Organizations and Custom Organizations (but not to Starter Organizations). Currently, the following Advanced Features have been implemented:

Batch create users by uploading a CSV file

Download History reports as a CSV file

Use filters to search History and Visits

**Update June 14, 2019:** Customize the viewer login page (what appears in Firestorm before you login)

**Update June 14, 2019:** An API for managing the Organization (in [Private Beta](https://www.kitely.com/virtual-world-news/2019/06/14/custom-viewer-login-page-and-kitely-api-beta/)) 

Upcoming Advanced Features include:

A tool to help you transfer content ownership between users in your Organization

Use your own domain name for the Organization

If you encounter any issue with our service, want to give us feedback about it, or have followup questions then please [let us know in our forums](https://www.kitely.com/forums/viewforum.php?f=45).

Try an Organization now risk-free with our 14-day money back guarantee. [Order Now](https://www.kitely.com/?g_createorg=1)

## Published by

### Oren Hurvitz

 Oren Hurvitz is the Co-Founder and VP R&D of Kitely. [ View all posts by Oren Hurvitz ](https://www.kitely.com/virtual-world-news/author/orenh/)