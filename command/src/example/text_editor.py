import logging

logger = logging.getLogger(__name__)


# Receiver — holds the document text and performs actual operations
class TextEditor:
    def __init__(self):
        self.text = ""

    def insert(self, content):
        self.text += content  # append content to the end
        logger.info(f"Inserted: '{content}' → text is now: '{self.text}'")

    def delete(self, count):
        removed = self.text[-count:]  # grab the last N characters
        self.text = self.text[:-count]  # trim them off
        logger.info(f"Deleted: '{removed}' → text is now: '{self.text}'")
        return removed

    def __str__(self):
        return self.text
