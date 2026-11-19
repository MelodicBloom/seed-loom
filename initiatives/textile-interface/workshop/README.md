# Textile workshop research and implementation prompt suite

This suite translates the attached Keep It Moving workshop direction into named
materials, components, scenes, assets, formulas, tests and corrective work. It is
a consumer specification inside Seed Loom's Textile Interface initiative.
The current implementation contains a deterministic specification compiler and
the existing Core ThreadButton. Enhanced fabric rendering and workshop product
routes remain planned. Specification coverage must not be reported as runtime
completion or material realism.

Research was checked on November 6, 2026. Numeric material and controller values
are selected starting points, not measurements of real fabrics. The source
attachment was reviewed as a snapshot; its original source was not changed.

## Start here

1. Open the [complete prompt index](generated/PROMPTS.md). Each entry links to a
   versioned prompt with selected values, dependencies, outputs and sources.
   The standalone command expands the shared contract and every dependency into
   one copyable JSON prompt: `python scripts/generate_textile_workshop.py --prompt P-M14`.
   To export every resolved prompt, use `--export-directory /path/to/workshop-export`.
2. Start integration with P-I01 and P-I18. For the first material pilot use
   P-M14, P-M31, P-A01, P-A02, P-C06, P-C13, P-SC03 and P-SC04.
3. Use [design intent to code methods](generated/METHODS.md) and
   [material construction options](generated/material-options.json) for the
   translation boundary. These recipes do not imply a renderer has been built.
4. Review the [source findings and interpretations](generated/SOURCES.md),
   [field dictionary](generated/field-dictionary.json), and
   [traceability graph](generated/traceability.json) before changing parameters.
5. Run the checks below. Keep every unmet visual, runtime or deployment gate
   explicit. A prompt written by an agent is not a passed experiment.

## Coverage and ownership

| Group | Count | IDs | Purpose |
|---|---:|---|---|
| Surfaces | 32 | M01–M32 | Construction, shading, dimensions, maps, edges and review conditions |
| Components | 25 | C01–C25 | Layout, native semantics, states, actions, motion and dependencies |
| Scenes | 8 | SC01–SC08 | Composition, camera, lighting and responsive behavior |
| Assets | 18 | A01–A18 | Geometry, vectors, fonts, sound, concepts and specimen photographs |
| Methods | 9 | F01–F09 | Named functions, formulas, examples and approximation limits |
| Rules | 16 | R01–R16 | Explicit implementation and evidence requirements |
| Implementation tasks | 18 | I01–I18 | Bounded modules with consumer and verification contracts |
| Experiments | 8 | E01–E08 | Hypotheses, controls, measurements, falsifiers and rollback |
| Gaps and fixes | 10 | G01–G10 | Unresolved capabilities and the claims they block |
| Total prompts | 144 | P followed by record ID | All records have a resolved prompt and trace node |

The canonical consumer source is [registry.json](registry.json). The canonical
Core runtime token source remains [textile.tokens.json](../tokens/textile.tokens.json).
The suite compiler reads both; it does not overwrite the Core palette with the
proposed workshop palette. Core force values are normalized visual controls.
The physical-unit examples belong to future, explicitly bounded simulation
recipes. They are separate types and must never be silently interchanged.

The existing [v0.1 specification](../SPECIFICATION.md) and
[v0.2 evidence register](../EVIDENCE-v0.2.md) retain their boundaries. The workshop
does not establish a replacement Textile language or optical-material authority.
No cross-repository port or Figma synchronization is asserted.

## Design intent and selected approach

The experience should resemble a welcoming repair workshop. Material construction
should help users recognize offerings and understand actions. Reading, navigation,
selection and form status remain ordinary live text and native controls. The
primary task is to understand the offerings, inspect the repair pilot and preview
an interest form. The form is explicitly a local preview, with no network request
or claim that registration occurred.

Three implementation approaches were considered. Photographic backgrounds provide
convincing fixed appearances but cannot respond consistently to changed lighting
or deformation. A full fiber simulation across the page is costly and complicates
ordinary tasks. The selected approach is semantic DOM/CSS with selective material
rendering and one explicit close inspector. The richer view is optional; the
same selection and task outcome remain available in the semantic baseline.

The first pilot is indigo denim, cream cotton stitches, a satin label and a wooden
fastener. Resolve this small set before expanding into velvet, sheer fabrics or
full drape. The rationale is to test the hardest visual question early: whether
the surface reveals plausible construction when inspected closely.

## Material and offering map

| Offering or role | Surface IDs | Selected construction and appearance |
|---|---|---|
| Repair Commons | M14, M31, M21 | 3x1 indigo twill, cream three-ply sewing cotton, leather appearance label |
| Textile Network | M15, M17 | Teal ripstop with 4 mm reinforcing grid; optional open technical mesh |
| Futures Lab | M18, M05 | Irregular natural-fiber appearance; optional sheer silk study |
| Creative Studio | M11, M20 | Dark wine velvet and restrained metallic embroidery |
| Structural surfaces | M01, M02, M03 | Heavy canvas, coarse burlap and washed linen |
| Labels and layered cloth | M04, M06, M07 | Satin, corduroy ribs and connected knit loops |
| Light-filtering studies | M08, M09, M10 | Openwork lace, chiffon and sheer linen |
| Additional pile studies | M12, M13, M28, M32 | Mohair/alpaca appearances, felt and batting as different constructions |
| Workshop setting | M22, M23 | Teak appearance and cutting mat with separate vector markings |
| Fasteners | M24–M27 | Maple, horn appearance, pearlescent appearance and brass |
| Progress and boundaries | M29, M30 | Coated measuring tape and woven ribbon |
| Repair and reuse studies | M16, M19 | Reused-canvas appearance and quilted patchwork |

Material names describe intended appearance. A generated image cannot prove
fiber identity, recycled content, biological origin or environmental benefit.
Pearlescence is a restrained thin-film approximation, not a calibrated nacre
multilayer model. Sheer cloth uses coverage openings first; it must not be treated
as a continuous sheet of glass merely because the renderer has transmission.

## First pilot values

| Parameter | Selected value | Translation |
|---|---:|---|
| Denim warp diameter | 0.42 mm | Yarn builder; 0.00042 m at runtime |
| Denim weft diameter | 0.357 mm | Separate weft strand size |
| Warp and weft spacing | 0.54 mm | Centerline grid; 4-cell twill repeat |
| Cross-section flattening | 0.65 | Vertical yarn radius multiplier |
| Crossing clearance | 0.02 mm | Gap between opposing yarn surfaces at sampled crossings |
| Fabric thickness | 0.95 mm | Sheet edge and attachment baseline |
| Denim roughness | 0.90 | Authored physical-material roughness factor |
| Denim sheen and anisotropy | 0.24 and 0.22 | Separate directional response controls |
| Thread diameter | 0.32 mm | Geometry diameter, not a CSS border width |
| Thread ply count and twist | 3 and 1.5 turns/mm | Helical offsets in a transported centerline frame |
| Thread fiber size | 17 micrometers | Selected micro-detail target, not a measured cotton sample |
| Thread fuzz length | 0.35 mm | Bounded visible fibers in the close inspector |
| Wooden button | 14 mm diameter, 2.6 mm thick | Four 1.6 mm holes with 4.2 mm spacing |
| Inspector zoom | 1x and 4x | Explicit controls; no hover-only magnifier |
| Control target | At least 48 by 48 CSS px | Selected project target, above the AA minimum with its exceptions |

Exact parameter names and all other selected values are in the registry and each
resolved prompt. Zeros explicitly disable nonapplicable features. Receipt values
such as not-produced and not-reviewed are status sentinels, never fake hashes or
measurements. Proposed values are versioned design decisions, not universal
defaults for the physical material.

## Layout and behavior translation

| Scene | Components | Behavior and acceptance |
|---|---|---|
| SC01 hero | C01, C06 | Live heading and clear repair-pilot link over one restrained workbench composition |
| SC02 offerings | C02–C05 | One, two or four columns at the selected breakpoints; each offering has its own explicit details action |
| SC03 repair pilot | C02, C06, C12, C17 | Inspect or select the sample; pulling is optional and has click/tap and keyboard equivalents |
| SC04 inspector | C13, C18, C19 | Material, zoom and neutral/warm/grazing lighting controls; one active detailed material |
| SC05 interest preview | C14–C16, C07 | Native labels, local validation, actual step count and truthful preview confirmation |
| SC06 phone | C21, C06, C02 | Separate composition and normal vertical reading order; no scaled-down desktop text |
| SC07 acceptance fixture | C13, C19 | Internal fixed-seed comparison scene, not product navigation |
| SC08 fallback | Core task components | Rendering loss retains state and all meaningful actions |

Body text is 18 px IBM Plex Sans at line-height 1.55. Fraunces 600 is selected for
headings; IBM Plex Mono 500 at 14 px is selected for compact labels. These font
assets are specified, not downloaded or bundled. Opaque label surfaces protect
text contrast from cloth texture and moving highlights. The maximum content width
is 1200 px; mobile gutter is 20 px, card gap 24 px, and the column breakpoints are
768 and 1200 px. Scene millimeters are composition units, not a global CSS scale.
The inspector's selected one-times view uses 4 CSS px per mm.

Interaction, selection, operation and disabled state are separate axes. A hover
effect cannot mean saved. Animation completion cannot mean registration succeeded.
A toggle keeps its accessible name and uses aria-pressed or the native checked
state to communicate selection. Modal details use a native dialog with explicit
close, useful initial focus and return to the invoker. Optional sound and motion
preferences remain independent. No physical haptic output is specified.

## Map and rendering contracts

Each surface specifies a whole-repeat tile, a 2048 px master and close-view texture,
and a 1024 px normal viewing texture. All eight requested maps have filenames,
channels, bit depth, color-space metadata and neutral values: base color, normal,
ORM, height, sheen color, sheen roughness, anisotropy and coverage. These are
production requirements; none is claimed to exist in this PR.

Base-color images are full-color authored albedo appearances; binding one requires
a white material color factor to avoid applying the selected color twice. ORM is
R ambient occlusion, G roughness multiplier and B metalness multiplier. Sheen
roughness uses alpha. Anisotropy uses RG direction and B strength. Coverage is a
numeric grayscale map with white meaning covered. Color maps use sRGB annotation;
numeric maps use NoColorSpace. OpenGL tangent-space normals use the +Y convention.

Geometry contains fabric edges, lifted corners, protruding stitches and yarn
crossings. Residual normal and height maps must not duplicate relief already
modeled in that geometry. Loose textures and imported glTF textures have different
orientation handling: the declared loose-texture route uses flipY=true;
GLTFLoader owns imported texture orientation and transforms. A fixed-UV diagnostic
must verify both paths rather than blindly flipping every normal map.

The enhanced recipe targets Three.js 0.187.0. It uses the r187 iridescence thickness
minimum and maximum fields. The Core slice adds no Three.js dependency. Key and
fill intensities are authored renderer controls; they are not measured illuminance.
The selected view uses an orthographic camera, Linear-sRGB working color, sRGB
output, ACES filmic tone mapping at exposure 1.0, and no bloom, chromatic aberration,
motion blur or global postprocessing. See the three explicit light presets in
the registry. A directional light needs a positioned and added target.

## Executable compiler and Core bindings

| Capability | Function or file | Actual consumer | Test and CI |
|---|---|---|---|
| Core token lookup and flattening | value, flat_values, outputs in generate_textile_adapters.py | CSS, TypeScript, motion JSON and offline Figma mapping | Every token independently mutated; four exports must change |
| Resolved prompt generation | compile_outputs, dependencies, records in generate_textile_workshop.py | 144 prompt contracts and prompt index | Determinism, stale output detection, full graph validation |
| Material translation | material_options | material-options.json; future renderer recipe | Parameter sensitivity and channel/unit contract checks |
| Field dictionary | leaf_rows, field_meaning | Named fields, units, selected values and consumers | Canonical mutation changes dictionary and prompts |
| Runtime commitment toggle | existing ThreadButton click handler | aria-pressed, data-state and live status | Pointer, reversal, keyboard and touch checks |
| Normalized Core force mapping | ThreadButton CSS | Bounded shadow, press displacement and duration | Computed CSS and active transform checked in Chromium |
| Browser evidence | verify_textile_visual.py | Run-scoped screenshots and digest receipt | Exactly 17 checks required; incomplete runs fail |
| Evidence negative control | verify_textile_evidence_failure.py | Deliberately interrupted child run | Nonzero exit plus fresh failed/incomplete diagnostic receipt |
| CI orchestration | signal-validation.yml | Contract validation precedes browser job; both upload evidence | Missing expected artifact is an error |

The Core mapping is intentionally modest: tension controls shadow offset,
compression controls pressed displacement, elasticity controls shadow blur, and
recovery controls duration. For the current canonical values this means 3.84 px
shadow offset, 9.44 px blur, 0.52 px pressed displacement, scale 0.97 and 161.64 ms
transition. These affordances consume the tokens; they do not simulate fibers,
thread tension or measured fabric mechanics.

The method recipes F01–F09 cover unit conversion, crossing clearance, weave
selection, ply helices, damped springs, XPBD distance constraints, projected-detail
LOD, linear color/contrast and height-derived normals. Their function signatures,
formulas and selected examples are copyable in METHODS.md. They remain recipes
until a real runtime consumer and its evidence are added. XPBD's selected bend
control is a distance-based surrogate; no calibrated angular bending or
self-collision is claimed.

## Workflow and CI commands

From the repository root:

```bash
python scripts/generate_textile_adapters.py --check
python scripts/verify_textile_adapter_mutation.py
python scripts/validate_textile_interface.py
python scripts/generate_textile_workshop.py --check
python scripts/verify_textile_workshop.py
python scripts/verify_textile_evidence_failure.py
python scripts/verify_textile_visual.py
```

After editing a canonical source, regenerate the applicable outputs, review the
diff and rerun these gates. Do not hand-edit generated files. Signal Validation
runs the same contract checks and requires their job before browser evidence.
Browser receipts identify source hashes, expected/completed check counts,
completion status, errors and screenshot hashes. An interrupted run is explicitly
diagnostic. A green compiler job does not close a visual or deployment gap.

## Measurements and experiments

| Experiment | Controlled comparison | Measurement and acceptance boundary |
|---|---|---|
| E01 fibers | Same material, camera, seed and light; fiber detail on/off | Named user rates plausibility; selected one-point improvement target is a personal design gate |
| E02 light | Neutral, warm and grazing presets | Matched captures; no detached shadows or structural contradiction |
| E03 detail level | Mapped, yarn and fiber modes | Actual device frame statistics and review of popping/shimmer |
| E04 tiers and failure | T0/T1/T2 plus lost renderer during a task | Same task completion, retained data and focus |
| E05 input | Drag, click/tap placement and keyboard placement | Identical selected ID/destination and useful announced status |
| E06 parameter sensitivity | Denim warp diameter increased by 0.05 mm in memory | Prompt, dictionary and material translation change; originals remain unchanged |
| E07 motion | System reduced motion off/on | Static state feedback, no decorative displacement, same semantic result |
| E08 verifier failure | Controlled exception before browser completion | Nonzero exit and incomplete diagnostic receipt |

E01–E05 require future assets or runtime fixtures; the registry keeps them planned.
E06 and the Core portions of E07/E08 have executable checks in this PR. Their
execution receipts provide their actual result; the planned experiment entry is
not silently rewritten into a scientific finding.

Proposed performance targets are desktop p95 frame time at most 16.7 ms and phone
p95 at most 33.3 ms over 20 seconds after 5 seconds warmup. Record the actual
device, browser, renderer version, viewport, DPR, asset hashes and sample data.
Triangle/draw/texture targets are 100000 visible triangles, 60 draw calls and
64 MiB estimated resident textures. Initial compressed-transfer target is 900 KiB;
the inspector is a separate lazy transfer target of 3000 KiB. These numbers are
selected budgets, not achieved measurements. Uncompressed PNG size is not GPU
memory usage. Compare the declared compression, mipmaps and actual residency.

## Open work and correction loop

G01–G06 and G09–G10 retain material-fidelity, renderer, deployment, full operation
states, asset acquisition, real-device measurement, physical calibration and
language-conformance gaps. G07/G08 identify the bounded Core naming and evidence
fixes; their current acceptance comes from fresh test results, not from this list.
The full gap prompts specify their fixes, affected records, verification IDs and
blocked claims.

The feedback path is intent → canonical specification → prompt/adapter → actual
consumer → test → raw evidence → experiment and human review → versioned
correction. A failed observation stays in the evidence. A proposed correction
names the parameter or rule it changes, the affected consumers and the rerun
needed to check it. This makes new visual work accountable to the same workflow
without pretending all future modules are already implemented.
