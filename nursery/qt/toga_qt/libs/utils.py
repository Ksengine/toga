try:  # try import PySide2
    from PySide2.QtCore import qVersion
    GUI = 'pyside2'

except ImportError:
    try:  # try import PySide
        from PySide.QtCore import qVersion
        GUI = 'pyside'

    except ImportError:
        raise

_major, _minor, _micro = tuple(map(int, qVersion().split(".")[:3]))
QT_VERSION = (_major << 16) + (
    _minor << 8) + _micro  # fix version
QT_VERSION_STR = '{}.{}.{}'.format(
    _major, _minor, _micro)  # fix version string
