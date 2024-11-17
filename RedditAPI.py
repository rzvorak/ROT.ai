import matplotlib.pyplot as plt
import datetime
import pandas as pd
import praw
import time
import os

def testRedditAPI(word):
        # Initialize reddit api
        reddit = praw.Reddit(client_id='H5092zuImQyMCKARxvK8QQ',
                     client_secret='HSMR_yOGA2vGc7yLv-oPt4xV4Ibv_A',
                     user_agent='Mint_Swirls')
        # Set the slang word you want to track
        slang_word = word

        c1 = 0
        c2 = 0
        c1_total = 0
        c2_total = 0
        # Search for the slang word in the most recent posts on Reddit
        for submission in reddit.subreddit('all').search(slang_word, sort='top', time_filter='day', limit=20):
            """
            print(submission.title, submission.url)
            print("Num Upvotes: ", submission.score, "      Upvote Ratio: ", submission.upvote_ratio, "      Num Comments: ", submission.num_comments)
            """
            c1 = c1 + 1
            c1_total = c1_total + submission.upvote_ratio
        
        daily_ratio = c1_total/c1

        for submission in reddit.subreddit('all').search(slang_word, sort='top', time_filter='month', limit=20):
            """
            print(submission.title, submission.url)
            print("Num Upvotes: ", submission.score, "      Upvote Ratio: ", submission.upvote_ratio, "      Num Comments: ", submission.num_comments)
            """
            c2 = c2 + 1
            c2_total = c2_total + submission.upvote_ratio
       
        monthly_ratio = c2_total/c2

        return [daily_ratio, monthly_ratio]



