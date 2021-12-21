mod math{
    pub fn acos(){}
}

use math::acos;

pub fn distance_earth_venus(){

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
        psi = acos();
    }

}