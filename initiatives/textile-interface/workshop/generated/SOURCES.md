# Research sources and interpretations

Values in the registry are authored starting points unless explicitly identified as API/standards constraints. No source is claimed to validate these selected material values. Research checked 2026-11-06.

## S01 Irawan and Marschner 2012

Woven appearance depends on fiber reflection, yarn geometry, and weave pattern across viewing and lighting angles.

Interpretation: Model topology, yarn, and fibers separately. The selected dimensions below are authored values, not fitted measurements.

Source: https://www.cs.cornell.edu/~srm/publications/TOG12-cloth.html

## S02 Yu et al 2025 ray wave hybrid cloth

This research models reflection and transmission using simulation-informed ray and wave methods, including variation among plies.

Interpretation: Use it to understand the limits of simple cloth shading. This pack does not implement or claim equivalence to that model.

Source: https://research.nvidia.com/labs/rtr/publication/yu2025realistic/

## S03 Filament materials cloth model

Cloth shading treats sheen separately and provides specific guidance for dark velvet and ordinary cloth.

Interpretation: Use directional grazing response to distinguish materials. Filament and Three.js parameter values are not interchangeable.

Source: https://google.github.io/filament/main/materials.html

## S04 Three.js MeshPhysicalMaterial

Defines sheen, anisotropy, iridescence, and other physical material controls, with added rendering cost.

Interpretation: Map named shading fields to this API. Use r187 thickness minimum and maximum fields, not the deprecated range property.

Source: https://threejs.org/docs/pages/MeshPhysicalMaterial.html

## S05 Three.js MeshStandardMaterial

Normal and bump shading differ from geometry displacement; displacement moves vertices.

Interpretation: Keep silhouettes, thickness, protruding stitches, and lifted edges in geometry. Use maps for remaining small-scale detail.

Source: https://threejs.org/docs/pages/MeshStandardMaterial.html

## S06 Three.js color management

Color inputs and outputs require explicit color-space handling; numeric maps are non-color data.

Interpretation: Mark base color and sheen color as sRGB, numeric maps as NoColorSpace, and work in Linear-sRGB.

Source: https://threejs.org/manual/pages/color-management.html

## S07 Khronos sheen extension

Sheen color occupies RGB; sheen roughness is sampled from alpha.

Interpretation: Export separate color and numeric texture views. Retain the exact channel metadata in the asset receipt.

Source: https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_materials_sheen/README.md

## S08 Khronos anisotropy extension

Anisotropy direction is encoded in red and green, strength in blue, with a defined tangent space.

Interpretation: Preserve UV orientation and tangents. Test rotated fabric under fixed lighting before accepting a material.

Source: https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_materials_anisotropy/README.md

## S09 Macklin Muller Chentanez XPBD 2016

XPBD introduces compliance and accumulated constraint multipliers to address timestep and iteration coupling in ordinary PBD.

Interpretation: Use the distance-constraint kernel for optional drape work. Tune and test the complete solver; the kernel alone is not a cloth simulation.

Source: https://matthias-research.github.io/pages/publications/XPBD.pdf

## S10 W3C dragging movements

Dragging needs an equivalent single-pointer operation without dragging; keyboard access is a separate requirement.

Interpretation: Provide click or tap selection followed by placement controls, alongside keyboard controls.

Source: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements

## S11 W3C animation from interactions

Nonessential interaction-triggered motion can be disabled; this particular criterion is Level AAA.

Interpretation: Respect reduced motion throughout this design. Retain state changes with static visual and text feedback.

Source: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions

## S12 W3C contrast minimum

Normal text generally needs 4.5:1 contrast and qualifying large text 3:1, with stated exceptions.

Interpretation: Put live text on opaque labels and test the rendered states, not only palette swatches.

Source: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum

## S13 W3C target size minimum

The AA minimum is 24 by 24 CSS pixels subject to exceptions.

Interpretation: Select a more generous 48 by 48 CSS pixel project target. That chosen target does not establish whole-site conformance.

Source: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum

## S14 MDN context loss testing

The extension can simulate context loss and restoration for testing.

Interpretation: Keep semantic controls and data outside the canvas. Verify fallback during an active task.

Source: https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_lose_context

## S15 Undercase Type Fraunces

The font repository publishes Fraunces under OFL-1.1.

Interpretation: Use for craft-manual headings; retain the actual downloaded font license and version in production.

Source: https://github.com/undercasetype/Fraunces

## S16 IBM Plex

IBM publishes the Plex family under the Open Font License.

Interpretation: Use Plex Sans for reading and Plex Mono for compact labels. Font files are specified, not bundled in this pack.

Source: https://github.com/ibm/plex

## S17 Three.js KTX2Loader

The loader detects supported compressed formats and requires its transcoder files.

Interpretation: Use detectSupport before loading; ship transcoder assets with the same pinned Three.js release.

Source: https://threejs.org/docs/pages/KTX2Loader.html

## S18 Three.js r187 release

The release is available and the current documented material API includes r187 changes.

Interpretation: Pin three to 0.187.0 for a new implementation. Do not upgrade an existing repository without checking its lockfile and migration needs.

Source: https://github.com/mrdoob/three.js/releases/tag/r187

## S19 MDN native modal dialog

showModal opens a dialog in the top layer and makes outside document content inert.

Interpretation: Use a native dialog, an explicit close control, a useful initial focus target, and tested focus restoration.

Source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal

## S20 Three.js DirectionalLight

The light direction follows its position and target rather than its rotation.

Interpretation: Set and add the light target explicitly. Keep light intensity values as authored renderer controls, not measured daylight.

Source: https://threejs.org/docs/pages/DirectionalLight.html

## S00 Attached Keep It Moving textile interface brief

Workshop setting, four textile offerings, tactile controls, cloth motion, close-up fibers, optional sound.

Interpretation: Preserve the material ambition while specifying topology, task behavior, fallbacks, and verification.

Source: supplied attachment snapshot. Original source not refreshed or edited. Snapshot SHA-256: b3a887d1485e05ed0a1b78b8c7b3e629d24c2e0d321a2a2fb7c0003fbf42ff93

