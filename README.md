kwin-fix-dual-screens
=====================

When I use a dual screen setup, I prefer to have independant virtual desktops on each screens, so if I change desktop or activities on my main screen the secondary one doesn't change.
KDE doesn't have that option, so I wrote this ugly hack.

I have very little knowledge of kwin and dbus, so there's probably a much better way to do this.

Limitations : the secondary screen can only have one effective virtual desktop

## How does it work

The kwinscript will set all the windows that come into the secondary screen in "allDesktop", the dbus service will do the same for activities.
When the window change to the primary screen the allDesktop and allActivities flags are cleared.

When you switchs virtual desktops your secondary screen will switch too, but since all desktops and all activities will share the same windows it will look as if the secondary screen is "fixed".

## Installation

git clone git@github.com:dromar56/kwin-fix-dual-screens.git
plasmapkg --type kwinscript -i kwin-fix-dual-screens
cp dbus-set-activities.py ~/.kde4/Autostart/

