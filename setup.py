from cx_Freeze import setup, Executable
# python setup.py build

setup(
    name = "Super snake",
    version = "0.1",
    description = "УДАЛИ МЕНЯ",
    # если приложение консольное то пишем - base=None
    # если приложение с графическим интерфейсом то пишем - base='Win32GUI'
    executables = [Executable("main.py", base='Win32GUI',icon="icone.ico")]
)