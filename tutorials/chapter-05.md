# Electronic Structure of Atoms and Ions
> Describe one-electron orbitals with quantum numbers, nodes, probability distributions, and energy levels.

## 5.1 Learning Objectives
Identify valid quantum-number sets, describe s, p, and d orbital shapes, count radial and angular nodes, and calculate energies of hydrogen-like species. Distinguish an orbital's wavefunction from its probability density and distinguish one-electron energy rules from the multi-electron rules introduced in Chapter 7.

## 5.2 One-electron Atoms and Ions
Hydrogen-like species contain exactly one electron: H, He⁺, and Li²⁺ are examples. Their electron experiences the attraction of a nucleus with charge +Ze without electron–electron repulsion. Their orbitals are solutions of the Schrödinger equation for a Coulomb potential.

Three quantum numbers label a spatial orbital:

- Principal quantum number: `n = 1, 2, 3, …`.
- Angular momentum quantum number: `ℓ = 0, 1, …, n − 1`; ℓ = 0, 1, 2, 3 correspond to s, p, d, f.
- Magnetic quantum number: `mℓ = −ℓ, …, 0, …, +ℓ`, giving 2ℓ + 1 orbitals in a subshell.

### Worked example: allowed subshells
For n = 3, allowed ℓ values are 0, 1, and 2, giving 3s, 3p, and 3d. A 3f orbital is impossible because f requires ℓ = 3 and therefore n ≥ 4. A 3d subshell contains five spatial orbitals.

## 5.3 Mid-point Summary
A **shell** has a fixed n; a **subshell** has fixed n and ℓ; an individual **orbital** additionally has a specified mℓ in the usual basis. A shell contains n² spatial orbitals, obtained by adding 1 + 3 + 5 + … + (2n − 1).

For n = 2, there is one 2s orbital and three 2p orbitals: four orbitals altogether. An orbital is a mathematical state, not an electron trajectory or a hard-walled container. The possible electron spins and occupancies are developed in Chapter 7.

## 5.4 Shapes of s, p, and d Orbitals
Orbital boundary surfaces usually enclose a chosen fraction of the electron probability. They do not mark a physical edge. Colours or plus/minus signs on orbital lobes normally show wavefunction phase, not electric charge.

For a hydrogen-like orbital, the number of angular nodes is ℓ, the number of radial nodes is `n − ℓ − 1`, and the total is n − 1. Radial nodes occur at spherical surfaces of nonzero radius; angular nodes depend on direction.

### Worked example: node counting
A 3p orbital has ℓ = 1: one angular node and 3 − 1 − 1 = one radial node, for two total nodes. A 3d orbital has two angular nodes and no radial nodes. The nucleus is not counted as an extra radial node.

## 5.4.1 s Orbitals
An s orbital has ℓ = 0 and spherical symmetry. A 1s orbital has no nodes. A 2s orbital has one spherical radial node and changes wavefunction sign across it. Higher s orbitals have additional radial nodes.

For an s state, the radial probability distribution is `P(r) = 4πr²|ψ(r)|²`. The factor 4πr² accounts for the volume of a spherical shell per unit radial thickness. Hydrogen 1s has its greatest probability density at the nucleus, but its radial probability is zero at r = 0 and reaches its maximum at the Bohr radius. Density and radial probability are different quantities.

## 5.4.2 p Orbitals
A p subshell has ℓ = 1 and three orbitals. The familiar real pₓ, pᵧ, and p𝓏 orbitals each have two lobes separated by a nodal plane through the nucleus. The lobes have opposite phases; both contribute positively to |ψ|².

The lowest p subshell is 2p. A 2p orbital has one angular node and no radial nodes; 3p adds one radial node. The x, y, z drawings are convenient real combinations of angular-momentum basis functions, so the labels should not be read as three different energies in an isolated hydrogen-like atom.

## 5.4.3 d Orbitals
A d subshell has ℓ = 2 and five orbitals. Four familiar real shapes are four-lobed: dₓᵧ, dₓ𝓏, dᵧ𝓏, and dₓ²₋ᵧ². The d𝓏² orbital has two axial lobes and a toroidal region of opposite phase.

All d orbitals have two angular nodes. For d𝓏² these are conical surfaces rather than two nodal planes. The lowest d subshell is 3d, with zero radial nodes. Different angular shapes in the same hydrogen-like shell do not by themselves imply different energies.

## 5.5 Energies of One-electron Atoms and Ions
Ignoring fine structure and small reduced-mass corrections, a hydrogen-like species has `Eₙ = −(2.1799 × 10⁻¹⁸ J) Z²/n²`, or approximately `−13.6 Z²/n² eV`. Zero energy represents an electron infinitely far from the nucleus. Bound states have negative energies; more negative means more tightly bound.

In this model, energy depends only on n and Z. Thus 2s and 2p are degenerate for the same one-electron species. This degeneracy generally does not hold in multi-electron atoms.

### Worked example: ionizing He⁺ from n = 2
For Z = 2 and n = 2, E₂ = −13.6(4)/4 = −13.6 eV. Ionizing to E = 0 requires +13.6 eV per ion. From the ground state, E₁ = −54.4 eV, so substantially more energy is needed.

## 5.6 Summary
Use quantum-number rules to decide whether a state exists, node rules to interpret its shape, and the hydrogen-like energy formula only when there is one electron. Larger Z contracts a given hydrogen-like orbital and increases binding; larger n generally increases its spatial extent and makes the energy less negative.

Before calculating, write the species, its electron count, Z, and n. That short check prevents applying the one-electron formula to neutral helium or to a multi-electron ion.

## Practice
::: Is n = 2, ℓ = 2, mℓ = 0 allowed?
No. For n = 2, ℓ can only be 0 or 1. The d subshell requires n ≥ 3.
:::

::: How many radial and angular nodes does 4d have?
ℓ = 2 gives two angular nodes. The radial count is 4 − 2 − 1 = 1. There are three nodes in total.
:::

::: Compare the n = 1 energies of H and Li²⁺.
Li²⁺ has Z = 3 and one electron, so its energy is nine times as negative: approximately −122.4 eV compared with −13.6 eV for H. Its ground-state ionization energy is correspondingly nine times larger in this model.
:::
