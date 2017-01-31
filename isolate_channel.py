""" Isolate the selected channel into a new container.

The plugin creates a new container with a copy of the selected data field and
all its related metadata.


Copyright (c) 2017 Tino Wagner

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import gwy
import gwyutils

plugin_menu = "/Plug-ins/Isolate channel"
plugin_desc = "Isolate channel"
plugin_type = "PROCESS"

def run(container, mode):
    data_field_id = gwy.gwy_app_data_browser_get_current(gwy.APP_DATA_FIELD_ID)
    data_field = container[gwy.gwy_app_get_data_key_for_id(data_field_id)]

    new_container = gwy.Container()
    gwy.gwy_app_data_browser_add(new_container)

    # Need to populate container with dummy data, otherwise
    # gwy_app_data_browser_copy_channel crashes.
    dummy_id = gwy.gwy_app_data_browser_add_data_field(
        data_field, new_container, False
    )
    new_id = gwy.gwy_app_data_browser_copy_channel(
        container, data_field_id, new_container
    )
    gwy.gwy_app_data_browser_select_data_field(new_container, new_id)

    # Get rid of dummy reference.
    new_container.remove_by_prefix('/{}/'.format(dummy_id))
