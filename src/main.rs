use std::io::{stdin};

mod math{
    pub fn acos(){}
}

use math::acos;

fn date_between_the_last_inferior_conjunction(){

}

fn angle_venus_sun_earth(){

}

fn angle_sun_venus_earth(){

}

fn angle_sun_earth_venus(){

}

fn distance_earth_venus(){

    let mut str_error: &str;
    let mut integer_error: u8;
    
    let mut psi: f64 = 0.0; 
    let mut phi: f64 = 0.0; 
    let mut theta: f64 = 0.0; 
    let mut tau: f64 = 0.0; 
    let mut upsilon: f64 = 0.0; 
    
    const beta: f64 = 10.81;
    const gama: f64 = 14.95;

    let mut distance_earth_venus: String = String::new();
    stdin().read_line(&mut distance_earth_venus).expect("Did not enter a correct string!");
    let mut value_distance_earth_venus: f64 = distance_earth_venus.trim().parse().expect("Invalid option. Try again.");
    let power: u64 = u64::pow(10, 7);
    value_distance_earth_venus = value_distance_earth_venus / power as f64;

    if value_distance_earth_venus == 25.76{
        str_error = "conjusup";
    }else if value_distance_earth_venus > 25.76{
        integer_error = 2;
    }else if value_distance_earth_venus == 4.14{
        str_error = "conjuinf";
    }else if value_distance_earth_venus < 4.15{
        integer_error = 2;    
    }else{

    }

}

fn main(){

    let mut information: String = String::new();
    println!("Wich information do you have? \n 1) distance Earth-Venus \n 2) angle Sun-Earth-Venus \n 3) angle Sun-Venus-Earth \n 4) angle Venus-Sun-Earth \n 5) date between the last inferior conjunction (2020-06-03) and the next (2022-01-08) \n Input the corresponding number: ");
    stdin().read_line(&mut information).expect("Did not enter a correct string!");
    let option: u8 = information.trim().parse().expect("Invalid option. Try again.");

    if option == 1{
        distance_earth_venus();
    }else if option == 2{
        angle_sun_earth_venus();
    }else if option == 3{
        angle_sun_venus_earth();
    }else if option == 4{
        angle_venus_sun_earth();
    }else if option == 5{
        date_between_the_last_inferior_conjunction();
    }else{
        println!("Invalid option. Try again.");
        main();
    }

}