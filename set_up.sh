#!/usr/bin/env bash
# Set up the environment for Stylemate

sudo service mysql start
sudo cat setup_mysql.sql | mysql -uroot -p
tmux new-session -s stylemate_web_app -c ./frontend -d 'python3 -m web_app'
tmux new-session -s stylemate_api -d 'python3 -m api.v1.stylemate_app'
