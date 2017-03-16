#!/bin/sh
#Wrapper to make use of docker secrets

source $SECRETS

python get_tweets.py

