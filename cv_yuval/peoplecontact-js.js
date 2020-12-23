console.log("");


fetch('https://reqres.in/api/users?page=2').then(response => response.json())
.then(responseJSON => myContactList(responseJSON.data)).catch(err => 
    console.log(err));

    function myContactList(contacts){
        const mycontactMain = document.querySelector("main");
        for(let contact of contacts){
            const section = document.createElement("section");
            section.innerHTML=`
    
    <div class="name" style="display: inline;">
     ${contact.first_name + " " + contact.last_name}
     </div>
    
    <div id="contactpic">
   <img src="${contact.avatar}" alt="contact pic" >
    </div>

    <div id="email">
    ${contact.email}
    </div>`;
    mycontactMain.appendChild(section);  
}
}