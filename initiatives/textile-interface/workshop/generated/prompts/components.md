# Components prompt contracts

<a id="p-c01"></a>

## P-C01 Care label navigation

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C01",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C01",
    "name": "Care label navigation",
    "status": "planned-consumer",
    "materialIds": [
      "M04",
      "M31"
    ],
    "kind": "navigation",
    "layout": {
      "widthDesktopPx": 280,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 64,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "nav",
      "type": "button",
      "label": "Keep It Moving",
      "action": "navigate to existing anchored section",
      "targetId": "top",
      "keyboard": [
        "Tab",
        "Enter"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "aria-current for active navigation only"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "saddle",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c01.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A12",
      "A13"
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
    "M04",
    "M31",
    "A12",
    "A13",
    "M20"
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
    "S06",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C01"
}
```

<a id="p-c02"></a>

## P-C02 Repair Commons denim swatch

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C02",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C02",
    "name": "Repair Commons denim swatch",
    "status": "planned-consumer",
    "materialIds": [
      "M14",
      "M04",
      "M31"
    ],
    "kind": "card",
    "layout": {
      "widthDesktopPx": 282,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 360,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "article with h2 and explicit details button",
      "type": "button",
      "label": "Repair Commons",
      "action": "open offering details",
      "targetId": "c02-details",
      "keyboard": [
        "Tab",
        "Enter",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none on article",
      "description": "Repair and restyle what you already own."
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 16,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "sashiko",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c02.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A01",
      "A10"
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
    "M04",
    "M31",
    "A01",
    "A10",
    "M27"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C02"
}
```

<a id="p-c03"></a>

## P-C03 Textile Network ripstop swatch

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C03",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C03",
    "name": "Textile Network ripstop swatch",
    "status": "planned-consumer",
    "materialIds": [
      "M15",
      "M04",
      "M31"
    ],
    "kind": "card",
    "layout": {
      "widthDesktopPx": 282,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 360,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "article with h2 and explicit details button",
      "type": "button",
      "label": "Textile Network",
      "action": "open offering details",
      "targetId": "c03-details",
      "keyboard": [
        "Tab",
        "Enter",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none on article",
      "description": "Find people, skills, and materials for the next repair."
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 16,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c03.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A01"
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
    "M15",
    "M04",
    "M31",
    "A01"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C03"
}
```

<a id="p-c04"></a>

## P-C04 Futures Lab natural fiber swatch

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C04",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C04",
    "name": "Futures Lab natural fiber swatch",
    "status": "planned-consumer",
    "materialIds": [
      "M18",
      "M04",
      "M31"
    ],
    "kind": "card",
    "layout": {
      "widthDesktopPx": 282,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 360,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "article with h2 and explicit details button",
      "type": "button",
      "label": "Futures Lab",
      "action": "open offering details",
      "targetId": "c04-details",
      "keyboard": [
        "Tab",
        "Enter",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none on article",
      "description": "Explore material possibilities through documented experiments."
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 16,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c04.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A01"
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
    "M18",
    "M04",
    "M31",
    "A01"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C04"
}
```

<a id="p-c05"></a>

## P-C05 Creative Studio velvet swatch

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C05",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C05",
    "name": "Creative Studio velvet swatch",
    "status": "planned-consumer",
    "materialIds": [
      "M11",
      "M04",
      "M31"
    ],
    "kind": "card",
    "layout": {
      "widthDesktopPx": 282,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 360,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "article with h2 and explicit details button",
      "type": "button",
      "label": "Creative Studio",
      "action": "open offering details",
      "targetId": "c05-details",
      "keyboard": [
        "Tab",
        "Enter",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none on article",
      "description": "Develop expressive textile and visual work."
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 16,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c05.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A01"
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
    "M04",
    "M31",
    "A01"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C05"
}
```

<a id="p-c06"></a>

## P-C06 Sewn wooden call to action

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C06",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C06",
    "name": "Sewn wooden call to action",
    "status": "planned-consumer",
    "materialIds": [
      "M24",
      "M31",
      "M14"
    ],
    "kind": "action",
    "layout": {
      "widthDesktopPx": 280,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 56,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "a",
      "type": "button",
      "label": "Explore the repair pilot",
      "action": "navigate to repair-pilot section",
      "targetId": "repair-pilot",
      "keyboard": [
        "Tab",
        "Enter"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "four-hole cross",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.3,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ],
      "buttonDiameterMm": 14,
      "buttonThicknessMm": 2.6,
      "holeDiameterMm": 1.6,
      "holeSpacingMm": 4.2,
      "threadLoopCount": 4
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c06.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A01",
      "A02"
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
    "M31",
    "M14",
    "A01",
    "A02"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C06"
}
```

<a id="p-c07"></a>

## P-C07 Measuring tape progress

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C07",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C07",
    "name": "Measuring tape progress",
    "status": "planned-consumer",
    "materialIds": [
      "M29"
    ],
    "kind": "progress",
    "layout": {
      "widthDesktopPx": 320,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 48,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "progress with adjacent live text",
      "type": "button",
      "label": "Step 1 of 2",
      "action": "show actual form step; no invented metric",
      "targetId": "interest-form",
      "keyboard": [],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle"
      ],
      "selection": [
        "not-applicable"
      ],
      "operation": [
        "idle"
      ],
      "disabled": false,
      "initial": {
        "interaction": "idle",
        "selection": "not-applicable",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c07.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "progress": {
      "minimum": 0,
      "maximum": 2,
      "initialValue": 1,
      "unit": "form step",
      "unitProvenance": "application state",
      "majorMarkPx": 32,
      "minorMarksPerMajor": 4,
      "animateValue": false
    },
    "assetIds": [
      "A07"
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
    "M29",
    "A07"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C07"
}
```

<a id="p-c08"></a>

## P-C08 Ribbon section divider

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C08",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C08",
    "name": "Ribbon section divider",
    "status": "planned-consumer",
    "materialIds": [
      "M30"
    ],
    "kind": "decoration",
    "layout": {
      "widthDesktopPx": 320,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 16,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "div aria-hidden=true",
      "type": "button",
      "label": "",
      "action": "separate content groups",
      "targetId": "none",
      "keyboard": [],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle"
      ],
      "selection": [
        "not-applicable"
      ],
      "operation": [
        "idle"
      ],
      "disabled": false,
      "initial": {
        "interaction": "idle",
        "selection": "not-applicable",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 0,
      "hoverLiftPx": 0,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c08.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A08"
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
    "M30",
    "A08"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C08"
}
```

<a id="p-c09"></a>

## P-C09 Zipper progress alternative

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C09",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C09",
    "name": "Zipper progress alternative",
    "status": "planned-consumer",
    "materialIds": [
      "M27",
      "M15"
    ],
    "kind": "progress",
    "layout": {
      "widthDesktopPx": 320,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 48,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "progress with live numeric label",
      "type": "button",
      "label": "Preview progress",
      "action": "show a real two-step preview state",
      "targetId": "interest-form",
      "keyboard": [],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle"
      ],
      "selection": [
        "not-applicable"
      ],
      "operation": [
        "idle"
      ],
      "disabled": false,
      "initial": {
        "interaction": "idle",
        "selection": "not-applicable",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c09.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "progress": {
      "minimum": 0,
      "maximum": 2,
      "initialValue": 1,
      "unit": "preview step",
      "unitProvenance": "application state",
      "toothPitchMm": 2,
      "pullerTravelPx": 240
    },
    "assetIds": [
      "A09"
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
    "M15",
    "A09"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C09"
}
```

<a id="p-c10"></a>

## P-C10 Buttonhole sound toggle

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C10",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C10",
    "name": "Buttonhole sound toggle",
    "status": "planned-consumer",
    "materialIds": [
      "M25",
      "M03",
      "M31"
    ],
    "kind": "toggle",
    "layout": {
      "widthDesktopPx": 160,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 56,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "input type=checkbox with visible label",
      "type": "button",
      "label": "Sound",
      "action": "toggle optional sound",
      "targetId": "audio-preferences",
      "keyboard": [
        "Tab",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "native checked"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "off",
        "on"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "off",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 0,
      "hoverLiftPx": 0,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 0,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c10.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A03",
      "A06",
      "A14"
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
    "M25",
    "M03",
    "M31",
    "A03",
    "A06",
    "A14"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C10"
}
```

<a id="p-c11"></a>

## P-C11 Curtain detail dialog

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C11",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C11",
    "name": "Curtain detail dialog",
    "status": "planned-consumer",
    "materialIds": [
      "M10",
      "M04"
    ],
    "kind": "dialog",
    "layout": {
      "widthDesktopPx": 560,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 480,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "dialog via showModal",
      "type": "button",
      "label": "Repair pilot details",
      "action": "open or close offering details",
      "targetId": "repair-dialog",
      "keyboard": [
        "Tab",
        "Shift+Tab",
        "Escape"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none",
      "initialFocus": "dialog heading tabindex=-1"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 0,
      "hoverLiftPx": 0,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 240,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 0,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "blanket",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 2,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c11.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13",
      "S19"
    ],
    "assetIds": [
      "A18"
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
    "M10",
    "M04",
    "A18",
    "M14",
    "M31"
  ],
  "sourceIds": [
    "S00",
    "S10",
    "S11",
    "S12",
    "S13",
    "S19",
    "S01",
    "S03",
    "S04",
    "S05",
    "S06",
    "S07",
    "S08"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C11"
}
```

<a id="p-c12"></a>

## P-C12 Bounded pull tab

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C12",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C12",
    "name": "Bounded pull tab",
    "status": "planned-consumer",
    "materialIds": [
      "M30",
      "M31"
    ],
    "kind": "action",
    "layout": {
      "widthDesktopPx": 160,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 56,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "button",
      "type": "button",
      "label": "Open material details",
      "action": "reveal material details; click is equivalent to pull",
      "targetId": "repair-pilot",
      "keyboard": [
        "Tab",
        "Enter",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "aria-pressed only for toggle or selectable option"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.025,
      "springStiffnessNPerM": 85,
      "springDampingNsPerM": 2.92,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "box stitch",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c12.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A08"
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
    "M30",
    "M31",
    "A08"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C12"
}
```

<a id="p-c13"></a>

## P-C13 Macro material inspector

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C13",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C13",
    "name": "Macro material inspector",
    "status": "planned-consumer",
    "materialIds": [
      "M14",
      "M31"
    ],
    "kind": "inspector",
    "layout": {
      "widthDesktopPx": 640,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 480,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "section with labeled zoom and light controls",
      "type": "button",
      "label": "Inspect denim",
      "action": "inspect selected material at 1x or 4x",
      "targetId": "material-inspector",
      "keyboard": [
        "Tab",
        "Enter",
        "Space",
        "ArrowLeft",
        "ArrowRight"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "aria-pressed on discrete zoom buttons"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c13.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "inspector": {
      "zoomSteps": [
        1,
        4
      ],
      "initialZoom": 1,
      "initialLightPreset": "neutral",
      "availableLightPresets": [
        "neutral",
        "warm",
        "grazing"
      ],
      "panEnabled": false,
      "rotationMaxDeg": 15,
      "resetControl": true,
      "minimumTouchControlPx": 48,
      "cssPxPerMmAtOneX": 4
    },
    "assetIds": [
      "A18"
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
    "A18"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C13"
}
```

<a id="p-c14"></a>

## P-C14 Repair interest form

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C14",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C14",
    "name": "Repair interest form",
    "status": "planned-consumer",
    "materialIds": [
      "M03",
      "M04"
    ],
    "kind": "form",
    "layout": {
      "widthDesktopPx": 480,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 400,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "form with native labeled inputs",
      "type": "button",
      "label": "Preview your interest",
      "action": "validate locally and show preview confirmation",
      "targetId": "interest-form",
      "keyboard": [
        "Tab",
        "Shift+Tab",
        "Enter"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Preview complete. Your details have not been sent.",
      "errorCopy": "Check the highlighted fields.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c14.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "form": {
      "mode": "preview",
      "networkRequestsAllowed": false,
      "storage": "memory only",
      "fields": [
        {
          "name": "firstName",
          "type": "text",
          "label": "First name",
          "required": true,
          "minLength": 1,
          "maxLength": 60,
          "autocomplete": "given-name"
        },
        {
          "name": "email",
          "type": "email",
          "label": "Email",
          "required": true,
          "minLength": 3,
          "maxLength": 254,
          "autocomplete": "email"
        },
        {
          "name": "interest",
          "type": "select",
          "label": "What would you like to explore?",
          "required": true,
          "options": [
            "Repair",
            "Restyle",
            "Learn a skill"
          ],
          "initialValue": "Repair"
        }
      ],
      "submitLabel": "Preview sign-up",
      "successText": "Preview complete. Your details have not been sent.",
      "errorText": "Check the highlighted fields.",
      "remoteIntegrationStatus": "not implemented; requires a separate reviewed endpoint contract"
    },
    "assetIds": [
      "A13"
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
    "A13"
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
    "S06",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C14"
}
```

<a id="p-c15"></a>

## P-C15 Readable input label and error

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C15",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C15",
    "name": "Readable input label and error",
    "status": "planned-consumer",
    "materialIds": [
      "M04"
    ],
    "kind": "field",
    "layout": {
      "widthDesktopPx": 320,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 80,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "label + input + associated error text",
      "type": "button",
      "label": "Email",
      "action": "show field purpose, requirement, and local error",
      "targetId": "email",
      "keyboard": [
        "Tab"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c15.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "field": {
      "inputMinHeightPx": 48,
      "borderWidthPx": 2,
      "errorIcon": "exclamation plus text",
      "errorAssociation": "aria-describedby",
      "invalidAttribute": "aria-invalid",
      "placeholderIsLabel": false
    },
    "assetIds": [
      "A13"
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
    "M04",
    "A13"
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
    "S06",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C15"
}
```

<a id="p-c16"></a>

## P-C16 Embroidered felt status badge

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C16",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C16",
    "name": "Embroidered felt status badge",
    "status": "planned-consumer",
    "materialIds": [
      "M28",
      "M20"
    ],
    "kind": "status",
    "layout": {
      "widthDesktopPx": 180,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 48,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "p role=status",
      "type": "button",
      "label": "Preview only",
      "action": "display actual operation status",
      "targetId": "preview-status",
      "keyboard": [],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle"
      ],
      "selection": [
        "not-applicable"
      ],
      "operation": [
        "idle"
      ],
      "disabled": false,
      "initial": {
        "interaction": "idle",
        "selection": "not-applicable",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Checking your preview…",
      "successCopy": "Preview complete. Nothing sent.",
      "errorCopy": "Check the form fields.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "blanket",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c16.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A12"
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
    "M28",
    "M20",
    "A12",
    "M31"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C16"
}
```

<a id="p-c17"></a>

## P-C17 Pinned selection marker

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C17",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C17",
    "name": "Pinned selection marker",
    "status": "planned-consumer",
    "materialIds": [
      "M27",
      "M31"
    ],
    "kind": "selector",
    "layout": {
      "widthDesktopPx": 140,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 48,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "button",
      "type": "button",
      "label": "Select denim",
      "action": "select a swatch; pinned means selected only",
      "targetId": "selected-swatch",
      "keyboard": [
        "Tab",
        "Enter",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "aria-pressed"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "none",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c17.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A10"
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
    "M31",
    "A10"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C17"
}
```

<a id="p-c18"></a>

## P-C18 Material choice chips

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C18",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C18",
    "name": "Material choice chips",
    "status": "planned-consumer",
    "materialIds": [
      "M03",
      "M14",
      "M15",
      "M18",
      "M11"
    ],
    "kind": "selector",
    "layout": {
      "widthDesktopPx": 320,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 56,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "fieldset with legend and native radio inputs",
      "type": "button",
      "label": "Material",
      "action": "choose active inspector material",
      "targetId": "material-inspector",
      "keyboard": [
        "Tab",
        "ArrowLeft",
        "ArrowRight",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "native checked"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c18.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "selection": {
      "options": [
        "M14",
        "M15",
        "M18",
        "M11"
      ],
      "initialValue": "M14"
    },
    "assetIds": [
      "A12"
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
    "M14",
    "M15",
    "M18",
    "M11",
    "A12",
    "M31",
    "M20"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C18"
}
```

<a id="p-c19"></a>

## P-C19 Light preset controls

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C19",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C19",
    "name": "Light preset controls",
    "status": "planned-consumer",
    "materialIds": [
      "M04",
      "M27"
    ],
    "kind": "selector",
    "layout": {
      "widthDesktopPx": 320,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 56,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "fieldset with native radios",
      "type": "button",
      "label": "Inspection light",
      "action": "change inspection light without changing material",
      "targetId": "material-inspector",
      "keyboard": [
        "Tab",
        "ArrowLeft",
        "ArrowRight",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "native checked"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c19.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "selection": {
      "options": [
        "neutral",
        "warm",
        "grazing"
      ],
      "initialValue": "neutral"
    },
    "assetIds": []
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
    "M04",
    "M27"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C19"
}
```

<a id="p-c20"></a>

## P-C20 Motion preference control

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C20",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C20",
    "name": "Motion preference control",
    "status": "planned-consumer",
    "materialIds": [
      "M03",
      "M25"
    ],
    "kind": "toggle",
    "layout": {
      "widthDesktopPx": 240,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 56,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "select with visible label",
      "type": "button",
      "label": "Motion",
      "action": "choose motion mode independently from sound",
      "targetId": "motion-preferences",
      "keyboard": [
        "Tab",
        "ArrowUp",
        "ArrowDown"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "native selected"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 0,
      "hoverLiftPx": 0,
      "maxTiltDeg": 0,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c20.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "selection": {
      "options": [
        "system",
        "reduced"
      ],
      "initialValue": "system"
    },
    "assetIds": [
      "A03",
      "A06"
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
    "M25",
    "A03",
    "A06",
    "M31"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C20"
}
```

<a id="p-c21"></a>

## P-C21 Mobile navigation disclosure

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C21",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C21",
    "name": "Mobile navigation disclosure",
    "status": "planned-consumer",
    "materialIds": [
      "M04",
      "M31"
    ],
    "kind": "action",
    "layout": {
      "widthDesktopPx": 80,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 48,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "button controlling nav",
      "type": "button",
      "label": "Menu",
      "action": "expand section links",
      "targetId": "mobile-nav",
      "keyboard": [
        "Tab",
        "Enter",
        "Space",
        "Escape"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "aria-expanded"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c21.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A12"
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
    "M04",
    "M31",
    "A12",
    "M20"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C21"
}
```

<a id="p-c22"></a>

## P-C22 Close and return control

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C22",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C22",
    "name": "Close and return control",
    "status": "planned-consumer",
    "materialIds": [
      "M27",
      "M04"
    ],
    "kind": "action",
    "layout": {
      "widthDesktopPx": 160,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 48,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "button",
      "type": "button",
      "label": "Close details",
      "action": "close dialog and restore focus",
      "targetId": "repair-dialog",
      "keyboard": [
        "Tab",
        "Enter",
        "Space",
        "Escape"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c22.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A05"
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
    "M04",
    "A05"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C22"
}
```

<a id="p-c23"></a>

## P-C23 Material loading placeholder

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C23",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C23",
    "name": "Material loading placeholder",
    "status": "planned-consumer",
    "materialIds": [
      "M03"
    ],
    "kind": "status",
    "layout": {
      "widthDesktopPx": 320,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 240,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "p role=status",
      "type": "button",
      "label": "Loading material view…",
      "action": "show loading status while retaining controls",
      "targetId": "material-inspector",
      "keyboard": [],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle"
      ],
      "selection": [
        "not-applicable"
      ],
      "operation": [
        "idle"
      ],
      "disabled": false,
      "initial": {
        "interaction": "idle",
        "selection": "not-applicable",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Loading material view…",
      "successCopy": "Action complete.",
      "errorCopy": "Material view unavailable. Details remain available below.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 0,
      "hoverLiftPx": 0,
      "maxTiltDeg": 0,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c23.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": []
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
    "M03"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C23"
}
```

<a id="p-c24"></a>

## P-C24 Source footer label

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C24",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C24",
    "name": "Source footer label",
    "status": "planned-consumer",
    "materialIds": [
      "M04",
      "M31"
    ],
    "kind": "navigation",
    "layout": {
      "widthDesktopPx": 320,
      "widthMobile": "min(100%, desktop width)",
      "minHeightPx": 80,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 2,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "footer with ordinary links",
      "type": "button",
      "label": "Project notes",
      "action": "navigate to actual project and contact links",
      "targetId": "project-notes",
      "keyboard": [
        "Tab",
        "Enter"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "none"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "saddle",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "none",
      "plannedPath": "reference/workshop/c24.js",
      "rendererTier": "T0 semantic; T1 decoration; T2 inspection only",
      "implementedStates": []
    },
    "intent": "Make the next action legible while material construction reinforces its state.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A13"
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
    "M04",
    "M31",
    "A13"
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
    "S06",
    "S15",
    "S16"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C24"
}
```

<a id="p-c25"></a>

## P-C25 Core ThreadButton integration anchor

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-C25",
  "task": "Implement this component against its explicit semantic task and state contract. Keep text and essential controls in the DOM. Material decoration must not change keyboard, tap, focus, or reduced-motion outcomes. Report unsupported states.",
  "specification": {
    "id": "C25",
    "name": "Core ThreadButton integration anchor",
    "status": "existing-core-reference-with-planned-enhancement",
    "materialIds": [
      "M14",
      "M31"
    ],
    "kind": "toggle",
    "layout": {
      "widthDesktopPx": 0,
      "widthMobile": "intrinsic label and padding constrained by container; zero widthDesktopPx denotes auto",
      "minHeightPx": 48,
      "paddingPx": [
        16,
        20
      ],
      "gapPx": 12,
      "radiusPx": 12,
      "labelMaxLines": 0,
      "textBackdrop": "opaque label",
      "zOrder": 10
    },
    "semantics": {
      "element": "button",
      "type": "button",
      "label": "Stitch commitment",
      "action": "toggle local commitment state reversibly",
      "targetId": "button-status",
      "keyboard": [
        "Tab",
        "Enter",
        "Space"
      ],
      "tapAlternative": "same labeled control",
      "focusRestoration": "return to invoker after dismissal",
      "liveRegion": "polite status only",
      "selectionAttribute": "aria-pressed; stable accessible name"
    },
    "states": {
      "interaction": [
        "idle",
        "hover",
        "focus-visible",
        "pressed"
      ],
      "selection": [
        "unselected",
        "selected"
      ],
      "operation": [
        "idle",
        "loading",
        "success",
        "error"
      ],
      "disabled": true,
      "initial": {
        "interaction": "idle",
        "selection": "unselected",
        "operation": "idle",
        "disabled": false
      },
      "visualStateRule": "disabled overrides interaction; operation and selection remain separately represented",
      "loadingCopy": "Working…",
      "successCopy": "Action complete.",
      "errorCopy": "Action could not complete. Try again.",
      "disabledRule": "native disabled for unavailable actions; reason in adjacent text"
    },
    "motion": {
      "pressTravelPx": 1.5,
      "hoverLiftPx": 1,
      "maxTiltDeg": 1.5,
      "settleDurationMs": 180,
      "springMassKg": 0.06,
      "springStiffnessNPerM": 140,
      "springDampingNsPerM": 5.8,
      "dragLimitPx": 24,
      "reducedMotion": "zero displacement; static state and text remain"
    },
    "construction": {
      "borderStitch": "running",
      "stitchPitchMm": 3,
      "stitchVisibleLengthMm": 1.8,
      "threadDiameterMm": 0.32,
      "insetMm": 2.5,
      "threadMaterialId": "M31",
      "edgeLiftMm": 0.7,
      "contactShadowOpacity": 0.18,
      "shadowBlurPx": 8,
      "shadowOffsetPx": [
        0,
        3
      ]
    },
    "runtimeBinding": {
      "existingPath": "initiatives/textile-interface/reference/thread-button/index.html",
      "plannedPath": "same existing reference; enhanced material rendering deferred",
      "rendererTier": "Core DOM/CSS",
      "implementedStates": [
        "loose",
        "committed",
        "hover",
        "pressed",
        "focus-visible",
        "reduced-motion",
        "forced-colors"
      ],
      "coreLayoutRule": "Actual CSS uses 3rem min-height, 0.75rem block and 1.1rem inline padding, intrinsic width and no line clamp. Planned material geometry fields do not describe current Core rendering.",
      "coreMotionRule": "Use coreTokenValues and coreForceMapping; no spring solver is wired to Core."
    },
    "intent": "Preserve and improve the existing repository component. It is a Core reference, not evidence of fiber realism.",
    "acceptance": [
      "Label and purpose remain clear with decoration removed.",
      "Keyboard and tap complete the same action.",
      "State is not communicated by material or color alone.",
      "No layout shift from moving decoration."
    ],
    "sourceIds": [
      "S00",
      "S10",
      "S11",
      "S12",
      "S13"
    ],
    "assetIds": [
      "A01"
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
    "A01"
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
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-C25"
}
```
