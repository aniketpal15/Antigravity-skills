---
name: mattpocock-skills
description: "Matt Pocock's elite TypeScript and React development rules for AI assistants. Enforces strict type inference, zero 'any' escapes, advanced generic patterns, Zod schema validation, discrimination unions, and modern React 19 / Server Component best practices."
metadata:
  argument-hint: "[code to typecheck or refactor] or [typescript challenge]"
  triggers:
    - "mattpocock-skills"
    - "matt pocock"
    - "typescript wizard"
    - "advanced typescript"
    - "strict types"
    - "zod typing"
---

# Matt Pocock Skills — Elite TypeScript & React Engineering

`mattpocock-skills` codifies the TypeScript teaching and architectural rules of Matt Pocock (Total TypeScript). It eliminates sloppy AI type annotations (`any`, unnecessary `as` assertions, loose object types) in favor of bulletproof, inferable, compiler-verified code.

---

## ⚡ Non-Negotiable Rules

1. **Let TypeScript Infer**: Never annotate what the compiler already knows. Let return types and variable assignments flow naturally.
2. **Zero `any`**: Use `unknown` with type narrowing (type guards, Zod parsers, or `asserts`) instead of bypassing type checking.
3. **Discriminated Unions**: Model distinct states with explicit `kind` or `status` discriminant literals rather than optional boolean flags.
4. **Zod as Single Source of Truth**: Define runtime boundaries with Zod schemas and derive static types using `z.infer<typeof Schema>`.
5. **Generics with Constraints**: Always bound generic parameters (`<T extends Record<string, unknown>>`) rather than using bare `<T>`.

---

## 🛠️ Usage
- `"mattpocock: review and type this complex API response"`
- `"mattpocock: convert this loose interface into a discriminated union"`
- `"mattpocock: write a type-safe event bus with strict payload inference"`
