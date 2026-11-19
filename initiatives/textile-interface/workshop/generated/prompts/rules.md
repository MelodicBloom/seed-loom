# Rules prompt contracts

<a id="p-r01"></a>

## P-R01 Units are explicit

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R01",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R01",
    "name": "Units are explicit",
    "requirement": "All authored asset distances use mm; runtime distances use m. Reject missing or mixed units.",
    "methodId": "F01",
    "status": "normative-for-this-suite"
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
    "F01"
  ],
  "sourceIds": [
    "S00",
    "S05"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R01"
}
```

<a id="p-r02"></a>

## P-R02 Topology determines construction

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R02",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R02",
    "name": "Topology determines construction",
    "requirement": "Woven crossings, knit loops, pile, felt, and solid hardware take separate geometry routes.",
    "methodId": "F02",
    "status": "normative-for-this-suite"
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
    "F02"
  ],
  "sourceIds": [
    "S00",
    "S01",
    "S05"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R02"
}
```

<a id="p-r03"></a>

## P-R03 Material values are design selections

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R03",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R03",
    "name": "Material values are design selections",
    "requirement": "Do not present selected roughness, fiber size, or stiffness as measured specimen data.",
    "methodId": "F05",
    "status": "normative-for-this-suite"
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
    "F05"
  ],
  "sourceIds": [
    "S00",
    "S09"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R03"
}
```

<a id="p-r04"></a>

## P-R04 One lighting model

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R04",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R04",
    "name": "One lighting model",
    "requirement": "All active 3D elements share a scene light preset; DOM text remains outside illumination.",
    "methodId": "F08",
    "status": "normative-for-this-suite"
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
    "F08"
  ],
  "sourceIds": [
    "S00",
    "S06",
    "S12"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R04"
}
```

<a id="p-r05"></a>

## P-R05 No baked illumination in maps

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R05",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R05",
    "name": "No baked illumination in maps",
    "requirement": "Base color contains albedo appearance, not directional shadow or shine.",
    "methodId": "F09",
    "status": "normative-for-this-suite"
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
    "F09"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R05"
}
```

<a id="p-r06"></a>

## P-R06 No relief counted twice

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R06",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R06",
    "name": "No relief counted twice",
    "requirement": "Modeled yarn relief is excluded from residual normal/height maps used on that yarn.",
    "methodId": "F09",
    "status": "normative-for-this-suite"
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
    "F09"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R06"
}
```

<a id="p-r07"></a>

## P-R07 Accessible actions are invariant

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R07",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R07",
    "name": "Accessible actions are invariant",
    "requirement": "Native controls, keyboard, tap alternatives, readable status, and focus survive all tiers.",
    "methodId": "F08",
    "status": "normative-for-this-suite"
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
    "F08"
  ],
  "sourceIds": [
    "S00",
    "S06",
    "S12"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R07"
}
```

<a id="p-r08"></a>

## P-R08 Motion is optional

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R08",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R08",
    "name": "Motion is optional",
    "requirement": "Reduced motion disables displacement and inertia while preserving operation and selection.",
    "methodId": "F05",
    "status": "normative-for-this-suite"
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
    "F05"
  ],
  "sourceIds": [
    "S00",
    "S09"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R08"
}
```

<a id="p-r09"></a>

## P-R09 Audio is independent

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R09",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R09",
    "name": "Audio is independent",
    "requirement": "Sound defaults off and never carries unique action or failure information.",
    "methodId": "F05",
    "status": "normative-for-this-suite"
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
    "F05"
  ],
  "sourceIds": [
    "S00",
    "S09"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R09"
}
```

<a id="p-r10"></a>

## P-R10 Effects have bounded work

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R10",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R10",
    "name": "Effects have bounded work",
    "requirement": "One active inspector; selected triangle, texture, frame, and draw budgets; degrade predictably.",
    "methodId": "F07",
    "status": "normative-for-this-suite"
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
    "F07"
  ],
  "sourceIds": [
    "S00",
    "S01",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R10"
}
```

<a id="p-r11"></a>

## P-R11 Evidence is run scoped

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R11",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R11",
    "name": "Evidence is run scoped",
    "requirement": "Completion requires all expected checks and fresh source hashes. Interrupted output is diagnostic.",
    "methodId": "F08",
    "status": "normative-for-this-suite"
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
    "F08"
  ],
  "sourceIds": [
    "S00",
    "S06",
    "S12"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R11"
}
```

<a id="p-r12"></a>

## P-R12 No synthetic physical provenance

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R12",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R12",
    "name": "No synthetic physical provenance",
    "requirement": "Generated concepts do not establish fiber identity, recycled content, or optical accuracy.",
    "methodId": "F04",
    "status": "normative-for-this-suite"
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
    "F04"
  ],
  "sourceIds": [
    "S00",
    "S01",
    "S02"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R12"
}
```

<a id="p-r13"></a>

## P-R13 Single canonical source per boundary

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R13",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R13",
    "name": "Single canonical source per boundary",
    "requirement": "Workshop registry owns this consumer specification; existing TIL tokens own the Core runtime.",
    "methodId": "F01",
    "status": "normative-for-this-suite"
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
    "F01"
  ],
  "sourceIds": [
    "S00",
    "S05"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R13"
}
```

<a id="p-r14"></a>

## P-R14 No orphan capability

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R14",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R14",
    "name": "No orphan capability",
    "requirement": "Every implemented node names its runtime consumer, test, CI job, and evidence. Planned nodes stay visibly planned.",
    "methodId": "F01",
    "status": "normative-for-this-suite"
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
    "F01"
  ],
  "sourceIds": [
    "S00",
    "S05"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R14"
}
```

<a id="p-r15"></a>

## P-R15 Stable toggle naming

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R15",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R15",
    "name": "Stable toggle naming",
    "requirement": "A toggle keeps its accessible name while aria-pressed reports selection.",
    "methodId": "F08",
    "status": "normative-for-this-suite"
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
    "F08"
  ],
  "sourceIds": [
    "S00",
    "S06",
    "S12"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R15"
}
```

<a id="p-r16"></a>

## P-R16 No physical unit metaphor leakage

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-R16",
  "task": "Audit the linked implementation against this rule. Return concrete source locations, evidence, a counterexample, and the smallest corrective change. Do not call absent evidence a pass.",
  "specification": {
    "id": "R16",
    "name": "No physical unit metaphor leakage",
    "requirement": "Tape markings are decorative unless their units correspond to actual application data.",
    "methodId": "F01",
    "status": "normative-for-this-suite"
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
    "F01"
  ],
  "sourceIds": [
    "S00",
    "S05"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-R16"
}
```
