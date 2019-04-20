from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
from qiskit import Aer, IBMQ
from qiskit.providers.aer import noise
import matplotlib


# Authentication
IBMQ.save_account('nice try :) ')
IBMQ.load_accounts()

# Device selection
device = IBMQ.get_backend('ibmq_16_melbourne')
properties = device.properties()
coupling_map = device.configuration().coupling_map

# Noise model
noise_model = noise.device.basic_device_noise_model(properties)
basis_gates = noise_model.basis_gates

# Circuit definition
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

# Circuit initialization
qc.h(q[0])
qc.cx(q[0], q[1])
qc.measure(q, c)

# Select qasm
backend = Aer.get_backend('qasm_simulator')

# Generate x number of pairs
for x in range(1000):
    pair_sim = execute(qc, backend,
                       coupling_map=coupling_map,
                       noise_model=noise_model,
                       basis_gates=basis_gates)
    sim_result = pair_sim.result()
    print(sim_result.get_counts(qc))
