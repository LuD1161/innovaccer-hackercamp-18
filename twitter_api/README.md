# Setup


# API Endpoints 

## Fetch New tweets
**GET** `/api/query/?q=`

## Search in Tweets ( with filters )
**GET** `/api/tweets/?text=&text__icontains=&in_reply_to_screen_name=&in_reply_to_screen_name__icontains=&place=&place__icontains=&id=&id__contains=`

**GET** `/api/users/?url=&url__contains=&followers_count__gt=&followers_count__lt=&followers_count=&location=&location__contains=&name=&name__contains=&screen_name=&screen_name__contains=`

## Format
### CSV
**GET** `/api/tweets/?format=csv&id=&id__contains=&in_reply_to_screen_name=&in_reply_to_screen_name__icontains=&place=&place__icontains=&text=&text__icontains=`

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