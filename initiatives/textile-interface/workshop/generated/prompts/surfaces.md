# Surfaces prompt contracts

<a id="p-m01"></a>

## P-M01 Heavy natural canvas

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M01",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M01",
    "name": "Heavy natural canvas",
    "status": "specified-not-rendered",
    "seed": 314159,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.52,
      "yarnDiameterWeftMm": 0.442,
      "warpSpacingMm": 0.67,
      "weftSpacingMm": 0.67,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 1.15,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.5,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 2,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#B7A88B",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#B7A88B",
      "roughness": 0.88,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.28,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.12,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.092,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.16,
        32.16
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M01_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M01_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M01_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M01_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M01_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M01_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M01_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M01_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M01"
}
```

<a id="p-m02"></a>

## P-M02 Coarse burlap

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M02",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M02",
    "name": "Coarse burlap",
    "status": "specified-not-rendered",
    "seed": 314260,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.95,
      "yarnDiameterWeftMm": 0.8075,
      "warpSpacingMm": 1.55,
      "weftSpacingMm": 1.55,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 1.6,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 1.1,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 3.0,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0.16,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#9D835A",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#9D835A",
      "roughness": 0.94,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.22,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.12,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.55,
        32.55
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M02_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M02_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M02_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M02_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M02_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M02_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M02_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M02_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M02"
}
```

<a id="p-m03"></a>

## P-M03 Washed linen

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M03",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M03",
    "name": "Washed linen",
    "status": "specified-not-rendered",
    "seed": 314361,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.35,
      "yarnDiameterWeftMm": 0.2975,
      "warpSpacingMm": 0.5,
      "weftSpacingMm": 0.5,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.17,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.65,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.3,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 1.3,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#D8CFBB",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#D8CFBB",
      "roughness": 0.86,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.32,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.18,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.052000000000000005,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.0,
        32.0
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M03_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M03_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M03_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M03_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M03_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M03_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M03_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M03_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M03"
}
```

<a id="p-m04"></a>

## P-M04 Cream satin label

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M04",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M04",
    "name": "Cream satin label",
    "status": "specified-not-rendered",
    "seed": 314462,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "satin-5",
      "yarnDiameterWarpMm": 0.16,
      "yarnDiameterWeftMm": 0.136,
      "warpSpacingMm": 0.21,
      "weftSpacingMm": 0.21,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.35,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.3,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.3,
      "fuzzCoverageRatio": 0.008,
      "frayLengthMm": 0.6,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#E8DCC3",
      "secondaryColorHex": "#FFF4DA",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#E8DCC3",
      "roughness": 0.32,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.45,
      "sheenColorHex": "#FFF4DA",
      "sheenRoughness": 0.6,
      "anisotropy": 0.78,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.024,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        31.5,
        31.5
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M04_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M04_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M04_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M04_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M04_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M04_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M04_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M04_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M04"
}
```

<a id="p-m05"></a>

## P-M05 Sheer silk

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M05",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M05",
    "name": "Sheer silk",
    "status": "specified-not-rendered",
    "seed": 314563,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.09,
      "yarnDiameterWeftMm": 0.0765,
      "warpSpacingMm": 0.17,
      "weftSpacingMm": 0.17,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.16,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.04,
      "fuzzCoverageRatio": 0.005,
      "frayLengthMm": 0.32,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0.22,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#E5D6BE",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#E5D6BE",
      "roughness": 0.4,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.36,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.65,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.0128,
      "displacementBiasMm": 0.0,
      "alphaMode": "MASK",
      "alphaCutoff": 0.4,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        31.96,
        31.96
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M05_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M05_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M05_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M05_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M05_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M05_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M05_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M05_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06",
      "S07",
      "S08"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06",
    "S07",
    "S08"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M05"
}
```

<a id="p-m06"></a>

## P-M06 Moss corduroy

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M06",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M06",
    "name": "Moss corduroy",
    "status": "specified-not-rendered",
    "seed": 314664,
    "role": "secondary material option",
    "topology": "ribbed-woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.32,
      "yarnDiameterWeftMm": 0.272,
      "warpSpacingMm": 0.42,
      "weftSpacingMm": 0.42,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 1.8,
      "pileHeightMm": 0.55,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.2,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 2,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 2.8,
      "ribHeightMm": 0.65,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#65705A",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#65705A",
      "roughness": 0.9,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.7,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.25,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        30.8,
        30.8
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M06_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M06_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M06_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M06_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M06_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M06_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M06_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M06_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M06"
}
```

<a id="p-m07"></a>

## P-M07 Ribbed knit

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M07",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M07",
    "name": "Ribbed knit",
    "status": "specified-not-rendered",
    "seed": 314765,
    "role": "secondary material option",
    "topology": "knitted",
    "construction": {
      "pattern": "rib-2x2",
      "yarnDiameterWarpMm": 0.9,
      "yarnDiameterWeftMm": 0.765,
      "warpSpacingMm": 1.25,
      "weftSpacingMm": 1.25,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 2.4,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.65,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 2,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 4.4,
      "ribHeightMm": 0.7,
      "knitLoopWidthMm": 2.2,
      "knitLoopHeightMm": 3.1,
      "knitLoopDepthMm": 0.8,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#92816F",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#92816F",
      "roughness": 0.93,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.5,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.15,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        30.8,
        30.8
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M07_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M07_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M07_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M07_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M07_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M07_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M07_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M07_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M07"
}
```

<a id="p-m08"></a>

## P-M08 Openwork lace

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M08",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M08",
    "name": "Openwork lace",
    "status": "specified-not-rendered",
    "seed": 314866,
    "role": "secondary material option",
    "topology": "openwork",
    "construction": {
      "pattern": "hexagonal floral openwork; 8mm motif repeat",
      "yarnDiameterWarpMm": 0.18,
      "yarnDiameterWeftMm": 0.153,
      "warpSpacingMm": 0.4,
      "weftSpacingMm": 0.4,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.35,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.08,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 0.7,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0.64,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#EDE3CD",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#EDE3CD",
      "roughness": 0.83,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.35,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.2,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.027999999999999997,
      "displacementBiasMm": 0.0,
      "alphaMode": "MASK",
      "alphaCutoff": 0.45,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M08_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M08_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M08_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M08_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M08_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M08_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M08_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M08_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06",
      "S07",
      "S08"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06",
    "S07",
    "S08"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M08"
}
```

<a id="p-m09"></a>

## P-M09 Chiffon

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M09",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M09",
    "name": "Chiffon",
    "status": "specified-not-rendered",
    "seed": 314967,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.075,
      "yarnDiameterWeftMm": 0.0638,
      "warpSpacingMm": 0.13,
      "weftSpacingMm": 0.13,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 2.2,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.12,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.025,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 0.24,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0.3,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#C9C0AD",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#C9C0AD",
      "roughness": 0.72,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.28,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.35,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.0096,
      "displacementBiasMm": 0.0,
      "alphaMode": "MASK",
      "alphaCutoff": 0.4,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        31.98,
        31.98
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M09_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M09_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M09_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M09_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M09_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M09_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M09_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M09_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06",
      "S07",
      "S08"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06",
    "S07",
    "S08"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M09"
}
```

<a id="p-m10"></a>

## P-M10 Sheer linen curtain

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M10",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M10",
    "name": "Sheer linen curtain",
    "status": "specified-not-rendered",
    "seed": 315068,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.24,
      "yarnDiameterWeftMm": 0.204,
      "warpSpacingMm": 0.44,
      "weftSpacingMm": 0.44,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.4,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.25,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 0.8,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0.38,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#DDD3BB",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#DDD3BB",
      "roughness": 0.86,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.3,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.18,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.032,
      "displacementBiasMm": 0.0,
      "alphaMode": "MASK",
      "alphaCutoff": 0.45,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.12,
        32.12
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M10_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M10_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M10_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M10_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M10_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M10_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M10_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M10_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06",
      "S07",
      "S08"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06",
    "S07",
    "S08"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M10"
}
```

<a id="p-m11"></a>

## P-M11 Wine velvet

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M11",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M11",
    "name": "Wine velvet",
    "status": "specified-not-rendered",
    "seed": 315169,
    "role": "Creative Studio primary",
    "topology": "pile",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.16,
      "yarnDiameterWeftMm": 0.136,
      "warpSpacingMm": 0.22,
      "weftSpacingMm": 0.22,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 1.7,
      "pileHeightMm": 1.1,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.18,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 2,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#2C1825",
      "secondaryColorHex": "#A95779",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#2C1825",
      "roughness": 0.85,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.92,
      "sheenColorHex": "#A95779",
      "sheenRoughness": 0.38,
      "anisotropy": 0.3,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        31.9,
        31.9
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M11_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M11_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M11_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M11_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M11_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M11_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M11_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M11_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M11"
}
```

<a id="p-m12"></a>

## P-M12 Mohair inspired pile

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M12",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M12",
    "name": "Mohair inspired pile",
    "status": "specified-not-rendered",
    "seed": 315270,
    "role": "secondary material option",
    "topology": "pile",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.8,
      "yarnDiameterWeftMm": 0.68,
      "warpSpacingMm": 1.1,
      "weftSpacingMm": 1.1,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 26,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 3.2,
      "pileHeightMm": 2.0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 3.5,
      "fuzzCoverageRatio": 0.16,
      "frayLengthMm": 2,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#8A8872",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#8A8872",
      "roughness": 0.92,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.68,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.2,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        31.9,
        31.9
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M12_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M12_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M12_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M12_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M12_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M12_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M12_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M12_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M12"
}
```

<a id="p-m13"></a>

## P-M13 Alpaca inspired pile

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M13",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M13",
    "name": "Alpaca inspired pile",
    "status": "specified-not-rendered",
    "seed": 315371,
    "role": "secondary material option",
    "topology": "pile",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.65,
      "yarnDiameterWeftMm": 0.5525,
      "warpSpacingMm": 0.95,
      "weftSpacingMm": 0.95,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 22,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 2.7,
      "pileHeightMm": 1.5,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 2.5,
      "fuzzCoverageRatio": 0.12,
      "frayLengthMm": 2,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#AEA08C",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#AEA08C",
      "roughness": 0.94,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.62,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.15,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.3,
        32.3
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M13_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M13_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M13_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M13_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M13_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M13_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M13_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M13_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M13"
}
```

<a id="p-m14"></a>

## P-M14 Indigo repair denim

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M14",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M14",
    "name": "Indigo repair denim",
    "status": "specified-not-rendered",
    "seed": 315472,
    "role": "Repair Commons primary",
    "topology": "woven",
    "construction": {
      "pattern": "twill-3x1",
      "yarnDiameterWarpMm": 0.42,
      "yarnDiameterWeftMm": 0.357,
      "warpSpacingMm": 0.54,
      "weftSpacingMm": 0.54,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.95,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.45,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 2.2,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#253B54",
      "secondaryColorHex": "#C4B79D",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#253B54",
      "roughness": 0.9,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.24,
      "sheenColorHex": "#C4B79D",
      "sheenRoughness": 0.6,
      "anisotropy": 0.22,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.076,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.4,
        32.4
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M14_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M14_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M14_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M14_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M14_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M14_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M14_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M14_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M14"
}
```

<a id="p-m15"></a>

## P-M15 Teal ripstop nylon

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M15",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M15",
    "name": "Teal ripstop nylon",
    "status": "specified-not-rendered",
    "seed": 315573,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "plain plus 4mm reinforcing grid",
      "yarnDiameterWarpMm": 0.15,
      "yarnDiameterWeftMm": 0.1275,
      "warpSpacingMm": 0.22,
      "weftSpacingMm": 0.22,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.25,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.025,
      "fuzzCoverageRatio": 0.004,
      "frayLengthMm": 0.5,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#1D5B54",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#1D5B54",
      "roughness": 0.51,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.28,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.55,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.02,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M15_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M15_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M15_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M15_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M15_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M15_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M15_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M15_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M15"
}
```

<a id="p-m16"></a>

## P-M16 Reused canvas appearance

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M16",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M16",
    "name": "Reused canvas appearance",
    "status": "specified-not-rendered",
    "seed": 315674,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.5,
      "yarnDiameterWeftMm": 0.425,
      "warpSpacingMm": 0.68,
      "weftSpacingMm": 0.68,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 1.1,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.7,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 2,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#8F947B",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#8F947B",
      "roughness": 0.91,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.25,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.15,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.08800000000000001,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        31.96,
        31.96
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M16_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M16_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M16_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M16_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M16_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M16_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M16_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M16_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Suggest patched and reused cloth through appearance; no verified recycled-content claim.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M16"
}
```

<a id="p-m17"></a>

## P-M17 Technical mesh

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M17",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M17",
    "name": "Technical mesh",
    "status": "specified-not-rendered",
    "seed": 315775,
    "role": "Textile Network secondary",
    "topology": "openwork",
    "construction": {
      "pattern": "hexagonal mesh 1.4mm repeat",
      "yarnDiameterWarpMm": 0.22,
      "yarnDiameterWeftMm": 0.187,
      "warpSpacingMm": 0.7,
      "weftSpacingMm": 0.7,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.5,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.03,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 1.0,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0.55,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#536D63",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#536D63",
      "roughness": 0.62,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.25,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.4,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.04,
      "displacementBiasMm": 0.0,
      "alphaMode": "MASK",
      "alphaCutoff": 0.45,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.2,
        32.2
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M17_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M17_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M17_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M17_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M17_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M17_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M17_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M17_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06",
      "S07",
      "S08"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06",
    "S07",
    "S08"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M17"
}
```

<a id="p-m18"></a>

## P-M18 Banana fiber inspired cloth

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M18",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M18",
    "name": "Banana fiber inspired cloth",
    "status": "specified-not-rendered",
    "seed": 315876,
    "role": "Futures Lab primary",
    "topology": "woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.28,
      "yarnDiameterWeftMm": 0.238,
      "warpSpacingMm": 0.46,
      "weftSpacingMm": 0.46,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.22,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.55,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.5,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 1.1,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#C7B892",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#C7B892",
      "roughness": 0.86,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.3,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.28,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.044000000000000004,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.2,
        32.2
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M18_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M18_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M18_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M18_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M18_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M18_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M18_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M18_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "A coarse natural-fiber appearance only; fiber identity and environmental benefits are unverified.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M18"
}
```

<a id="p-m19"></a>

## P-M19 Quilted patchwork

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M19",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M19",
    "name": "Quilted patchwork",
    "status": "specified-not-rendered",
    "seed": 315977,
    "role": "secondary material option",
    "topology": "quilted",
    "construction": {
      "pattern": "plain patch panels with diagonal quilt lines",
      "yarnDiameterWarpMm": 0.3,
      "yarnDiameterWeftMm": 0.255,
      "warpSpacingMm": 0.42,
      "weftSpacingMm": 0.42,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 4.0,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.3,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 2,
      "edgeType": "cut with bounded fray",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 18,
      "quiltLoftMm": 3,
      "grainDirectionRad": 0,
      "primaryColorHex": "#987B76",
      "secondaryColorHex": "#61736A",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#987B76",
      "roughness": 0.9,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.4,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.16,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        36,
        36
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M19_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M19_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M19_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M19_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M19_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M19_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M19_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M19_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M19"
}
```

<a id="p-m20"></a>

## P-M20 Metallic embroidery thread

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M20",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M20",
    "name": "Metallic embroidery thread",
    "status": "specified-not-rendered",
    "seed": 316078,
    "role": "secondary material option",
    "topology": "thread",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.28,
      "yarnDiameterWeftMm": 0.238,
      "warpSpacingMm": 0.4,
      "weftSpacingMm": 0.4,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 3,
      "plyTwistTurnsPerMm": 1.2,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.3,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.02,
      "fuzzCoverageRatio": 0.003,
      "frayLengthMm": 0.6,
      "edgeType": "cut ends",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#B99A59",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#B99A59",
      "roughness": 0.36,
      "metalness": 0.9,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.7,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.024,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.0,
        32.0
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M20_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M20_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M20_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M20_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M20_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M20_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M20_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M20_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M20"
}
```

<a id="p-m21"></a>

## P-M21 Leather label

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M21",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M21",
    "name": "Leather label",
    "status": "specified-not-rendered",
    "seed": 316179,
    "role": "secondary material option",
    "topology": "solid",
    "construction": {
      "pattern": "fine irregular leather grain",
      "yarnDiameterWarpMm": 0,
      "yarnDiameterWeftMm": 0.0,
      "warpSpacingMm": 0,
      "weftSpacingMm": 0,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 1.2,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0,
      "fuzzCoverageRatio": 0,
      "frayLengthMm": 0,
      "edgeType": "rounded cut edge",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#704A32",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.08
    },
    "pbr": {
      "baseColorHex": "#704A32",
      "roughness": 0.68,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.08,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.096,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M21_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M21_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M21_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M21_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M21_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M21_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M21_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M21_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M21"
}
```

<a id="p-m22"></a>

## P-M22 Weathered teak bench

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M22",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M22",
    "name": "Weathered teak bench",
    "status": "specified-not-rendered",
    "seed": 316280,
    "role": "secondary material option",
    "topology": "solid",
    "construction": {
      "pattern": "longitudinal wood grain",
      "yarnDiameterWarpMm": 0,
      "yarnDiameterWeftMm": 0.0,
      "warpSpacingMm": 0,
      "weftSpacingMm": 0,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 24,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0,
      "fuzzCoverageRatio": 0,
      "frayLengthMm": 0,
      "edgeType": "3mm bevel",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#805D3E",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#805D3E",
      "roughness": 0.72,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.32,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.08,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M22_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M22_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M22_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M22_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M22_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M22_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M22_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M22_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M22"
}
```

<a id="p-m23"></a>

## P-M23 Tailor cutting mat

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M23",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M23",
    "name": "Tailor cutting mat",
    "status": "specified-not-rendered",
    "seed": 316381,
    "role": "secondary material option",
    "topology": "solid",
    "construction": {
      "pattern": "subtle polymer stipple; grid is separate vector decal",
      "yarnDiameterWarpMm": 0,
      "yarnDiameterWeftMm": 0.0,
      "warpSpacingMm": 0,
      "weftSpacingMm": 0,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 3,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0,
      "fuzzCoverageRatio": 0,
      "frayLengthMm": 0,
      "edgeType": "1mm bevel",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#31594F",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#31594F",
      "roughness": 0.82,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M23_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M23_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M23_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M23_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M23_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M23_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M23_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M23_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M23"
}
```

<a id="p-m24"></a>

## P-M24 Four hole maple button

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M24",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M24",
    "name": "Four hole maple button",
    "status": "specified-not-rendered",
    "seed": 316482,
    "role": "secondary material option",
    "topology": "solid",
    "construction": {
      "pattern": "subtle wood grain",
      "yarnDiameterWarpMm": 0,
      "yarnDiameterWeftMm": 0.0,
      "warpSpacingMm": 0,
      "weftSpacingMm": 0,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 2.6,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0,
      "fuzzCoverageRatio": 0,
      "frayLengthMm": 0,
      "edgeType": ".7mm rounded rim",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#A77B4C",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#A77B4C",
      "roughness": 0.62,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.12,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M24_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M24_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M24_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M24_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M24_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M24_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M24_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M24_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M24"
}
```

<a id="p-m25"></a>

## P-M25 Horn inspired button

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M25",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M25",
    "name": "Horn inspired button",
    "status": "specified-not-rendered",
    "seed": 316583,
    "role": "secondary material option",
    "topology": "solid",
    "construction": {
      "pattern": "irregular warm brown striation; no animal-source claim",
      "yarnDiameterWarpMm": 0,
      "yarnDiameterWeftMm": 0.0,
      "warpSpacingMm": 0,
      "weftSpacingMm": 0,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 2.4,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0,
      "fuzzCoverageRatio": 0,
      "frayLengthMm": 0,
      "edgeType": ".6mm rounded rim",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#42382D",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#42382D",
      "roughness": 0.38,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.18,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.12,
      "clearcoatRoughness": 0.35,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M25_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M25_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M25_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M25_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M25_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M25_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M25_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M25_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M25"
}
```

<a id="p-m26"></a>

## P-M26 Mother of pearl inspired button

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M26",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M26",
    "name": "Mother of pearl inspired button",
    "status": "specified-not-rendered",
    "seed": 316684,
    "role": "secondary material option",
    "topology": "solid",
    "construction": {
      "pattern": "soft irregular pearlescent lamellae; illustrative",
      "yarnDiameterWarpMm": 0,
      "yarnDiameterWeftMm": 0.0,
      "warpSpacingMm": 0,
      "weftSpacingMm": 0,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 2.1,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0,
      "fuzzCoverageRatio": 0,
      "frayLengthMm": 0,
      "edgeType": ".5mm rounded rim",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#D8D8CD",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#D8D8CD",
      "roughness": 0.26,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.12,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.45,
      "iridescenceIOR": 1.35,
      "iridescenceThicknessMinNm": 220,
      "iridescenceThicknessMaxNm": 460,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M26_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M26_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M26_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M26_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M26_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M26_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M26_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M26_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Use a restrained thin-film appearance approximation; this is not a calibrated nacre multilayer model.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06",
      "S02"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06",
    "S02"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M26"
}
```

<a id="p-m27"></a>

## P-M27 Brushed brass fastener

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M27",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M27",
    "name": "Brushed brass fastener",
    "status": "specified-not-rendered",
    "seed": 316785,
    "role": "secondary material option",
    "topology": "solid",
    "construction": {
      "pattern": "directional brushed metal",
      "yarnDiameterWarpMm": 0,
      "yarnDiameterWeftMm": 0.0,
      "warpSpacingMm": 0,
      "weftSpacingMm": 0,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 1.6,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0,
      "fuzzCoverageRatio": 0,
      "frayLengthMm": 0,
      "edgeType": ".3mm bevel",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#B99A59",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#B99A59",
      "roughness": 0.42,
      "metalness": 1.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.65,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M27_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M27_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M27_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M27_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M27_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M27_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M27_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M27_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M27"
}
```

<a id="p-m28"></a>

## P-M28 Embroidered wool felt badge

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M28",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M28",
    "name": "Embroidered wool felt badge",
    "status": "specified-not-rendered",
    "seed": 316886,
    "role": "secondary material option",
    "topology": "felt",
    "construction": {
      "pattern": "nonwoven entangled fibers",
      "yarnDiameterWarpMm": 0,
      "yarnDiameterWeftMm": 0.0,
      "warpSpacingMm": 0,
      "weftSpacingMm": 0,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 2.2,
      "pileHeightMm": 0.4,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.6,
      "fuzzCoverageRatio": 0.13,
      "frayLengthMm": 0,
      "edgeType": "soft cut edge",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#D4BB87",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#D4BB87",
      "roughness": 0.97,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.5,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.05,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M28_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M28_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M28_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M28_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M28_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M28_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M28_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M28_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M28"
}
```

<a id="p-m29"></a>

## P-M29 Flexible measuring tape

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M29",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M29",
    "name": "Flexible measuring tape",
    "status": "specified-not-rendered",
    "seed": 316987,
    "role": "secondary material option",
    "topology": "woven-coated",
    "construction": {
      "pattern": "coated plain weave; markings are separate live/vector layer",
      "yarnDiameterWarpMm": 0.16,
      "yarnDiameterWeftMm": 0.136,
      "warpSpacingMm": 0.23,
      "weftSpacingMm": 0.23,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.4,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.03,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 0,
      "edgeType": "bound edge",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#E1CC93",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#E1CC93",
      "roughness": 0.72,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.12,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.1,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.032,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        31.97,
        31.97
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M29_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M29_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M29_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M29_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M29_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M29_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M29_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M29_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M29"
}
```

<a id="p-m30"></a>

## P-M30 Woven cotton ribbon

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M30",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M30",
    "name": "Woven cotton ribbon",
    "status": "specified-not-rendered",
    "seed": 317088,
    "role": "secondary material option",
    "topology": "woven",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.18,
      "yarnDiameterWeftMm": 0.153,
      "warpSpacingMm": 0.25,
      "weftSpacingMm": 0.25,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 2,
      "plyTwistTurnsPerMm": 0.9,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.4,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.15,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 0.2,
      "edgeType": "woven selvedge",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#9B5A48",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#9B5A48",
      "roughness": 0.83,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.35,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.3,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.032,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32.0,
        32.0
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M30_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M30_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M30_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M30_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M30_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M30_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M30_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M30_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M30"
}
```

<a id="p-m31"></a>

## P-M31 Cream sewing cotton

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M31",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M31",
    "name": "Cream sewing cotton",
    "status": "specified-not-rendered",
    "seed": 317189,
    "role": "secondary material option",
    "topology": "thread",
    "construction": {
      "pattern": "plain",
      "yarnDiameterWarpMm": 0.32,
      "yarnDiameterWeftMm": 0.272,
      "warpSpacingMm": 0.45,
      "weftSpacingMm": 0.45,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 3,
      "plyTwistTurnsPerMm": 1.5,
      "fiberDiameterMicrometers": 17,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 0.35,
      "pileHeightMm": 0,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.35,
      "fuzzCoverageRatio": 0.05,
      "frayLengthMm": 0.7,
      "edgeType": "cut ends",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#D9CDB0",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#D9CDB0",
      "roughness": 0.86,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.32,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.15,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.027999999999999997,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        31.95,
        31.95
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M31_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M31_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M31_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M31_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M31_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M31_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M31_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M31_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M31"
}
```

<a id="p-m32"></a>

## P-M32 Cotton batting underside

For a self-contained copy with all dependency values, run the standaloneCommand in this contract. For image-only tools, use appearance fields while retaining the concept-only boundary.

```json
{
  "promptId": "P-M32",
  "task": "Author this exact material and its asset-build recipe. Separate shape, yarn topology, and residual fiber shading. Name all texture exports and their channels. A generated beauty image is only a concept, never an aligned PBR texture set or measured reference.",
  "specification": {
    "id": "M32",
    "name": "Cotton batting underside",
    "status": "specified-not-rendered",
    "seed": 317290,
    "role": "secondary material option",
    "topology": "felt",
    "construction": {
      "pattern": "nonwoven loose fiber web",
      "yarnDiameterWarpMm": 0,
      "yarnDiameterWeftMm": 0.0,
      "warpSpacingMm": 0,
      "weftSpacingMm": 0,
      "flatteningZ": 0.65,
      "crossingGapMm": 0.02,
      "plyCount": 0,
      "plyTwistTurnsPerMm": 0,
      "fiberDiameterMicrometers": 18,
      "yarnDiameterJitterRatio": 0.08,
      "positionJitterRatio": 0.04,
      "thicknessMm": 3.0,
      "pileHeightMm": 0.4,
      "pileDirectionRad": 0.0,
      "pileBendMaxRad": 0.3,
      "fuzzLengthMm": 0.9,
      "fuzzCoverageRatio": 0.17,
      "frayLengthMm": 0,
      "edgeType": "soft compressed edge",
      "ribPitchMm": 0,
      "ribHeightMm": 0,
      "knitLoopWidthMm": 0,
      "knitLoopHeightMm": 0,
      "knitLoopDepthMm": 0,
      "openAreaRatio": 0,
      "quiltCellMm": 0,
      "quiltLoftMm": 0,
      "grainDirectionRad": 0,
      "primaryColorHex": "#E4DBC8",
      "secondaryColorHex": "#D6CDB9",
      "colorVariationRatio": 0.055
    },
    "pbr": {
      "baseColorHex": "#E4DBC8",
      "roughness": 0.98,
      "metalness": 0.0,
      "ior": 1.5,
      "specularIntensity": 1.0,
      "sheen": 0.35,
      "sheenColorHex": "#D6CDB9",
      "sheenRoughness": 0.6,
      "anisotropy": 0.03,
      "anisotropyRotationRad": 0.0,
      "normalScaleXY": [
        0.45,
        0.45
      ],
      "displacementScaleMm": 0.12,
      "displacementBiasMm": 0.0,
      "alphaMode": "OPAQUE",
      "alphaCutoff": 0.5,
      "opacity": 1.0,
      "transmission": 0.0,
      "clearcoat": 0.0,
      "clearcoatRoughness": 0.6,
      "iridescence": 0.0,
      "iridescenceIOR": 1.3,
      "iridescenceThicknessMinNm": 100,
      "iridescenceThicknessMaxNm": 400,
      "doubleSided": true
    },
    "textureContract": {
      "tileSizeMm": [
        32,
        32
      ],
      "masterResolutionPx": 2048,
      "runtimeResolutionT1Px": 1024,
      "runtimeResolutionT2Px": 2048,
      "tileSeamToleranceNormalized": 0.025,
      "uvOrigin": "lower-left",
      "uvRotationRad": 0.0,
      "heightOrigin": "lowest represented shading surface",
      "detailSeparation": "height and normal contain unresolved detail only; modeled yarn relief must not be duplicated",
      "requiredMaps": {
        "baseColor": {
          "filename": "M32_basecolor.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": "authored base color; no baked lighting"
        },
        "normal": {
          "filename": "M32_normal.png",
          "channels": "RGB",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            128,
            128,
            255
          ]
        },
        "orm": {
          "filename": "M32_orm.png",
          "channels": "R=AO G=roughness multiplier B=metalness multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "height": {
          "filename": "M32_height.png",
          "channels": "R=normalized height; G=B=R",
          "bitDepth": 16,
          "colorSpace": "non-color",
          "neutralValue": 0
        },
        "sheenColor": {
          "filename": "M32_sheen-color.png",
          "channels": "RGB multiplier",
          "bitDepth": 8,
          "colorSpace": "sRGB",
          "neutralValue": [
            255,
            255,
            255
          ]
        },
        "sheenRoughness": {
          "filename": "M32_sheen-roughness.png",
          "channels": "A=roughness multiplier; RGB=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        },
        "anisotropy": {
          "filename": "M32_anisotropy.png",
          "channels": "R=direction X encoded 0..1 G=direction Y encoded 0..1 B=strength multiplier",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            128,
            255
          ]
        },
        "coverage": {
          "filename": "M32_coverage.png",
          "channels": "R=G=B=coverage; A=255",
          "bitDepth": 8,
          "colorSpace": "non-color",
          "neutralValue": [
            255,
            255,
            255,
            255
          ]
        }
      },
      "geometryLod": "modeled yarn crop in inspector; mapped sheet elsewhere",
      "requiredAttributes": [
        "POSITION",
        "NORMAL",
        "TEXCOORD_0",
        "TANGENT"
      ],
      "runtimeCompression": "KTX2 Basis UASTC, mipmaps; retain uncompressed masters",
      "compressionQualityPolicy": "reject visible normal block artifacts and lost coverage holes",
      "looseTextureFlipY": true,
      "gltfImportPolicy": "GLTFLoader owns flipY and texture transforms; never apply loose-texture overrides to imported glTF textures."
    },
    "intent": "Reveal plausible construction at close range while retaining readable foreground labels.",
    "rationale": "Separate silhouette, yarn topology, and fiber response so texture noise cannot stand in for construction.",
    "sourceIds": [
      "S00",
      "S01",
      "S03",
      "S04",
      "S05",
      "S06"
    ],
    "acceptance": [
      "Front and grazing views show coherent construction.",
      "No baked shadow in base color.",
      "No silhouette detail claimed from normal maps.",
      "At full size and 4x inspector view, no obvious repeated scratch pattern or plastic highlight.",
      "Material name remains illustrative until an actual specimen is documented."
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
    "S01",
    "S03",
    "S04",
    "S05",
    "S06"
  ],
  "standaloneCommand": "python scripts/generate_textile_workshop.py --prompt P-M32"
}
```
