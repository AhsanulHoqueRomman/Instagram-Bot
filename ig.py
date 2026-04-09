from instabot import Bot
import os

bot = Bot()

username = input("Enter username: ")
password = input("Enter password: ")

bot.login(username=username, password=password)

bot.follow("hoque_romman")