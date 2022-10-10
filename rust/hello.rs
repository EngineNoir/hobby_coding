fn main() {

    println!("Hey there, {2}! I am {1}, and you are {0}", 0, "Matt", "Aimee");
    println!("{letter:>15}", letter = "Love");

    println!("My name is {0}, {1} {0}", "Bond", "James");
    
    let number: f64 = 1.0;
    let width: usize = 5;
    println!("{number:>width$}");

    let pi = 3.14159;
    println!("pi is {0:.3}", pi);

}
