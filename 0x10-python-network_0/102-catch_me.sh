#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!,
curl -s -X PUT -H "Origin: School" 0.0.0.0:5000/catch_me_3