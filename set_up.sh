#!/usr/bin/env bash
# Set up the environment for Stylemate

sudo service mysql start
sudo cat setup_mysql.sql | mysql -uroot -p
tmux new-session -c ./frontend -d 'python3 -m web_app'
tmux new-session -d 'python3 -m api.v1.stylemate_app'
