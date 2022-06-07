from actor import Actor


class Artifact(Actor):
    """An item that can be caught.
    
    The responsibility of an Artifact is to provide a score when caught.

    Attributes:
        _score (int): A score that adds or subtracts.
    """
    def __init__(self):
        super().__init__()
        self._score = ""
        
    def get_score(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._score
    
    def set_score(self, score):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._score = score
       