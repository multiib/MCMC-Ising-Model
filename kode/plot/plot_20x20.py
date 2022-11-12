import numpy as np
import matplotlib.pyplot as plt
import pyarma as pa

"""Load data"""

# ENERGY
E = pa.mat()  # Create pa.mat object (just as arma::mat in C++)
E.load("./plot/binary_data/20x20_E_mean.bin")
E = np.array(E)  # Convert to numpy array

# MAGNETIZATION
M = pa.mat()  # Create pa.mat object (just as arma::mat in C++)
M.load("./plot/binary_data/20x20_M_mean.bin")
M = np.array(M)  # Convert to numpy array

#energy per spin
e_1 = pa.mat()
e_24 = pa.mat()
e_1.load("./plot/binary_data/20x20_1_e.bin")
e_24.load("./plot/binary_data/20x20_24_e.bin")
e_1 = np.array(e_1)
e_24 = np.array(e_24)

"""
MATRIX INDICES (Temprature, Initial state)
0: T = 1, Random  |  1: T = 1, Ordered |  2: T = 2.4, Random |  3: T = 2.4, Ordered
"""

n_cycles = len(E[0])

"""Plot"""

# ENERGY PLOT T = 1
fig = plt.figure(figsize=(6, 4.5))

plt.plot(
    np.arange(n_cycles),
    E[0],
    "-",
    color="#8a1629",
    linewidth=2.0,
    alpha=0.8,
    label="T = 1, Random",
)
plt.plot(
    np.arange(n_cycles),
    E[1],
    "-",
    color="#8b8229",
    linewidth=2.0,
    alpha=0.8,
    label="T = 1, Ordered",
)

plt.xlabel("Monte Carlo cycles")
plt.ylabel("Energy, expected values")
plt.legend()
plt.grid()

plt.savefig("plot/figures/20x20_1_E.pdf")

# ENERGY PLOT T = 2.4
fig = plt.figure(figsize=(6, 4.5))
plt.plot(
    np.arange(n_cycles),
    E[2],
    "-",
    color="#2c1629",
    linewidth=2.0,
    alpha=0.8,
    label="T = 2.4, Random",
)
plt.plot(
    np.arange(n_cycles),
    E[3],
    "-",
    color="#4d8229",
    linewidth=2.0,
    alpha=0.8,
    label="T = 2.4, Ordered",
)

plt.xlabel("Monte Carlo cycles")
plt.ylabel("Energy, expected values")
plt.legend()
plt.grid()

plt.savefig("plot/figures/20x20_24_E.pdf")


# MAGNETIZATION PLOT T = 1
fig = plt.figure(figsize=(6, 4.5))

plt.plot(
    np.arange(n_cycles),
    M[0],
    "-",
    color="#8a1629",
    linewidth=2.0,
    alpha=0.8,
    label="T = 1, Random",
)
plt.plot(
    np.arange(n_cycles),
    M[1],
    "-",
    color="#8b8229",
    linewidth=2.0,
    alpha=0.8,
    label="T = 1, Ordered",
)
plt.xlabel("Monte Carlo cycles")
plt.ylabel("Magnetization, expected values")
plt.legend()
plt.grid()

plt.savefig("plot/figures/20x20_1_M.pdf")

# MAGNETIZATION PLOT T = 2.4
fig = plt.figure(figsize=(6, 4.5))
plt.plot(
    np.arange(n_cycles),
    M[2],
    "-",
    color="#2c1629",
    linewidth=2.0,
    alpha=0.8,
    label="T = 2.4, Random",
)
plt.plot(
    np.arange(n_cycles),
    M[3],
    "-",
    color="#4d8229",
    linewidth=2.0,
    alpha=0.8,
    label="T = 2.4, Ordered",
)

plt.xlabel("Monte Carlo cycles")
plt.ylabel("Magnetization, expected values")
plt.legend()
plt.grid()

plt.savefig("plot/figures/20x20_24_M.pdf")


#Energy histogram T = 1
counts, bins = np.histogram(e_1, bins = 400)
fig = plt.figure(figsize=(6, 4.5))
plt.stairs(counts, bins)
plt.savefig("plot/figures/20x20_1_pdf.pdf")

#Energy histogram T = 2.4
counts, bins = np.histogram(e_24, bins = 400)
fig = plt.figure(figsize=(6, 4.5))
plt.stairs(counts, bins)
plt.savefig("plot/figures/20x20_24_pdf.pdf")
