# ~/Library/Application Support/Anki2/addons21/copy-noteid-plugin

from aqt import mw
from aqt.utils import showInfo, qconnect, tooltip
from aqt.qt import *
from aqt.reviewer import Reviewer
import platform  

def onReviewShortcut():
    # Check if the current state is reviewing (showing a card)
    if mw.state == 'review':
        card = mw.reviewer.card # Get the current card
        if card:
            note_id = str(card.nid)
            QApplication.clipboard().setText(note_id)
            tooltip(f"Note ID {note_id} copied to clipboard.", period=1000)

def addShortcut():
    shortcut = QAction("Copy Note ID", mw)
    shortcut.setShortcut(QKeySequence("Ctrl+9"))
    # shortcut.triggered.connect(onReviewShortcut) 
    qconnect(shortcut.triggered, onReviewShortcut)
    mw.form.menuTools.addAction(shortcut) # add to the tools menu

addShortcut()
