# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "blender-auto-filepath",
    "author" : "Airyz",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from bpy.app.handlers import persistent


class AutoFilepathPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    mode: bpy.props.EnumProperty( items = [('RELATIVE','Relative','','',0), ('ABSOLUTE','Absolute','','',1)], name = "Mode",default = 'RELATIVE')

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "mode")

def handle_paths():
    mode = bpy.context.preferences.addons[__name__].preferences.mode

    if mode == "RELATIVE":
        print("Making paths relative")
        bpy.ops.file.make_paths_relative()

    if mode == "ABSOLUTE":
        print("Making paths absolute")
        bpy.ops.file.make_paths_absolute()

@persistent
def pre_save_handler(dummy):
    handle_paths()


def register():
    bpy.utils.register_class(AutoFilepathPreferences)
    bpy.app.handlers.save_pre.append(pre_save_handler)

def unregister():
    bpy.app.handlers.save_pre.remove(pre_save_handler)
    bpy.utils.unregister_class(AutoFilepathPreferences)
