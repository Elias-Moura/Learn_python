import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["pandas", "numpy", "requests", "openpyxl", "datetime", "lxml"]}

# GUI applications require a different base on Windopipws (the default is for
# a console application).
#base = None
#if sys.platform == "win32":
#   base = "Win32GUI"

setup(
    name="Coleta FII-teste",
    version="0.1",
    description="Busca os dados de FII's e gera uma tabela em excel",
    options={"build_exe": build_exe_options},
    executables=[Executable("coletaFii.py")]
)