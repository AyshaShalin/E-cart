function seller_validation() {
    var firstname = document.getElementById("exampleInputfirstname").value
    var secondname = document.getElementById("exampleInputsecondname").value
    var email = document.getElementById("exampleInputemail").value
    var number = document.getElementById("exampleInputnum").value
    var address = document.getElementById("exampleInputaddress").value
    var accountno = document.getElementById("exampleInputaccount").value
    var ifsc = document.getElementById("exampleInputifsc").value
    var accountname = document.getElementById("exampleInputaccountname").value
    var image = document.getElementById("exampleInputimage").value
    var password = document.getElementById("exampleInputpassword").value
    var pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" 
    var status = 0

    if (firstname == ''){
      document.getElementById("exampleInputfirstname").style.border = "1px solid red"
      document.getElementById("span1").innerHTML = "Enter your first name"
      document.getElementById("span1").style.color = "Red"
      status = 1
    }
    else {
      document.getElementById("exampleInputfirstname").style.border = "1px solid black"
      document.getElementById("span1").innerHTML = ""
    }

    if (secondname == ''){
      document.getElementById("exampleInputsecondname").style.border = "1px solid red"
      document.getElementById("span2").innerHTML = "Enter your second name"
      document.getElementById("span2").style.color = "Red"
      status = 1
    }
    else {
      document.getElementById("exampleInputsecondname").style.border = "1px solid black"
      document.getElementById("span2").innerHTML = ""
    }

    if (email == ''){
        document.getElementById("exampleInputemail").style.border = "1px solid red"
        document.getElementById("span3").innerHTML = "Enter your email"
        document.getElementById("span3").style.color = "Red"
        status = 1
    }
    else{
        document.getElementById("exampleInputemail").style.border = "1px solid black"
        document.getElementById("span3").innerHTML = ""
        
        if (email.match(pattern) == null){
            document.getElementById("span3").innerHTML = "Enter a valid email"
            document.getElementById("span3").style.color = "Red"
            document.getElementById("exampleInputemail").style.border = "1px solid red"
        }
    }

    if (number == ''){
        document.getElementById("exampleInputnum").style.border = "1px solid red"
        document.getElementById("span4").innerHTML = "Enter your mobile number"
        document.getElementById("span4").style.color = "Red"
        status = 1
    }
    else{
        document.getElementById("exampleInputnum").style.border = "1px solid black"
        document.getElementById("span4").innerHTML = ""
    }

    if (address == ''){
        document.getElementById("exampleInputaddress").style.border = "1px solid red"
        document.getElementById("span5").innerHTML = "Enter your address"
        document.getElementById("span5").style.color = "Red"
        status = 1
    }
    else{
        document.getElementById("exampleInputaddress").style.border = "1px solid black"
        document.getElementById("span5").innerHTML = ""
    }

    if (accountno == ''){
        document.getElementById("exampleInputaccount").style.border = "1px solid red"
        document.getElementById("span6").innerHTML = "Enter your account number"
        document.getElementById("span6").style.color = "Red"
        status = 1
    }
    else{
        document.getElementById("exampleInputaccount").style.border = "1px solid black"
        document.getElementById("span6").innerHTML = ""
    }

    if (ifsc == ''){
        document.getElementById("exampleInputifsc").style.border = "1px solid red"
        document.getElementById("span7").innerHTML = "Enter your IFSC code"
        document.getElementById("span7").style.color = "Red"
        status = 1
    }
    else{
        document.getElementById("exampleInputifsc").style.border = "1px solid black"
        document.getElementById("span7").innerHTML = ""
    }

    if (accountname == ''){
        document.getElementById("exampleInputaccountname").style.border = "1px solid red"
        document.getElementById("span8").innerHTML = "Enter the name of account holder"
        document.getElementById("span8").style.color = "Red"
        status = 1
    }
    else{
        document.getElementById("exampleInputaccountname").style.border = "1px solid black"
        document.getElementById("span8").innerHTML = ""
    }

    if (image == ''){
        document.getElementById("exampleInputimage").style.border = "1px solid red"
        document.getElementById("span9").innerHTML = "Upload the image"
        document.getElementById("span9").style.color = "Red"
        status = 1
    }
    else{
        document.getElementById("exampleInputimage").style.border = "1px solid black"
        document.getElementById("span9").innerHTML = ""
    }

    if (password == ''){
        document.getElementById("exampleInputpassword").style.border = "1px solid red"
        document.getElementById("span10").innerHTML = "Enter your password"
        document.getElementById("span10").style.color = "Red"
        status = 1
    }
    else{
        document.getElementById("exampleInputpassword").style.border = "1px solid black"
        document.getElementById("span10").innerHTML = ""
    }

    if (status == 1){
        return false
    }

  }
