Icon Panel
==========

- **Author:** Frank Rueter
- **Maintainer:** Sean Wallitsch
- **Email:** sean@grenadehop.com
- **License:** MIT
- **Status:** Development
- **Python Versions:** 2.6-2.7
- **Nuke Versions:** 6.3 and up

A debug panel for Nuke that displays and provides location for every icon
in Nuke's icon folder.

Usage
-----

This dockable panel can be instantiated from the panes menu, under the submenu
'Panes' where you find the 'Nodes' panel. Once you create the panel, you'll
see the an entry for every icon found.

Entries are split into *External icons* and *Internal icons*. External icons
can be found on disk in the `plugins/icons` folder, and mostly contain toolbar
icons. Internal icons are built into Nuke, and aren't found on disk at all.

Entries look like:
::
    icon_name ICON <knob text>

You can then use this path for assigning external_icons to menus, panels, etc.

Installation
------------

To install, simply ensure the 'iconPanel' directory is in your .nuke
directory or anywhere else within the Nuke python path.

Then, add the following lines to your 'menu.py' file:
::
    import iconPanel
    iconPanel.run()

Changelog
---------

*New in version 1.2:*

- Adds external icons.
    - Icons found within Nuke's `plugins/icons/` directory are now under the 'External Icons' tab.
    - Added syntax for including external icons in knobs.
    - External icons are alphabetical, with the tab name displaying the first two letters as opposed to index of icon.
- Internal icons can now be found under the 'Internal Icons' tab.
- Refactoring

License
-------

The MIT License (MIT)

    iconPanel
    Copyright (c) 2010-2011 Frank Rueter

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
