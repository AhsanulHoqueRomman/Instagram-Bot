from instabot import Bot
import time
import random


class InstagramBot:

    def __init__(self):
        self.bot = Bot()

    # Authentication
    def login(self, username, password):
        self.bot.login(username=username, password=password)

    def logout(self):
        self.bot.logout()

    # Profile
    def get_profile_info(self, username):
        return self.bot.get_user_info(username)

    def edit_profile(self, bio):
        print("Edit profile not supported directly in instabot")

    # Follow System
    def follow(self, user):
        self.bot.follow(user)

    def unfollow(self, user):
        self.bot.unfollow(user)

    def follow_multiple(self, users):
        for user in users:
            self.bot.follow(user)
            self.random_delay()

    def unfollow_non_followers(self):
        print("Custom logic needed")

    def get_followers(self):
        return self.bot.get_user_followers(self.bot.user_id)

    def get_following(self):
        return self.bot.get_user_following(self.bot.user_id)

    # Like System
    def like_post(self, post_id):
        self.bot.like(post_id)

    def like_recent_posts(self, user):
        medias = self.bot.get_user_medias(user, filtration=False)
        for media in medias[:5]:
            self.bot.like(media)
            self.random_delay()

    def like_by_hashtag(self, tag):
        medias = self.bot.get_hashtag_medias(tag)
        for media in medias[:5]:
            self.bot.like(media)

    # Comment System
    def comment_on_post(self, post_id, text):
        self.bot.comment(post_id, text)

    def comment_on_hashtag(self, tag, text):
        medias = self.bot.get_hashtag_medias(tag)
        for media in medias[:5]:
            self.bot.comment(media, text)

    # Messaging
    def send_message(self, user, message):
        user_id = self.bot.get_user_id_from_username(user)
        self.bot.send_message(message, [user_id])

    def broadcast_message(self, users, message):
        for user in users:
            self.send_message(user, message)
            self.random_delay()

    # Search
    def search_user(self, username):
        return self.bot.search_users(username)

    def search_hashtag(self, tag):
        return self.bot.search_tags(tag)

    # Post Management
    def upload_photo(self, path, caption=""):
        self.bot.upload_photo(path, caption=caption)

    def upload_video(self, path, caption=""):
        print("Video upload may not be supported")

    # Automation
    def auto_like(self, tag):
        self.like_by_hashtag(tag)

    def auto_follow(self, tag):
        users = self.bot.get_hashtag_users(tag)
        for user in users[:5]:
            self.bot.follow(user)

    def auto_unfollow(self):
        print("Custom logic needed")

    # Scheduling
    def schedule_post(self, path, caption, delay):
        print(f"Waiting {delay} seconds...")
        time.sleep(delay)
        self.upload_photo(path, caption)

    # Safety
    def random_delay(self):
        time.sleep(random.randint(2, 5))

    def limit_actions(self, count):
        print(f"Limit set to {count} actions")

    # Data Handling
    def save_users_to_file(self, users, filename="users.txt"):
        with open(filename, "w") as f:
            for user in users:
                f.write(user + "\n")

    def load_users_from_file(self, filename="users.txt"):
        with open(filename, "r") as f:
            return [line.strip() for line in f]

    def log_activity(self, text):
        with open("log.txt", "a") as f:
            f.write(text + "\n")


# Run Example
if __name__ == "__main__":
    bot = InstagramBot()

    username = input("Enter username: ")
    password = input("Enter password: ")

    bot.login(username, password)

    bot.follow("hoque_romman")
    bot.like_by_hashtag("python")

    bot.logout()