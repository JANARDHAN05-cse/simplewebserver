# EX01 Developing a Simple Webserver
## Date: 07.03.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
    <title>
        Time Table
    </title>
    <body align="center">
        <h2>PRIME TIME TABLE</h2>
        <table border="2">
            <tr>
		<th colspan="4" align="center" bgcolor="#FF8C00">
		WEB DEVELOPMENT AND FUNDAMENTAL OF AI-BATCH
		</th>
	    </tr>
	    <tr>
                <td bgcolor="#FFA500">     </td>
                <td bgcolor="#FFA500" align="center">8-10</td>
                <td bgcolor="#FFA500" align="center">10-12</td>
                <td bgcolor="#FFA500" align="center">1-3</td>
            </tr>
            <tr>
                <th bgcolor="#FFA500">MONDAY</th>
                <td bgcolor="white">WEB DEVELOPMENT</td>
                <td bgcolor="white">TASK ASSIGNMENT</td>
                <td bgcolor="white">FUNDAMENTAL OF AI</td>
            </tr>
            <tr bgcolor="white">
                <th bgcolor="#FFA500">TUESDAY</th>
                <td>TASK COMPLETION</td>
                <td>WEB DEVELOPMENT</td>
                <td>MODULE COMPLETION</td>
            </tr>
            <tr bgcolor="white">
                <th bgcolor="#FFA500">WEDNESDAY</th>
                <td>ASSESSMENT HOUR</td>
                <td>TASK COMPLETION</td>
                <td bgcolor = "green">MENTOR MEET</td>
            </tr>
            <tr bgcolor="white">
                <th bgcolor="#FFA500">THURSDAY</th>
                <td>MODULE COMPLETION</td>
                <td>FUNDAMENTAL OF AI</td>
                <td>TASK PRESENTATION</td>
            </tr>
            <tr bgcolor="white">
                <th bgcolor="#FFA500">FRIDAY</th>
                <td>TASK COMPLETION</td>
                <td>WEB DEVELOPMENT</td>
                <td>TASK COMPLETION</td>
            </tr>
	    <tr bgcolor="white">
		<th bgcolor="#FFA500">SATURDAY</th>
		<td colspan="3" align="center">
		MODULE ASSESSMENT COMPLETION
		</td>
	    </tr>

        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot (1).png>)
![alt text](<Screenshot (2).png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
