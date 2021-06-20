import parse

def get_input():
  get_string = input("Enter your string: ")
  if(get_string == "exit"):
    exit()
  else:
    get_character = parse.get_characters(get_string)
    print(get_character)
    get_input()
    
if __name__ == "__main__":
  get_input()
