#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that makes the server respond with the message "You got me!".
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
