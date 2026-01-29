# Project Constitution

## Data Schemas

### Conversion Payload
**Input:**
```json
{
  "java_code": "String (Raw Selenium Java code)",
  "target_language": "String ('javascript' | 'typescript')",
  "output_directory": "String (Absolute path or relative to project root)"
}
```

**Output:**
```json
{
  "converted_code": "String (Transpiled Playwright code)",
  "file_path": "String (Location of the saved file)",
  "logs": "List<String> (Conversion steps/warnings)",
  "status": "String ('success' | 'partial' | 'error')"
}
```

## Behavioral Rules
1. **Comprehensive Coverage:** Attempt to convert all Selenium constructs (Locators, Waits, Actions, Assertions) to their Playwright equivalents.
2. **UI Interactivity:** The system must provide a UI for inputting code and viewing results.
3. **Persistence:** Converted code must be saved to the disk in a new directory.
4. **Determinism:** Use **Ollama (CodeLlama)** for intelligence, but validate output structure where possible.

## Architectural Invariants
1. **Frontend-Backend Separation:** UI (HTML/JS) communicates with `tools/` (Python) via Flask.
2. **AI-Driven Logic:** Conversion logic delegates to local Ollama API (Model: `codellama`).
3. **Atomic Conversion:** Each test/class is converted independently.
