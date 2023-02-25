const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

var ut_sec = os.uptime();
var ut_min = ut_sec/60;
var ut_hour = ut_min/60;
var ut_day = ut_hour/24;
   
ut_sec = Math.floor(ut_sec);
ut_min = Math.floor(ut_min);
ut_hour = Math.floor(ut_hour);
ut_day = Math.floor(ut_day);

ut_day = ut_day%24;  
ut_hour = ut_hour%60;
ut_min = ut_min%60;
ut_sec = ut_sec%60;

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${ut_day} days ${ut_hour} hours ${ut_min} minutes and ${ut_sec} seconds </p>
        <p>Total Memory: ${os.totalmem() /1000000} MB </p>
        <p>Free Memory: ${os.freemem() /1000000} MB</p>
        <p>Number of CPUs: ${os.cpus().length}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");