# Design intent to code translation

These snippets are implementation recipes. The current PR ships the specification compiler and Core reference fixes; it does not ship these enhanced-renderer functions.

## F01 Millimeters to runtime meters

Signature: mmToM(mm: number): number

Formula: m = mm * 0.001

Selected example:

```json
{
  "inputMm": 0.32,
  "outputM": 0.00032
}
```

```js
const mmToM = mm => mm * 0.001;
```

Boundary: Exact unit conversion; not a physical measurement.

## F02 Yarn crossing clearance

Signature: crossingHeights(warpDiameterMm, weftDiameterMm, flatteningZ, gapMm, warpOver)

Formula: rW = warpDiameterMm * flatteningZ / 2; rF = weftDiameterMm * flatteningZ / 2; zW = sign * (rW + gapMm/2); zF = -sign * (rF + gapMm/2)

Selected example:

```json
{
  "warpDiameterMm": 0.42,
  "weftDiameterMm": 0.357,
  "flatteningZ": 0.65,
  "gapMm": 0.02,
  "warpOver": true,
  "warpCenterZMm": 0.1465,
  "weftCenterZMm": -0.126025
}
```

```js
const sign = warpOver ? 1 : -1; const zWarp = sign * (warpDiameterMm * flatteningZ / 2 + gapMm / 2); const zWeft = -sign * (weftDiameterMm * flatteningZ / 2 + gapMm / 2);
```

Boundary: Illustrative crossing samples only. Requires continuous curve/contact checks before use as yarn geometry.

## F03 Weave pattern selection

Signature: warpOver(i: integer, j: integer, pattern: string): boolean

Formula: plain: (i+j) mod 2 = 0; twill-3x1: (i-j) mod 4 < 3; satin-5: (i-2*j) mod 5 != 0

Selected example:

```json
{
  "pattern": "twill-3x1",
  "periodCells": 4,
  "warpDominanceRatio": 0.75
}
```

```js
const mod = (x,n) => ((x%n)+n)%n; const over = pattern === "plain" ? mod(i+j,2)===0 : pattern === "twill-3x1" ? mod(i-j,4)<3 : mod(i-2*j,5)!==0;
```

Boundary: Authored binary crossing pattern. Knit loops, lace, felt, and pile do not use this woven topology.

## F04 Twisted ply centerline

Signature: plyOffset(sMm, plyIndex, plyCount, radiusMm, turnsPerMm)

Formula: theta = 2*pi*(turnsPerMm*sMm + plyIndex/plyCount); offset = radiusMm * (cos(theta)*N + sin(theta)*B)

Selected example:

```json
{
  "plyCount": 3,
  "radiusMm": 0.07,
  "turnsPerMm": 1.5,
  "threadDiameterMm": 0.32
}
```

```js
const theta = 2*Math.PI*(turnsPerMm*sMm + plyIndex/plyCount); const offsetN = radiusMm*Math.cos(theta); const offsetB = radiusMm*Math.sin(theta);
```

Boundary: Sweep in a parallel-transport frame, not a fixed global frame. Check radius and strand overlap.

## F05 Damped spring response

Signature: stepSpring(positionM, velocityMps, targetM, massKg, stiffnessNPerM, dampingNsPerM, dtS)

Formula: m*xSecondDerivative + c*xFirstDerivative + k*(x-target) = 0; dampingRatio = c/(2*sqrt(k*m))

Selected example:

```json
{
  "massKg": 0.06,
  "stiffnessNPerM": 140,
  "dampingNsPerM": 5.8,
  "fixedDtSeconds": 0.008333333333333333,
  "maxAccumulatedSeconds": 0.05,
  "maxSubsteps": 6
}
```

```js
const acceleration = (-k*(x-target)-c*v)/m; v += acceleration*dt; x += v*dt;
```

Boundary: Semi-implicit Euler illustration with fixed substeps and bounds. These controller values are not measured denim mechanics.

## F06 XPBD distance constraint

Signature: solveDistance(x0, x1, inverseMass0, inverseMass1, restLengthM, complianceMPerN, lambda, dtS)

Formula: C=length(x1-x0)-L; alphaTilde=alpha/(dt*dt); deltaLambda=(-C-alphaTilde*lambda)/(w0+w1+alphaTilde); lambda+=deltaLambda; deltaXi=wi*gradientCi*deltaLambda

Selected example:

```json
{
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
}
```

```js
const a = compliance/(dt*dt); const dl = (-constraint-a*lambda)/(w0+w1+a); lambda += dl;
```

Boundary: Distance-based bend surrogate, not calibrated angular cloth bending. Reset multipliers each substep; retain across solver iterations. No self-collision claim.

## F07 Level of detail from projected yarn size

Signature: chooseLod(projectedYarnDiameterPx, inspectionRequested)

Formula: if !inspectionRequested or diameterPx<0.8 -> mapped surface; if 0.8<=diameterPx<2 -> modeled yarn; else modeled yarn plus bounded fiber detail

Selected example:

```json
{
  "mappedThresholdPx": 0.8,
  "fiberThresholdPx": 2,
  "transitionHysteresisRatio": 0.15,
  "fiberSegmentsMax": 24000,
  "activeInspectorCount": 1
}
```

```js
const lod = !inspect || yarnPx < .8 ? "mapped" : yarnPx < 2 ? "yarn" : "fiber";
```

Boundary: Design-selected perceptual thresholds; validate for shimmer and popping. No universal perceptual equivalence claim.

## F08 Linear color and contrast

Signature: srgbToLinear(c01); contrastRatio(rgbA, rgbB)

Formula: linear(c)=c/12.92 if c<=0.04045 else ((c+0.055)/1.055)^2.4; Y=.2126R+.7152G+.0722B; ratio=(max(Y1,Y2)+.05)/(min(Y1,Y2)+.05)

Selected example:

```json
{
  "foregroundHex": "#242821",
  "backgroundHex": "#FFFDF7",
  "normalTextMinimum": 4.5
}
```

```js
const linear = c => c <= .04045 ? c/12.92 : ((c+.055)/1.055)**2.4;
```

Boundary: Use actual rendered foreground/background samples for textured states; a palette calculation alone is insufficient.

## F09 Height-derived tangent normal

Signature: heightNormal(heightField, samplePitchMm, displacementScaleMm)

Formula: dHdu=(H(u+e,v)-H(u-e,v))*scale/(2*e); dHdv=(H(u,v+e)-H(u,v-e))*scale/(2*e); N=normalize(-dHdu,-dHdv,1)

Selected example:

```json
{
  "samplePitchMm": 0.04,
  "normalConvention": "OpenGL +Y",
  "displacementScaleMm": 0.076
}
```

```glsl
vec3 normalTS = normalize(vec3(-dHdu, -dHdv, 1.0));
```

Boundary: Shading detail only. Derivatives must use compatible physical units and correct image orientation.

