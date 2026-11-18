---
name: Saring
description: A locally run phishing email checker with research proof margin clarity.
colors:
  ink: "#182725"
  pine: "#163f38"
  leaf: "#2f6759"
  paper: "#f1eee4"
  sheet: "#faf9f4"
  rule: "#d2cec2"
  muted: "#52615e"
  rust: "#a83f2d"
  safe: "#276348"
  measure: "#ba7146"
typography:
  display:
    fontFamily: 'Literata, Georgia, serif'
    fontSize: "clamp(40px, 5.4vw, 70px)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.035em"
  title:
    fontFamily: 'Literata, Georgia, serif'
    fontSize: "25px"
    fontWeight: 500
    lineHeight: 1.25
  wordmark:
    fontFamily: 'Literata, Georgia, serif'
    fontSize: "30px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.035em"
  body:
    fontFamily: 'IBM Plex Sans, Segoe UI, sans-serif'
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.55
  action:
    fontFamily: 'IBM Plex Sans, Segoe UI, sans-serif'
    fontSize: "14px"
    fontWeight: 600
  measurement:
    fontFamily: 'IBM Plex Mono, Consolas, monospace'
    fontSize: "10px"
    fontWeight: 400
    letterSpacing: "0.09em"
rounded:
  none: "0"
  sm: "2px"
  circle: "50%"
components:
  button-primary:
    backgroundColor: "{colors.pine}"
    textColor: "#fffdf5"
    rounded: "{rounded.sm}"
    padding: "12px 19px"
    height: "48px"
    typography: "{typography.action}"
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.pine}"
    rounded: "{rounded.none}"
    padding: "0"
    typography: "{typography.action}"
  input-text:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "10px 13px"
    height: "48px"
    typography: "{typography.body}"
  textarea:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "16px"
    typography: "{typography.body}"
  nav-masthead:
    backgroundColor: "{colors.pine}"
    textColor: "#f8f5ea"
    height: "82px"
    padding: "0 clamp(22px, 6vw, 88px)"
    typography: "{typography.body}"
  url-annotation:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    padding: "20px 0 22px 18px"
  probability-track:
    backgroundColor: "#dcd9cf"
    height: "5px"
  verdict:
    backgroundColor: "transparent"
    textColor: "{colors.rust}"
    padding: "25px 0 22px"
---

# Design System: Saring

## Overview

**Creative North Star: "Margin Proof"**

Margin Proof treats phishing review as a careful reading and measurement task. Warm paper and a deep pine masthead frame an expressive editorial display face; a workhorse sans carries controls and explanations, while mono is reserved for measurements. Thin rules and open surfaces keep the page legible without turning it into a dashboard of equal-weight cards.

The page gives the email editor seven columns and the report five. The report keeps the model's label and phishing probability distinct from the narrow, rust-marked URL measurement gutter. URL traits describe observable features; they are not presented as the model's reasons for its classification.

**Key Characteristics:**
- Warm paper surfaces under a deep pine shell.
- An asymmetrical editor and report, with the editor leading on narrow screens.
- Mono type for measured values and a single annotated URL gutter.
- Flat, open sections divided by thin rules.

## Colors

The palette pairs warm paper neutrals with pine structure and restrained rust and amber measurement accents.

### Primary
- **Deep Pine** (`pine`): The masthead and primary analysis action anchor the interface in this dark green.
- **Warm Rust** (`rust`): Focus outlines, errors, and the phishing verdict use this warning color.

### Secondary
- **Measurement Amber** (`measure`): The URL observation rail and probability fill use this separate measurement accent.
- **Leaf Green** (`leaf`): Small technical labels and scrollbar accents use this quieter green.
- **Safe Green** (`safe`): The non-phishing model verdict uses this semantic state color.

### Neutral
- **Ink** (`ink`): Main text and structural rules that need strong contrast.
- **Warm Paper** (`paper`): The page canvas.
- **Proof Sheet** (`sheet`): Email fields sit on this slightly lighter surface.
- **Rule Gray** (`rule`): Thin dividers between editorial sections.
- **Muted Green Gray** (`muted`): Supporting copy, status details, and secondary values.

**The Evidence Separation Rule.** Keep the URL measurement accent in its annotation gutter and the classification in its own verdict treatment; never make URL observations read as an explanation for the model.

## Typography

**Display Font:** Literata (with Georgia, serif fallback)

**Body Font:** IBM Plex Sans (with Segoe UI, sans-serif fallback)

**Label/Mono Font:** IBM Plex Mono (with Consolas, monospace fallback)

**Character:** Literata brings an editorial voice to the page title and report headings. IBM Plex Sans keeps the form and explanatory copy direct; IBM Plex Mono marks measurements and compact technical labels.

### Hierarchy
- **Display** (500, `clamp(40px, 5.4vw, 70px)`, 1.08): The introductory headline, with tight tracking and a 13-character measure.
- **Title** (500, 25px, 1.25): Editor and report section headings.
- **Wordmark** (600, 30px, 1): The masthead identity.
- **Body** (400, 16px, 1.55): Default reading and form text; introductory copy is capped at 65ch.
- **Action** (600, 14px): Primary action and text controls.
- **Measurement label** (400, 10px, 0.09em): Small uppercase mono labels; numerical readings use the same mono family at compact sizes.

## Layout

The centered page shell is capped at 1480px, with horizontal padding clamped from 22px to 88px. The introduction uses 12 equal columns: copy spans eight and the input/output note spans four. The workbench uses the same 12-column grid, with a seven-column editor and five-column report separated by a fluid gap (`clamp(34px, 5.5vw, 82px)`).

At 960px, the introduction shifts to a 9/3 split and the workbench gap becomes 36px. At 760px, the introduction and workbench use six columns and the editor and report each span the full width, in that order. At 480px, the page gutters become 18px and the primary action fills the available width. The system favors open reading space over dense repeated modules.

## Elevation & Depth

The stylesheet uses no box shadows. Depth comes from the paper canvas and lighter field surface, the pine masthead, and thin rules; the editor and report remain open rather than raised cards. Result arrival and probability fill animate with the same cubic-bezier easing, and reduced-motion preferences shorten transitions and animations to near zero.

**The Flat-Sheet Rule.** Keep surfaces flat at rest; use tonal contrast, rules, and placement to establish hierarchy.

## Shapes

Controls have nearly square corners (2px); text actions have no corner rounding, and the model-presence mark is circular. Thin one-pixel borders define fields and dividers. The report's URL gutter is a straight vertical annotation rule rather than a pill, badge, or enclosed card.

## Components

### Buttons
- **Shape:** Nearly square corners (2px) on the primary action; text actions remain unboxed (0 radius).
- **Primary:** Pine fill, warm white text, and 12px 19px padding with a 48px minimum height.
- **Hover / Focus:** The primary action darkens to the adjacent pine shade on hover. Keyboard focus uses a 3px rust outline offset by 3px.
- **Text action:** Transparent and underlined, with pine text that changes to rust on hover.
- **Disabled:** The primary action dims to 72% opacity and shows a wait cursor while analysis runs.

### Cards / Containers
- **Corner Style:** The editor and report are open sections, not cards.
- **Background:** The page uses paper; the fields use the lighter sheet surface.
- **Shadow Strategy:** None; use tonal layering and rules as described in Elevation & Depth.
- **Border:** Strong top rules identify the editor and report; finer rules divide report sections.
- **Internal Padding:** The main shell uses responsive side padding; sections use measured local spacing rather than a shared spacing scale.

### Inputs / Fields
- **Style:** Full-width sheet fields with a one-pixel warm-gray stroke and 2px corners. The subject field is 48px tall; the body field has a 286px minimum height and can be resized vertically.
- **Focus:** A 3px rust outline with a 3px offset.
- **Disabled:** The field surface shifts to a muted paper tone and the cursor indicates waiting.

### Navigation
- **Style:** A pine masthead places the Literata wordmark opposite model-file status and compact model metadata. At 760px, model metadata and its divider hide while status remains visible.

### URL Measurement Gutter
The distinctive report annotation uses a thin amber vertical rule beside a set of ruled measurements. Values use mono; the gutter remains separate from the model verdict and probability label.

## Do's and Don'ts

### Do:
- **Do** keep the 12-column asymmetry and let the email editor remain the dominant interaction.
- **Do** keep classification and probability distinct from descriptive URL measurements.
- **Do** use expressive editorial typography, a workhorse sans for controls, and mono only for measurements.
- **Do** keep surfaces open and use thin rules to organize the report.

### Don't:
- **Don't** use Inter, Roboto, Fraunces, or a system-default display face.
- **Don't** add purple, violet, or indigo gradients, glows, or repeated soft shadows.
- **Don't** turn the page into a generic three-card feature grid or add placeholder emojis or decorative badges.
- **Don't** add hover motion that does not clarify a state.
- **Don't** present URL traits as the model's explanation or claim real-world detection performance.
