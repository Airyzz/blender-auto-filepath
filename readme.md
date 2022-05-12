## Blender Auto Filepath

### A simple plugin to enforce a specific type of filepath for referenced files
---
This plugin will automatically convert all referenced file paths to be either relative to the current .blend file, or absolute, every time the file is saved. 


This can be useful as in some cases, such as linking from the Asset Browser, Blender defaults to absolute file paths, when it may be preferable to use relative paths.

The filepath mode can be selected in the addon preferences, as either 'Relative' or 'Absolute'