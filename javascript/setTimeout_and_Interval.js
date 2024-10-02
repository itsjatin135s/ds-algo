const interval = setInterval(() => {
    console.log("hello");
}, 500);

setTimeout(() => {
    clearInterval(interval);
    console.log("Interval stopped")
}, 3000);