#!/bin/bash

celery --app=mysite worker --loglevel=info --pool=solo