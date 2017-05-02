""" Export all channels in the currently active container into a subfolder.

The plugin creates a new folder with the same basename as the active file and
`OUTPUT_SUFFIX` appended, where it exports all datafields of the active
container. The exported files follow the scheme `###_TITLE.OUTPUT_SUFFIX`, where
`###` is the datafield id and `TITLE` its title. The export dialog is shown for
the first datafield, and the same settings are used for further exports.


Copyright (c) 2017 Tino Wagner

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
import os
import gwy

plugin_menu = "/Plug-ins/Export all channels"
plugin_desc = "Export all channels"
plugin_type = "PROCESS"

OUTPUT_SUFFIX = '-out'
OUTPUT_FILESUFFIX = 'png'

def run(container, mode):
    container = gwy.gwy_app_data_browser_get_current(gwy.APP_CONTAINER)
    filename = container['/filename']
    path, _ = os.path.splitext(filename)
    output_path = path + OUTPUT_SUFFIX
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for i, id_ in enumerate(gwy.gwy_app_data_browser_get_data_ids(container)):
        title = container['/{}/data/title'.format(id_)]
        gwy.gwy_app_data_browser_select_data_field(container, id_)
        output_filename = '{:03d}_{}.{}'.format(id_, title, OUTPUT_FILESUFFIX)
        output_filename = os.path.join(output_path, output_filename)
        mode = gwy.RUN_INTERACTIVE if i == 0 else gwy.RUN_NONINTERACTIVE
        print 'Exporting {} ...'.format(output_filename)
        gwy.gwy_file_save(container, output_filename, mode)
