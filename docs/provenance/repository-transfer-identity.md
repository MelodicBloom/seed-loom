# Repository transfer identity

The repository currently named `MelodicBloom/seed-loom` has GitHub repository ID
`1295858033`. It was previously named `qt314wink/seed-loom` before the transfer.
The ID and historical name are recorded here rather than as unrecognized fields
in the version 1 verification profile. Existing schema identifiers, commit URLs,
and historical receipts retain their original names; this record does not
rewrite their provenance or establish a deployment authority.

- Follow-up: `.melodicbloom/verification-profile.json` now carries `repository_id: 1295858033` and `former_repository_names: ["qt314wink/seed-loom"]` (schema support added in MelodicBloom/.github#21).


- Identity precedence: when both the profile and runtime expose a repository ID, the stable ID is authoritative; a current or former name match cannot override a conflicting explicit ID. Name matching is a fallback only when a stable ID is unavailable on one side.
