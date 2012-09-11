var http = require("http");
var url=require("url")
function start(route,handle){
    function onRequest(request, response) {
	var pathname=url.parse(request.url).pathname
	// response.writeHead(200, {"Content-Type": "text/plain"});
	// response.write("<h>request received</h>");
	// response.write("<span> "+pathname+"</span>");
	var postData=''
	request.setEncoding('utf8')
	request.addListener('data',function(chunk){
	    postData+=chunk
	    console.log(chunk+'/////');
	})
	request.addListener('end',function(){
	    route(pathname,handle,response,postDatap)
	})
    }
    http.createServer(onRequest).listen(8888);
}
exports.start=start
