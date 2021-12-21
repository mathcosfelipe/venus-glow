use std::io::{stdin};

mod distance_earth_venus{
    pub fn distance_earth_venus(){}
}

mod angle_sun_earth_venus{
    pub fn angle_sun_earth_venus(){}
}

mod angle_sun_venus_earth{
    pub fn angle_sun_venus_earth(){}
}

mod angle_venus_sun_earth{
    pub fn angle_venus_sun_earth(){}
}

mod date_between_the_last_inferior_conjunction{
    pub fn date_between_the_last_inferior_conjunction(){}
}

use distance_earth_venus::distance_earth_venus;
use angle_sun_earth_venus::angle_sun_earth_venus;
use angle_sun_venus_earth::angle_sun_venus_earth;
use angle_venus_sun_earth::angle_venus_sun_earth;
use date_between_the_last_inferior_conjunction::date_between_the_last_inferior_conjunction;

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