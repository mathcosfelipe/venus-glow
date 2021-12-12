use std::io::{stdin};

fn date_between_the_last_inferior_conjunction(){

}

fn angle_venus_sun_earth(){

}

fn angle_sun_venus_earth(){

}

fn angle_sun_earth_venus(){

}

fn distance_earth_venus(){
    let mut distance_earth_venus: String = String::new();
    stdin().read_line(&mut &mut distance_earth_venus).expect("Did not enter a correct string!");
    let value_distance_earth_venus: f64 = distance_earth_venus.trim().parse().expect("Invalid option. Try again.");
    print!("{}", value_distance_earth_venus);
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