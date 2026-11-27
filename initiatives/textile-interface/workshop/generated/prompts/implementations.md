# Implementations prompt contracts

<a id="p-i01"></a>

## P-I01 Canonical registry and compilation

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I01",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I01",
    "name": "Canonical registry and compilation",
    "status": "integration-target",
    "dependencyIds": [
      "M14",
      "C25"
    ],
    "methodIds": [
      "F01"
    ],
    "task": "Compile every prompt, source reference, field dictionary, material option, traceability edge and CSS token deterministically. Reject stale outputs.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "C25",
    "F01",
    "M31",
    "A01"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S01",
    "S03",
    "S06",
    "S11",
    "S12",
    "S13"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I01"
}
```

<a id="p-i02"></a>

## P-I02 Woven geometry

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I02",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I02",
    "name": "Woven geometry",
    "status": "planned-implementation",
    "dependencyIds": [
      "M01",
      "M14",
      "M04"
    ],
    "methodIds": [
      "F02",
      "F03",
      "F04"
    ],
    "task": "Build crossing-consistent yarn centerlines for plain, 3x1 twill and 5-harness satin. Model a cropped inspector region only.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "M01",
    "M14",
    "M04",
    "F02",
    "F03",
    "F04"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S01",
    "S03",
    "S06",
    "S02"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I02"
}
```

<a id="p-i03"></a>

## P-I03 Knit topology

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I03",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I03",
    "name": "Knit topology",
    "status": "planned-implementation",
    "dependencyIds": [
      "M07"
    ],
    "methodIds": [
      "F04"
    ],
    "task": "Construct connected interlocking knit loops with explicit wale/course dimensions. Do not remap a plain weave normal onto a knit and call it knitted geometry.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "M07",
    "F04"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S01",
    "S03",
    "S06",
    "S02"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I03"
}
```

<a id="p-i04"></a>

## P-I04 Pile and fuzz

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I04",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I04",
    "name": "Pile and fuzz",
    "status": "planned-implementation",
    "dependencyIds": [
      "M11",
      "M12",
      "M13",
      "M28"
    ],
    "methodIds": [
      "F07"
    ],
    "task": "Align pile direction with the tangent field; add bounded edge fibers only in the active inspector. Felt is nonwoven.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "M11",
    "M12",
    "M13",
    "M28",
    "F07"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S01",
    "S03",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I04"
}
```

<a id="p-i05"></a>

## P-I05 Stitch attachment and tension

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I05",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I05",
    "name": "Stitch attachment and tension",
    "status": "planned-implementation",
    "dependencyIds": [
      "A01",
      "C06",
      "C25"
    ],
    "methodIds": [
      "F04",
      "F05"
    ],
    "task": "Bind thread entry and exit points to the deforming substrate. Preserve loop length and prevent button-thread intersections.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "A01",
    "C06",
    "C25",
    "F04",
    "F05",
    "M31",
    "M24",
    "M14",
    "A02"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S06",
    "S11",
    "S12",
    "S13",
    "S01",
    "S02",
    "S03"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I05"
}
```

<a id="p-i06"></a>

## P-I06 Lighting and color pipeline

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I06",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I06",
    "name": "Lighting and color pipeline",
    "status": "planned-implementation",
    "dependencyIds": [
      "SC01",
      "SC04",
      "SC07"
    ],
    "methodIds": [
      "F08"
    ],
    "task": "Set the declared lights, orthographic camera and output color management. Prove no double color conversion.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "SC01",
    "SC04",
    "SC07",
    "F08",
    "M22",
    "M23",
    "M14",
    "M31",
    "C01",
    "C06",
    "C13",
    "C18",
    "C19",
    "M04",
    "A12",
    "A13",
    "M24",
    "A01",
    "A02",
    "A18",
    "M03",
    "M15",
    "M18",
    "M11",
    "M27",
    "M20"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S06",
    "S12",
    "S20",
    "S01",
    "S03",
    "S11",
    "S13",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I06"
}
```

<a id="p-i07"></a>

## P-I07 Material texture importer

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I07",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I07",
    "name": "Material texture importer",
    "status": "planned-implementation",
    "dependencyIds": [
      "M14",
      "M11",
      "M26"
    ],
    "methodIds": [
      "F01",
      "F09"
    ],
    "task": "Honor map channels, factors, color spaces, UV orientation and normal convention. Never square the base color by applying a colored map and the same color factor.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "M11",
    "M26",
    "F01",
    "F09"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S01",
    "S03",
    "S06",
    "S02"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I07"
}
```

<a id="p-i08"></a>

## P-I08 Bounded direct manipulation

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I08",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I08",
    "name": "Bounded direct manipulation",
    "status": "planned-implementation",
    "dependencyIds": [
      "C12",
      "C17"
    ],
    "methodIds": [
      "F05"
    ],
    "task": "Implement pointer capture, pointercancel, bounded displacement, tap selection and keyboard operation with identical semantic outcomes.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "F05",
    "M30",
    "M31",
    "A08",
    "M27",
    "A10"
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
    "S01",
    "S03",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I08"
}
```

<a id="p-i09"></a>

## P-I09 Optional curtain drape

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I09",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I09",
    "name": "Optional curtain drape",
    "status": "planned-implementation",
    "dependencyIds": [
      "C11",
      "M10"
    ],
    "methodIds": [
      "F06"
    ],
    "task": "Add pinned XPBD sheet motion only after static behavior works. Use distance constraints and the declared surrogate bend compliance. Stop on nonfinite values or exceeded stretch.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "C11",
    "M10",
    "F06",
    "M04",
    "A18",
    "M14",
    "M31"
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
    "S19",
    "S01",
    "S03",
    "S06",
    "S07",
    "S08"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I09"
}
```

<a id="p-i10"></a>

## P-I10 Operation and interaction state

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I10",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I10",
    "name": "Operation and interaction state",
    "status": "planned-implementation",
    "dependencyIds": [
      "C06",
      "C14",
      "C16",
      "C25"
    ],
    "methodIds": [
      "F05"
    ],
    "task": "Separate hover/focus/press, selection, operation status and disabled state. Do not infer saved state from animation completion.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "C06",
    "C14",
    "C16",
    "C25",
    "F05",
    "M24",
    "M31",
    "M14",
    "A01",
    "A02",
    "M03",
    "M04",
    "A13",
    "M28",
    "M20",
    "A12"
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
    "S01",
    "S03",
    "S06",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I10"
}
```

<a id="p-i11"></a>

## P-I11 Form preview integration

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I11",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I11",
    "name": "Form preview integration",
    "status": "planned-implementation",
    "dependencyIds": [
      "C14",
      "C15",
      "C16"
    ],
    "methodIds": [
      "F08"
    ],
    "task": "Wire labeled native fields to local validation and truthful preview confirmation. No network request or fake registration success.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "C14",
    "C15",
    "C16",
    "F08",
    "M03",
    "M04",
    "A13",
    "M28",
    "M20",
    "A12",
    "M31"
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
    "S01",
    "S03",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I11"
}
```

<a id="p-i12"></a>

## P-I12 Optional foley

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I12",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I12",
    "name": "Optional foley",
    "status": "planned-implementation",
    "dependencyIds": [
      "A14",
      "A15",
      "A16",
      "C10"
    ],
    "methodIds": [
      "F05"
    ],
    "task": "Use user-initiated audio enablement, gain .12, two-voice ceiling and 180ms replay guard. No scroll-loop sound.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "A14",
    "A15",
    "A16",
    "C10",
    "F05",
    "M25",
    "M03",
    "M31",
    "A03",
    "A06"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S06",
    "S11",
    "S12",
    "S13",
    "S01",
    "S03"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I12"
}
```

<a id="p-i13"></a>

## P-I13 Asset production and receipts

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I13",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I13",
    "name": "Asset production and receipts",
    "status": "planned-implementation",
    "dependencyIds": [
      "A01",
      "A02",
      "A03",
      "A04",
      "A05",
      "A06",
      "A07",
      "A08",
      "A09",
      "A10",
      "A11",
      "A12",
      "A13",
      "A14",
      "A15",
      "A16",
      "A17",
      "A18"
    ],
    "methodIds": [
      "F01"
    ],
    "task": "Produce exact requested dimensions and maps. Export glTF 2.0 and KTX2 with retained masters. Attach real license evidence and SHA-256 after production.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "A01",
    "A02",
    "A03",
    "A04",
    "A05",
    "A06",
    "A07",
    "A08",
    "A09",
    "A10",
    "A11",
    "A12",
    "A13",
    "A14",
    "A15",
    "A16",
    "A17",
    "A18",
    "F01",
    "M31",
    "M24",
    "M25",
    "M26",
    "M27",
    "M03",
    "M29",
    "M30",
    "M15",
    "M23",
    "M20",
    "M22",
    "M14"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S06",
    "S15",
    "S16",
    "S01",
    "S03",
    "S02"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I13"
}
```

<a id="p-i14"></a>

## P-I14 Capability and failure tiers

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I14",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I14",
    "name": "Capability and failure tiers",
    "status": "planned-implementation",
    "dependencyIds": [
      "SC08",
      "C23"
    ],
    "methodIds": [
      "F07"
    ],
    "task": "Base behavior on renderer initialization and runtime health, not API presence alone. Context loss retains form and selection state in DOM/application state.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "C23",
    "F07",
    "M03",
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "C06",
    "C14",
    "M04",
    "M31",
    "A12",
    "A13",
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
    "S05",
    "S09",
    "S10",
    "S14",
    "S06",
    "S12",
    "S20",
    "S11",
    "S13",
    "S01",
    "S03",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I14"
}
```

<a id="p-i15"></a>

## P-I15 Responsive layout and typography

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I15",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I15",
    "name": "Responsive layout and typography",
    "status": "planned-implementation",
    "dependencyIds": [
      "SC01",
      "SC02",
      "SC06",
      "A13"
    ],
    "methodIds": [
      "F08"
    ],
    "task": "Use the selected 1/2/4 column grid and real text. Test 320,375,768,1440 CSS px widths and 200/400 percent zoom.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "SC01",
    "SC02",
    "SC06",
    "A13",
    "F08",
    "M22",
    "M23",
    "M14",
    "M31",
    "C01",
    "C06",
    "M15",
    "M18",
    "M11",
    "C02",
    "C03",
    "C04",
    "C05",
    "C21",
    "M04",
    "A12",
    "M24",
    "A01",
    "A02",
    "A10",
    "M20",
    "M27"
  ],
  "sourceIds": [
    "S00",
    "S04",
    "S05",
    "S09",
    "S10",
    "S14",
    "S06",
    "S12",
    "S20",
    "S15",
    "S16",
    "S01",
    "S03",
    "S11",
    "S13"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I15"
}
```

<a id="p-i16"></a>

## P-I16 Visual and numerical validation

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I16",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I16",
    "name": "Visual and numerical validation",
    "status": "planned-implementation",
    "dependencyIds": [
      "SC07",
      "A18"
    ],
    "methodIds": [
      "F02",
      "F07",
      "F08"
    ],
    "task": "Record fixed-seed front/grazing/edge/reverse captures, ablations, measured frame statistics and named human judgments.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "A18",
    "F02",
    "F07",
    "F08",
    "M14",
    "M31",
    "C13",
    "C19",
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
    "S06",
    "S12",
    "S20",
    "S01",
    "S03",
    "S11",
    "S13"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I16"
}
```

<a id="p-i17"></a>

## P-I17 Core reference fixes

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I17",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I17",
    "name": "Core reference fixes",
    "status": "integration-target",
    "dependencyIds": [
      "C25"
    ],
    "methodIds": [
      "F08"
    ],
    "task": "Keep the toggle accessible name stable; connect generated normalized force tokens to bounded CSS affordances; test every token propagation.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
    "F08",
    "M14",
    "M31",
    "A01"
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
    "S01",
    "S03"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I17"
}
```

<a id="p-i18"></a>

## P-I18 CI and evidence integration

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-I18",
  "task": "Implement only this named bounded module within the existing repository. Resolve inputs through the canonical registry and Core token authority. Wire the consumer, test and CI path together. Return changed files, executed results and remaining gaps.",
  "specification": {
    "id": "I18",
    "name": "CI and evidence integration",
    "status": "integration-target",
    "dependencyIds": [
      "C25",
      "SC07"
    ],
    "methodIds": [
      "F01"
    ],
    "task": "Run deterministic checks, schema and graph validation, mutation controls and browser evidence. Fail absent or incomplete evidence; retain diagnostics with explicit failure status.",
    "parameters": {
      "scope": "one bounded module per prompt",
      "packageVersion": "three@0.187.0 only for future enhanced renderer; do not add to Core slice",
      "fixedSeed": 314159,
      "maxChangedSubsystems": 1,
      "preserveExistingCore": true,
      "noUnverifiedPassClaims": true,
      "requiredReturnFields": [
        "changedPaths",
        "canonicalInputs",
        "generatedOutputs",
        "runtimeConsumers",
        "testsRun",
        "results",
        "evidencePaths",
        "openGaps",
        "rollback"
      ]
    },
    "acceptance": [
      "Trace each input to an observable consumer or an explicit planned boundary.",
      "Run relevant negative and boundary controls.",
      "Link exact source digest and environment to evidence.",
      "Stop and report unavailable inputs rather than inventing them."
    ],
    "sourceIds": [
      "S00",
      "S04",
      "S05",
      "S09",
      "S10",
      "S14"
    ]
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-I18"
}
```
