#![allow(unused)]

use std::io;
use rand::Rng;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;


fn main() {
    
    // Input functions
    fn ask_for_name () {
        println!("What is your name?");
        
        let mut name: String = String::new();
        let greeting: &str = "Nice to meet you!";
        
        io::stdin().read_line(&mut name)
            .expect("Didn't receive input!");
    
        println!("Hello, {}! {}", name.trim_end(), greeting);
    }

    // ask_for_name();

    // Variable Types
    fn lesson_in_types() {
        const ONE_MIL: u32 = 1_000_000; //unsigned int of 32-bits
        const PI: f32 = 3.141592; //float
        let age: &str = "47"; //string
        let mut age: u32 = age.trim().parse()
            .expect("Age wasn't assigned a number");
        age = age + 1;

        println!("I'm {} and I want ${}!", age, ONE_MIL);

        // Unsigned integers: u8, u16, u32, u64, u128, usize
        // Signed integers: i8, i16, i32, i64, i128, isize

        // Get maximums
        println!("Max u32 : {}", u32::MAX);
        println!("Max u64 : {}", u64::MAX);
        println!("Max usize : {}", usize::MAX);
        println!("Max u128 : {}", u128::MAX);
        println!("Max f32 : {}", f32::MAX);
        println!("Max i32 : {}", i32::MAX);
        println!("Max i64 : {}", i64::MAX);
        println!("Max i128 : {}", i128::MAX);
        println!("Max isize : {}", isize::MAX);

        let is_true= true;
        let is_char = 'A';

        let num_1: f32 = 1.111111111111111;
        println!("f32 : {}", num_1 + 0.111111111111111);
        let num_2: f64 = 1.111111111111111;
        println!("f64 : {}", num_2 + 0.111111111111111);

        let num_3 = 5;
        let num_4: u32 = 4;

        println!("5 + 4 = {}", num_3 + num_4);
        println!("5 - 4 = {}", num_3 - num_4);
        println!("5 * 4 = {}", num_3 * num_4);
        println!("As integer: 5 / 4 = {}", num_3 / num_4);
        println!("5 % 4 = {}", num_3 % num_4);
        let num_3 = u32::pow(num_3, num_4);
        println!("5 ^ 4 = {}", num_3);

        //random range bound is (inclusive..exclusive)
        //the below goes from 1 to 100
        let random_num = rand::thread_rng().gen_range(1..101); 
        println!("A random number: {}", random_num);

    }        

    // lesson_in_types();

    fn lessons_in_conditionals() {

        println!("Please input an age:");

        let mut age: i32 = 0;
        let mut age_string: String = String::new();
        io::stdin().read_line(&mut age_string)
            .expect("Didn't receive input!");
        
        age = age_string.trim().parse().expect("Not a valid number!");
        
        if (age >= 1) && (age < 18){
            println!("You're a baby!");
        } else if (age == 27) || (age == 22) {
            println!("You're either Matt or Aimee...")
        } else if age >= 65 {
            println!("You're a boomer!");
        } else {
            println!("Age ain't nuffin special.");
        }

        let can_vote: bool = if age >= 18 {
            true
        } else {
            false
        };

        if can_vote {
            println!("This person is old enough to vote!")
        } else {
            println!("Can't vote!")
        };

        //alternatively
        match age {
            1..=17 => println!("You're a baby!"), // the = includes 17
            27 | 22 => println!("You're either Matt or Aimee..."),
            65..=i32::MAX => println!("You're a boomer!"),
            _ => println!("Age ain't nuffin special."),
        };

        let voting_age: i32 = 18;

        match age.cmp(&voting_age){
            Ordering::Less => println!("Can't vote!"),
            Ordering::Greater => println!("This person is old enough to vote!"),
            Ordering::Equal => println!("You gained the right to vote!"),
        };

    }

    lessons_in_conditionals();

}
