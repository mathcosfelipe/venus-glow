use std::io::{stdin,stdout,Write};

fn main() {
    
    let mut information = String::new();
    print!("What information do you have?: \n 1) ");
    let _error = stdout().flush();
    stdin().read_line(&mut information).expect("Did not enter a correct string");
    
    println!("You typed: {}", information);

}