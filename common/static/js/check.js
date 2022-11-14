function check() {
    var firstname = document.getElementById('exampleInputfirstname').value
    var secondname = document.getElementById('exampleInputsecondname').value
    var email = document.getElementById('exampleInputemail').value
    var number = document.getElementById('exampleInputnum').value
    var address = document.getElementById('exampleInputaddress').value
    var password = document.getElementById('exampleInputpassword').value
    var pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"  
    var status = 1

    if (firstname == ''){
        document.getElementById('span1').innerHTML = 'Enter your firstname'
        document.getElementById('span1').style.color = 'red'
        document.getElementById('exampleInputfirstname').style.border ='1px solid red'
        status = 0
    }
    else{
        document.getElementById('span1').innerHTML =''
        document.getElementById('exampleInputfirstname').style.border ='1px solid black'
    }

    if (secondname == ''){
        document.getElementById('span4').innerHTML = 'Enter your secondname'
        document.getElementById('span4').style.color = 'red'
        document.getElementById('exampleInputsecondname').style.border ='1px solid red'
        status = 0
    }
    else{
        document.getElementById('span4').innerHTML ='' 
        document.getElementById('exampleInputsecondname').style.border  = '1px solid black'
    }

    if (email == ''){
        document.getElementById('span3').innerHTML = 'Enter your email'
        document.getElementById('span3').style.color  = 'red'
        document.getElementById('exampleInputemail').style.border = '1px solid red'
        status = 0
    }
    else{
        document.getElementById('span3').innerHTML = ''
        document.getElementById('exampleInputemail').style.border = '1px solid black'
    
    if (email.match(pattern) == null){
        document.getElementById('span3').innerHTML = 'Enter a vaild email'
        document.getElementById('span3').style.color  = 'red'
        document.getElementById('exampleInputemail').style.border = '1px solid red'
    }
    }

    if (number == ''){
        document.getElementById('span2').innerHTML = 'Enter your number'
        document.getElementById('span2').style.color  = 'red'
        document.getElementById('exampleInputnum').style.border = '1px solid red'
        status = 0
    }
    else{
        document.getElementById('span2').innerHTML = ''
        document.getElementById('exampleInputnum').style.border = '1px solid black'
    }

    if (address == ''){
        document.getElementById('span5').innerHTML = 'Enter your address'
        document.getElementById('span5').style.color  = 'red'
        document.getElementById('exampleInputaddress').style.border = '1px solid red'
        status = 0
    }
    else{
        document.getElementById('span5').innerHTML = ''
        document.getElementById('exampleInputaddress').style.border = '1px solid black'
    }
    
    if (password == ''){
        document.getElementById('span6').innerHTML = 'Enter your password'
        document.getElementById('span6').style.color  = 'red'
        document.getElementById('exampleInputpassword').style.border = '1px solid red'
        status = 0
    }
    else{
        document.getElementById('span6').innerHTML = ''
        document.getElementById('exampleInputpassword').style.border = '1px solid black'
    }
    if (status == 0){
        return false
    }

}
