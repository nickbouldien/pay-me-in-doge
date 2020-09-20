# pay me in doge
a django app that lets users list websites that accept dogecoin as payment

## setup
```bash
python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```bash
python manage.py runserver
```

### with docker
```bash
docker build -t paymeindoge:latest .
```

```bash
docker run --rm --name pay-me-in-doge -e "PORT=8000" -e "DEBUG=1" -p 8000:8000 paymeindoge:latest
```


## sample data/commands
look at the following markdown file to see data/commands to quickly experiment in the shell (run `python manage.py shell`)
[shell data/commands](docs/shell_sample.md)


## installed apps
- [django-vote](https://github.com/shanbay/django-vote)


## sources

### django
- [class based views](http://ccbv.co.uk/)


### dogecoin
- wallet validation
  - https://www.reddit.com/r/dogecoindev/comments/1y60ov/regular_expression_to_check_if_wallet_adress_is/
  - https://www.reddit.com/r/dogecoin/comments/374535/need_help_verifying_dogecoin_address/
  - https://www.reddit.com/r/dogecoin/comments/2ovy9z/how_to_setup_a_dogecoin_vanity_address/