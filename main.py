class usuario:
  def __init__(self, username, password):
    self.username = username
    self.password = password

get_user = usuario("Mikel", "1234")

print(get_user.username)
print(get_user.password)


    