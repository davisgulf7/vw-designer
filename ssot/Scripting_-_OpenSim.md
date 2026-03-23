# Scripting - OpenSim

Atlassian uses cookies to improve your browsing experience, perform analytics and research, and conduct advertising. Accept all cookies to indicate that you agree to our use of cookies on your device. [Atlassian cookies and tracking notice , (opens new window)](https://www.atlassian.com/legal/cookies)OpenSim[OpenSim Documentation](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[User's Guide](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[User's Guide](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Download](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[Download](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Examples & Tutorials](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[Examples & Tutorials](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Forum](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[Forum](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Upcoming Events](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[Upcoming Events](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[OpenSim Fellows](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[OpenSim Fellows](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

Results will update as you type.

[Getting Started](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Documentation](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[User's Guide](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Theory and Publications](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Developer Pages](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Scripting and Development](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[Introduction to the OpenSim API](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Scripting](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)[Common Scripting Commands](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Scripting Versions of OpenSim C++ API Calls](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Scripting in the GUI](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Scripting with Matlab](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Scripting in Python](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Guide to Using Doxygen](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Developer's Guide](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Examples and Tutorials](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Troubleshooting](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Models, Data, & Utilities](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Teaching Hub](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[See the Work](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

[Join the Community](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/overview?homepageId=53084162)

# You‘re viewing this with anonymous access, so some content might be blocked. / Scripting[Updated Sept 06, 2018](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/history/53089359)Scripting

By Jennifer Hicks Sept 06, 2018

Scripting allows you to access OpenSim's functionality through the following programming languages:

The scripting shell in the OpenSim GUI (which is a Jython interpreter embedded in the application)

Matlab

Python

In other words, you can access OpenSim's Application Programming Interface without compiling your code in C++.

## What's available?

With OpenSim scripting, you can:

Run tools from setup files or programmatically.

Perform batch processing of common workflows (e.g., inverse kinematics, computed muscle control, EMG-driven simulation).

Utilize the OpenSim API without the overhead of learning to program in C++ and setting up a development environment.

Write "main" programs similar to those written by C++ developers, while taking advantage of the many open-source Matlab/Python packages for data processing, statistics, machine learning, etc. 

Access common SimTK/Simbody numeric types (e.g., Vec3, Vector, Mat33, State, Inertia) and a limited subset of Simbody multibody calculations.

Access the OpenSim API to create and simulate models.

Use the Simbody visualizer.

## Limitations

In general, you cannot create new components (e.g., a custom muscle; though there are some exceptions).

You cannot create plugins for use through the GUI or command-line.

In Matlab/Python, there’s no access to OpenSim's plotter (use Matlab/Python native plotter) or visualizer (use the Simbody visualizer).

Many SimTK/Simbody classes (that belong to the SimTK namespace and simbody internals) are not available (e.g., integrators).

The sections below outline how to get started with scripting and describe the available functionality.

[Common Scripting Commands](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/history/53089359)

[Scripting Versions of OpenSim C++ API Calls](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/history/53089359)

[Scripting in the GUI](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/history/53089359)

[Scripting with Matlab](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/history/53089359)

[Scripting in Python](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/history/53089359)[Conda Package](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/history/53089359)

Next: [Common Scripting Commands](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/pages/53089391/Common+Scripting+Commands)

Previous: [Guide to Using Doxygen](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/pages/53089363/Guide+to+Using+Doxygen)

Home: [Scripting and Development](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/pages/53089342/Scripting+and+Development)

{"serverDuration": 45, "requestCorrelationId": "45b61bc2ecd64b479ac0b0d0fe65a0fa"}  