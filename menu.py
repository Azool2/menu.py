# ShortcutChange https://www.nukepedia.com/python/ui/shortcut-editor/finishdown?miv=3&mjv=1
# Oben kann man das downloaden

try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
    import NukeServerSocket
    

    
    
except Exception:
    import traceback
    traceback.print_exc()

