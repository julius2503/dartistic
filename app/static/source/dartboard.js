function deleteThrows(){
    document.getElementById("first-dart").value = "";
    document.getElementById("second-dart").value = "";
    document.getElementById("third-dart").value = "";
}

function writeValue(value){
    dart1 = document.getElementById("first-dart");
    dart2 = document.getElementById("second-dart");
    dart3 = document.getElementById("third-dart");
    switch(value){
        case 'T':
            if(dart1.value == "" || dart1.value == "D" || dart1.value == "T"){
                dart1.value = value;
                break;
            }
            else if(dart2.value == "" || dart2.value == "D" || dart2.value == "T"){
                dart2.value = value;
                break;
            }
            else if(dart3.value == "" || dart3.value == "D" || dart3.value == "T"){
                dart3.value = value;
                break;
            }
            break;

        case 'D':
            if(dart1.value == "" || dart1.value == "D" || dart1.value == "T"){
                dart1.value = value;
                break;
            }
            else if(dart2.value == "" || dart2.value == "D" || dart2.value == "T"){
                dart2.value = value;
                break;
            }
            else if(dart3.value == "" || dart3.value == "D" || dart3.value == "T"){
                dart3.value = value;
                break;
            }
            break;
        
        case '0':
            if(dart1.value == "" || dart1.value == "T" || dart1.value == "D"){
                dart1.value = value;
                break;
            }
            else if(dart2.value == "" || dart2.value == "T" || dart2.value == "D"){
                dart2.value = value;
                break;
            }
            else if(dart3.value == "" || dart3.value == "T" || dart3.value == "D"){
                dart3.value = value;
                break;
            }
            break;

        case '25':
            if(dart1.value == "" || dart1.value == "D" || dart1.value == "T"){
                if(dart1.value == "T"){
                    dart1.value = value;
                    break;
                }
                dart1.value = dart1.value + value;
                break;
            }
            else if(dart2.value == "" || dart2.value == "D" || dart2.value == "T"){
                if(dart2.value == "T"){
                    dart2.value = value;
                    break;
                }
                dart2.value = dart2.value + value;
                break;
            }
            else if(dart3.value == "" || dart3.value == "D" || dart3.value == "T"){
                if(dart3.value == "T"){
                    dart3.value = value;
                    break;
                }
                dart3.value = dart3.value + value;
                break;
            }
            break;
            
        default:
            if(dart1.value == "" || dart1.value == "D" || dart1.value == "T"){
                dart1.value = dart1.value + value;
                break;
            }
            else if(dart2.value == "" || dart2.value == "D" || dart2.value == "T"){
                dart2.value = dart2.value + value;
                break;
            }
            else if(dart3.value == "" || dart3.value == "D" || dart3.value == "T"){
                dart3.value = dart3.value + value;
                break;
            }
            break;
    }
}