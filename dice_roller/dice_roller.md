# Dice Roller

## Description

A Program that uses qubits and quantum gates to randomize a number from 1 to 6

## Representation

```
        ┌───┐ ░ ┌─┐
   q_0: ┤ H ├─░─┤M├──────
        ├───┤ ░ └╥┘┌─┐
   q_1: ┤ H ├─░──╫─┤M├───
        ├───┤ ░  ║ └╥┘┌─┐
   q_2: ┤ H ├─░──╫──╫─┤M├
        └───┘ ░  ║  ║ └╥┘
meas: 3/═════════╩══╩══╩═
                 0  1  2
```

## How it works

The dice roller program aims to simulate the function of a physical dice roller, where a random number between 1 and 6 is generated. It utilizes three qubits, each capable of being in two states: 0 and 1. This allows for a total of 8 possible outcomes. If the result is 0 or 7, the dice is automatically rerolled.

### The Hadamard Gate

To introduce randomness into the number generation process, a Hadamard gate is applied to each qubit, placing it in a superposition between 0 and 1. This means that each qubit has a 50% chance of collapsing to either 0 or 1. Here are a few examples of possible results:

- 111
- 110
- 000
- 101

Once the binary number is obtained, it is translated and displayed in the terminal.
