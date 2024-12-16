from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
import matplotlib.pyplot as plt

# Step 1: Create a simple quantum circuit
qc = QuantumCircuit(2, 2)  # 2 qubits and 2 classical bits

# Apply a Hadamard gate on the first qubit
qc.h(0)

# Apply a CNOT gate (controlled-X) on the two qubits (control=0, target=1)
qc.cx(0, 1)

# Measure both qubits and store the result in the classical bits
qc.measure([0, 1], [0, 1])

# Step 2: Visualize the quantum circuit
circuit_drawer(qc, output='mpl')  # Use 'mpl' for a matplotlib diagram

plt.show()
