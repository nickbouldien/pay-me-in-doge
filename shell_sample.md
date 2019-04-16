# sample data
just some data to quickly experiment in the shell with `python manage.py shell`

## util
log queries
```
from django.db import connection
connection.queries
```

## user
```
from django.contrib.auth.models import User
user = User.objects.get(pk=2)
```

## site
```
from board.models import Site

s1 = Site(name="test", poster=user, url="https://www.testsite.com", description="cool site!!")

s2 = Site(name="againtest", poster=user, url="https://www.againtest.com", description="again test site that sells food=")

s1 = Site.objects.get(pk=1)
s2 = Site.objects.get(pk=2)
```

## vote
```
from django.contrib.auth.models import User
from board.models import Site

user = User.objects.get(pk=1)
u2 = User.objects.get(pk=2)
site = Site.objects.get(pk=1)

site.votes.up(user.id)
site.votes.down(user.id)
site.votes.count()
```
