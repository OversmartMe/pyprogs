from instapy import InstaPy
from instapy import smart_run

#login credentials
insta_username ='oversmartbot'
insta_password ='Rashmi.28'

session =InstaPy(username=insta_username,
                  password=insta_password)

with smart_run(session):

    session.set_do_follow(True, percentage=50)

    session.set_do_comments(True, percentage=50)

    session.set_comments(['great content', 'beautiful', 'keep posting'])

    session.set_quota_supervisor(enabled=True,
                                 peak_comments_daily=250,
                                 peak_comments_hourly=30,
                                 peak_likes_daily=250,
                                 peak_likes_hourly=30,
                                 sleep_after=['likes', 'follows'])

    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    min_followers=150,
                                    min_following=50)

    session.like_by_tags(['rockmusic', 'moon', 'pinkfloyd'], ammount=300)


session.end()

