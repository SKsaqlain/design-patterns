import logging

from src.example.command import Command

logger = logging.getLogger(__name__)


# Invoker — executes commands and manages undo/redo stacks
class CommandManager:
    def __init__(self):
        self.undo_stack = []  # commands that have been executed
        self.redo_stack = []  # commands that have been undone

    def execute(self, command: Command):
        command.execute()
        self.undo_stack.append(command)  # push onto undo history
        self.redo_stack.clear()  # new action invalidates redo history
        logger.info(f"Executed: {command.__class__.__name__}")

    def undo(self):
        if not self.undo_stack:
            logger.warning("Nothing to undo")
            return
        command = self.undo_stack.pop()  # most recent command
        command.undo()
        self.redo_stack.append(command)  # move to redo stack
        logger.info(f"Undone: {command.__class__.__name__}")

    def redo(self):
        if not self.redo_stack:
            logger.warning("Nothing to redo")
            return
        command = self.redo_stack.pop()  # most recently undone command
        command.execute()
        self.undo_stack.append(command)  # move back to undo stack
        logger.info(f"Redone: {command.__class__.__name__}")
