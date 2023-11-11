<!-- ABOUT THE PROJECT -->
## Django-sitenews

This is a news site about the world of IT technologies, designed in the form of a small blog. There is user registration via email, account confirmation via email, and the ability to leave comments on a post for registered users.

![sitenews](https://github.com/IgorBekchruin/django_sitenews/assets/107909070/c1a26c4a-c39d-4bf3-8d71-577a9aef3223)

Backend:
* Python
* Django

Frontend:
* HTML
* CSS
* Bootstrap

DB:
* PostgreSQL

Tools:
* Redis
* Celery
* Docker/Docker-compose

To implement user registration via email, the basic AbstractUser model was redefined.
Added redis caching for pages with a lot of news.
Sending messages to confirm registration is implemented using celery.
The project is designed in docker and docker-compose.
