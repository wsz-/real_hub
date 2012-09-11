var server=require("./test")
var router=require("./router")
var requestHandlers=require("./requestHandlers")
var handle={}
handle['/']=requestHandlers.start
handle['/start']=requestHandlers.start
handle['/upload']=requestHandlers.upload
handle['/exec']=requestHandlers.exec
server.start(router.route,handle);
