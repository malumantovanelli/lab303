import sys
from cx_Freeze import setup, Executable

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Xlsx 2 Txt",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Xlsx 2 Txt.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}
build_exe_options = {"packages": ["os", "pandas", "threading", "sys"], "include_files": ["View\\", "Controle\\", "Util\\", "Model\\", "icone.ico"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Xlsx 2 Txt",
        version = "0.1",
        description = "Conversor de Xlsx para txt.",
        options = {"build_exe": build_exe_options,"bdist_msi": bdist_msi_options},
        executables = [Executable("Xlsx2Txt.py", base=base)])


