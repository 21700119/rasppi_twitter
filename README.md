# rasppi_twitter
<img src="https://upload.wikimedia.org/wikipedia/ko/thumb/9/9e/%ED%8A%B8%EC%9C%84%ED%84%B0_%EB%A1%9C%EA%B3%A0_%282012%29.svg/1200px-%ED%8A%B8%EC%9C%84%ED%84%B0_%EB%A1%9C%EA%B3%A0_%282012%29.svg.png" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>
## 1. What does this project do? 

This is a project which can send and receive tweets using python and Raspberry Pi.

## 2. Why is this project useful? 

By following this project, you will learn:
- How to create Twitter API keys to use in an application
- How to use Twython to send tweets using Python
- How to upload images to Twitter using Twython

## 3. How do I get started?
1. go to rasppi server
2. install python module (twython)
```pip install twython```
3. Create a Twitter account at [Twitter](twitter.com)
4. Apply for a developer account at [Developer](developer.twitter.com)
   : Apply > Apply for a developer account
5. Go to [Developer](developer.twitter.com), select Apps from the menu, and click on the Create an app button.
6. Complete the application details form. You must enter an app name, description, website (this can be https://www.raspberrypi.org)
7. Click on the Keys and tokens tab to view your keys and access tokens.
8. Click on the Create button under Access token & access token secret.
9. You should now see your Consumer API key, Consumer API secret key, Access token, and Access token secret. You need these four keys to connect to your Twitter account from your Python program.
10. Now you have your API key, you’re ready to send a tweet from Python and Raspberry Pi
11. Test it with the attached code.

## 4. Where can I get more help, if I need it?
https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api/1

http://raspi.tv/raspitweets 

http://makeshare.org/bbs/board.php?bo_table=raspberrypi&wr_id=39

## 5. contents
With these scripts you should be able to:
- auth.py - store Twitter API keys
- twitter.py - send a tweet from python
- tweet.py - send a tweet you want from python
- twitter_img.py - tweet a picture

Have fun tweeting from your Raspberry Pi :]
