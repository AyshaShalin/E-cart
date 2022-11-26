function check() {  
    var email = document.getElementById('email').value
    var password = document.getElementById('password').value
    var pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"  
    var status = 1

    if (email == ''){
        document.getElementById('span1').innerHTML = 'Enter your email'
        document.getElementById('span1').style.color  = 'red'
        document.getElementById('email').style.border = '1px solid red'
        status = 0
    }
    else{
        document.getElementById('span1').innerHTML = ''
        document.getElementById('email').style.border = '1px solid black'
    
        if (email.match(pattern) == null){
        document.getElementById('span1').innerHTML = 'Enter a vaild email'
        document.getElementById('span1').style.color  = 'red'
        document.getElementById('email').style.border = '1px solid red'
        }
    }

    if (password == ''){
        document.getElementById('span2').innerHTML = 'Enter your password'
        document.getElementById('span2').style.color  = 'red'
        document.getElementById('password').style.border = '1px solid red'
        status = 0
    }
    else{
        document.getElementById('span2').innerHTML = ''
        document.getElementById('password').style.border = '1px solid black'
    }
    if (status == 0){
        return false
    }

}
