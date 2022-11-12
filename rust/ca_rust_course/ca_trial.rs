fn main() {
      
    // First Trial and Experiment

    println!("First Trial:");
    macro_rules! make_it {
              ( $var:ident => $($count:expr),+) => {
                  $($var.push($count);)+
              }
      }

      let mut count = vec![];

      make_it![count => u8::MIN, 1, 2];

      println!("{count:?}");

      // Second Trial
      println!("Second Trial:");
      
      let sum = {
          let number_1 = 11;
          let number_2 = 31;
          number_1 + number_2
      };

      fn sum_2() -> u32 {
          let number_1 = 11;
          let number_2 = 31;
          number_1 + number_2
      }

      println!("{sum}, or as a function, we get {}", sum_2());

      // Check scopes
      let numbah = 10;
      {
          let numbah = 29;
          println!("{numbah} same variable in block");
      }
      println!("{numbah} same variable outside of block");

      // Make variables public by adding pub
      // mod defines a Module which has its own scope.

      pub struct Number {
          pub value: i32,
      }

      let mut number_3 = Number { value: 0};
      number_3.value += 1;
      println!("{}", number_3.value);

}
