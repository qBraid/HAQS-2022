import os
import csv
import json
import pennylane as qml
import pennylane.numpy as np
from scipy.stats import unitary_group


def encode_data(x):
    """Non-linear encoding (transformation) of one input data vector

    Args:
        x : shape (2,) tensor containing one input data vector

    Returns:
        triple of data encoded coefficients phi_1, phi_2, phi_{1,2}
    """

    return x[0], x[1], (np.pi - x[0]) * (np.pi - x[1])


def feature_map(x, meas=False):
    """Short depth feature map with entanglement

    Args:
        x : shape (3,) tensor containing one encoded data vector
        meas : boolean where `True` prompts a probabilistic measurement at the end of the circuit

    Returns:
        (iff `meas = True`) shape (2,) tensor containing probability of each computational basis state
    """

    # apply series of Hadamards and diagonal phase gate compoenents
    for _ in range(2):
        qml.Hadamard(wires=0)
        qml.Hadamard(wires=1)
        qml.RX(x[0], wires=0)
        qml.RX(x[1], wires=1)
        qml.CNOT(wires=[0, 1])
        qml.RX(x[2], wires=1)
        qml.CNOT(wires=[0, 1])

    if meas:
        return qml.probs(wires=[0, 1])


def gen_label(x, f, V, delta):
    """Generate labels for data vectors

    Args:
        x : shape (3,) tensor containing one encoded data vector
        f : shape (4,4) tensor representing the chosen parity function
        V : shape (4,4) tensor representing a random unitary in SU(4)
        delta : magnitude of data seperation

    Returns:
        one of {-1, 0, +1} according to expectation value of constructed observable w.r.t. feature mapped state
    """

    obs = np.conj(V).T @ f @ V  # constructed observable

    dev = qml.device("default.qubit", wires=2)
    fm_circuit = qml.QNode(feature_map, dev)
    fm_circuit(encode_data(x), meas=True)
    fm_state = (dev._state).flatten()  #  feature mapped state

    output = np.real(np.conj(fm_state).T @ obs @ fm_state)  # expectation value

    if output >= delta:
        return 1
    elif output <= -1 * delta:
        return -1
    else:
        return 0


def gen_data(n_points, **params):
    """Generate data vectors and associated labels

    Args:
        n_points : number of data points
        f : shape (4,4) tensor representing the chosen parity function
        V : shape (4,4) tensor representing a random unitary in SU(4)
        delta : magnitude of data seperation

    Returns:
        tuple of tensors containing data vectors Xs of shape (n_points,2) and associated labels Ys of shape (n_points,)
    """
    np.random.seed(42)

    nonzero = []

    Xs = np.zeros((n_points, 2))
    Ys = np.zeros(n_points)

    Xs = np.random.uniform(
        0, 2 * np.pi, size=(n_points, 2)
    )  # uniform distribution between [0, 2*pi)
    Ys = np.zeros(n_points)

    for i, x in enumerate(Xs):
        Ys[i] = gen_label(x, **params)  # assign labels
        if Ys[i] in [1.0, -1.0]:
            nonzero.append(i)

    return Xs[nonzero], Ys[nonzero]


if __name__ == "__main__":

    SAVE_PATH = "data/"

    Z = np.array([[1, 0], [0, -1]])  # Pauli-Z operator
    f = np.array(np.kron(Z, Z), requires_grad=False)  # Parity function
    V = unitary_group.rvs(4)  # random 4x4 unitary
    delta = 0.3  # gap between data vectors (larger = easier to seperate)
    params = {"f": f, "V": V, "delta": delta}
    n_points = 10000

    Xs, Ys = gen_data(n_points, **params)

    n_nonzero = len(Xs)

    os.makedirs(SAVE_PATH, exist_ok=True)

    with open(SAVE_PATH + "binary_data.csv", mode="w") as file:
        csvwriter = csv.writer(file)

        for i in range(n_nonzero):
            csvwriter.writerow([Xs[i][0].item(), Xs[i][1].item(), Ys[i].item()])

    with open(SAVE_PATH + "params.json", mode="w") as file:
        save_params = {"f": str(f), "V": str(V), "delta": delta, "n_points": n_nonzero}
        json.dump(save_params, file)
