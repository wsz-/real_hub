function add(a,b){
    return a+b;
}
function minus(a,b){
    return a-b;
}
function multi(a,b){
    return a*b
}
function divide(a,b){
    return a/b
}
function opt(f,a,b){
    return f(a,b)
}
function move(arr,i){
    var arr=arr.slice()
    for(;i<arr.length;i++){
	arr[i]=arr[i+1]
    }
    arr.pop()
    return arr
}
function genPair(arr){
    var result=[]
    var count=0
    for(var i=0;i<arr.length;i++){
	var arr=move(arr,i)
	for(var j=i;j<arr.length;j++){
	    var arr=move(arr,j)
	    result[count]=arr
	    count+=1
	}
    }
    return result
}
function x(arr,a){
    var result=[]
    var ai=0;
    for(var i=0;i<arr.length;i++){
	if(i==a[ai]){
	    ai+=1
	}else{
	    result.push(arr[i])
	}
    }
    return result
}
function gp(arr){
    var result=[]
    var count=0
    for(var i=0;i<arr.length-1;i++){
	for(var j=i+1;j<arr.length;j++){
	    var pair=[]
	    pair[0]=arr[i]
	    pair[1]=arr[j]
	    pair[2]=x(arr,[i,j])
	    result[count]=pair
	    count+=1
	}
    }
    return result
}
// arr[0]: [his,pairs]
function find(a){
    arr=a[1]
    if(arr.length==2){
	for(var f in o){
	    var ar=arr[1]
	    var tmp=f(ar[1],ar[0])
	    if(tmp==24){
		return [arr,his,f]
	    }
	}
    }else{
	var pairs=gp(arr)
	for(var p in pairs){
	    var h=[]
	    h.push([arr[0],arr[1]])
	}
    }
}
var o=[add,minus,divide,multi]
var arr=[4,3,4,5]
var over=false
find(arr,[])
