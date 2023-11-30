from qiskit import *
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Code starts here ----

# Create a Quantum Register with 3 qubits
qr = QuantumRegister(3, "q")

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(qr)

circuit.h(0)
circuit.h(1)
circuit.h(2)

## Measure the qubits ----

# Map the quantum measurement to the classical bits
def roll_dice():
    circuit.measure_all()

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
    result_dict = counts

    # Extract the key using the keys() method
    key_list = list(result_dict.keys())

    # If you only have one key, you can access it directly
    key = key_list[0]
    answer = int(key, 2)
    return answer

print(roll_dice())
