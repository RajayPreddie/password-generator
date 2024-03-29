import argparse
class ArgumentParser:
  def __init__(self):
    # Argument parser
    self.arg_parser = argparse.ArgumentParser(description="Generate a password", usage="python main.py -l 10 -u -n -s")
    # Argument for length of the password
    self.arg_parser.add_argument("-le", "--length", type=int, help="Length of the password")
    # Argument for uppercase password 
    self.arg_parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    # Argment for lowercase password
    self. arg_parser.add_argument("-lo", "--lowercase", action="store_true", help="Include lowercase letters")
    # Argument for numbers
    self.arg_parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers")
    # Argument for symbols
    self.arg_parser.add_argument("-s", "--symbols", action="store_true", help="Include symbols")
    # Parse the args
    self.args = self.arg_parser.parse_args()
  # Obtain the length of the password
  def get_length(self):
    return self.args.length
  # Check if the password should include uppercase letters
  def is_uppercase(self):
    return self.args.uppercase
  # Check if the password should include lowercase letters
  def is_lowercase(self):
    return self.args.lowercase
  # Check if the password should include numbers
  def is_numbers(self):
    return self.args.numbers
  # Check if the password should include symbols
  def is_symbols(self):
    return self.args.symbols
  
      