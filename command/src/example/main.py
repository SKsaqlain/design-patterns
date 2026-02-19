import logging

from src.example.text_editor import TextEditor
from src.example.commands import InsertCommand, DeleteCommand
from src.example.command_manager import CommandManager

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def run():
    editor = TextEditor()  # receiver
    manager = CommandManager()  # invoker with undo/redo

    # Insert "Hello"
    manager.execute(InsertCommand(editor, "Hello"))
    # Insert " World"
    manager.execute(InsertCommand(editor, " World"))
    logger.info(f"Current text: '{editor}'")

    # Undo " World" → back to "Hello"
    manager.undo()
    logger.info(f"After undo: '{editor}'")

    # Redo " World" → back to "Hello World"
    manager.redo()
    logger.info(f"After redo: '{editor}'")

    # Delete last 5 chars ("World") → "Hello "
    manager.execute(DeleteCommand(editor, 5))
    logger.info(f"After delete: '{editor}'")

    # Undo delete → restores "Hello World"
    manager.undo()
    logger.info(f"After undo delete: '{editor}'")

    # Insert "!" → "Hello World!"
    manager.execute(InsertCommand(editor, "!"))
    logger.info(f"Final text: '{editor}'")


if __name__ == '__main__':
    run()
