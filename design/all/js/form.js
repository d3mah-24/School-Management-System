
 const nametxt = document.getElementById("nametxt");


 const fnametxt = document.getElementById("fametxt");


 const lnametxt = document.getElementById("lnametxt");

 const passtxt = document.getElementById("pass");


 const numtxt = document.getElementById("numtxt");

 const pnumtxt = document.getElementById("pnumtxt");

 const ppasstxt = document.getElementById("ppasstxt");


 const pnametxt = document.getElementById("pnametxt");


 var er1 = 1,
     er2 = 1,
     er3 = 1;


 const bt = document.getElementById('ahi');




 function testname(inp, ty) {
     const j = document.getElementById(ty);
     if (inp.value.length < 4) {
         j.innerText = "Your Name Must Be >= 4";
         inp.style.border = "5px solid red";
         er1 = 1;
         if (er1 + er3 + er2 === 0) {
             const bt = document.getElementById('ahi');
             bt.disabled = false;
             bt.style.background = "orange";
         } else {
             const bt = document.getElementById('ahi');
             bt.disabled = true;
             bt.style.background = "grey";
         }

     } else {
         inp.style.border =  "0px solid green";
         j.innerText = "";
         er1 = 0;
         if (er1 + er3 + er2 === 0) {

             const bt = document.getElementById('ahi');
             bt.disabled = false;
             bt.style.background = "orange";
         } else {
             const bt = document.getElementById('ahi');
             bt.disabled = true;
             bt.style.background = "grey";
         }




     }





 }




 function testpass(inp, ty) {
     const j = document.getElementById(ty);
     if (inp.value.length < 7) {

         j.innerText = "Your Password Is Too Short";
         inp.style.border =  "5px solid red";
         er2 = 1;
         if (er1 + er3 + er2 === 0) {

             const bt = document.getElementById('ahi');
             bt.disabled = false;
             bt.style.background = "orange";
         } else {
             const bt = document.getElementById('ahi');
             bt.disabled = true;
             bt.style.background = "grey";
         }


     } else {
         inp.style.border =  "0px solid green";
         j.innerText = "";
         er2 = 0;
         if (er1 + er3 + er2 === 0) {

             const bt = document.getElementById('ahi');
             bt.disabled = false;
             bt.style.background = "orange";
         } else {
             const bt = document.getElementById('ahi');
             bt.disabled = true;
             bt.style.background = "grey";
         }
     }






 }





 function testnum(inp, ty) {
     const j = document.getElementById(ty);
     if (inp.value.length !== 10 || inp.value.slice(0, 2) !== "09") {

         j.innerText = "Invalid Phone Number";
         inp.style.border =  "5px solid red";
         er3 = 1;
         if (er1 + er3 + er2 === 0) {

             const bt = document.getElementById('ahi');
             bt.disabled = false;
             bt.style.background = "orange";
         } else {
             const bt = document.getElementById('ahi');
             bt.disabled = true;
             bt.style.background = "grey";

         }

     } else {
         inp.style.border =  "0px solid green";
         j.innerText = "";
         er3 = 0;
         if (er1 + er3 + er2 === 0) {


             const bt = document.getElementById('ahi');
             bt.disabled = false;
             bt.style.background = "orange";
         } else {
             const bt = document.getElementById('ahi');
             bt.disabled = true;
             bt.style.background = "grey";
         }
     }



 }