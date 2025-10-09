class Test:
  def __init__(self, user_name, user_id):
    self.name = user_name
    self.id = user_id
    self.followers = 0
    self.following = 0


  def follow(self, user):
    self.following += 1
    user.followers += 1



user_1 = Test("angela", 1)
user_2 = Test("jack", 2)


user_1.follow(user_2)

print (user_1.followers)
print (user_1.following)
print (user_2.followers)
print (user_2.following)
