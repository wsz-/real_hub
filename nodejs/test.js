var http = require("http");
var url=require("url")
function start(route,handle){
    function onRequest(request, response) {
	var pathname=url.parse(request.url).pathname
	// response.writeHead(200, {"Content-Type": "text/plain"});
	// response.write("<h>request received</h>");
	// response.write("<span> "+pathname+"</span>");
	route(pathname,handle,response)
    }
    http.createServer(onRequest).listen(8888);
}
exports.start=start
