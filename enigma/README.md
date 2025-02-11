This Enigma machine was made for a University of Bath Artificial Intelligence MSc assignment and solved various provided Enigma codes. The end mark for this work was 80%.

### Index of Coincidence

While initially solving Code 5, I failed to find an answer using my initial crib guesses and I started to doubt my Enigma and Code 5 solver implementations. After double checking both, I decided to look for a similarity measure as a way to identify the crib using targeted guesses.

I utilised the index of coincidence (IoC) to narrow down the crib. Letters appear in the English language with certain average frequencies, so it's possible to measure letter frequencies in partially decrypted strings to understand whether an Enigma machine's settings are likely partially correct. The IoC measures the closeness of the letter frequency distribution to the uniform distribution, and I used the following formula:

$$IoC=\frac{26 \sum^Z_{i=A}{f_i(f_i-1)}}{N(N-1)}$$

The IoC of English language text is around $1.73$, so I calculated it and printed all results where the IoC was greater than $1.6$, and manually scanned through these strings for substrings that partially matched social media platform names I had in mind. I noticed the string "INST" a few times which prompted me to explore "INSTAGRAM" being the correct crib.

#### References

1. University of Southampton, 2024. Index of Coincidence [Online]. Available from: https://www.southampton.ac.uk/~wright/1001/index-of-coincidence.html [Accessed 25 October 2024].

### Parallel Processing

I implemented parallel processing for code 3 for two reasons:

1. out of curiosity to learn how it's done in Python
2. code 3 has the largest search space of the code breaking problems, with up to $3 \times {}_{4}P_{3} \times 8^3 = 36,864$ configurations to check, and took approximately 4 minutes to complete

Python has features that allow the use of more than one processor by the application. Implementing parallel processing means the code breaking application can test multiple Enigma settings concurrently, reducing execution time.

I chose to implement a very simple parallelisation of the code breaking algorithm, assigning each reflector to a separate thread. This means that, if the operating system allocates 3 threads to the application, each thread will handle at most $\frac{36864}{3}$ simulations instead of at most $36864$. The algorithm terminates early if the correct configuration is found, and with these changes the algorithm is able to find the correct settings in approximately 55 seconds. This result can be recreated by running _enigma/decryption/code3parallel.py_.

This horizontal scalability would be especially important if we were brute forcing a larger number of configurations.

### Logging Service

I have implemented a package level logging service to provide control over when and where logs detailing the Enigma machine's inner workings are displayed. By default, the logs are output to a file called "enigma.log" and can be viewed retrospectively as needed. Besides precise control over logging, this has 2 further benefits:

1. performance - many print statement executions significantly slow down an application and the logging module enables us to work around the performance hit using features like buffering
2. persistence - the logs won't disappear on closing the terminal, and they are more easily shared and debugged i.e. in any text editor

### Configuration from Files

I have implemented a JSON config file loader to support easy Enigma config data injection. This is a powerful feature as it allows users of the machine to experiment with new kinds of rotors and reflectors without needing to modify the code directly, meaning the barrier to entry to using advanced features of this simulator is lowered. This could also be extended to fetch configurations from e.g. a web server, unlocking even more dynamic configuration possibilities.

Given configurations are loaded up front using a standard JSON decoder, and given that the configurations have a small memory footprint, there's no concern around time or space complexity relating to this behaviour.

### Unit Testing

Each behaviour is thoroughly unit tested beyond the assertions made in this notebook. This greatly improves the maintainability and extensibility of this simulator by giving future contributors confidence in the correct operation of each component of this complex simulated machine.
