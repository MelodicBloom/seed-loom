# Experiments prompt contracts

<a id="p-e01"></a>

## P-E01 Visible fiber contribution

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-E01",
  "task": "Run this trial only after required fixtures exist. Freeze device, versions, seed, camera and control condition before measurement. Preserve failures and raw data. Return planned, pass, fail, blocked or inconclusive without promoting a proxy check to material acceptance.",
  "specification": {
    "id": "E01",
    "name": "Visible fiber contribution",
    "hypothesis": "Fiber detail increases perceived textile realism relative to the identical yarn-only view.",
    "independentVariable": "Fiber detail enabled versus disabled, same camera, light, seed and material.",
    "measurement": "Named user rates plausibility 1..5 and explains visible construction.",
    "acceptanceThreshold": "At least one-point improvement without new aliasing or unreadable labels.",
    "falsifier": "No improvement, plastic appearance, or distracting shimmer.",
    "dependencyIds": [
      "SC04",
      "M14",
      "M31"
    ],
    "claimBoundary": "Visual preference hypothesis; no optical calibration.",
    "status": "planned",
    "fixture": {
      "seed": 314159,
      "desktopViewportPx": [
        1440,
        900
      ],
      "phoneViewportPx": [
        375,
        812
      ],
      "repetitions": 3,
      "reviewer": "unassigned",
      "device": "must be recorded before execution"
    },
    "stopRule": "Stop on data loss, nonfinite simulation, exceeded work budget, or scope expansion.",
    "rollback": "Restore previous reference and generated artifacts; preserve failed evidence."
  },
  "returnContract": {
    "required": [
      "resultStatus",
      "selectedValuesUsed",
      "changedFilesOrAssets",
      "implementationMapping",
      "testsExecuted",
      "evidence",
      "openGaps",
      "interpretations"
    ],
    "permittedResultStatus": [
      "specified",
      "implemented-unverified",
      "pass",
      "fail",
      "blocked",
      "inconclusive"
    ],
    "rules": [
      "Keep source facts, design choices, interpretations and measurements distinct.",
      "No invented specimen data, licenses, hashes, successful tests, or deployments.",
      "Do not silently change values; propose and justify a versioned change.",
      "No unrelated refactor, force push, merge, publication, or message to another person."
    ]
  },
  "globalContractRef": "../../registry.json#/global",
  "dependencyIds": [
    "SC04",
    "M14",
    "M31",
    "C13",
    "C18",
    "C19",
    "A18",
    "M03",
    "M15",
    "M18",
    "M11",
    "A12",
    "M04",
    "M27",
    "M20"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S06",
    "S12",
    "S20",
    "S01",
    "S03",
    "S05",
    "S10",
    "S11",
    "S13"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-E01"
}
```

<a id="p-e02"></a>

## P-E02 Lighting robustness

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-E02",
  "task": "Run this trial only after required fixtures exist. Freeze device, versions, seed, camera and control condition before measurement. Preserve failures and raw data. Return planned, pass, fail, blocked or inconclusive without promoting a proxy check to material acceptance.",
  "specification": {
    "id": "E02",
    "name": "Lighting robustness",
    "hypothesis": "The chosen structure remains convincing under neutral, warm, and grazing light.",
    "independentVariable": "Only light preset changes.",
    "measurement": "Matched captures and reviewer notes for weave, edge, and thread contact.",
    "acceptanceThreshold": "All three presets reviewed; no detached shadow or silhouette contradiction.",
    "falsifier": "Realism depends entirely on warm tint or hidden dark areas.",
    "dependencyIds": [
      "SC07",
      "M14"
    ],
    "claimBoundary": "Design acceptance.",
    "status": "planned",
    "fixture": {
      "seed": 314159,
      "desktopViewportPx": [
        1440,
        900
      ],
      "phoneViewportPx": [
        375,
        812
      ],
      "repetitions": 3,
      "reviewer": "unassigned",
      "device": "must be recorded before execution"
    },
    "stopRule": "Stop on data loss, nonfinite simulation, exceeded work budget, or scope expansion.",
    "rollback": "Restore previous reference and generated artifacts; preserve failed evidence."
  },
  "returnContract": {
    "required": [
      "resultStatus",
      "selectedValuesUsed",
      "changedFilesOrAssets",
      "implementationMapping",
      "testsExecuted",
      "evidence",
      "openGaps",
      "interpretations"
    ],
    "permittedResultStatus": [
      "specified",
      "implemented-unverified",
      "pass",
      "fail",
      "blocked",
      "inconclusive"
    ],
    "rules": [
      "Keep source facts, design choices, interpretations and measurements distinct.",
      "No invented specimen data, licenses, hashes, successful tests, or deployments.",
      "Do not silently change values; propose and justify a versioned change.",
      "No unrelated refactor, force push, merge, publication, or message to another person."
    ]
  },
  "globalContractRef": "../../registry.json#/global",
  "dependencyIds": [
    "SC07",
    "M14",
    "M31",
    "C13",
    "C19",
    "A18",
    "M04",
    "M27"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S06",
    "S12",
    "S20",
    "S01",
    "S03",
    "S05",
    "S10",
    "S11",
    "S13"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-E02"
}
```

<a id="p-e03"></a>

## P-E03 Detail level transition

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-E03",
  "task": "Run this trial only after required fixtures exist. Freeze device, versions, seed, camera and control condition before measurement. Preserve failures and raw data. Return planned, pass, fail, blocked or inconclusive without promoting a proxy check to material acceptance.",
  "specification": {
    "id": "E03",
    "name": "Detail level transition",
    "hypothesis": "LOD reduces work while avoiding obvious transition artifacts.",
    "independentVariable": "Mapped, yarn, fiber modes at fixed scales.",
    "measurement": "Frame time p50/p95, visible popping, edge shimmer.",
    "acceptanceThreshold": "Selected frame budget met over 20 seconds after 5-second warmup; user reports no disruptive transition.",
    "falsifier": "Budget exceeded twice or disruptive popping.",
    "dependencyIds": [
      "SC04",
      "I04"
    ],
    "claimBoundary": "Performance targets require a named real device.",
    "status": "planned",
    "fixture": {
      "seed": 314159,
      "desktopViewportPx": [
        1440,
        900
      ],
      "phoneViewportPx": [
        375,
        812
      ],
      "repetitions": 3,
      "reviewer": "unassigned",
      "device": "must be recorded before execution"
    },
    "stopRule": "Stop on data loss, nonfinite simulation, exceeded work budget, or scope expansion.",
    "rollback": "Restore previous reference and generated artifacts; preserve failed evidence."
  },
  "returnContract": {
    "required": [
      "resultStatus",
      "selectedValuesUsed",
      "changedFilesOrAssets",
      "implementationMapping",
      "testsExecuted",
      "evidence",
      "openGaps",
      "interpretations"
    ],
    "permittedResultStatus": [
      "specified",
      "implemented-unverified",
      "pass",
      "fail",
      "blocked",
      "inconclusive"
    ],
    "rules": [
      "Keep source facts, design choices, interpretations and measurements distinct.",
      "No invented specimen data, licenses, hashes, successful tests, or deployments.",
      "Do not silently change values; propose and justify a versioned change.",
      "No unrelated refactor, force push, merge, publication, or message to another person."
    ]
  },
  "globalContractRef": "../../registry.json#/global",
  "dependencyIds": [
    "SC04",
    "I04",
    "M14",
    "M31",
    "C13",
    "C18",
    "C19",
    "M11",
    "M12",
    "M13",
    "M28",
    "F07",
    "A18",
    "M03",
    "M15",
    "M18",
    "A12",
    "M04",
    "M27",
    "M20"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S06",
    "S12",
    "S20",
    "S05",
    "S09",
    "S10",
    "S14",
    "S01",
    "S03",
    "S11",
    "S13"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-E03"
}
```

<a id="p-e04"></a>

## P-E04 Task completion across tiers

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-E04",
  "task": "Run this trial only after required fixtures exist. Freeze device, versions, seed, camera and control condition before measurement. Preserve failures and raw data. Return planned, pass, fail, blocked or inconclusive without promoting a proxy check to material acceptance.",
  "specification": {
    "id": "E04",
    "name": "Task completion across tiers",
    "hypothesis": "The repair preview task remains complete in T0, T1, T2 and context loss.",
    "independentVariable": "Disable or lose rendering during an active selection and filled form.",
    "measurement": "Task completion, retained fields, focus position, errors.",
    "acceptanceThreshold": "Every case finishes with preserved data and truthful preview confirmation.",
    "falsifier": "Lost entry, inaccessible action, or incorrect confirmation.",
    "dependencyIds": [
      "SC08",
      "C14",
      "I14"
    ],
    "claimBoundary": "Functional equivalence.",
    "status": "planned",
    "fixture": {
      "seed": 314159,
      "desktopViewportPx": [
        1440,
        900
      ],
      "phoneViewportPx": [
        375,
        812
      ],
      "repetitions": 3,
      "reviewer": "unassigned",
      "device": "must be recorded before execution"
    },
    "stopRule": "Stop on data loss, nonfinite simulation, exceeded work budget, or scope expansion.",
    "rollback": "Restore previous reference and generated artifacts; preserve failed evidence."
  },
  "returnContract": {
    "required": [
      "resultStatus",
      "selectedValuesUsed",
      "changedFilesOrAssets",
      "implementationMapping",
      "testsExecuted",
      "evidence",
      "openGaps",
      "interpretations"
    ],
    "permittedResultStatus": [
      "specified",
      "implemented-unverified",
      "pass",
      "fail",
      "blocked",
      "inconclusive"
    ],
    "rules": [
      "Keep source facts, design choices, interpretations and measurements distinct.",
      "No invented specimen data, licenses, hashes, successful tests, or deployments.",
      "Do not silently change values; propose and justify a versioned change.",
      "No unrelated refactor, force push, merge, publication, or message to another person."
    ]
  },
  "globalContractRef": "../../registry.json#/global",
  "dependencyIds": [
    "SC08",
    "C14",
    "I14",
    "M03",
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "C06",
    "M04",
    "A13",
    "C23",
    "F07",
    "M31",
    "A12",
    "M14",
    "A01",
    "A10",
    "M15",
    "M18",
    "M11",
    "M24",
    "A02",
    "M20",
    "M27"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S06",
    "S12",
    "S20",
    "S10",
    "S11",
    "S13",
    "S05",
    "S09",
    "S14",
    "S01",
    "S03",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-E04"
}
```

<a id="p-e05"></a>

## P-E05 Drag alternatives

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-E05",
  "task": "Run this trial only after required fixtures exist. Freeze device, versions, seed, camera and control condition before measurement. Preserve failures and raw data. Return planned, pass, fail, blocked or inconclusive without promoting a proxy check to material acceptance.",
  "specification": {
    "id": "E05",
    "name": "Drag alternatives",
    "hypothesis": "Pointer drag, click/tap placement and keyboard placement produce identical selection.",
    "independentVariable": "Change input modality only.",
    "measurement": "Selected ID, destination, focus and announced status.",
    "acceptanceThreshold": "Exact same semantic state for all cases and pointercancel recovery.",
    "falsifier": "Different selected item, lost focus, or drag-only action.",
    "dependencyIds": [
      "C12",
      "C17",
      "I08"
    ],
    "claimBoundary": "Interaction equivalence.",
    "status": "planned",
    "fixture": {
      "seed": 314159,
      "desktopViewportPx": [
        1440,
        900
      ],
      "phoneViewportPx": [
        375,
        812
      ],
      "repetitions": 3,
      "reviewer": "unassigned",
      "device": "must be recorded before execution"
    },
    "stopRule": "Stop on data loss, nonfinite simulation, exceeded work budget, or scope expansion.",
    "rollback": "Restore previous reference and generated artifacts; preserve failed evidence."
  },
  "returnContract": {
    "required": [
      "resultStatus",
      "selectedValuesUsed",
      "changedFilesOrAssets",
      "implementationMapping",
      "testsExecuted",
      "evidence",
      "openGaps",
      "interpretations"
    ],
    "permittedResultStatus": [
      "specified",
      "implemented-unverified",
      "pass",
      "fail",
      "blocked",
      "inconclusive"
    ],
    "rules": [
      "Keep source facts, design choices, interpretations and measurements distinct.",
      "No invented specimen data, licenses, hashes, successful tests, or deployments.",
      "Do not silently change values; propose and justify a versioned change.",
      "No unrelated refactor, force push, merge, publication, or message to another person."
    ]
  },
  "globalContractRef": "../../registry.json#/global",
  "dependencyIds": [
    "C12",
    "C17",
    "I08",
    "M30",
    "M31",
    "A08",
    "M27",
    "A10",
    "F05"
  ],
  "sourceIds": [
    "S00",
    "S10",
    "S11",
    "S12",
    "S13",
    "S04",
    "S05",
    "S09",
    "S14",
    "S01",
    "S03",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-E05"
}
```

<a id="p-e06"></a>

## P-E06 Parameter sensitivity

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-E06",
  "task": "Run this trial only after required fixtures exist. Freeze device, versions, seed, camera and control condition before measurement. Preserve failures and raw data. Return planned, pass, fail, blocked or inconclusive without promoting a proxy check to material acceptance.",
  "specification": {
    "id": "E06",
    "name": "Parameter sensitivity",
    "hypothesis": "Changing a canonical material dimension affects the resolved prompt and material translation.",
    "independentVariable": "Mutate denim yarnDiameterWarpMm by +0.05 in memory.",
    "measurement": "Generated prompt, field dictionary and material-options JSON change; original source remains unchanged.",
    "acceptanceThreshold": "Expected outputs change deterministically; missing inputs and unknown references fail.",
    "falsifier": "Mutation does not propagate or baseline files change.",
    "dependencyIds": [
      "M14",
      "I01"
    ],
    "claimBoundary": "Compiler integrity, not rendered material fidelity.",
    "status": "planned",
    "fixture": {
      "seed": 314159,
      "desktopViewportPx": [
        1440,
        900
      ],
      "phoneViewportPx": [
        375,
        812
      ],
      "repetitions": 3,
      "reviewer": "unassigned",
      "device": "must be recorded before execution"
    },
    "stopRule": "Stop on data loss, nonfinite simulation, exceeded work budget, or scope expansion.",
    "rollback": "Restore previous reference and generated artifacts; preserve failed evidence."
  },
  "returnContract": {
    "required": [
      "resultStatus",
      "selectedValuesUsed",
      "changedFilesOrAssets",
      "implementationMapping",
      "testsExecuted",
      "evidence",
      "openGaps",
      "interpretations"
    ],
    "permittedResultStatus": [
      "specified",
      "implemented-unverified",
      "pass",
      "fail",
      "blocked",
      "inconclusive"
    ],
    "rules": [
      "Keep source facts, design choices, interpretations and measurements distinct.",
      "No invented specimen data, licenses, hashes, successful tests, or deployments.",
      "Do not silently change values; propose and justify a versioned change.",
      "No unrelated refactor, force push, merge, publication, or message to another person."
    ]
  },
  "globalContractRef": "../../registry.json#/global",
  "dependencyIds": [
    "M14",
    "I01",
    "C25",
    "F01",
    "M31",
    "A01"
  ],
  "sourceIds": [
    "S00",
    "S01",
    "S03",
    "S04",
    "S05",
    "S06",
    "S09",
    "S10",
    "S14",
    "S11",
    "S12",
    "S13"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-E06"
}
```

<a id="p-e07"></a>

## P-E07 Motion preference invariance

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-E07",
  "task": "Run this trial only after required fixtures exist. Freeze device, versions, seed, camera and control condition before measurement. Preserve failures and raw data. Return planned, pass, fail, blocked or inconclusive without promoting a proxy check to material acceptance.",
  "specification": {
    "id": "E07",
    "name": "Motion preference invariance",
    "hypothesis": "Reduced motion removes displacement while retaining action and selection state.",
    "independentVariable": "System reduced motion off versus on.",
    "measurement": "Computed transform, transition duration, aria state and text.",
    "acceptanceThreshold": "Zero decorative displacement with identical action result.",
    "falsifier": "Moving decoration persists or operation semantics change.",
    "dependencyIds": [
      "C25",
      "C20"
    ],
    "claimBoundary": "Automated Core checks plus future enhanced-tier verification.",
    "status": "planned",
    "fixture": {
      "seed": 314159,
      "desktopViewportPx": [
        1440,
        900
      ],
      "phoneViewportPx": [
        375,
        812
      ],
      "repetitions": 3,
      "reviewer": "unassigned",
      "device": "must be recorded before execution"
    },
    "stopRule": "Stop on data loss, nonfinite simulation, exceeded work budget, or scope expansion.",
    "rollback": "Restore previous reference and generated artifacts; preserve failed evidence."
  },
  "returnContract": {
    "required": [
      "resultStatus",
      "selectedValuesUsed",
      "changedFilesOrAssets",
      "implementationMapping",
      "testsExecuted",
      "evidence",
      "openGaps",
      "interpretations"
    ],
    "permittedResultStatus": [
      "specified",
      "implemented-unverified",
      "pass",
      "fail",
      "blocked",
      "inconclusive"
    ],
    "rules": [
      "Keep source facts, design choices, interpretations and measurements distinct.",
      "No invented specimen data, licenses, hashes, successful tests, or deployments.",
      "Do not silently change values; propose and justify a versioned change.",
      "No unrelated refactor, force push, merge, publication, or message to another person."
    ]
  },
  "globalContractRef": "../../registry.json#/global",
  "dependencyIds": [
    "C25",
    "C20",
    "M14",
    "M31",
    "A01",
    "M03",
    "M25",
    "A03",
    "A06"
  ],
  "sourceIds": [
    "S00",
    "S10",
    "S11",
    "S12",
    "S13",
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-E07"
}
```

<a id="p-e08"></a>

## P-E08 Evidence interruption

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-E08",
  "task": "Run this trial only after required fixtures exist. Freeze device, versions, seed, camera and control condition before measurement. Preserve failures and raw data. Return planned, pass, fail, blocked or inconclusive without promoting a proxy check to material acceptance.",
  "specification": {
    "id": "E08",
    "name": "Evidence interruption",
    "hypothesis": "An interrupted browser run can never be reported as a complete pass.",
    "independentVariable": "Inject a controlled exception before browser checks finish.",
    "measurement": "Exit code, completion status, expected count, screenshot hashes.",
    "acceptanceThreshold": "Nonzero exit and incomplete/failed status; artifact remains explicitly diagnostic.",
    "falsifier": "Zero exit or complete status with missing checks.",
    "dependencyIds": [
      "I18",
      "C25"
    ],
    "claimBoundary": "Verifier falsification test.",
    "status": "planned",
    "fixture": {
      "seed": 314159,
      "desktopViewportPx": [
        1440,
        900
      ],
      "phoneViewportPx": [
        375,
        812
      ],
      "repetitions": 3,
      "reviewer": "unassigned",
      "device": "must be recorded before execution"
    },
    "stopRule": "Stop on data loss, nonfinite simulation, exceeded work budget, or scope expansion.",
    "rollback": "Restore previous reference and generated artifacts; preserve failed evidence."
  },
  "returnContract": {
    "required": [
      "resultStatus",
      "selectedValuesUsed",
      "changedFilesOrAssets",
      "implementationMapping",
      "testsExecuted",
      "evidence",
      "openGaps",
      "interpretations"
    ],
    "permittedResultStatus": [
      "specified",
      "implemented-unverified",
      "pass",
      "fail",
      "blocked",
      "inconclusive"
    ],
    "rules": [
      "Keep source facts, design choices, interpretations and measurements distinct.",
      "No invented specimen data, licenses, hashes, successful tests, or deployments.",
      "Do not silently change values; propose and justify a versioned change.",
      "No unrelated refactor, force push, merge, publication, or message to another person."
    ]
  },
  "globalContractRef": "../../registry.json#/global",
  "dependencyIds": [
    "I18",
    "C25",
    "SC07",
    "F01",
    "M14",
    "M31",
    "A01",
    "C13",
    "C19",
    "A18",
    "M04",
    "M27"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S11",
    "S12",
    "S13",
    "S06",
    "S20",
    "S01",
    "S03"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-E08"
}
```
