# twitter-bot
Twitter bot with tweepy in python

-----
 
## Getting Started

### Prerequsites
+ [python3](https://www.python.org/downloads/) 
+ [pip](https://pip.pypa.io/en/stable/installing/)
+ [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
+ [venv](https://docs.python.org/3/library/venv.html) (optional)

### Clone
Clone this repo to your local machine
```sh
git clone https://github.com/j-tesla/twitter-bot.git
```

### Installing
```sh
cd twitter-bot
```
#### Virtual environment (optional)
```sh
python3 -m pip install venv
python3 -m venv venv
source venv/bin/activate
```

#### Install dependencies
```sh
python3 -m pip install -r requirements.txt
```

### Configuring
1. Log onto https://developer.twitter.com/

2. Create an [app](https://developer.twitter.com/en/docs/basics/apps/overview) with *read and write* [permissions](https://developer.twitter.com/en/docs/basics/apps/guides/app-permissions)

3. Generate api and access keys and copy them

4. Copy [example-keys.json](example-keys.json) to a new file **keys.json** and fill the appropriate fields. (Never make your **keys.json** file public)

## Deployment
Run [main.py](main.py):
```sh
python3 main.py
```

## Built with
+ [Tweepy](https://www.tweepy.org/) for Twitter's API
+ [Tkinter](https://wiki.python.org/moin/TkInter) for GUI

## License
This project is licensed under the MIT License - check the [LICENSE file](LICENSE) for details.
