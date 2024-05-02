from qiskit import *
from qiskit_aer import AerSimulator

# Step 0
s = "110101"
n = len(s)

circuit = QuantumCircuit(n + 1, n)

circuit.x(n)  # the n+1 qubits are indexed 0...n, so the last qubit is index n

circuit.barrier()  # just a visual aid for now

# Step 1

circuit.h(
    range(n + 1)
)  # range(n+1) returns [0,1,2,...,n] in Python. This covers all the qubits

circuit.barrier()  # just a visual aid for now

# Step 2

for ii, yesno in enumerate(reversed(s)):
    if yesno == "1":
        circuit.cx(ii, n)

circuit.barrier()  # just a visual aid for now

# Step 3

circuit.h(
    range(n + 1)
)  # range(n+1) returns [0,1,2,...,n] in Python. This covers all the qubits

circuit.barrier()  # just a visual aid for now

circuit.measure(
    range(n), range(n)
)  # measure the qubits indexed from 0 to n-1 and store them into the classical bits indexed 0 to n-1


# Use Aer's AerSimulator
simulator = AerSimulator()

# Compile the circuit for the support instruction set (basis_gates)
# and topology (coupling_map) of the backend
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the aer simulator
job = simulator.run(compiled_circuit, shots=1)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print(f"\nthe format is 'bits : probability' {counts}")

print(circuit)
