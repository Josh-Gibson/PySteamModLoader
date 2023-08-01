  # PySteamModLoader
A clunky mod loader for Ravenfield in Steam

This is a janky build of a mod manager for Ravenfield.

![mod](https://github.com/Josh-Gibson/PySteamModLoader/assets/22622013/19ddd864-5193-4cb7-bda4-fcad6caa39a4)

<b>Situation:</b>
- Ravenfield loads in all mods at once. This becomes a problem when someone (such as myself) has downloaded several, several mods, and they are all loaded up in the RAM. This makes the game slow and choppy, and not the most fun to play

<b>Solution:</b>
- I created this little python script to manually move the mods so that the game won't recognize where they are and won't load them. Thus, I can select specifically which mods I want without loading every single one.

<b>How it works:</b>

In the Ravenfield game mods foldier, I added another one called "saved." Steam doesn't recognize it as a mod, so it bypasses the contents inside. This allows me to put unwanted mods inside it so that they won't be loaded.
Using shutil.move, I can copy and move the mod folders in and out of the saved folder. I also added PyQt5 for some quick useful GUI.

Originally this was all done in the command line. With PyQt5, I was able to create a basic application that makes the process much faster.

<b>Dependencies:</b>
- This was coded in core python, but PyQt5 is the only external dependency

