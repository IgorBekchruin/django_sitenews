<!-- ABOUT THE PROJECT -->
## Django-sitenews

This is a news site about the world of IT technologies, designed in the form of a small blog. There is user registration via email, account confirmation via email, and the ability to leave comments on a post for registered users.

Backend:
* Python
* Django

Frontend:
* HTML
* CSS
* Bootstrap

DB:
* Posregresql

Tools:
* Redis
* Celery
* Docker/Docker-compose

To implement user registration via email, the basic AbstractUser model was redefined.
Added redis caching for pages with a lot of news.
Sending messages to confirm registration is implemented using celery.
The project is designed in docker and docker-compose.
