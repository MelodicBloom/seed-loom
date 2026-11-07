# Methods prompt contracts

<a id="p-f01"></a>

## P-F01 Millimeters to runtime meters

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-F01",
  "task": "Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.",
  "specification": {
    "id": "F01",
    "name": "Millimeters to runtime meters",
    "signature": "mmToM(mm: number): number",
    "formula": "m = mm * 0.001",
    "selectedExample": {
      "inputMm": 0.32,
      "outputM": 0.00032
    },
    "code": "const mmToM = mm => mm * 0.001;",
    "scope": "Exact unit conversion; not a physical measurement.",
    "sourceIds": [
      "S05"
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
    "S05"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-F01"
}
```

<a id="p-f02"></a>

## P-F02 Yarn crossing clearance

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-F02",
  "task": "Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.",
  "specification": {
    "id": "F02",
    "name": "Yarn crossing clearance",
    "signature": "crossingHeights(warpDiameterMm, weftDiameterMm, flatteningZ, gapMm, warpOver)",
    "formula": "rW = warpDiameterMm * flatteningZ / 2; rF = weftDiameterMm * flatteningZ / 2; zW = sign * (rW + gapMm/2); zF = -sign * (rF + gapMm/2)",
    "selectedExample": {
      "warpDiameterMm": 0.42,
      "weftDiameterMm": 0.357,
      "flatteningZ": 0.65,
      "gapMm": 0.02,
      "warpOver": true,
      "warpCenterZMm": 0.1465,
      "weftCenterZMm": -0.126025
    },
    "code": "const sign = warpOver ? 1 : -1; const zWarp = sign * (warpDiameterMm * flatteningZ / 2 + gapMm / 2); const zWeft = -sign * (weftDiameterMm * flatteningZ / 2 + gapMm / 2);",
    "scope": "Illustrative crossing samples only. Requires continuous curve/contact checks before use as yarn geometry.",
    "sourceIds": [
      "S01",
      "S05"
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
    "S01",
    "S05"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-F02"
}
```

<a id="p-f03"></a>

## P-F03 Weave pattern selection

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-F03",
  "task": "Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.",
  "specification": {
    "id": "F03",
    "name": "Weave pattern selection",
    "signature": "warpOver(i: integer, j: integer, pattern: string): boolean",
    "formula": "plain: (i+j) mod 2 = 0; twill-3x1: (i-j) mod 4 < 3; satin-5: (i-2*j) mod 5 != 0",
    "selectedExample": {
      "pattern": "twill-3x1",
      "periodCells": 4,
      "warpDominanceRatio": 0.75
    },
    "code": "const mod = (x,n) => ((x%n)+n)%n; const over = pattern === \"plain\" ? mod(i+j,2)===0 : pattern === \"twill-3x1\" ? mod(i-j,4)<3 : mod(i-2*j,5)!==0;",
    "scope": "Authored binary crossing pattern. Knit loops, lace, felt, and pile do not use this woven topology.",
    "sourceIds": [
      "S01"
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
    "S01"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-F03"
}
```

<a id="p-f04"></a>

## P-F04 Twisted ply centerline

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-F04",
  "task": "Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.",
  "specification": {
    "id": "F04",
    "name": "Twisted ply centerline",
    "signature": "plyOffset(sMm, plyIndex, plyCount, radiusMm, turnsPerMm)",
    "formula": "theta = 2*pi*(turnsPerMm*sMm + plyIndex/plyCount); offset = radiusMm * (cos(theta)*N + sin(theta)*B)",
    "selectedExample": {
      "plyCount": 3,
      "radiusMm": 0.07,
      "turnsPerMm": 1.5,
      "threadDiameterMm": 0.32
    },
    "code": "const theta = 2*Math.PI*(turnsPerMm*sMm + plyIndex/plyCount); const offsetN = radiusMm*Math.cos(theta); const offsetB = radiusMm*Math.sin(theta);",
    "scope": "Sweep in a parallel-transport frame, not a fixed global frame. Check radius and strand overlap.",
    "sourceIds": [
      "S01",
      "S02"
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
    "S01",
    "S02"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-F04"
}
```

<a id="p-f05"></a>

## P-F05 Damped spring response

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-F05",
  "task": "Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.",
  "specification": {
    "id": "F05",
    "name": "Damped spring response",
    "signature": "stepSpring(positionM, velocityMps, targetM, massKg, stiffnessNPerM, dampingNsPerM, dtS)",
    "formula": "m*xSecondDerivative + c*xFirstDerivative + k*(x-target) = 0; dampingRatio = c/(2*sqrt(k*m))",
    "selectedExample": {
      "massKg": 0.06,
      "stiffnessNPerM": 140,
      "dampingNsPerM": 5.8,
      "fixedDtSeconds": 0.008333333333333333,
      "maxAccumulatedSeconds": 0.05,
      "maxSubsteps": 6
    },
    "code": "const acceleration = (-k*(x-target)-c*v)/m; v += acceleration*dt; x += v*dt;",
    "scope": "Semi-implicit Euler illustration with fixed substeps and bounds. These controller values are not measured denim mechanics.",
    "sourceIds": [
      "S09"
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
    "S09"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-F05"
}
```

<a id="p-f06"></a>

## P-F06 XPBD distance constraint

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-F06",
  "task": "Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.",
  "specification": {
    "id": "F06",
    "name": "XPBD distance constraint",
    "signature": "solveDistance(x0, x1, inverseMass0, inverseMass1, restLengthM, complianceMPerN, lambda, dtS)",
    "formula": "C=length(x1-x0)-L; alphaTilde=alpha/(dt*dt); deltaLambda=(-C-alphaTilde*lambda)/(w0+w1+alphaTilde); lambda+=deltaLambda; deltaXi=wi*gradientCi*deltaLambda",
    "selectedExample": {
      "gridSize": [
        24,
        18
      ],
      "fixedDtSeconds": 0.008333333333333333,
      "solverIterations": 8,
      "stretchComplianceMPerN": 2e-07,
      "shearComplianceMPerN": 1e-06,
      "distanceBendComplianceMPerN": 8e-05,
      "gravityMps2": [
        0,
        -9.81,
        0
      ],
      "particleMassKg": 0.0002,
      "velocityRetentionPerSecond": 0.7,
      "selfCollision": false,
      "maxLiftMm": 12,
      "maxStretchRatio": 1.04
    },
    "code": "const a = compliance/(dt*dt); const dl = (-constraint-a*lambda)/(w0+w1+a); lambda += dl;",
    "scope": "Distance-based bend surrogate, not calibrated angular cloth bending. Reset multipliers each substep; retain across solver iterations. No self-collision claim.",
    "sourceIds": [
      "S09"
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
    "S09"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-F06"
}
```

<a id="p-f07"></a>

## P-F07 Level of detail from projected yarn size

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-F07",
  "task": "Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.",
  "specification": {
    "id": "F07",
    "name": "Level of detail from projected yarn size",
    "signature": "chooseLod(projectedYarnDiameterPx, inspectionRequested)",
    "formula": "if !inspectionRequested or diameterPx<0.8 -> mapped surface; if 0.8<=diameterPx<2 -> modeled yarn; else modeled yarn plus bounded fiber detail",
    "selectedExample": {
      "mappedThresholdPx": 0.8,
      "fiberThresholdPx": 2,
      "transitionHysteresisRatio": 0.15,
      "fiberSegmentsMax": 24000,
      "activeInspectorCount": 1
    },
    "code": "const lod = !inspect || yarnPx < .8 ? \"mapped\" : yarnPx < 2 ? \"yarn\" : \"fiber\";",
    "scope": "Design-selected perceptual thresholds; validate for shimmer and popping. No universal perceptual equivalence claim.",
    "sourceIds": [
      "S01",
      "S04"
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
    "S01",
    "S04"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-F07"
}
```

<a id="p-f08"></a>

## P-F08 Linear color and contrast

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-F08",
  "task": "Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.",
  "specification": {
    "id": "F08",
    "name": "Linear color and contrast",
    "signature": "srgbToLinear(c01); contrastRatio(rgbA, rgbB)",
    "formula": "linear(c)=c/12.92 if c<=0.04045 else ((c+0.055)/1.055)^2.4; Y=.2126R+.7152G+.0722B; ratio=(max(Y1,Y2)+.05)/(min(Y1,Y2)+.05)",
    "selectedExample": {
      "foregroundHex": "#242821",
      "backgroundHex": "#FFFDF7",
      "normalTextMinimum": 4.5
    },
    "code": "const linear = c => c <= .04045 ? c/12.92 : ((c+.055)/1.055)**2.4;",
    "scope": "Use actual rendered foreground/background samples for textured states; a palette calculation alone is insufficient.",
    "sourceIds": [
      "S06",
      "S12"
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
    "S06",
    "S12"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-F08"
}
```

<a id="p-f09"></a>

## P-F09 Height-derived tangent normal

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-F09",
  "task": "Translate this formula into a bounded function with explicit inputs, units, failure conditions and tests. Preserve the stated approximation limits. A method snippet is not evidence that the whole feature works.",
  "specification": {
    "id": "F09",
    "name": "Height-derived tangent normal",
    "signature": "heightNormal(heightField, samplePitchMm, displacementScaleMm)",
    "formula": "dHdu=(H(u+e,v)-H(u-e,v))*scale/(2*e); dHdv=(H(u,v+e)-H(u,v-e))*scale/(2*e); N=normalize(-dHdu,-dHdv,1)",
    "selectedExample": {
      "samplePitchMm": 0.04,
      "normalConvention": "OpenGL +Y",
      "displacementScaleMm": 0.076
    },
    "code": "vec3 normalTS = normalize(vec3(-dHdu, -dHdv, 1.0));",
    "scope": "Shading detail only. Derivatives must use compatible physical units and correct image orientation.",
    "sourceIds": [
      "S05",
      "S06"
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
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-F09"
}
```
