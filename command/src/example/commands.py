import logging

from src.example.command import Command
from src.example.text_editor import TextEditor

logger = logging.getLogger(__name__)


# Concrete Command — inserts text; undo deletes the same amount
class InsertCommand(Command):
    def __init__(self, editor: TextEditor, content: str):
        self.editor = editor
        self.content = content

    def execute(self):
        self.editor.insert(self.content)

    def undo(self):
        self.editor.delete(len(self.content))  # remove exactly what was inserted


# Concrete Command — deletes N chars; undo re-inserts them
class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, count: int):
        self.editor = editor
        self.count = count
        self.deleted_text = ""  # saved on execute so undo can restore it

    def execute(self):
        self.deleted_text = self.editor.delete(self.count)

    def undo(self):
        self.editor.insert(self.deleted_text)  # put back exactly what was removed
