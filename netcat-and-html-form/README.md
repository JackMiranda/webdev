# Observe what an HTML server sees

## Installation instructions

1. Clone this repo into your C9 instance
2. cd into the the repo
3. run ./install.sh to prepare your C9 workspace with the necessary programs
4. run ./run-netcat-and-html-form.sh to start this simple server

## How do I use it?

Upon launch, the script will print a banner which counts the number of requests
it has served. It will then repeatedly serve the contents of http.headers and
index.html to any browser which connects with it.

To exit, press Ctrl-C twice in quick succession.

You may edit either of http.headers and index.html as the program runs to observe the
effects of

	* Changing the type of HTTP method used
	* Sending different values to the server
	* Changing the types of input widgets used

Due to the way the script works, you will have to reload the page TWICE to view
any changes to the headers or HTML file. *OR* you may press Ctrl-C once to
restart the server and it will reload the files.

IMPORTANT!!! Leave at least one blank line at the bottom of http.headers, or
else your webpage will become corrupt! The presence of this blank line is
actually called for by the HTTP protocol.
