import instaloader

L = instaloader.Instaloader()

def logIn(username,password):
    L.login(username,password)


'''
L = instaloader.Instaloader()
L.login("yourusername","yourpassword")
profile = instaloader.Profile.from_username(L.context,"mcanulkr")
followers = profile.get_followers()
following = profile.get_followees()

follower_list = []
following_list = []
list = []

for follower in followers:
    follower_list.append(follower.username)

for follow in following:
    if follow.username not in follower_list:
        list.append(follow.username)'''