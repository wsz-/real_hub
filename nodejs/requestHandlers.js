var exe=require('child_process').exec
var querystring=require('querystring')
function start(response,postData) {
  console.log("Request handler 'start' was called.");

  var body = '<html>'+
    '<head>'+
    '<meta http-equiv="Content-Type" content="text/html; '+
    'charset=UTF-8" />'+
    '</head>'+
    '<body>'+
    '<form action="/upload" method="post">'+
	'<input type="text" name="text" id="sss"/>'+
    '<textarea name="text" rows="20" cols="60"></textarea>'+
    '<input type="submit" value="Submit text" />'+
    '</form>'+
    '</body>'+
    '</html>';

    response.writeHead(200, {"Content-Type": "text/html"});
    response.write(body);
    response.end();
}

function upload(response,postData) {
  console.log("Request handler 'upload' was called.");
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write("Hello Upload :"+
		querystring.parse(postData).text);
  response.end();
}

function starts(response){
    console.log("Request hander start********");
    _res(response)
    response.write("start**")
    _res_end(response)
}
function exec(response){
    console.log('R ***********');
    // exe('find /v /n "ss" .\\home.7z',function(error,stdout,stderr){
    exe('pause',function(error,stdout,stderr){
	function ss(callbac){
	    var time=0
	    for(var i=0;i<100000000;i++){
		s=s+i
		if(i==100000000-1){
		    // if(time<=10){
		    // 	i=0
		    // 	time+=1
		    // 	continue
		    // }
		    callbac(s)
		}
	    }
	}
	function call(s){
	    _res(response)
	    response.write(""+error)
	    response.write(""+stdout)
	    response.write(""+stderr)
	    response.write("ooooooooooooooooooooooooooooooooo "+s)
	    _res_end(response)
	}
	s=0
	ss(call)
    });
}
function _res(response){
    response.writeHead(200, {"Content-Type": "text/plain"});
}
function _res_end(response){
    response.end();
}
function uploads(response){
    console.log("Request hander upload");
    _res(response)
    response.write("upload**")
    _res_end(response)
}
exports.start=start
exports.upload=upload
exports.exec=exec
