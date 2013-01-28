# Introduction

This is a URL shortener exmaple build on Django

## settings


    BASE_URL = 'The basic URL of your shortener site'
    SECRET_CODE = 'AP96YKVoviNBM2E1bmgrzcnRWalGZJFQ3Xsxq7L8kIduT540hpDwSCtfOjyHeU'

SECERT_CODE must only cotains A-Z, a-z, 0-9, you can generate SECERT_CODE by:

    import random, string
    secret_code = list(string.digits+string.ascii_letters)
    random.shuffle(secret_code)
    print ''.join(secret_code)

## Usage

Visit http://localhost:8000/ to generate short URL by form

## API

### POST /api/

Generate a short url

Format

    {
        "url" : "http://www.google.com/"
    }

Reponse

    {
            "url": "http://www.google.com/",
            "short_url": "http://localhost:8000/8AAAAA"
    }

### GET /api/{code}

Get the statisitics of short url {code}

Example GET /api/8AAAAAA

Response

    {
        url: "http://www.icoding.co/"
        updated: "2013-01-28T03:37:01.411"
        clicks: 0
        created: "2013-01-28T03:37:01.404"
    }


