const input = document.getElementById("input");
const button = document.getElementById("submit_btn");
const output = document.getElementById("output");
button.addEventListener("click", ()=>{
    if (input.value !== ""){
        const fetchoptions ={
            method: "POST",
            header: new Headers({
                "Content-Type": "application/json"
            })
        }
        let jsondata = {}
        jsondata.stri = input.value
        fetchoptions.body = JSON.stringify(jsondata)
        const url = "http://127.0.0.1:5000/validatethisjson"
        fetch(url, fetchoptions)
        .then(r => r.json())
        .then(r => {
            if (r.isvalid){
                input.value = r.value
                output.innerText = "Valid"
            }
            else{
                output.innerText = "Invalid"
            }
        })
        .catch(e => console.log(e))
    }
})
