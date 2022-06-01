# How to start

``` docker-compose up ```

visit ```localhost:8000/admin``` to view the admin site
admin credentials are listed in docker-compose.yml
email: admin@admin.com
password: admin

## Navigation
signup: localhost:8000/accounts/signup
login: localhost:8000/accounts/login


## APIs

create auth token: localhost:8000/token/
Get current user's task items: /api/v1/items/
Get a particulat item: /api/v1/item/<item_uuid>/


