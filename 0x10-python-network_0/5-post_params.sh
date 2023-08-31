#!/bin/bash
# This script takes in a URL,
# sends a POST request to the passed URL,
# and displays the body of the response

curl -s -X POST --data-urlencode "email=test@gmail.com&subject=I will always be here for PLD" "$1"

# -s => Silent mode
# -X, --request <command> => Specify request command (method) to use
# -d, --data <data> =>
#              (HTTP) Sends the specified data in a POST request to the HTTP server, in the same way that a browser does when a user has filled in an HTML form.
# <data> in form => "variable1=value1&variable2=value2" and spaces should be typed as %20 or:
#  --data-urlencode <data> =>
#              (HTTP) This posts data, similar to the other -d, --data options with the exception that this performs URL-encoding.
#              To  be  CGI-compliant, the <data> part should begin with a name followed by a separator and a content specification.
#
