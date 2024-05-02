from qiskit import *
from qiskit_aer import AerSimulator

# Code starts here ----

# Create a Quantum Register with 3 qubits
qr = QuantumRegister(2, "q")

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(qr)

# circuit.h(0)
circuit.h(0)
circuit.cx(0, 1)
circuit.x(0)

# circuit.y(0)
# circuit.h(0)

## Measure the qubits ----

# Map the quantum measurement to the classical bits
circuit.measure_all()

# Use Aer's AerSimulator
simulator = AerSimulator()

# Compile the circuit for the support instruction set (basis_gates)
# and topology (coupling_map) of the backend
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the aer simulator
job = simulator.run(compiled_circuit, shots=100)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print(f"\nthe format is 'bits : probability' {counts}")

print(circuit)
