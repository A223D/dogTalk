//#A @ 66.96.162.148 n/a
function speak() {
    something = document.getElementById("speakButton").value;
    console.log(something)
    const res = axios.put('https://manager-be70e-default-rtdb.firebaseio.com/.json', {
        Data: something
    });

}