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