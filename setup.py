#!/user/bin/env python3

from distutils.core import setup 
import py2exe 
import sys, os, site, shutil

site_dir = site.getsitepackages()[1] 
include_dll_path = os.path.join(site_dir, "gnome") 

gtk_dirs_to_include = ['etc', 'lib\\gtk-3.0', 'lib\\girepository-1.0', 'lib\\gio', 'lib\\gdk-pixbuf-2.0', 'share\\glib-2.0', 'share\\fonts', 'share\\icons', 'share\\themes\\Default', 'share\\themes\\HighContrast'] 

gtk_dlls = [] 
tmp_dlls = [] 
cdir = os.getcwd() 
for dll in os.listdir(include_dll_path): 
    if dll.lower().endswith('.dll'): 
        gtk_dlls.append(os.path.join(include_dll_path, dll)) 
        tmp_dlls.append(os.path.join(cdir, dll)) 

for dll in gtk_dlls: 
    shutil.copy(dll, cdir) 

# -- change main.py if needed -- #
setup(windows=['main.py'], options={ 
    'py2exe': { 
        'includes' : ['gi'], 
        'packages': ['gi'] 
    } 
}) 

dest_dir = os.path.join(cdir, 'dist') 

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for dll in tmp_dlls: 
    shutil.copy(dll, dest_dir) 
    os.remove(dll) 

for d  in gtk_dirs_to_include: 
    shutil.copytree(os.path.join(site_dir, "gnome", d), os.path.join(dest_dir, d))
