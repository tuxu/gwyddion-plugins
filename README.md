# gwyddion-plugins

This is my collection of a few handy plugins for the
[SPM](https://en.wikipedia.org/wiki/Scanning_probe_microscopy) image processing
tool [Gwyddion](http://gwyddion.net/).

## Installation

- Copy plugin files into `~/.gwyddion/pygwy/`.

## Plugin descriptions

### `export_all_channels.py`

- **Menu**: `Plug-ins/Export all channels`
- **Short description**: Export all channels in the currently active container
  into a subfolder.
- **Description**: The plugin creates a new folder with the same basename as the
active file and `OUTPUT_SUFFIX` appended, where it exports all datafields of the
active container. The exported files follow the scheme
`###_TITLE.OUTPUT_SUFFIX`, where `###` is the datafield id and `TITLE` its
title. The export dialog is shown for the first datafield, and the same settings
are used for further exports.

## License

This project is licensed under the MIT license.

© 2017 [Tino Wagner](http://www.tinowagner.com/)
