# Artifact Model

The exact schema can evolve, but the project should likely normalize toward records like:

- `Source`
- `Document`
- `Block`
- `Chunk`
- `Claim`
- `Citation`
- `Reference`
- `Edge`
- `RetrievalBundle`
- `Report`
- `SemanticLink`

## Conceptual Meanings

- `Source`
  Raw acquisition unit: file, URL, paper record, note, PDF.

- `Document`
  Logical normalized document derived from a source.

- `Block` or `Chunk`
  Searchable passage or section unit.

- `Claim`
  A proposition stated or extracted.

- `Citation`
  Link from a claim or output to a supporting source passage.

- `Reference`
  Explicit citation/reference relationship between documents.

- `Edge`
  Typed explicit relationship.

- `RetrievalBundle`
  Ranked evidence package for a question or subquestion.

- `Report`
  Structured research output.

- `SemanticLink`
  Suggested relatedness edge with score and review state.

## Record Qualities

All normalized records should favor:

- stable IDs
- reproducibility
- source provenance
- explicit warnings / uncertainty flags
- timestamps where useful
- schema versioning where useful

## Suggested Semantic Link Types

- `RELATED_PAPER`
- `SUPPORTS_ARTICLE`
- `MISSING_CITATION_CANDIDATE`
- `OVERLAPPING_ARTICLE`
- `SIMILAR_ARGUMENT`

These should start as suggestions, not accepted truth.

