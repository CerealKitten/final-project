function print(str) {
    console.log(str);
}

print("Hello world!");

var test = 23.3454;


function thingWithCallback(callback) {
    console.log("Doing the thing");
    callback();
}

thingWithCallback(function() {
    console.log("Do whatever");
});