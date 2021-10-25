use std::io::{stdin, stdout, Write};



pub fn first_choice(){

    let mut ray = String::new();
    print!("Input the value of distance between Earth-Venus, in kilometers: ");
    let _error = stdout().flush();
    stdin().read_line(&mut ray).expect("Did not enter a correct string!");
    let ray: f64 = ray.trim().parse().expect("Invalid input.");

    ray = ray / f64::powf(10.0, 7.0);
    

}