function speak() {
    something = document.getElementById("speakButton").value;
    console.log(something)
    const res = axios.put('https://manager-be70e-default-rtdb.firebaseio.com/.json', {
        Data: something
    });

}