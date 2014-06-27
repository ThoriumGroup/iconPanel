#!/usr/bin/env python
"""

Icon Panel
==========

A debug panel for Nuke that displays and provides location for every icon
in Nuke's icon folder.

## Usage

This dockable panel can be instantiated from the Layout menu, by default it's
placed under the Pane submenu. Once you create the panel, you'll see the an
entry for every icon found.

Entries look like:
::
    icon_name ICON icon/path/icon.png

You can then use this path for assigning external_icons to menus, panels, etc.

## Installation

To install, simply ensure the 'iconPanel' directory is in your .nuke
directory or anywhere else within the Nuke python path.

Then, add the following lines to your 'menu.py' file:
::
    import iconPanel
    iconPanel.run()

## Public Functions

    run()
        Adds the iconPanel panel to the Layout Menu

## License

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

"""

# =============================================================================
# IMPORTS
# =============================================================================

# Nuke Imports
try:
    import nuke
    import nukescripts
except ImportError:
    pass

# animatedSnap3D Imports
from .iconPanel import IconPanel

# =============================================================================
# GLOBALS
# =============================================================================

__author__ = "Frank Rueter"
__author_email__ = "frank@ohufx.com"
__copyright__ = "Copyright 2010-2011 Frank Rueter"
__credits__ = ["Frank Rueter", "Sean Wallitsch", ]
__license__ = "MIT"
__version__ = "1.2b1"
__maintainer__ = "Sean Wallitsch"
__maintainer_email__ = "sean@grenadehop.com"
__module_name__ = "iconPanel"
__short_desc__ = "A panel for Nuke that displays and provides path for every icon"
__status__ = "Development"
__url__ = "http://github.com/ThoriumGroup/iconPanel"

# =============================================================================
# EXPORTS
# =============================================================================

__all__ = [
    'run',
    'IconPanel'
]

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================


def run():
    """Adds the iconPanel panel to the Layout Menu"""
    def add_icon_panel():
        global iconPanel
        iconPanel = iconPanel.IconPanel()
        return iconPanel.addToPane()

    pane_menu = nuke.menu('Pane')
    pane_menu.addCommand('Universal Icons', add_icon_panel)
    nukescripts.registerPanel('com.thorium.iconPanel', add_icon_panel)