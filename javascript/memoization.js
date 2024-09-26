function memoize(fn) {
    let cache = {};
    return function(arg1, arg2){
        if (cache[arg1]){
            console.log("return from cache", cache[arg1], arg1)
            return cache[arg1];
        }else{
            let res = fn(arg1, arg2);
            cache[arg1] = res;
            console.log("calculating", res, arg1)
            return res
        }
    }
}

const sum = (a,b) =>{
    return a + b;
}

const newSum = memoize(sum);

newSum(1,2);
newSum(1,2);
newSum(23,2);
