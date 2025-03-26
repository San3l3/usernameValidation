
import re
def CodelandUsernameValidation(username):

  #Check the length of the username
  if not (4 <= len(username) <= 25):
    return "false"
  
  #Check if it starts with a letter
  if not username[0].isalpha():
    return "false"
  
  #Check if it only contains letters, numbers and underscores
  if not re.match(r'^[a-zA-Z0-9_]+$', username):
    return "false"

  #Check if it ends with an underscore
  if username[-1] == "_":
    return "false"
  
  return "true"

#Calling the function
print(CodelandUsernameValidation("aa_"))
print(CodelandUsernameValidation("u__hello_world123"))