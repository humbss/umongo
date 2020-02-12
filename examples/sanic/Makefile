env:
  ifneq ("$(wildcard .env)","")
    include .env
    export $(shell sed 's/=.*//' .env)
  endif

run: env
	. .envi/bin/activate && python3 main.py
