---
Data: "{{date:DD-MM-YYYY}}"
Ora: "{{time:HH:mm}}"
tags:
  - argomento
---
# {{title}}

## Indice:

```dataview
TABLE descrizione AS "Descrizione"
WHERE contains(argomenti, this.file.link)
SORT file.name asc
```