# Blender FLIP Fluids Add-on
# Copyright (C) 2021 Ryan L. Guy
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import bpy, os, sys

from . import version_compatibility_utils as vcu

IS_INSTALLATION_UTILS_INITIALIZED = False
IS_INSTALLATION_COMPLETE = False
IS_STABLE_BUILD = False

def is_installation_complete():
    global IS_INSTALLATION_UTILS_INITIALIZED
    global IS_INSTALLATION_COMPLETE

    if IS_INSTALLATION_UTILS_INITIALIZED:
        return IS_INSTALLATION_COMPLETE

    script_dir = os.path.dirname(os.path.realpath(__file__))
    addon_dir = os.path.dirname(script_dir)
    install_file = os.path.join(addon_dir, "resources", "installation_data", "installation_complete")

    if os.path.exists(install_file):
        IS_INSTALLATION_COMPLETE = True
    else:
        IS_INSTALLATION_COMPLETE = False

    IS_INSTALLATION_UTILS_INITIALIZED = True

    return IS_INSTALLATION_COMPLETE


def complete_installation():
    global IS_INSTALLATION_UTILS_INITIALIZED
    global IS_INSTALLATION_COMPLETE

    script_dir = os.path.dirname(os.path.realpath(__file__))
    addon_dir = os.path.dirname(script_dir)
    install_file = os.path.join(addon_dir, "resources", "installation_data", "installation_complete")

    if not os.path.exists(install_file):
        with open(install_file, 'w') as f:
            f.write("1")

    IS_INSTALLATION_COMPLETE = True
    IS_INSTALLATION_UTILS_INITIALIZED = True


def get_module_name():
    from ..properties import preferences_properties
    prefs = preferences_properties.get_addon_preferences()

    module_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    module_name = os.path.basename(os.path.normpath(module_dir))
    if prefs.enable_addon_directory_renaming:
        return module_name
    else:
        hardcoded_name = "flip_fluids_addon"
        if module_name != hardcoded_name:
            errmsg = "Installation Error Detected"
            errdesc = "The FLIP Fluids addon directory located at <" + module_dir + "> must be named 'flip_fluids_addon'. Please rename this directory, restart Blender, and re-enable the addon."
            bpy.ops.flip_fluid_operators.display_error(
                'INVOKE_DEFAULT',
                error_message=errmsg,
                error_description=errdesc,
                popup_width=600
                )
        return hardcoded_name


def get_enabled_flip_fluids_addon_installations():
    import addon_utils
    bl_prefs = vcu.get_blender_preferences()

    name_prefix = "FLIP Fluids"
    description_prefix = "A FLIP Fluid Simulation Tool for Blender"
    flip_fluids_installations = []
    for mod_name in bl_prefs.addons.keys():
        try:
            module = sys.modules[mod_name]
            name = module.bl_info.get('name', "")
            description = module.bl_info.get('description', "")
            if name.startswith(name_prefix) and description.startswith(description_prefix):
                d = {}
                d['module_name'] = mod_name
                d['addon_name'] = name
                flip_fluids_installations.append(d)
        except:
            pass

    return flip_fluids_installations


def is_experimental_build():
    global IS_STABLE_BUILD
    return not IS_STABLE_BUILD
