# Fundamentals of Quantum Mechanics
> Use standing waves to understand allowed states, probability, and discrete energy levels.

## 4.1 Wave-like Properties of Matter
Electrons and other particles can produce interference and diffraction. Their de Broglie wavelength is `λ = h/p`, where h = 6.62607015 × 10⁻³⁴ J s and p is momentum. For nonrelativistic motion, p = mv. A larger momentum means a shorter wavelength.

### Worked example: electron wavelength
For an electron moving at 1.00 × 10⁶ m s⁻¹, p = (9.109 × 10⁻³¹ kg)(1.00 × 10⁶ m s⁻¹). Therefore λ = 7.27 × 10⁻¹⁰ m = 0.727 nm. This is a scale on which wave behaviour matters in chemistry. The same calculation for a macroscopic object gives an extremely small wavelength.

## 4.2 Wave Concepts
A wave has a spatial pattern and a time dependence. **Amplitude** measures its displacement or wavefunction magnitude, **wavelength** λ is the distance between equivalent phase points, and **frequency** ν is the number of cycles per second. **Phase** specifies where a point lies in the cycle.

For a travelling wave, `v = λν`. Superposition means adding amplitudes, including their signs or complex phases. It is the resulting amplitude that is squared to obtain an intensity or probability density where the relevant model calls for that.

## 4.3 Transverse Wave Characteristics
In a transverse mechanical wave, displacement is perpendicular to the direction of propagation. Crests and troughs have opposite signs relative to equilibrium. The period is `T = 1/ν`, measured in seconds; frequency is measured in hertz, s⁻¹.

For a wave with λ = 0.50 m and ν = 4.0 Hz, v = 2.0 m s⁻¹ and T = 0.25 s. Doubling frequency at fixed speed halves the wavelength. A quantum wavefunction is not literally a vibrating rope, but rope waves provide a useful analogy for nodes and phase.

## 4.4 Standing Waves
Standing waves arise from superposition of waves travelling in opposite directions. In a string fixed at both ends, the endpoints must be nodes, so an integer number of half-wavelengths fits into length L: `L = nλ/2`, with n = 1, 2, 3, … .

The nth pattern has n half-wavelengths and n − 1 internal nodes. Boundary conditions exclude arbitrary wavelengths. This idea will produce quantized energies when the standing-wave pattern describes a confined particle.

## 4.5 Wave-like Behaviour and Probability
The wavefunction ψ is a probability amplitude. The probability density is `|ψ|² = ψ*ψ`, which is nonnegative. In one dimension, the probability of finding a particle from a to b is `P(a to b) = ∫ₐᵇ |ψ(x)|² dx`.

A normalized wavefunction has total probability one. A negative value of a real ψ is a phase sign, not a negative probability. Two states can have similar densities yet differ in phase and therefore behave differently in interference.

## 4.6 Heisenberg Uncertainty Principle
For position and momentum along the same axis, `Δx Δpₓ ≥ ℏ/2`, where ℏ = h/(2π). The Δ values are statistical spreads in repeated measurements on identically prepared systems. Confining a particle more tightly requires a broader momentum distribution.

### Worked example: localization limit
If Δx = 1.00 × 10⁻¹⁰ m, then Δpₓ ≥ 5.27 × 10⁻²⁵ kg m s⁻¹. For an electron this implies Δvₓ ≥ 5.79 × 10⁵ m s⁻¹ in the nonrelativistic model. This is an intrinsic state property, not merely a statement about poor instruments.

## 4.7 Classical Particle-in-a-Box Model
In the one-dimensional classical model, a particle moves freely between perfectly reflecting walls. Its kinetic energy can take any nonnegative value. For a particle moving at constant nonzero speed, equal-length intervals contain equal fractions of its travel time, so the time-averaged position distribution is uniform.

Classical physics permits a particle at rest with zero kinetic energy. The quantum infinite-well model instead requires a nonzero lowest energy because a confined wavefunction must satisfy boundary conditions.

## 4.8 Quantum Mechanics Basics
A quantum state is described by a wavefunction. Observables are associated with operators. An eigenstate of an operator has a definite corresponding measurement value; a general state can be a superposition of eigenstates and yield several possible results.

For energy eigenstates, the probabilities are stationary even though the wavefunction has a time-dependent phase. Avoid picturing an orbital or box eigenstate as a tiny particle following a definite classical path.

## 4.9 Schrödinger Equation
The time-independent equation is `Ĥψ = Eψ`. For a particle in one dimension, the Hamiltonian is `Ĥ = −(ℏ²/2m)(d²/dx²) + V(x)`. The first term represents kinetic energy and the second potential energy.

Solving the equation means finding allowed wavefunctions and energies that also satisfy the physical boundary conditions and normalization. E is an eigenvalue, not a freely chosen constant for every trial function.

## 4.10 Quantum Particle-in-a-Box Model
For an infinite well from x = 0 to x = L, V = 0 inside and is infinite outside. The wavefunction vanishes at the walls and outside. The normalized stationary states are `ψₙ(x) = √(2/L) sin(nπx/L)` for n = 1, 2, 3, … .

Allowed wavelengths are `λₙ = 2L/n`. The state n = 0 is excluded because it gives the zero function everywhere and cannot be normalized. The sinusoidal model applies to this idealized one-dimensional well, not directly to every atomic orbital.

## 4.11 Wavefunctions and Probability Distributions
For the box, `|ψₙ|² = (2/L) sin²(nπx/L)`. The nth state has n − 1 internal nodes. At a node, density is zero. Probability over a finite region comes from the area under the density curve; the density at a point is not itself a finite probability.

### Worked example: the box centre
At x = L/2, ψ₁ is maximal in magnitude, while ψ₂ = 0. The n = 2 state has a central node. Both states nevertheless have an average position of L/2 by symmetry. Average position and most probable region are different ideas.

## 4.12 Energy Quantization
For the infinite well, `Eₙ = n²h²/(8mL²)`. Increasing n raises energy quadratically; increasing mass lowers all levels, and doubling L reduces each energy to one quarter. The ground-state energy E₁ is greater than zero.

### Worked example: a 1.00 nm electron box
Using the electron mass gives E₁ = 6.02 × 10⁻²⁰ J = 0.376 eV. E₂ = 4E₁ = 1.50 eV, so the n = 1 → 2 energy gap is 3E₁ = 1.13 eV. A transition uses the difference between levels, not the upper level's energy alone.

## 4.13 Superpositions of Wavefunctions
A normalized state can be written `Ψ = c₁ψ₁ + c₂ψ₂ + …`, using an orthonormal basis. The probability of measuring energy Eₙ is |cₙ|², with the probabilities summing to one. Relative phase matters: `|ψ₁ + ψ₂|²` includes cross terms and is not generally `|ψ₁|² + |ψ₂|²`.

For an equal superposition of two energy eigenstates, Ψ = (ψ₁ + ψ₂)/√2 at a chosen time, each energy has probability 1/2. The mean energy is (E₁ + E₂)/2, even though an individual energy measurement yields one allowed eigenvalue. Different energy components evolve with different phases.

## 4.14 Review of Important Quantum Mechanics Concepts
Follow the chain: **confinement → boundary conditions → allowed wavefunctions → allowed energies → probabilities**. Distinguish ψ from |ψ|², energy from an energy gap, and a superposition from an incoherent statistical mixture.

Useful constants are h = 6.62607015 × 10⁻³⁴ J s, ℏ ≈ 1.05457 × 10⁻³⁴ J s, mₑ ≈ 9.109 × 10⁻³¹ kg, and 1 eV = 1.602176634 × 10⁻¹⁹ J. Use SI units before substituting into box-energy formulas.

## Practice
::: How many internal nodes does the n = 4 box state have?
Three. In general there are n − 1 internal nodes; the two boundary nodes are not included in that count.
:::

::: What happens to the n = 1 → 2 gap if the box length doubles?
The gap is proportional to 1/L², so it becomes one quarter of its original value. The particle mass and the two quantum numbers are held fixed.
:::

::: A state is (√3/2)ψ₁ + (1/2)ψ₂. What are its energy probabilities?
P(E₁) = 3/4 and P(E₂) = 1/4. The squared magnitudes sum to one. Its mean energy is (3/4)E₁ + (1/4)E₂.
:::
