# Scenes prompt contracts

<a id="p-sc01"></a>

## P-SC01 Workshop hero

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-SC01",
  "task": "Compose this scene using its linked components and surfaces. Preserve selected dimensions, camera, lighting, live text, and responsive intent. Do not invent additional product routes, metrics, or backend capabilities.",
  "specification": {
    "id": "SC01",
    "name": "Workshop hero",
    "status": "planned-consumer",
    "componentIds": [
      "C01",
      "C06"
    ],
    "materialIds": [
      "M22",
      "M23",
      "M14",
      "M31"
    ],
    "layout": {
      "viewWidthMm": 360,
      "viewHeightMm": 180,
      "canvasAspectRatio": 2.0,
      "textLayer": "DOM outside canvas",
      "mobileComposition": "separate SC06 composition; never scale desktop text into a small canvas",
      "captionMaxWidthCh": 48,
      "title": "Keep It Moving",
      "subtitle": "Repair what matters. Make room for what comes next.",
      "safeInsetRatio": 0.08
    },
    "camera": {
      "type": "orthographic",
      "positionM": [
        0,
        0,
        0.6
      ],
      "targetM": [
        0,
        0,
        0
      ],
      "nearM": 0.01,
      "farM": 2,
      "viewHeightM": 0.18,
      "orbitEnabled": false,
      "orbitAngleLimitDeg": 15,
      "zoomInitial": 1
    },
    "lightPreset": "warm",
    "objects": [
      {
        "asset": "bench",
        "positionMm": [
          0,
          0,
          -12
        ],
        "sizeMm": [
          420,
          240,
          24
        ]
      },
      {
        "asset": "cutting-mat",
        "positionMm": [
          -40,
          -12,
          1.5
        ],
        "sizeMm": [
          230,
          140,
          3
        ]
      },
      {
        "asset": "denim-patch",
        "positionMm": [
          52,
          -10,
          4
        ],
        "sizeMm": [
          84,
          100,
          0.95
        ]
      }
    ],
    "compositionRules": [
      "One consistent source of cast-shadow direction.",
      "Readable text stays outside lighting and deformation.",
      "No invented testimonials, counts, or sustainability badges."
    ],
    "renderTier": "T1",
    "sourceIds": [
      "S00",
      "S04",
      "S06",
      "S12",
      "S20"
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
    "M23",
    "M14",
    "M31",
    "C01",
    "C06",
    "M04",
    "A12",
    "A13",
    "M24",
    "A01",
    "A02",
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
    "S13",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-SC01"
}
```

<a id="p-sc02"></a>

## P-SC02 Four offering overview

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-SC02",
  "task": "Compose this scene using its linked components and surfaces. Preserve selected dimensions, camera, lighting, live text, and responsive intent. Do not invent additional product routes, metrics, or backend capabilities.",
  "specification": {
    "id": "SC02",
    "name": "Four offering overview",
    "status": "planned-consumer",
    "componentIds": [
      "C02",
      "C03",
      "C04",
      "C05"
    ],
    "materialIds": [
      "M14",
      "M15",
      "M18",
      "M11"
    ],
    "layout": {
      "viewWidthMm": 340,
      "viewHeightMm": 150,
      "canvasAspectRatio": 2.2667,
      "textLayer": "DOM outside canvas",
      "mobileComposition": "separate SC06 composition; never scale desktop text into a small canvas",
      "captionMaxWidthCh": 48,
      "title": "Four ways to take part",
      "subtitle": "Explore repair, connection, experiments, and creative work.",
      "safeInsetRatio": 0.08
    },
    "camera": {
      "type": "orthographic",
      "positionM": [
        0,
        0,
        0.6
      ],
      "targetM": [
        0,
        0,
        0
      ],
      "nearM": 0.01,
      "farM": 2,
      "viewHeightM": 0.15,
      "orbitEnabled": false,
      "orbitAngleLimitDeg": 15,
      "zoomInitial": 1
    },
    "lightPreset": "warm",
    "objects": [],
    "compositionRules": [
      "One consistent source of cast-shadow direction.",
      "Readable text stays outside lighting and deformation.",
      "No invented testimonials, counts, or sustainability badges."
    ],
    "renderTier": "T1",
    "sourceIds": [
      "S00",
      "S04",
      "S06",
      "S12",
      "S20"
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
    "M15",
    "M18",
    "M11",
    "C02",
    "C03",
    "C04",
    "C05",
    "M04",
    "M31",
    "A01",
    "A10",
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-SC02"
}
```

<a id="p-sc03"></a>

## P-SC03 Repair pilot arrangement

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-SC03",
  "task": "Compose this scene using its linked components and surfaces. Preserve selected dimensions, camera, lighting, live text, and responsive intent. Do not invent additional product routes, metrics, or backend capabilities.",
  "specification": {
    "id": "SC03",
    "name": "Repair pilot arrangement",
    "status": "planned-consumer",
    "componentIds": [
      "C02",
      "C06",
      "C12",
      "C17"
    ],
    "materialIds": [
      "M14",
      "M31",
      "M24",
      "M03"
    ],
    "layout": {
      "viewWidthMm": 220,
      "viewHeightMm": 150,
      "canvasAspectRatio": 1.4667,
      "textLayer": "DOM outside canvas",
      "mobileComposition": "separate SC06 composition; never scale desktop text into a small canvas",
      "captionMaxWidthCh": 48,
      "title": "Repair and restyle pilot",
      "subtitle": "Inspect the repair sample, then preview your interest.",
      "safeInsetRatio": 0.08
    },
    "camera": {
      "type": "orthographic",
      "positionM": [
        0,
        0,
        0.6
      ],
      "targetM": [
        0,
        0,
        0
      ],
      "nearM": 0.01,
      "farM": 2,
      "viewHeightM": 0.15,
      "orbitEnabled": false,
      "orbitAngleLimitDeg": 15,
      "zoomInitial": 1
    },
    "lightPreset": "neutral",
    "objects": [
      {
        "asset": "repair-swatch",
        "positionMm": [
          0,
          0,
          1
        ],
        "sizeMm": [
          84,
          100,
          0.95
        ]
      },
      {
        "asset": "satin-label",
        "positionMm": [
          0,
          -22,
          2
        ],
        "sizeMm": [
          48,
          16,
          0.3
        ]
      }
    ],
    "compositionRules": [
      "One consistent source of cast-shadow direction.",
      "Readable text stays outside lighting and deformation.",
      "No invented testimonials, counts, or sustainability badges."
    ],
    "renderTier": "T1",
    "sourceIds": [
      "S00",
      "S04",
      "S06",
      "S12",
      "S20"
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
    "M31",
    "M24",
    "M03",
    "C02",
    "C06",
    "C12",
    "C17",
    "M04",
    "A01",
    "A10",
    "A02",
    "M30",
    "A08",
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-SC03"
}
```

<a id="p-sc04"></a>

## P-SC04 Close material inspection

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-SC04",
  "task": "Compose this scene using its linked components and surfaces. Preserve selected dimensions, camera, lighting, live text, and responsive intent. Do not invent additional product routes, metrics, or backend capabilities.",
  "specification": {
    "id": "SC04",
    "name": "Close material inspection",
    "status": "planned-consumer",
    "componentIds": [
      "C13",
      "C18",
      "C19"
    ],
    "materialIds": [
      "M14",
      "M31"
    ],
    "layout": {
      "viewWidthMm": 32,
      "viewHeightMm": 32,
      "canvasAspectRatio": 1.0,
      "textLayer": "DOM outside canvas",
      "mobileComposition": "separate SC06 composition; never scale desktop text into a small canvas",
      "captionMaxWidthCh": 48,
      "title": "Look closer",
      "subtitle": "Examine the weave, stitches, and edges.",
      "safeInsetRatio": 0.08
    },
    "camera": {
      "type": "orthographic",
      "positionM": [
        0,
        0,
        0.6
      ],
      "targetM": [
        0,
        0,
        0
      ],
      "nearM": 0.01,
      "farM": 2,
      "viewHeightM": 0.032,
      "orbitEnabled": true,
      "orbitAngleLimitDeg": 15,
      "zoomInitial": 1
    },
    "lightPreset": "neutral",
    "objects": [
      {
        "asset": "yarn-crop",
        "positionMm": [
          0,
          0,
          0
        ],
        "sizeMm": [
          32,
          32,
          0.95
        ]
      }
    ],
    "compositionRules": [
      "One consistent source of cast-shadow direction.",
      "Readable text stays outside lighting and deformation.",
      "No invented testimonials, counts, or sustainability badges."
    ],
    "renderTier": "T2",
    "sourceIds": [
      "S00",
      "S04",
      "S06",
      "S12",
      "S20"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-SC04"
}
```

<a id="p-sc05"></a>

## P-SC05 Interest preview

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-SC05",
  "task": "Compose this scene using its linked components and surfaces. Preserve selected dimensions, camera, lighting, live text, and responsive intent. Do not invent additional product routes, metrics, or backend capabilities.",
  "specification": {
    "id": "SC05",
    "name": "Interest preview",
    "status": "planned-consumer",
    "componentIds": [
      "C14",
      "C15",
      "C16",
      "C07"
    ],
    "materialIds": [
      "M03",
      "M04"
    ],
    "layout": {
      "viewWidthMm": 160,
      "viewHeightMm": 140,
      "canvasAspectRatio": 1.1429,
      "textLayer": "DOM outside canvas",
      "mobileComposition": "separate SC06 composition; never scale desktop text into a small canvas",
      "captionMaxWidthCh": 48,
      "title": "Preview your interest",
      "subtitle": "This preview checks the form locally. Your details are not sent.",
      "safeInsetRatio": 0.08
    },
    "camera": {
      "type": "orthographic",
      "positionM": [
        0,
        0,
        0.6
      ],
      "targetM": [
        0,
        0,
        0
      ],
      "nearM": 0.01,
      "farM": 2,
      "viewHeightM": 0.14,
      "orbitEnabled": false,
      "orbitAngleLimitDeg": 15,
      "zoomInitial": 1
    },
    "lightPreset": "neutral",
    "objects": [],
    "compositionRules": [
      "One consistent source of cast-shadow direction.",
      "Readable text stays outside lighting and deformation.",
      "No invented testimonials, counts, or sustainability badges."
    ],
    "renderTier": "T1",
    "sourceIds": [
      "S00",
      "S04",
      "S06",
      "S12",
      "S20"
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
    "M04",
    "C14",
    "C15",
    "C16",
    "C07",
    "A13",
    "M28",
    "M20",
    "A12",
    "M29",
    "A07",
    "M31"
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
    "S13",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-SC05"
}
```

<a id="p-sc06"></a>

## P-SC06 Phone workshop

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-SC06",
  "task": "Compose this scene using its linked components and surfaces. Preserve selected dimensions, camera, lighting, live text, and responsive intent. Do not invent additional product routes, metrics, or backend capabilities.",
  "specification": {
    "id": "SC06",
    "name": "Phone workshop",
    "status": "planned-consumer",
    "componentIds": [
      "C21",
      "C06",
      "C02"
    ],
    "materialIds": [
      "M22",
      "M14",
      "M31"
    ],
    "layout": {
      "viewWidthMm": 88,
      "viewHeightMm": 98,
      "canvasAspectRatio": 0.898,
      "textLayer": "DOM outside canvas",
      "mobileComposition": "separate SC06 composition; never scale desktop text into a small canvas",
      "captionMaxWidthCh": 48,
      "title": "Keep It Moving",
      "subtitle": "A clear invitation, followed by one offering per row.",
      "safeInsetRatio": 0.08
    },
    "camera": {
      "type": "orthographic",
      "positionM": [
        0,
        0,
        0.6
      ],
      "targetM": [
        0,
        0,
        0
      ],
      "nearM": 0.01,
      "farM": 2,
      "viewHeightM": 0.098,
      "orbitEnabled": false,
      "orbitAngleLimitDeg": 15,
      "zoomInitial": 1
    },
    "lightPreset": "warm",
    "objects": [
      {
        "asset": "repair-swatch",
        "positionMm": [
          12,
          -8,
          2
        ],
        "sizeMm": [
          48,
          58,
          0.95
        ]
      }
    ],
    "compositionRules": [
      "One consistent source of cast-shadow direction.",
      "Readable text stays outside lighting and deformation.",
      "No invented testimonials, counts, or sustainability badges."
    ],
    "renderTier": "T1",
    "sourceIds": [
      "S00",
      "S04",
      "S06",
      "S12",
      "S20"
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
    "M31",
    "C21",
    "C06",
    "C02",
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-SC06"
}
```

<a id="p-sc07"></a>

## P-SC07 Material acceptance fixture

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-SC07",
  "task": "Compose this scene using its linked components and surfaces. Preserve selected dimensions, camera, lighting, live text, and responsive intent. Do not invent additional product routes, metrics, or backend capabilities.",
  "specification": {
    "id": "SC07",
    "name": "Material acceptance fixture",
    "status": "planned-consumer",
    "componentIds": [
      "C13",
      "C19"
    ],
    "materialIds": [
      "M14",
      "M31"
    ],
    "layout": {
      "viewWidthMm": 40,
      "viewHeightMm": 40,
      "canvasAspectRatio": 1.0,
      "textLayer": "DOM outside canvas",
      "mobileComposition": "separate SC06 composition; never scale desktop text into a small canvas",
      "captionMaxWidthCh": 48,
      "title": "Material comparison fixture",
      "subtitle": "Internal acceptance scene; not product navigation.",
      "safeInsetRatio": 0.08
    },
    "camera": {
      "type": "orthographic",
      "positionM": [
        0,
        0,
        0.6
      ],
      "targetM": [
        0,
        0,
        0
      ],
      "nearM": 0.01,
      "farM": 2,
      "viewHeightM": 0.04,
      "orbitEnabled": true,
      "orbitAngleLimitDeg": 15,
      "zoomInitial": 1
    },
    "lightPreset": "grazing",
    "objects": [
      {
        "asset": "neutral-test-coupon",
        "positionMm": [
          0,
          0,
          0
        ],
        "sizeMm": [
          32,
          32,
          0.95
        ]
      }
    ],
    "compositionRules": [
      "One consistent source of cast-shadow direction.",
      "Readable text stays outside lighting and deformation.",
      "No invented testimonials, counts, or sustainability badges."
    ],
    "renderTier": "T2",
    "sourceIds": [
      "S00",
      "S04",
      "S06",
      "S12",
      "S20"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-SC07"
}
```

<a id="p-sc08"></a>

## P-SC08 Semantic fallback

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-SC08",
  "task": "Compose this scene using its linked components and surfaces. Preserve selected dimensions, camera, lighting, live text, and responsive intent. Do not invent additional product routes, metrics, or backend capabilities.",
  "specification": {
    "id": "SC08",
    "name": "Semantic fallback",
    "status": "planned-consumer",
    "componentIds": [
      "C01",
      "C02",
      "C03",
      "C04",
      "C05",
      "C06",
      "C14"
    ],
    "materialIds": [
      "M03"
    ],
    "layout": {
      "viewWidthMm": 120,
      "viewHeightMm": 120,
      "canvasAspectRatio": 1.0,
      "textLayer": "DOM outside canvas",
      "mobileComposition": "separate SC06 composition; never scale desktop text into a small canvas",
      "captionMaxWidthCh": 48,
      "title": "Keep It Moving",
      "subtitle": "Every task remains available without the material renderer.",
      "safeInsetRatio": 0.08
    },
    "camera": {
      "type": "orthographic",
      "positionM": [
        0,
        0,
        0.6
      ],
      "targetM": [
        0,
        0,
        0
      ],
      "nearM": 0.01,
      "farM": 2,
      "viewHeightM": 0.12,
      "orbitEnabled": false,
      "orbitAngleLimitDeg": 15,
      "zoomInitial": 1
    },
    "lightPreset": "neutral",
    "objects": [],
    "compositionRules": [
      "One consistent source of cast-shadow direction.",
      "Readable text stays outside lighting and deformation.",
      "No invented testimonials, counts, or sustainability badges."
    ],
    "renderTier": "T0",
    "sourceIds": [
      "S00",
      "S04",
      "S06",
      "S12",
      "S20"
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
    "S06",
    "S12",
    "S20",
    "S01",
    "S03",
    "S05",
    "S10",
    "S11",
    "S13",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-SC08"
}
```
