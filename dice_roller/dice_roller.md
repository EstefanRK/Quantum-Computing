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