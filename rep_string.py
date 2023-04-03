class RepString:
    def __init__(self, s='') -> None:
        self.txt = str(s)

    def __len__(self) -> int:
        return len(self.txt)

    # 
    # 
    def capitaliz(self):
        """
        Returns a copy of the string with the first character capitalized and the rest lowercased.
        
        Args:
            None.
        Returns:
            String object.
        """
        temp_string = ''
        if len(self.txt) > 0:
            temp_string = chr(ord(self.txt[0]) - 32) + self.txt[1:]
        return temp_string

    def upper(self):
        """
        Return a copy of the string with all the character in upper case.
        Args:
            None.
        Returns:
            String object.
        """
        temp_string = ''
        for character in self.txt:
            if 'a' <= character <= 'z':
                temp_string += chr(ord(character) - 32)
            else:
                temp_string += character
        return temp_string

