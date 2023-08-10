var delete_btn = document.getElementById('mydelete_btn')

function funki(){
    var delete =confirm('Are you sure you want delete?');
    if(delete){
        delete_btn.setAttribute("disabled='false'");
    }
}