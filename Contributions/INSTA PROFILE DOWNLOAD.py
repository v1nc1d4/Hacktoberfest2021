import instaloader
ig = instaloader.Instaloader()
username = input("Enter username: ")
print(ig.download_profile(username,profile_pic_only = True))
print("Downloaded Successfully :D\nIt's in your current directory")
