function settime(){
    let date=new Date();
    let yr=date.getFullYear();
    let month= date.getMonth();
    let day= date.getDate();
    let hour = date.getHours(); 
    let min = date.getMinutes();
    time.innerHTML = hour+":"+min+" / "+day+"-"+(month+1)+"-"+yr;
}
setInterval(settime,1000);


 