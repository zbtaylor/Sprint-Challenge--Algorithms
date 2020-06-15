#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n^3)
Number of steps increases by the cube of n

b) O(log(n) \* n)
The inner while loop is logarithmic, but it has to run n times

c) O(n)
Counts down by one from n and does nothing more than addition the entire time

## Exercise II

Assuming you know the number of floors in the building, I would:

Start halfway up, drop an egg
If it breaks, I know I'm too high
I'd then go to the floor half way between the floor I'm on and the ground floor
and repeat the process
If it doesn't break, I can go higher
Now I go to the floor half way between the floor I'm on and the top floor
and repeat the process
All the while I track the most recent floor that the dropped egg broke from
Repeat until no floor remains to be tested
By the end, the most recent floor to have broken an egg is found to be the limit

The runtime complexity is logarithmic.
