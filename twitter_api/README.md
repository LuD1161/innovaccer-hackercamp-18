# Setup
### Install the following dependencies
```
pip install -r requirements.txt
```
### Setup the database
1. Make a new database, named twitterapi
2. Create a new mysql user, named twitterapi with password 12345
3. Run the database on port 3306 ( default port )
4. Below is the commands for setting up on linux

```
mysql -u root -p12345 # my mysql username is root and password is 12345
# Now you will get mysql prompt
create database twitterapi;
create user 'twitterapi'@'localhost' identified by '12345';
grant all privileges on twitterapi.* to 'twitterapi'@'localhost';
```
### Setting up django
1. Make migrations
2. Migrate new migrations
3. Run server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# API Endpoints 

## Fetch New tweets
**GET** `/api/query/?q=`

## Search in Tweets ( with filters )
**GET** `/api/tweets/?text=&text__icontains=&in_reply_to_screen_name=&in_reply_to_screen_name__icontains=&place=&place__icontains=&id=&id__contains=`

**GET** `/api/users/?url=&url__contains=&followers_count__gt=&followers_count__lt=&followers_count=&location=&location__contains=&name=&name__contains=&screen_name=&screen_name__contains=`

## Format
### CSV
**GET** `/api/tweets/?format=csv&id=&id__contains=&in_reply_to_screen_name=&in_reply_to_screen_name__icontains=&place=&place__icontains=&text=&text__icontains=`

_CSV format to export filtered data from API_

### JSON
**GET** `/api/tweets/?format=json&id=&id__contains=&in_reply_to_screen_name=&in_reply_to_screen_name__icontains=&place=&place__icontains=&text=&text__icontains=`

### API ( default )
**GET** `/api/tweets/?id=&id__contains=&in_reply_to_screen_name=&in_reply_to_screen_name__icontains=&place=&place__icontains=&text=&text__icontains=`

## Ordering
### Ascending
**GET** `/api/tweets/?ordering=text`
**GET** `/api/users/?ordering=_id`

### Descending
**GET** `/api/tweets/?ordering=-text`
**GET** `/api/users/?ordering=-_id`


## P.S. 
### Output of `python --version`
```
Python 2.7.14+
```


# To Do 
- [ ] Switch over to twitter streaming API with start and stop request , the code is already there only need to add endpoints to start and stop streaming.
- [ ] Switch to NoSQL database ( switch to mongodb as database backend )
