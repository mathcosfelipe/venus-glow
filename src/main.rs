use std::io::{stdin,stdout,Write};

fn fifth_choice(){

}

fn fourth_choice(){

}

fn third_choice(){

}

fn second_choice(){

}

fn first_choice(){

}

fn main() {
    
    let mut information = String::new();
    print!("What information do you have?: 
    \n 1) Earth-Venus distance.
    \n 2) Sol-Earth-Venus angle.
    \n 3) Sol-Venus-Earth angle.
    \n 2) Venus-Sol-Terra angle.
    \n 5) Date - Between the last inferior conjunction (2020-06-03) and the next (2022-01-08)
    \n Just inform the correspondent number: ");
    let _error = stdout().flush();
    stdin().read_line(&mut information).expect("Did not enter a correct string");

    if information == "1"{
        first_choice();
    }else if information == "2"{
        second_choice();
    }else if information == "3"{
        third_choice();
    }else if information == "4"{
        fourth_choice();
    }else{
        fifth_choice();
    }

}