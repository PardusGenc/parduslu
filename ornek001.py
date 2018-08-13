#! /usr/bin/env python3

import locale
from dialog import Dialog

# This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

# You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
d = Dialog(dialog="dialog")
# Dialog.set_background_title() requires pythondialog 2.13 or later
d.set_background_title("Basit bir program")
# For older versions, you can use:
#   d.add_persistent_args(["--backtitle", "Basit bir program"])

# In pythondialog 3.x, you can compare the return code to d.OK, Dialog.OK or
# "ok" (same object). In pythondialog 2.x, you have to use d.DIALOG_OK, which
# is deprecated since version 3.0.0.
if d.yesno("Detayları görmek istiyor musun?") == d.OK:
    d.msgbox("Peki o zaman...")

    # We could put non-empty items here (not only the tag for each entry)
    code, tags = d.checklist("Tercihini yap?",
                             choices=[("Kedi", "",             False),
                                      ("Köpek", "",            False),
                                      ("At", "",              False),
                                      ("Kuş", "",         True),
                                      ("Aslan","",        True),
                                      ("Pardus", "", True)],
                             title="Hangilerini tercih edersin?",
                             backtitle="Öylesine şeyler "
                             "completely different...")
    if code == d.OK:
        # 'tags' now contains a list of the toppings chosen by the user
        pass
else:
    code, tag = d.menu("OK, o zaman iki seçeneğin var:",
                       choices=[("(1)", "Çıkabilirim"),
                                ("(2)", "Çıkabilirim")])
    if code == d.OK:
        # 'tag' is now either "(1)" or "(2)"
        pass
