# Audio Navigation - Minecraft Mods - CurseForge

BrowseBrowse all (118)Minecraft

The Sims 4

World of Warcraft

Minecraft Bedrock

Ark Survival Ascended

Hytale

inZOI

StarCraft II

Kerbal Space Program

Stardew Valley

American Truck Simulator

Hogwarts Legacy

Terraria

WildStar

World of Tanks

Palworld

Runes of Magic

Rift

Hytale New Worlds Contest

[Create](https://links.curseforge.com/hytalecontest-menu)MOD AUTHORS

[Become an Author](https://links.curseforge.com/hytalecontest-menu)

[Start a Project](https://links.curseforge.com/hytalecontest-menu)

[Project Submission Guide](https://links.curseforge.com/hytalecontest-menu)

MODDING TOOL DEVELOPERS

[Apply for an API Key](https://links.curseforge.com/hytalecontest-menu)

[Documentation](https://links.curseforge.com/hytalecontest-menu)

[Terms & Conditions](https://links.curseforge.com/hytalecontest-menu)

SOCIAL

[Join Our Discord!](https://links.curseforge.com/hytalecontest-menu)

[Authors Discord](https://links.curseforge.com/hytalecontest-menu)

Hytale New Worlds Contest

[Studios](https://links.curseforge.com/hytalecontest-menu)GAME DEVELOPERS

[Unlock Modding for Your Game](https://links.curseforge.com/hytalecontest-menu)

[Documentation](https://links.curseforge.com/hytalecontest-menu)

Hytale New Worlds Contest

[Help Center](https://links.curseforge.com/hytalecontest-menu)

[Our Blog](https://links.curseforge.com/hytalecontest-menu)

[Surprise me](https://links.curseforge.com/hytalecontest-menu)

[Legacy](https://links.curseforge.com/hytalecontest-menu)

[Go Premium](https://links.curseforge.com/hytalecontest-menu)

[Get CurseForge App](https://links.curseforge.com/hytalecontest-menu)

[Werewolf web](https://links.curseforge.com/hytalecontest-menu)

# Audio Navigation

By[emassey0135](https://www.curseforge.com/members/emassey0135)

[Mods](https://www.curseforge.com/members/emassey0135)

### A mod that adds audio navigation features for the blind, inspired by Soundscape Audio NavigationDetails

### Downloads 191 Created 1 year ago Updated 4 months ago Project ID 1221330 License[GNU General Public License version 3 (GPLv3)](https://www.curseforge.com#license)Game Versions

### [1.21.10](https://www.curseforge.com#license)[1.21.5](https://www.curseforge.com#license)[1.21.4](https://www.curseforge.com#license)Mod Loaders

[Fabric](https://www.curseforge.com#license)

[NeoForge](https://www.curseforge.com#license)

### Categories

[Player Transport](https://www.curseforge.com#license)

[Utility & QoL](https://www.curseforge.com#license)

[Addons](https://www.curseforge.com#license)

[World Gen](https://www.curseforge.com#license)

[Structures](https://www.curseforge.com#license)

### Links

### [Source](https://www.curseforge.com#license)Main File

1.21.10

Audio Navigation 0.4.3 (Fabric) Latest release

B

1.21.10

Fabric

Oct 25, 2025

### Recent Files[View all](https://www.curseforge.com/minecraft/mc-mods/audio-navigation/files/all?page=1&pageSize=20&showAlphaFiles=hide&sortBy=dateCreated&sortOrder=desc)

Minecraft 1.21

Audio Navigation 0.4.3 (Fabric) Latest release

B

1.21.10

Fabric

Oct 25, 2025

Audio Navigation 0.4.3 (NeoForge) Latest release

B

1.21.10

NeoForge

Oct 25, 2025

Audio Navigation 0.4.0 (NeoForge) Latest release

B

1.21.5

NeoForge

Apr 10, 2025

[Description](https://www.curseforge.com/minecraft/mc-mods/audio-navigation/files/all?page=1&pageSize=20&showAlphaFiles=hide&sortBy=dateCreated&sortOrder=desc)

[Comments](https://www.curseforge.com/minecraft/mc-mods/audio-navigation/files/all?page=1&pageSize=20&showAlphaFiles=hide&sortBy=dateCreated&sortOrder=desc)

[Files](https://www.curseforge.com/minecraft/mc-mods/audio-navigation/files/all?page=1&pageSize=20&showAlphaFiles=hide&sortBy=dateCreated&sortOrder=desc)

[Gallery (11)](https://www.curseforge.com/minecraft/mc-mods/audio-navigation/files/all?page=1&pageSize=20&showAlphaFiles=hide&sortBy=dateCreated&sortOrder=desc)

[Relations](https://www.curseforge.com/minecraft/mc-mods/audio-navigation/files/all?page=1&pageSize=20&showAlphaFiles=hide&sortBy=dateCreated&sortOrder=desc)

[Issues](https://www.curseforge.com/minecraft/mc-mods/audio-navigation/files/all?page=1&pageSize=20&showAlphaFiles=hide&sortBy=dateCreated&sortOrder=desc)

add_landmark.png

## Description

# Audio Navigation

This is a Minecraft mod to add audio navigation features, mostly to make it easier for blind players to play the game. It is intended to complement, not replace, the [Minecraft Access](https://github.com/minecraft-access/minecraft-access) mod. Some features in this mod are inspired by [Microsoft Soundscape](https://github.com/microsoft/soundscape).

It runs on both Fabric and NeoForge (on both servers and clients), and the server-side component runs on Paper and Purpur as well.

## Dependencies

This mod runs on either Fabric, NeoForge, or Paper/Purpur, and depends on the following mods:

Fabric API (Fabric only)

Fabric Language Kotlin (Fabric only)

Kotlin for Forge (NeoForge only)

Architectury API (Fabric and NeoForge only)

Fzzy Config (Fabric and NeoForge only)

Eclipse (Paper and Purpur only)

Also, it uses a [native library](https://github.com/emassey0135/audio-navigation-tts) for speech synthesis, which is downloaded automatically on first launch. The library is compiled for Windows, MacOS, and Linux, for both x86_64 and aarch64. Create an issue if you use an unsupported operating system or architecture and I will try to add it. The mod verifies the hash of the downloaded file to make sure it downloads correctly. The native library is not downloaded or used on dedicated servers.

You can also download the library yourself from [the release page](https://github.com/emassey0135/audio-navigation-tts/releases/tag/0.3.1). Download the correct file for your operating system and architecture, place it in your .minecraft folder, and extract the espeak-ng-data folder from espeak-ng-data.zip and copy it into your .minecraft folder.

## Things to Know

This mod must be installed on both the client and server side, so if you are playing on a server, you must install it there as well as on your client. Also, points of interest for trees and other features will not be created unless you generate the world with this mod installed. If you travel into ungenerated chunks, it will save points of interest there, but once a chunk is generated it is too late to generate these POIs. Points of interest are stored in poi.db inside your .minecraft folder, or in the Minecraft server root if you are playing on a dedicated server. Deleting this file will delete all POIs.

## Current Features

Points of interest will be announced as you pass, according to the configured radius, vertical distance limit, and maximum number of announcements. You will hear the announcement from the direction of the point of interest, and a sound will be played before speaking the announcement based on the type of the POI.

When a point of interest is announced, its name is always spoken, and optionally its distance from you and its direction. The direction can also include the vertical component, and the horizontal component can be spoken using clock hands, direction and angle, just direction, just angle, or compass direction. The vertical component can be spoken as direction and angle, just direction, or just angle, either relative to the direction you are facing or the absolute direction.

When a world is generated, or when you travel into ungenerated chunks or trigger chunk generation in some other way, points of interest are created for features such as trees, ice spikes, end islands, ore vanes, etc. Structures like villages are coming soon.

You can announce all nearby points of interest by pressing F7. This has a larger radius, vertical limit, and maximum number of POIs than automatic announcements by default.

You can stop speech at any time by pressing F9.

You can create landmarks by pressing F6 to open the menu and pressing the "Add landmark" button. They are saved as points of interest and announced as you pass. You can choose whether the new landmark is visible to other players or not.

To delete a landmark, open the menu with F6, press "Landmarks", find the landmark you want to delete, and press the "Delete" button.

You can start an audio beacon on a landmark by opening the list of landmarks, finding the landmark you want, and pressing "Start beacon". This will start a continuous sound coming from the direction of the landmark that you can follow to find it. The sound will change depending on if you're facing it, facing away from it, or facing in the opposite direction.

By default, the distance and direction to a beacon will be announced every 30 seconds. You can change the amount of time, disable either distance or direction, or disable this entirely in settings.

To stop an audio beacon, open the menu with F6 and press "Stop beacon".

To announce the distance and/or direction to the current beacon, press F8.

The landmark list is filtered by radius. To increase the radius in which landmarks are shown, press enter on the current radius.

This mod is extremely configurable. To open the settings, press F6 to open the menu, and choose "Settings". From there, the configuration screen should be pretty intuitive to use.

This mod can use multiple speech synthesizers. eSpeak NG is always included. On Windows, SAPI 5 is also supported, and on MacOS the mod can use AVSpeechSynthesizer to use all Apple TTS voices as well as third-party voices exposed to the system TTS.

Since the list of voices is extremely long if all voices are included, it is filtered by synthesizer and language. When you open the synthesizers or languages list in speech settings, you can select one or multiple options, which will change how the voice list is filtered. By default all speech synthesizers are selected, but the current Minecraft language is the only selected language.

The beacon sounds in this mod are taken from Soundscape, so if you are familiar with Soundscape's beacon names, they are the same sounds. If not, you can start a beacon and change the sound while the beacon is running, and the sound will change when you change the setting.

# Server Configuration

On a dedicated server, you can set a maximum radius at which POIs will be sent to clients. You can also prevent certain features, such as ore veins, from being sent to clients, whether or not players enable them in client settings. On Fabric and NeoForge servers, these can be changed in config/audio_navigation/server_config.toml. On Paper and Purpur, change them in plugins/AudioNavigation/config.yml. You can also use the settings UI to change server settings on Fabric and NeoForge servers, by joining the world, pressing F6, pressing "Settings", then pressing "Server Settings".

## The Audio Navigation Team

[emassey0135](https://github.com/emassey0135/audio-navigation-tts/releases/tag/0.3.1)Owner

2 Projects

204 Downloads

## More from emassey0135

### [Audio Navigation (Paper)](https://github.com/emassey0135/audio-navigation-tts/releases/tag/0.3.1)

By emassey0135

13

Bukkit Plugins

A mod that adds audio navigation features for the blind, inspired by Soundscape (Paper plugin for server-side component)

13

April 3, 2025

Bukkit Plugins

+ 3

[View](https://github.com/emassey0135/audio-navigation-tts/releases/tag/0.3.1)[Download](https://github.com/emassey0135/audio-navigation-tts/releases/tag/0.3.1)

[Terms of Service](https://github.com/emassey0135/audio-navigation-tts/releases/tag/0.3.1)

[Privacy Policy](https://github.com/emassey0135/audio-navigation-tts/releases/tag/0.3.1)

[Licenses](https://github.com/emassey0135/audio-navigation-tts/releases/tag/0.3.1)

[Mod Author Terms](https://github.com/emassey0135/audio-navigation-tts/releases/tag/0.3.1)

©  2026 Overwolf. All rights reserved.