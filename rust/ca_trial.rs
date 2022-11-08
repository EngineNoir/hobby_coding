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

}
