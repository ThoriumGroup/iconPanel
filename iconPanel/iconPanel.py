#!/usr/bin/env python
"""

Icon Panel
==========

A debug panel for Nuke that displays and provides location for every icon
in Nuke's icon folder.

## Classes

    IconPanel
        This is the icon panel itself, it displays the icon name, the icon
        itself, and the path to the icon for use.

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

# Standard Imports
import fnmatch
import os
import re

# Nuke Imports
try:
    import nuke
    import nukescripts
except ImportError:
    pass

# =============================================================================
# EXPORTS
# =============================================================================

__all__ = [
    'IconPanel'
]

# =============================================================================
# PRIVATE FUNCTIONS
# =============================================================================


def _find_files(directory, patterns):
    """Walks a directory recursively finding all files matching unix pattern.

    Args:
        directory : (str)
            The directory to search in.

        patterns : [str]
            A list of unix style patterns to search for. These should be the
            same patterns that fnmatch or glob would take, and not regex.

    Returns:
        [str]
            A list of filenames matching one of the patterns is returned. The
            filenames are relative to the directory we were given.

    Raises:
        N/A

    """
    matches = []
    pat = re.compile('|'.join(fnmatch.translate(grep) for grep in patterns))
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if pat.match(basename):
                filename = os.path.relpath(
                    os.path.join(root, basename),
                    directory
                )
                matches.append(filename)

    matches.sort()

    return matches

# =============================================================================
# CLASSES
# =============================================================================


class IconPanel(nukescripts.PythonPanel):
    """Displays the icon names, icons, and their paths"""

    def __init__(self):
        super(IconPanel, self).__init__(
            self,
            'Icon Debug Panel',
            'com.thorium.IconPanel'
        )

        self.icons = self.find_icons()
        self.batch = 30

        self.build_icon_list()

    # =========================================================================

    @staticmethod
    def build_icon_knob(icon):
        """Builds an individual icon knob

        Args:
            icon : (str)
                The icon filename relative to the icons directory.

        Returns:
            (<nuke.String_Knob>)
                A string knob with the filename and then the icon

        Raises:
            N/A

        """
        name = os.path.splitext(icon.split('/')[-1])[0]
        icon_string = '{name} <img src=":qrc/images/{icon}">'.format(
            name=name, icon=icon
        )
        icon_knob = nuke.String_Knob(icon, icon_string)
        icon_knob.setValue(icon_string)

        return icon_knob

    # =========================================================================

    def build_icon_list(self):
        """Builds the panel list of icons"""
        for i, icon in enumerate(self.icons):
            # Every time we hit the batch limit, we'll be creating a new tab
            counter = i % self.batch
            if counter == 0:
                tab = nuke.Tab_Knob(str(i), str(i))
                self.addKnob(tab)

            icon_knob = self.build_icon_knob(icon)
            self.addKnob(icon_knob)

    # =========================================================================

    @staticmethod
    def find_icons():
        """Finds all the icons in the Nuke icon folder"""
        nuke_dir = os.path.split(nuke.EXE_PATH)[0]
        icon_path = os.path.join(nuke_dir, 'plugins/icons')
        icons = _find_files(icon_path, ['*.png', '*.svg'])

        return icons