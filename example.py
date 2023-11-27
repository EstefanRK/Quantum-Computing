from qiskit import *
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Use Aer's AerSimulator
simulator = AerSimulator()

# Create a Quantum Register with 3 qubits
qr = QuantumRegister(1, "q")

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(qr)


circuit.x(0)  # Add a NOT gate on the first qubit

# Map the quantum measurement to the classical bits
circuit.measure_all()

# Compile the circuit for the support instruction set (basis_gates)
# and topology (coupling_map) of the backend
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the aer simulator
job = simulator.run(compiled_circuit, shots=100)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print(f"\nThe odds for the qubit to be a 1 or a 0 is: {counts}")

print(circuit)
