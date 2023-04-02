const http = require("http");
const data = require("C:/Users/juhas/it3038c-scripts/node/widgets.json");
const listBlue = (res) => {
  const colorBlue = data.filter((item) => {
    return item.color === "blue" || item.color === "green";
  });

  res.end(JSON.stringify(colorBlue));
}
const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.writeHead(200, {"Content-Type": "text/json"});
    res.end(JSON.stringify(data));
  } else if (req.url === "/color") {
    listBlue(res);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end("Data not found");
  }
});

server.listen(3000);
console.log("Server is listening on port 3000");