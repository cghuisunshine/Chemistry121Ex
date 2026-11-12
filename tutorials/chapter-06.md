# Interactions Between Light and Matter
> Connect wavelength and photon energy to electron emission, atomic transitions, and spectra.

## 6.1 Learning Objectives
Convert among wavelength, frequency, and photon energy; interpret the photoelectric effect; distinguish absorption from emission; and connect discrete spectral lines to energy differences. Track whether an energy is per photon, per electron, or per mole.

## 6.2 The Nature of Light
Light is electromagnetic radiation: oscillating electric and magnetic fields that propagate through space. In vacuum its speed is `c = λν = 2.99792458 × 10⁸ m s⁻¹`. Frequency remains fixed when light crosses a stationary interface, while its speed and wavelength can change in a medium.

For vacuum wavelength 500 nm, ν = (2.998 × 10⁸)/(500 × 10⁻⁹) = 6.00 × 10¹⁴ s⁻¹. Converting nanometres to metres before substitution avoids a factor-of-a-billion error.

## 6.3 The Electromagnetic Spectrum
In order of increasing frequency and photon energy, the regions are radio, microwave, infrared, visible, ultraviolet, X-ray, and gamma ray. Wavelength decreases in that order. Visible light spans approximately 400–700 nm; the boundaries are approximate rather than abrupt physical divisions.

The type of transition that a photon can induce depends on the material's energy levels and selection rules. Infrared often probes molecular vibrations; visible and ultraviolet often probe electronic transitions. A region label alone does not determine every possible interaction.

## 6.4 Continuous Spectrum of Light
A continuous spectrum contains a broad, uninterrupted range of wavelengths. Thermal radiation from a hot dense source is a familiar example. An atomic line spectrum instead contains distinct wavelengths associated with specific energy gaps.

A spectrum observed through a sample can have absorption dips within a continuous source spectrum. Separate the source's output from the sample's effect: missing wavelengths in transmitted light identify energies absorbed by the sample.

## 6.5 Wave-Particle Duality of Light
Light shows wave behaviour in interference and diffraction, while energy exchange occurs in quanta called photons. Each photon has `E = hν = hc/λ`. Its momentum in vacuum is p = h/λ.

### Worked example: a 450 nm photon
E = (6.626 × 10⁻³⁴)(2.998 × 10⁸)/(450 × 10⁻⁹) = 4.41 × 10⁻¹⁹ J per photon, or 2.76 eV. Multiplying by Avogadro's constant gives 266 kJ mol⁻¹ of photons. Do not label the single-photon value kJ mol⁻¹ without that conversion.

## 6.6 The Photoelectric Effect
In the basic one-photon model, an electron leaves a surface if the photon energy exceeds the work function Φ: `KE(max) = hν − Φ`. The threshold frequency is `ν₀ = Φ/h`, and the longest wavelength capable of emission is `λ₀ = hc/Φ`.

### Worked example: threshold and kinetic energy
For an illustrative surface with Φ = 2.00 eV, the threshold wavelength is about 620 nm. A 400 nm photon carries about 3.10 eV, giving KE(max) = 1.10 eV. A 700 nm photon carries only 1.77 eV and cannot eject an electron in this model.

Increasing intensity at a fixed above-threshold frequency normally increases the number of emitted electrons, not their maximum kinetic energy. Increasing frequency raises the maximum kinetic energy. The stopping-potential magnitude satisfies `eV(stop) = KE(max)`.

## 6.7 Light Absorbed or Emitted During Electronic Transitions
For absorption from a lower to a higher level, the system's energy change is `ΔE = E(final) − E(initial) > 0`, and the absorbed photon has E = ΔE. In emission, the system's ΔE is negative while the outgoing photon still has positive energy `E(photon) = |ΔE|`.

### Worked example: hydrogen n = 3 → 2
E₃ ≈ −1.51 eV and E₂ ≈ −3.40 eV. The atom changes energy by −1.89 eV, emitting a photon of +1.89 eV. Its wavelength is approximately (1240 eV nm)/(1.89 eV) = 656 nm. A negative wavelength would signal an incorrect sign convention.

## 6.8 Absorption and Emission Spectroscopy
Absorption spectroscopy measures which wavelengths a sample removes from incident radiation. Emission spectroscopy measures wavelengths the sample releases after excitation. The same pair of levels has the same gap in either direction, although actual spectral intensities depend on populations and transition probabilities.

For quantitative absorption work, `A = log₁₀(I₀/I)`. Where the Beer–Lambert model applies, `A = εbc`, with path length b, concentration c, and molar attenuation coefficient ε. If ε has units L mol⁻¹ cm⁻¹, use b in cm and c in mol L⁻¹; A is dimensionless. Mixtures, scattering, and chemical changes can complicate interpretation.

## 6.9 Atomic Spectroscopy
Atoms have discrete electronic energies, producing characteristic line spectra. For hydrogen-like species, `1/λ = R Z² |1/n(low)² − 1/n(high)²|`, with R approximately 1.097 × 10⁷ m⁻¹. This simple expression does not describe arbitrary multi-electron atoms.

Hydrogen transitions ending at n = 1 form the Lyman series, those ending at n = 2 the Balmer series, and those ending at n = 3 the Paschen series. As upper levels approach the ionization limit, adjacent lines converge because the energy levels become closer together.

## Practice
::: Which has higher photon energy: 350 nm or 700 nm light?
350 nm light. Because E = hc/λ, halving the wavelength doubles the energy per photon. Intensity is a separate quantity.
:::

::: A sample transmits 10% of the incident intensity. What is A?
I/I₀ = 0.10, so A = log₁₀(10) = 1.00. Transmitting 1% would give A = 2.00.
:::

::: Can increasing the intensity of below-threshold light produce photoelectrons in the basic model?
No. Each photon still has insufficient energy. The introductory one-photon model excludes multiphoton effects, which require a different treatment.
:::
