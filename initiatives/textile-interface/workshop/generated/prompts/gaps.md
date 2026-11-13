# Gaps prompt contracts

<a id="p-g01"></a>

## P-G01 Material realism not established

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G01",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G01",
    "name": "Material realism not established",
    "status": "open",
    "affectedIds": [
      "M14",
      "M31",
      "SC04"
    ],
    "fix": "Produce actual geometry and texture assets; compare to documented specimen captures.",
    "verificationIds": [
      "E01",
      "E02"
    ],
    "promotionBlocked": "material-fidelity or hyper-realism claims"
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
    "E01",
    "E02",
    "M14",
    "M31",
    "SC04",
    "SC07",
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06",
    "S12",
    "S20",
    "S10",
    "S11",
    "S13"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G01"
}
```

<a id="p-g02"></a>

## P-G02 Enhanced renderer absent

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G02",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G02",
    "name": "Enhanced renderer absent",
    "status": "open",
    "affectedIds": [
      "I02",
      "I03",
      "I04",
      "I05",
      "I06",
      "I07",
      "I09"
    ],
    "fix": "Implement bounded enhanced modules after Core and asset acceptance.",
    "verificationIds": [
      "E02",
      "E03",
      "E04"
    ],
    "promotionBlocked": "3D cloth or yarn runtime claims"
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
    "E02",
    "E03",
    "E04",
    "I02",
    "I03",
    "I04",
    "I05",
    "I06",
    "I07",
    "I09",
    "SC07",
    "M14",
    "SC04",
    "SC08",
    "C14",
    "I14",
    "M01",
    "M04",
    "F02",
    "F03",
    "F04",
    "M07",
    "M11",
    "M12",
    "M13",
    "M28",
    "F07",
    "A01",
    "C06",
    "C25",
    "F05",
    "SC01",
    "F08",
    "M26",
    "F01",
    "F09",
    "C11",
    "M10",
    "F06",
    "M31",
    "C13",
    "C19",
    "C18",
    "M03",
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "A13",
    "C23",
    "M24",
    "A02",
    "M22",
    "M23",
    "A18",
    "M27",
    "M15",
    "M18",
    "A12",
    "A10",
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
    "S02",
    "S19",
    "S07",
    "S08",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G02"
}
```

<a id="p-g03"></a>

## P-G03 Hosted route acceptance remains separate

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G03",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G03",
    "name": "Hosted route acceptance remains separate",
    "status": "open",
    "affectedIds": [
      "C25",
      "SC08"
    ],
    "fix": "Verify an actual preview URL serving exact-head CSS and interactions.",
    "verificationIds": [
      "E04"
    ],
    "promotionBlocked": "deployed acceptance claims"
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
    "E04",
    "C25",
    "SC08",
    "C14",
    "I14",
    "M14",
    "M31",
    "A01",
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
    "A12",
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
    "S10",
    "S11",
    "S12",
    "S13",
    "S04",
    "S06",
    "S20",
    "S05",
    "S09",
    "S14",
    "S01",
    "S03",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G03"
}
```

<a id="p-g04"></a>

## P-G04 Loading success and error state coverage incomplete

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G04",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G04",
    "name": "Loading success and error state coverage incomplete",
    "status": "open",
    "affectedIds": [
      "C14",
      "C16",
      "C25"
    ],
    "fix": "Implement operation states only with a truthful underlying operation and full transition tests.",
    "verificationIds": [
      "E04",
      "E07"
    ],
    "promotionBlocked": "all-state conformance"
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
    "E04",
    "E07",
    "C14",
    "C16",
    "C25",
    "SC08",
    "I14",
    "C20",
    "M03",
    "M04",
    "A13",
    "M28",
    "M20",
    "A12",
    "M14",
    "M31",
    "A01",
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "C06",
    "C23",
    "F07",
    "M25",
    "A03",
    "A06",
    "A10",
    "M15",
    "M18",
    "M11",
    "M24",
    "A02",
    "M27"
  ],
  "sourceIds": [
    "S00",
    "S10",
    "S11",
    "S12",
    "S13",
    "S04",
    "S06",
    "S20",
    "S05",
    "S09",
    "S14",
    "S01",
    "S03",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G04"
}
```

<a id="p-g05"></a>

## P-G05 Fonts audio and physical assets not produced

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G05",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G05",
    "name": "Fonts audio and physical assets not produced",
    "status": "open",
    "affectedIds": [
      "A13",
      "A14",
      "A15",
      "A16",
      "A18"
    ],
    "fix": "Acquire or create assets with permission, source/license records and real hashes.",
    "verificationIds": [
      "E01",
      "E02"
    ],
    "promotionBlocked": "asset availability and provenance completeness"
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
    "E01",
    "E02",
    "A13",
    "A14",
    "A15",
    "A16",
    "A18",
    "SC04",
    "M14",
    "M31",
    "SC07",
    "C13",
    "C18",
    "C19",
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
    "S15",
    "S16",
    "S05",
    "S06",
    "S04",
    "S12",
    "S20",
    "S01",
    "S03",
    "S10",
    "S11",
    "S13"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G05"
}
```

<a id="p-g06"></a>

## P-G06 Hardware performance unmeasured

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G06",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G06",
    "name": "Hardware performance unmeasured",
    "status": "open",
    "affectedIds": [
      "I14",
      "I16"
    ],
    "fix": "Measure the selected real phone and desktop with versioned environments.",
    "verificationIds": [
      "E03"
    ],
    "promotionBlocked": "performance certification or device-parity claims"
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
    "E03",
    "I14",
    "I16",
    "SC04",
    "I04",
    "SC08",
    "C23",
    "F07",
    "SC07",
    "A18",
    "F02",
    "F08",
    "M14",
    "M31",
    "C13",
    "C18",
    "C19",
    "M11",
    "M12",
    "M13",
    "M28",
    "M03",
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "C06",
    "C14",
    "M15",
    "M18",
    "A12",
    "M04",
    "M27",
    "A13",
    "A01",
    "A10",
    "M24",
    "A02",
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
    "S11",
    "S13",
    "S01",
    "S03",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G06"
}
```

<a id="p-g07"></a>

## P-G07 Core accessible toggle naming

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G07",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G07",
    "name": "Core accessible toggle naming",
    "status": "integration-target",
    "affectedIds": [
      "C25",
      "I17"
    ],
    "fix": "Keep Stitch commitment stable and let aria-pressed communicate state.",
    "verificationIds": [
      "E07"
    ],
    "promotionBlocked": "stable-toggle semantic claim until browser test passes"
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
    "E07",
    "C25",
    "I17",
    "C20",
    "M14",
    "M31",
    "A01",
    "F08",
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
    "S04",
    "S05",
    "S09",
    "S14",
    "S01",
    "S03",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G07"
}
```

<a id="p-g08"></a>

## P-G08 Interrupted evidence and stale screenshots

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G08",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G08",
    "name": "Interrupted evidence and stale screenshots",
    "status": "integration-target",
    "affectedIds": [
      "I18",
      "C25"
    ],
    "fix": "Run-scoped cleanup, expected check count, completion status, errors and screenshot digests.",
    "verificationIds": [
      "E08"
    ],
    "promotionBlocked": "complete-pass evidence until verifier controls pass"
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
    "E08",
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G08"
}
```

<a id="p-g09"></a>

## P-G09 Current normalized forces are not calibrated mechanics

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G09",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G09",
    "name": "Current normalized forces are not calibrated mechanics",
    "status": "open",
    "affectedIds": [
      "C25",
      "F05",
      "F06"
    ],
    "fix": "Document each selected mapping; measure physical samples before claiming engineering constants.",
    "verificationIds": [
      "E01"
    ],
    "promotionBlocked": "measured textile mechanics"
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
    "E01",
    "C25",
    "F05",
    "F06",
    "SC04",
    "M14",
    "M31",
    "A01",
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
    "S10",
    "S11",
    "S12",
    "S13",
    "S09",
    "S04",
    "S06",
    "S20",
    "S01",
    "S03",
    "S05"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G09"
}
```

<a id="p-g10"></a>

## P-G10 No whole-language conformance

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-G10",
  "task": "Resolve this gap with the smallest named fix and its declared verification. Retain the blocked claim until evidence exists. Link the resulting code, test, exact-head receipt and reviewer decision.",
  "specification": {
    "id": "G10",
    "name": "No whole-language conformance",
    "status": "open",
    "affectedIds": [
      "C25",
      "I17",
      "I18"
    ],
    "fix": "Retain v0.1/v0.2 authority boundaries and verify all normative states before promotion.",
    "verificationIds": [
      "E04",
      "E07"
    ],
    "promotionBlocked": "full TIL conformance, Figma synchronization, or complete accessibility certification"
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
    "E04",
    "E07",
    "C25",
    "I17",
    "I18",
    "SC08",
    "C14",
    "I14",
    "C20",
    "M14",
    "M31",
    "A01",
    "F08",
    "SC07",
    "F01",
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
    "M25",
    "A03",
    "A06",
    "C13",
    "C19",
    "A12",
    "A10",
    "M15",
    "M18",
    "M11",
    "M24",
    "A02",
    "A18",
    "M27",
    "M20"
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
    "S06",
    "S20",
    "S01",
    "S03",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-G10"
}
```
