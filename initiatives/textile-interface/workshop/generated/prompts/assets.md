# Assets prompt contracts

<a id="p-a01"></a>

## P-A01 Sewing and stitch geometry

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A01",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A01",
    "name": "Sewing and stitch geometry",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M31"
    ],
    "parameters": {
      "stitchTypes": [
        "running",
        "sashiko",
        "saddle",
        "blanket",
        "cross",
        "box"
      ],
      "threadDiameterMm": 0.32,
      "plyCount": 3,
      "twistTurnsPerMm": 1.5,
      "pitchMm": 3,
      "visibleLengthMm": 1.8,
      "surfaceClearanceMm": 0.03,
      "holeDiameterMm": 0.42,
      "radialSegments": 6,
      "curveSamplesPerMm": 6,
      "seed": 314159
    },
    "outputs": [
      "stitches.glb",
      "stitches.receipt.json"
    ],
    "intent": "Show the stitch entering and leaving cloth, with distinct front and reverse paths.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M31"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A01"
}
```

<a id="p-a02"></a>

## P-A02 Four hole maple button

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A02",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A02",
    "name": "Four hole maple button",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M24",
      "M31"
    ],
    "parameters": {
      "diameterMm": 14,
      "thicknessMm": 2.6,
      "rimBevelMm": 0.7,
      "holeDiameterMm": 1.6,
      "holeSpacingMm": 4.2,
      "holeCount": 4,
      "radialSegments": 48,
      "trianglesMax": 1600,
      "uvSets": 1
    },
    "outputs": [
      "button-maple.glb",
      "button-maple.receipt.json"
    ],
    "intent": "A recognizable fastener supports a labeled action.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M24",
    "M31"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A02"
}
```

<a id="p-a03"></a>

## P-A03 Horn appearance button variant

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A03",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A03",
    "name": "Horn appearance button variant",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M25"
    ],
    "parameters": {
      "diameterMm": 14,
      "thicknessMm": 2.4,
      "rimBevelMm": 0.6,
      "holeDiameterMm": 1.6,
      "holeSpacingMm": 4.2,
      "holeCount": 4,
      "trianglesMax": 1600
    },
    "outputs": [
      "button-horn-inspired.glb",
      "button-horn-inspired.receipt.json"
    ],
    "intent": "Appearance study only; no source-material claim.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M25"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A03"
}
```

<a id="p-a04"></a>

## P-A04 Pearlescent button variant

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A04",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A04",
    "name": "Pearlescent button variant",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M26"
    ],
    "parameters": {
      "diameterMm": 14,
      "thicknessMm": 2.1,
      "rimBevelMm": 0.5,
      "holeDiameterMm": 1.5,
      "holeSpacingMm": 4.0,
      "holeCount": 4,
      "trianglesMax": 1600
    },
    "outputs": [
      "button-pearl-inspired.glb",
      "button-pearl-inspired.receipt.json"
    ],
    "intent": "Restrained angle-dependent appearance without claiming measured nacre optics.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M26"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04",
    "S02"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A04"
}
```

<a id="p-a05"></a>

## P-A05 Brass snap fastener

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A05",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A05",
    "name": "Brass snap fastener",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M27"
    ],
    "parameters": {
      "diameterMm": 12,
      "heightMm": 2,
      "rimBevelMm": 0.3,
      "radialSegments": 48,
      "trianglesMax": 1800
    },
    "outputs": [
      "snap-brass.glb",
      "snap-brass.receipt.json"
    ],
    "intent": "Distinct metal response; no cloth-style sheen on metal.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M27"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A05"
}
```

<a id="p-a06"></a>

## P-A06 Stitched keyhole opening

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A06",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A06",
    "name": "Stitched keyhole opening",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M03",
      "M31"
    ],
    "parameters": {
      "slotLengthMm": 16,
      "slotWidthMm": 2,
      "roundEndDiameterMm": 4,
      "borderThreadDiameterMm": 0.22,
      "stitchPitchMm": 0.6,
      "trianglesMax": 3000
    },
    "outputs": [
      "buttonhole.glb",
      "buttonhole.receipt.json"
    ],
    "intent": "An actual opening with bound thread edges, rather than a dark line.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M03",
    "M31"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A06"
}
```

<a id="p-a07"></a>

## P-A07 Measuring tape strip

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A07",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A07",
    "name": "Measuring tape strip",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M29"
    ],
    "parameters": {
      "lengthMm": 160,
      "widthMm": 12,
      "thicknessMm": 0.4,
      "majorMarkMm": 10,
      "minorMarkMm": 2,
      "bendSegments": 64,
      "trianglesMax": 1200,
      "measurementMeaning": "decorative scale; actual progress remains DOM-labeled"
    },
    "outputs": [
      "measure-tape.glb",
      "measure-marks.svg",
      "measure-tape.receipt.json"
    ],
    "intent": "Keep decorative physical markings separate from application metrics.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M29"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A07"
}
```

<a id="p-a08"></a>

## P-A08 Woven ribbon strip

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A08",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A08",
    "name": "Woven ribbon strip",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M30"
    ],
    "parameters": {
      "lengthMm": 120,
      "widthMm": 10,
      "thicknessMm": 0.4,
      "bendSegments": 48,
      "trianglesMax": 1000
    },
    "outputs": [
      "ribbon.glb",
      "ribbon.receipt.json"
    ],
    "intent": "A restrained divider with visible selvedges.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M30"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A08"
}
```

<a id="p-a09"></a>

## P-A09 Zipper track and puller

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A09",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A09",
    "name": "Zipper track and puller",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M27",
      "M15"
    ],
    "parameters": {
      "trackLengthMm": 100,
      "toothPitchMm": 2,
      "toothWidthMm": 2.2,
      "toothHeightMm": 1.4,
      "pullerLengthMm": 13,
      "pullerWidthMm": 6,
      "trianglesMax": 6000
    },
    "outputs": [
      "zipper.glb",
      "zipper.receipt.json"
    ],
    "intent": "Continuous coherent tooth alignment across the functional slider position.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M27",
    "M15"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A09"
}
```

<a id="p-a10"></a>

## P-A10 Steel pin with brass head

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A10",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A10",
    "name": "Steel pin with brass head",
    "kind": "geometry",
    "status": "planned-not-produced",
    "materialIds": [
      "M27"
    ],
    "parameters": {
      "shaftLengthMm": 22,
      "shaftDiameterMm": 0.55,
      "headDiameterMm": 2.4,
      "trianglesMax": 700
    },
    "outputs": [
      "pin.glb",
      "pin.receipt.json"
    ],
    "intent": "Selection marker with visible relation to the swatch; never the only selected-state cue.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M27"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A10"
}
```

<a id="p-a11"></a>

## P-A11 Cutting mat grid decal

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A11",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A11",
    "name": "Cutting mat grid decal",
    "kind": "vector",
    "status": "planned-not-produced",
    "materialIds": [
      "M23"
    ],
    "parameters": {
      "widthMm": 230,
      "heightMm": 140,
      "majorGridMm": 10,
      "minorGridMm": 5,
      "lineWidthMm": 0.12,
      "lineColorHex": "#B7C1A2",
      "opacity": 0.45,
      "interactive": false
    },
    "outputs": [
      "cutting-mat-grid.svg",
      "cutting-mat-grid.receipt.json"
    ],
    "intent": "A quiet scale reference behind the garment.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M23"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A11"
}
```

<a id="p-a12"></a>

## P-A12 Embroidery motif set

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A12",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A12",
    "name": "Embroidery motif set",
    "kind": "vector",
    "status": "planned-not-produced",
    "materialIds": [
      "M31",
      "M20"
    ],
    "parameters": {
      "motifs": [
        "repair cross",
        "thread loop",
        "network knot",
        "lab swatch",
        "studio patch"
      ],
      "viewBox": [
        0,
        0,
        64,
        64
      ],
      "strokeWidth": 2,
      "strokeLinecap": "round",
      "decorativeOnly": true,
      "liveLabelRequired": true
    },
    "outputs": [
      "motifs.svg",
      "motifs.receipt.json"
    ],
    "intent": "Small crafted marks paired with readable labels.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M31",
    "M20"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A12"
}
```

<a id="p-a13"></a>

## P-A13 Workshop font subset

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A13",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A13",
    "name": "Workshop font subset",
    "kind": "font",
    "status": "planned-not-produced",
    "materialIds": [],
    "parameters": {
      "families": [
        "Fraunces",
        "IBM Plex Sans",
        "IBM Plex Mono"
      ],
      "weights": {
        "Fraunces": [
          600
        ],
        "IBM Plex Sans": [
          400,
          600
        ],
        "IBM Plex Mono": [
          500
        ]
      },
      "format": "woff2",
      "combinedTransferTargetKiB": 180,
      "fontDisplay": "swap",
      "retainLicense": true
    },
    "outputs": [
      "fraunces-600.woff2",
      "plex-sans-400-600.woff2",
      "plex-mono-500.woff2",
      "font-licenses.txt",
      "fonts.receipt.json"
    ],
    "intent": "Use craft-manual hierarchy without embroidered body text.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S15",
      "S16"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
  "dependencyIds": [],
  "sourceIds": [
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A13"
}
```

<a id="p-a14"></a>

## P-A14 Wood button tap

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A14",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A14",
    "name": "Wood button tap",
    "kind": "audio",
    "status": "planned-not-produced",
    "materialIds": [],
    "parameters": {
      "durationMs": 90,
      "sampleRateHz": 48000,
      "bitDepth": 24,
      "channels": 1,
      "peakDbfsMax": -12,
      "fadeInMs": 5,
      "fadeOutMs": 25,
      "runtimeGain": 0.12,
      "maxConcurrentVoices": 2,
      "minimumReplayIntervalMs": 180,
      "defaultEnabled": false
    },
    "outputs": [
      "a14.wav",
      "a14.receipt.json"
    ],
    "intent": "Quiet dry tap, no sharp transient or startling click.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
  "dependencyIds": [],
  "sourceIds": [
    "S00",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A14"
}
```

<a id="p-a15"></a>

## P-A15 Canvas movement rustle

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A15",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A15",
    "name": "Canvas movement rustle",
    "kind": "audio",
    "status": "planned-not-produced",
    "materialIds": [],
    "parameters": {
      "durationMs": 220,
      "sampleRateHz": 48000,
      "bitDepth": 24,
      "channels": 1,
      "peakDbfsMax": -15,
      "fadeInMs": 5,
      "fadeOutMs": 25,
      "runtimeGain": 0.12,
      "maxConcurrentVoices": 2,
      "minimumReplayIntervalMs": 180,
      "defaultEnabled": false
    },
    "outputs": [
      "a15.wav",
      "a15.receipt.json"
    ],
    "intent": "A short, restrained fabric rustle for deliberate pickup only.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
  "dependencyIds": [],
  "sourceIds": [
    "S00",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A15"
}
```

<a id="p-a16"></a>

## P-A16 Tailor shear accent

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A16",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A16",
    "name": "Tailor shear accent",
    "kind": "audio",
    "status": "planned-not-produced",
    "materialIds": [],
    "parameters": {
      "durationMs": 140,
      "sampleRateHz": 48000,
      "bitDepth": 24,
      "channels": 1,
      "peakDbfsMax": -15,
      "fadeInMs": 5,
      "fadeOutMs": 25,
      "runtimeGain": 0.12,
      "maxConcurrentVoices": 2,
      "minimumReplayIntervalMs": 180,
      "defaultEnabled": false
    },
    "outputs": [
      "a16.wav",
      "a16.receipt.json"
    ],
    "intent": "One soft snip for a deliberate cut or reset demonstration; never every click.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
  "dependencyIds": [],
  "sourceIds": [
    "S00",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A16"
}
```

<a id="p-a17"></a>

## P-A17 Workshop concept image set

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A17",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A17",
    "name": "Workshop concept image set",
    "kind": "image",
    "status": "planned-not-produced",
    "materialIds": [
      "M22",
      "M14",
      "M31"
    ],
    "parameters": {
      "frames": [
        {
          "name": "hero",
          "widthPx": 2400,
          "heightPx": 1200
        },
        {
          "name": "phone",
          "widthPx": 1170,
          "heightPx": 1560
        },
        {
          "name": "macro",
          "widthPx": 1600,
          "heightPx": 1600
        }
      ],
      "lightPreset": "warm",
      "textInImage": false,
      "watermark": false,
      "sourceType": "illustrative concept if generated",
      "measuredReference": false
    },
    "outputs": [
      "workshop-hero.webp",
      "workshop-phone.webp",
      "workshop-macro.webp",
      "concepts.receipt.json"
    ],
    "intent": "Establish composition. These pictures cannot substitute for aligned material maps or real specimen photographs.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M22",
    "M14",
    "M31"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A17"
}
```

<a id="p-a18"></a>

## P-A18 Documented textile reference photographs

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-A18",
  "task": "Produce this asset using the exact dimensions and output contract. Record actual creation method, source permissions, tool version, seed, and hashes. If you can only create a concept image, label that limitation and do not fabricate maps, geometry, or physical provenance.",
  "specification": {
    "id": "A18",
    "name": "Documented textile reference photographs",
    "kind": "reference",
    "status": "planned-not-produced",
    "materialIds": [
      "M14",
      "M31"
    ],
    "parameters": {
      "views": [
        "front",
        "grazing-left",
        "grazing-right",
        "edge",
        "reverse",
        "macro"
      ],
      "scaleRulerRequired": true,
      "neutralWhiteBalanceRequired": true,
      "minimumImagePx": 2400,
      "lightingLogRequired": true,
      "originalFilesRetained": true,
      "permissionRequired": true,
      "generatedImagesAllowedAsMeasurement": false
    },
    "outputs": [
      "reference-front.tif",
      "reference-grazing-left.tif",
      "reference-grazing-right.tif",
      "reference-edge.tif",
      "reference-reverse.tif",
      "reference-macro.tif",
      "reference.receipt.json"
    ],
    "intent": "Acquire an actual comparison specimen before making material-fidelity claims.",
    "method": "procedural or artist-authored from a documented reference; generated concepts remain illustrative",
    "sourceIds": [
      "S00",
      "S05",
      "S06"
    ],
    "receipt": {
      "creator": "unassigned",
      "creationMethod": "not-produced",
      "sourceAssetPaths": [],
      "license": "not-established",
      "licenseEvidencePath": "not-produced",
      "generatorVersion": "not-produced",
      "sha256": "not-produced",
      "reviewer": "unassigned",
      "reviewDate": "not-reviewed"
    },
    "acceptance": [
      "Exact dimensions and coordinate convention match the specification.",
      "Runtime asset contains no rasterized interactive label.",
      "Asset origin and license are recorded before release."
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
    "M31"
  ],
  "sourceIds": [
    "S00",
    "S05",
    "S06",
    "S01",
    "S03",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-A18"
}
```
