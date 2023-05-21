class DNI:
    def dictionary(csv):
        """
        Creates a dictionary from a CSV file where the DNI number is the key and the letter is the value.

        Parameters:
        - csv: The path to the CSV file.

        Returns:
        - dictionary: A dictionary mapping DNI numbers to letters.
        """
        dictionary = {}
        with open(csv, 'r') as file:
            for value in file.readlines():
                dictionary[value.split(';')[0]] = value.split(';')[1].strip('\n')
        return dictionary

    def letter(digits):
        """
        Determines the letter associated with the given DNI digits.

        Parameters:
        - digits: The numerical digits of the DNI number.

        Returns:
        - letter: The corresponding letter based on the DNI algorithm.
        """
        return 'TRWAGMYFPDXBNJZSQVHLCKE'[digits % 23]


