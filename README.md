# AskBeacon Code Base

AskBeacon core logic is presented in this repository. This repository contains the following jupyter notebooks and their functionality is as follows.

## 1 - Extract Information

This notebook outlines how we extract information pertaining to a Beacon query from the user.

## 2 - Ontology Retrieval

This notebook demonmstrate the ontology indexing and retrieval process based on extracted information. This uses the following files.

#### `terms.csv`

This directly comes from sBeacon backend. sBeacon keeps a terms table and has the following format.

| term        | label            | scope   |
| ----------- | ---------------- | ------- |
| OBI:0000070 | genotyping assay | cohorts |
| OBI:0000070 | genotyping assay | cohorts |

#### `embeddings.csv`

This is the resulting file from the embedding of ontology terms. This is loaded into memory and indexed using `docarray` for ontology lookup.

| term        | label            | scope   | embedding                   |
| ----------- | ---------------- | ------- | --------------------------- |
| OBI:0000070 | genotyping assay | cohorts | [-0.06088845431804657, ...] |
| OBI:0000070 | genotyping assay | cohorts | [-0.06088845431804657, ...] |

## 3 - Extraction

This is the extraction portion of the AskBeacon analytics facility. The notebook outlines how we generate the extractor code using the Beacon V2 SDK.

## 4 - Execution

This notebooks shows how we generate the code that we'll be executing to perform the analysis. Note that this notebook relies on the following file.

#### `metadata.json`

This file has the summary information of the extracted data from the previous step.

```json
{
  "table_names": ["data"],
  "table_metadata": [
    [
      [
        "id",
        "diseases",
        ...
      ],
      [
        "int",
        "list",
        "dict",
        ...
      ]
    ]
  ]
}
```

## Utils

You can find the utils we have used under following directories.

#### `utils`

This has pydantic models, templates, vector db and code sanitisers used in our implementation

#### `analytics_utils`

This has the runners of extractors and execution codes. You might also find how we generate the metadata for `metadata.json` here as well.
