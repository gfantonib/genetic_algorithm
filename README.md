# genetic_algorithm

<div align="center">
  <img src="image/holland.jpg" alt="holland">
</div>

John Henry Holland (February 2, 1929 – August 9, 2015) was an American scientist and professor of psychology and electrical engineering and computer science at the University of Michigan, Ann Arbor. He was a pioneer in what became known as genetic algorithms.

### Description
This algorithm generates, after several iterations, a resulting vector that can guess, with a certain probability, the characteristic of an element of a database.

Example: If I have a database provided by a bank that contains several variables from the clients and indicates, for each client, whether they are compliant or defaulting, this resulting vector can predict if a future client is going to be (with a certain probability) compliant or defaulting.

The name is 'genetic' because I will consider a vector to be a chromosome. This chromosome, initially random, will evolve across generations (iterations) by reproducing and mutating.

---

This implementation is based on lectures by Professor Ricieri from ITA on the topic of Big Data and Machine Learning, presented at the [Prandiano Museu da Matemática](https://www.prandiano.com.br/).
