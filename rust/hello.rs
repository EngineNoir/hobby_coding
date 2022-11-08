fn main() {
    

    fn say_something() {
        let answer = "Solution";
        println!("Print the {answer}");
    
        println!("This element is {0}, and this one the {1}", "First", "Second");
        let pi = 3.14159;
        println!("pi is {0:.3}", pi);
    }

    say_something();

    fn return_an_answer() -> String {
        let answer = "Solution".to_string();
        answer
    }

    println!("{}", return_an_answer());

}
