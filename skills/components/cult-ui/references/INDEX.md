# cult/ui 组件索引 · Component index

上游 `cult/ui`（https://cult-ui.com），本仓收录 **154 个组件源码** + 153 个示例/区块条目，共 307 条 registry 记录。

读法：`deps` = 该组件需要的 npm 依赖；`regDeps` = 它依赖的其他 cult/ui 组件（要先装）；`源码` = 本地 tsx 路径（相对本 skill 目录）；
## 风格族 / Style families

同一控件有多套外观族，选型时先定族再定组件，别混用：

- **Animated 族（控件的动效版）**（17）：badg, butto, car, composer, ropzo, fiel, pu, otificatio, umber, progress, search, seg, selec, switch, bs, oas, oggle-group
- **Halo 族（发光描边风格）**（15）：badge, button, card, dropzone, field, input, notification, progress, searc, segmented, select, switc, tabs, toast, toggle-group
- **Border-beam 族（光束边框）**（3）：utton, c, input
- **Organic 族（有机形态）**（3）：butt, d, d-small
- **Texture 族（材质叠加）**（3）：button, card, overlay
- **Pixel 族（像素字）**（4）：heading-character, heading-word, aragraph-words, aragraph-words-invers
- **Illustration 族（SVG 插画）**（6）：card-grid, comment-bubble, c, fluid-rendering, globe-verce, graph
- **Hero 族（首屏视觉）**（5）：color-panel, dithering, atmap, liquid-metal, static-radial-gradient
- **Feature 族（功能陈列）**（4）：carousel, poll, sticky-section, voting
- **Gateway 插画族**（3）：ndpoint-illustration, route-illustration, svg-illustration
- **背景族**（5）：animate-button, animated-fractal-dot-grid, animated-gradient, image-texture, media

用法与 props 看 `docs/components/<name>.mdx`，示例代码看 `registry/default/example/<name>-demo.tsx`。

## 布局、导航与交互块 / Layout, nav & interactive blocks（19）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `choice-poll` | Poll component with single or multiple selection, optional results, and keyboard navigat | @radix-ui/react-use-controllable-state, lucide-react, class-variance-authority | — | `choice-poll.tsx` |
| `code-block` | A beautiful code block component with tabs, copy functionality, and smooth animations | motion, lucide-react | — | `code-block.tsx` |
| `dock` | macOS-style dock component with hover effects and smooth animations | motion | — | `dock.tsx` |
| `expandable` | Expandable component system with smooth animations and customizable presets | motion, react-use-measure | — | `expandable.tsx` |
| `expandable-screen` | A full-screen expandable component with morphing animations using shared layout IDs for  | motion, lucide-react | — | `expandable-screen.tsx` |
| `family-drawer` | A multi-view drawer component with smooth animations, view navigation, and customizable  | motion, react-use-measure, vaul, @radix-ui/react-slot | — | `family-drawer.tsx` |
| `file-icons` | Icon set for file types and languages | lucide-react | — | `file-icons.tsx` |
| `floating-panel` | Floating panel component with backdrop blur and position-aware animations | motion, lucide-react | — | `floating-panel.tsx` |
| `intro-disclosure` | Intro disclosure component with expandable content and smooth animations | motion, react-use-measure, lucide-react | button, aspect-ratio, checkbox, dialog, drawer, progress | `intro-disclosure.tsx` |
| `kanban-board` | Kanban board with drag-and-drop columns and cards | motion | — | `kanban-board.tsx` |
| `onboarding` | Composable multi-step onboarding primitives: Onboarding root with step navigation, Featu | @radix-ui/react-use-controllable-state, class-variance-authority | button | `onboarding.tsx` |
| `poll-widget` | Poll widget with inline, popover, and dialog modes, optional results, and animations | @radix-ui/react-use-controllable-state, class-variance-authority, lucide-react, motion | button, dialog, popover | `poll-widget.tsx` |
| `security-checkpoint` | Security checkpoint illustration or component | — | — | `security-checkpoint.tsx` |
| `side-panel` | Sliding side panel component with customizable positioning and animations | motion, react-use-measure | — | `side-panel.tsx` |
| `sortable-list` | Drag-and-drop sortable list component with smooth animations and reordering | motion, react-use-measure, lucide-react | checkbox | `sortable-list.tsx` |
| `terminal-animation` | Composable terminal animation primitives with typed command playback, tabbed scenarios,  | @radix-ui/react-slot, @radix-ui/react-use-controllable-state | — | `terminal-animation.tsx` |
| `timer` | Countdown timer component with customizable duration and visual styles | class-variance-authority, lucide-react | — | `timer.tsx` |
| `toolbar-expandable` | Expandable toolbar component with step-based navigation, smooth animations, and enhanced | motion, @radix-ui/react-scroll-area | badge | `toolbar-expandable.tsx` |
| `wizard-expandable` | Expandable multi-step wizard with optional forward validation, scrollable step rail, and | @base-ui/react, @radix-ui/react-use-controllable-state, motion | badge, button | `wizard-expandable.tsx` |

## Animated 族（控件的动效版）（17）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `animated-badge` | Deprecated alias for halo-badge. Prefer npx shadcn add https://cult-ui.com/r/halo-badge. | — | https://cult-ui.com/r/halo-badge.json | `—` |
| `animated-button` | Deprecated alias for halo-button. Prefer npx shadcn add https://cult-ui.com/r/halo-butto | — | https://cult-ui.com/r/halo-button.json | `—` |
| `animated-card` | Deprecated alias for halo-card. Prefer npx shadcn add https://cult-ui.com/r/halo-card.js | — | https://cult-ui.com/r/halo-card.json | `—` |
| `animated-composer` | Deprecated alias for prompt-composer. Prefer npx shadcn add https://cult-ui.com/r/prompt | — | https://cult-ui.com/r/prompt-composer.json | `—` |
| `animated-dropzone` | Deprecated alias for halo-dropzone. Prefer npx shadcn add https://cult-ui.com/r/halo-dro | — | https://cult-ui.com/r/halo-dropzone.json | `—` |
| `animated-field` | Deprecated alias for halo-field. Prefer npx shadcn add https://cult-ui.com/r/halo-field. | — | https://cult-ui.com/r/halo-field.json | `—` |
| `animated-input` | Deprecated alias for halo-input. Prefer npx shadcn add https://cult-ui.com/r/halo-input. | — | https://cult-ui.com/r/halo-input.json | `—` |
| `animated-notification` | Deprecated alias for halo-notification. Prefer npx shadcn add https://cult-ui.com/r/halo | — | https://cult-ui.com/r/halo-notification.json | `—` |
| `animated-number` | Deprecated alias for rolling-number. Prefer npx shadcn add https://cult-ui.com/r/rolling | — | https://cult-ui.com/r/rolling-number.json | `—` |
| `animated-progress` | Deprecated alias for halo-progress. Prefer npx shadcn add https://cult-ui.com/r/halo-pro | — | https://cult-ui.com/r/halo-progress.json | `—` |
| `animated-search` | Deprecated alias for halo-search. Prefer npx shadcn add https://cult-ui.com/r/halo-searc | — | https://cult-ui.com/r/halo-search.json | `—` |
| `animated-segmented` | Deprecated alias for halo-segmented. Prefer npx shadcn add https://cult-ui.com/r/halo-se | — | https://cult-ui.com/r/halo-segmented.json | `—` |
| `animated-select` | Deprecated alias for halo-select. Prefer npx shadcn add https://cult-ui.com/r/halo-selec | — | https://cult-ui.com/r/halo-select.json | `—` |
| `animated-switch` | Deprecated alias for halo-switch. Prefer npx shadcn add https://cult-ui.com/r/halo-switc | — | https://cult-ui.com/r/halo-switch.json | `—` |
| `animated-tabs` | Deprecated alias for halo-tabs. Prefer npx shadcn add https://cult-ui.com/r/halo-tabs.js | — | https://cult-ui.com/r/halo-tabs.json | `—` |
| `animated-toast` | Deprecated alias for halo-toast. Prefer npx shadcn add https://cult-ui.com/r/halo-toast. | — | https://cult-ui.com/r/halo-toast.json | `—` |
| `animated-toggle-group` | Deprecated alias for halo-toggle-group. Prefer npx shadcn add https://cult-ui.com/r/halo | — | https://cult-ui.com/r/halo-toggle-group.json | `—` |

## Halo 族（发光描边风格）（15）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `halo-badge` | Badge with optional layout animation, live status dot, and gradient rim aligned with Hal | class-variance-authority, motion | badge | `halo-badge.tsx` |
| `halo-button` | Primary action button with animated gradient rim, frosted fill, staggered label, and loa | @base-ui/react, motion | — | `halo-button.tsx` |
| `halo-card` | Composable card with animated gradient rim, frosted fill, layered shadow, and Base UI bu | @base-ui/react, motion | — | `halo-card.tsx` |
| `halo-dropzone` | File dropzone with animated rim, frosted fill, moving border trail, and file-type glyphs | lucide-react, motion | — | `halo-dropzone.tsx` |
| `halo-field` | Form field layout (label, description, error) for HaloInput and HaloTextarea | — | field | `halo-field.tsx` |
| `halo-input` | Single-line and multiline inputs with frosted fill and gradient rim for generic forms | @base-ui/react, motion | — | `halo-input.tsx` |
| `halo-notification` | Polished notification surface for local AnimatePresence use with rim variants and glyph  | @base-ui/react, lucide-react, motion | — | `halo-notification.tsx` |
| `halo-progress` | Progress bar with spring-driven determinate fill and indeterminate gradient strip | @base-ui/react, motion | — | `halo-progress.tsx` |
| `halo-search` | Search input with animated gradient border, staggered placeholder, blur deletion on clea | @paper-design/shaders-react, motion | — | `halo-search.tsx` |
| `halo-segmented` | Segmented control with frosted track, gradient rim, and spring sliding thumb | @base-ui/react, motion | — | `halo-segmented.tsx` |
| `halo-select` | Composable animated select with gradient rim, frosted fill, and staggered label | @base-ui/react, lucide-react, motion | https://cult-ui.com/r/base-select.json | `halo-select.tsx` |
| `halo-switch` | Toggle switch with spring thumb, frosted track, and extended touch hit area | @base-ui/react, motion | — | `halo-switch.tsx` |
| `halo-tabs` | Base UI tabs with gradient indicator: underline or pill variant aligned with Halo Card r | @base-ui/react | — | `halo-tabs.tsx` |
| `halo-toast` | Sonner-backed polished toasts with rim variants; mount PolishedToaster once in the root  | lucide-react, motion, sonner | button | `halo-toast.tsx` |
| `halo-toggle-group` | Segmented single-select control with frosted track, gradient rim, and spring-driven slid | @base-ui/react, motion | — | `halo-toggle-group.tsx` |

## 视觉特效与背景 / Effects & surfaces（14）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `circuit-board` | Animated SVG circuit illustration with glowing traces and a central chip, for hero or pr | lucide-react, motion | — | `circuit-board.tsx` |
| `distorted-glass` | A glass morphism effect component using SVG filters with fractal noise to create visual  | — | — | `distorted-glass.tsx` |
| `dither-image` | Compound Next.js image figure with CSS Bayer dither via dither-plugin, partial reveal ov | dither-plugin | — | `dither-image.tsx` |
| `edge-blur` | Stacked backdrop-blur layers with a gradient mask for soft top or bottom screen edges | — | — | `edge-blur.tsx` |
| `fluted-glass` | Paper Design fluted-glass image shader with sensible defaults — ribbed, streaked distort | @paper-design/shaders-react | — | `fluted-glass.tsx` |
| `globe` | COBE-powered 3D globe with showcase presets, markers, arcs, DOM overlays, and theme-awar | cobe, motion, next-themes | — | `globe.tsx` |
| `gradient-heading` | Heading component with gradient text effects and customizable styling | @radix-ui/react-slot, class-variance-authority | — | `gradient-heading.tsx` |
| `morph-surface` | A morphing surface component with smooth animations, customizable dimensions, and config | motion | — | `morph-surface.tsx` |
| `shader-lens-blur` | WebGL shader component with lens blur effects and mouse interaction | motion, three, jotai, next-themes | — | `shader-lens-blur.tsx` |
| `squiggle-arrow` | A playful, hand-drawn squiggly arrow component with customizable variants, directions, a | — | — | `squiggle-arrow.tsx` |
| `stripe-bg-guides` | Stripe-style background guides component with animated patterns and effects | motion | — | `stripe-bg-guides.tsx` |
| `svg-bands` | Wide SVG section bands, battlement and zigzag trims, steep hero edges, and ornamental fr | — | — | `svg-bands.tsx` |
| `svg-shapes` | Wide-aspect SVG shape and panel components for backgrounds and hero decorations | — | — | `svg-shapes.tsx` |
| `svg-shapes-animated` | Scroll-triggered stroke-draw animations for wide SVG shapes and panels using Motion | motion | — | `svg-shapes-animated.tsx` |

## 控件 / Controls（12）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `base-select` | Base UI select primitives used by Halo Select | @base-ui/react, @hugeicons/react, @hugeicons/core-free-icons | — | `base-select.tsx` |
| `base-tooltip` | Base UI tooltip primitives used by Apple Pro Display XDR | @base-ui/react, @radix-ui/react-slot | — | `base-tooltip.tsx` |
| `color-picker` | Interactive color picker component with HSL support and preset colors | motion, lucide-react | button, input, label, popover | `color-picker.tsx` |
| `copy-button` | Button that copies content to clipboard with feedback | lucide-react, motion | button | `copy-button.tsx` |
| `cosmic-button` | Animated button/link with cosmic gradient border effect, renders as anchor or button | — | — | `cosmic-button.tsx` |
| `direction-aware-tabs` | Tab component with direction-aware animations and smooth transitions | motion, react-use-measure | — | `direction-aware-tabs.tsx` |
| `family-button` | Button component with family-style design and interactive hover effects | lucide-react, motion | — | `family-button.tsx` |
| `gradient-button-group` | Premium layered button group with animated active state, gradient ring accents, and them | motion, next-themes | — | `gradient-button-group.tsx` |
| `metal-button` | Shadcn Button wrapped in MetalFx: animated liquid metal ring with text and icon variants | metal-fx, class-variance-authority | button | `metal-button.tsx` |
| `popover` | Animated popover component with form support and smooth transitions | motion, lucide-react | — | `popover.tsx` |
| `popover-form` | Form popover component with success states and animated transitions | motion, lucide-react | — | `popover-form.tsx` |
| `tabs-illustration-vercel` | Tabs with Vercel-style illustrations | — | — | `tabs-illustration-vercel.tsx` |

## 卡片与陈列 / Cards & showcases（12）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `agent-suggest-card-stack` | Stack of suggestion cards for AI agent responses | — | — | `agent-suggest-card-stack.tsx` |
| `canvas-fractal-grid` | Interactive canvas-based fractal dot grid with mouse tracking and wave effects | motion | — | `canvas-fractal-grid.tsx` |
| `cutout-card` | Image card with cutout corners, hover motion, inset labels, pins, and reveal actions | motion, @radix-ui/react-use-controllable-state | — | `cutout-card.tsx` |
| `folded-card` | Card with folded corner clip-path accent | — | — | `folded-card.tsx` |
| `grid-beam` | Canvas grid beam animation with palette presets, SVG dividers, and composable headless p | — | — | `grid-beam.tsx` |
| `loading-carousel` | Loading carousel component with smooth transitions and customizable content | embla-carousel-autoplay, lucide-react, motion | carousel | `loading-carousel.tsx` |
| `logo-carousel` | Animated logo carousel with staggered animations and customizable columns | motion | — | `logo-carousel.tsx` |
| `minimal-card` | Clean and minimal card component with subtle styling and hover effects | — | — | `minimal-card.tsx` |
| `shadow-card` | Composable marketing card with L-shaped extrusion, optional pixel gradient mesh, and Rad | @radix-ui/react-slot | — | `shadow-card.tsx` |
| `shift-card` | Card component with shift animation effects and hover interactions | motion | — | `shift-card.tsx` |
| `three-d-carousel` | 3D carousel component with perspective effects and smooth item transitions | motion | — | `three-d-carousel.tsx` |
| `tweet-grid` | Grid layout component for displaying tweet-like content cards | class-variance-authority | — | `tweet-grid.tsx` |

## 设备与窗口拟物 / Device & window mockups（9）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `apple-iphone-17-pro` | iPhone-style device frame with Dynamic Island, status bar, and configurable frame colors | lucide-react, motion | — | `apple-iphone-17-pro.tsx` |
| `apple-keyboard` | Compact Apple-style keyboard with labeled keys and media row | @tabler/icons-react | — | `apple-keyboard.tsx` |
| `apple-pro-display-xdr` | Studio Display–style aluminum frame, screen modes, and interactive macOS dock | @tabler/icons-react, motion | https://cult-ui.com/r/base-tooltip.json | `apple-pro-display-xdr.tsx` |
| `apple-watch-ultra` | Watch Ultra–style case, complications, crown, and action button | lucide-react, motion | — | `apple-watch-ultra.tsx` |
| `dynamic-island` | iOS-style dynamic island component with expandable content and smooth animations | motion | — | `dynamic-island.tsx` |
| `hover-video-player` | Video player component that plays on hover with smooth animations | motion, lucide-react | button, slider | `hover-video-player.tsx` |
| `mac-screen` | Classic Mac frame with an image or GIF composited into the CRT | — | — | `mac-screen.tsx` |
| `mock-browser-window` | A customizable browser window mockup component with support for Chrome, Safari, and gene | — | texture-overlay | `mock-browser-window.tsx` |
| `youtube-video-player` | YouTube video player component with custom controls and smooth animations | motion, lucide-react | button | `youtube-video-player.tsx` |

## AI 与对话界面 / AI & chat UI（6）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `ai-blob-warp` | Circular avatar with Paper Design Warp shader; motion-safe pulse, pauses off-screen and  | @paper-design/shaders-react, motion | — | `ai-blob-warp.tsx` |
| `ai-instructions` | Manage and toggle AI instructions with a popover, search, and create-dialog | @hugeicons/core-free-icons, @hugeicons/react | button, command, dialog, hover-card, input, popover, textarea | `ai-instructions.tsx` |
| `fluid-ai-workloads` | Fluid visualization for AI workload states | — | — | `fluid-ai-workloads.tsx` |
| `prompt-composer` | Multiline prompt field with shader avatar, staggered placeholder, loading line, and send | @base-ui/react, @paper-design/shaders-react, lucide-react, motion | — | `prompt-composer.tsx` |
| `prompt-library` | Browse, insert, and manage prompt templates with categories and custom prompts | @hugeicons/core-free-icons, @hugeicons/react | button, command, dialog, hover-card, input, popover, textarea | `prompt-library.tsx` |
| `speech-bubble` | Speech bubble component | — | — | `speech-bubble.tsx` |

## Illustration 族（SVG 插画）（6）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `illustration-card-grid` | Grid of cards with gateway illustrations | — | https://cult-ui.com/r/gateway-endpoint-illustration.json, https://cult-ui.com/r/gateway-route-illustration.json, https://cult-ui.com/r/gateway-svg-illustration.json | `illustration-card-grid.tsx` |
| `illustration-comment-bubble` | Comment bubble illustration for code or chat UI | — | — | `illustration-comment-bubble.tsx` |
| `illustration-cursor` | Cursor illustration and demo for collaboration UI | — | — | `illustration-cursor.tsx` |
| `illustration-fluid-rendering` | Fluid rendering illustration | — | — | `illustration-fluid-rendering.tsx` |
| `illustration-globe-vercel` | Globe deployment illustration | — | — | `illustration-globe-vercel.tsx` |
| `illustration-graph` | Graph illustration component | — | — | `illustration-graph.tsx` |

## 背景族（5）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `bg-animate-button` | Button component with animated background effects and gradient transitions | @radix-ui/react-slot, class-variance-authority | — | `bg-animate-button.tsx` |
| `bg-animated-fractal-dot-grid` | Background animated fractal dot grid with performance optimization and responsive design | motion | — | `bg-animated-fractal-dot-grid.tsx` |
| `bg-animated-gradient` | Animated gradient background component with customizable color transitions | motion | — | `bg-animated-gradient.tsx` |
| `bg-image-texture` | Background texture component with multiple texture variants and customizable opacity | — | — | `bg-image-texture.tsx` |
| `bg-media` | Background media component with video/image support and overlay effects | class-variance-authority | — | `bg-media.tsx` |

## 数据与指标 / Data & metrics（5）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `analytics-chart` | Vercel-style gradient line chart with floating tooltip cards | — | — | `analytics-chart.tsx` |
| `lightboard` | Interactive lightboard component with customizable grid and lighting effects | — | — | `lightboard.tsx` |
| `marketing-hero-analytics` | Analytics hero section for marketing pages | — | — | `marketing-hero-analytics.tsx` |
| `rolling-number` | Number component with smooth counting animations and customizable formatting | motion | — | `rolling-number.tsx` |
| `vote-tally` | List of items with up-vote support, optional sorting by vote count, and controlled or un | @radix-ui/react-use-controllable-state | — | `vote-tally.tsx` |

## Hero 族（首屏视觉）（5）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `hero-color-panel` | Split-layout hero section with responsive ColorPanels shader visuals, CTA, and tech stac | @paper-design/shaders-react | badge, button | `hero-color-panel.tsx` |
| `hero-dithering` | Split-layout hero section with responsive dithering shader visuals, CTA, and tech stack  | @paper-design/shaders-react | badge, button | `hero-dithering.tsx` |
| `hero-heatmap` | Split-layout hero section with responsive Heatmap shader visuals, CTA, and tech stack ba | @paper-design/shaders-react | badge, button | `hero-heatmap.tsx` |
| `hero-liquid-metal` | Split-layout hero section with responsive LiquidMetal shader visuals, CTA, and tech stac | @paper-design/shaders-react | badge, button | `hero-liquid-metal.tsx` |
| `hero-static-radial-gradient` | Split-layout hero section with responsive StaticRadialGradient shader visuals, CTA, and  | @paper-design/shaders-react | badge, button | `hero-static-radial-gradient.tsx` |

## Feature 族（功能陈列）（4）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `feature-carousel` | Feature carousel component with smooth transitions and customizable layouts | motion, clsx, react-wrap-balancer | — | `feature-carousel.tsx` |
| `feature-poll` | Feature poll component with single or multiple selection, optional results, and keyboard | @radix-ui/react-use-controllable-state, lucide-react, class-variance-authority | — | `feature-poll.tsx` |
| `feature-sticky-section` | Sticky section with controllable panels and scroll behavior | @radix-ui/react-slot, @radix-ui/react-use-controllable-state | — | `feature-sticky-section.tsx` |
| `feature-voting` | List of features with up-vote support, optional sorting by vote count, and controlled or | @radix-ui/react-use-controllable-state | — | `feature-voting.tsx` |

## Pixel 族（像素字）（4）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `pixel-heading-character` | Per-character pixel-font heading with four animation modes using Geist pixel fonts | geist | — | `pixel-heading-character.tsx` |
| `pixel-heading-word` | Whole-word pixel-font heading that swaps or cycles fonts on hover using Geist pixel font | geist | — | `pixel-heading-word.tsx` |
| `pixel-paragraph-words` | Paragraph where specific words render in an interactive pixel font that swaps or cycles  | geist | — | `pixel-paragraph-words.tsx` |
| `pixel-paragraph-words-inverse` | Paragraph in pixel font where specific words escape into interactive sans/mono with hove | geist | — | `pixel-paragraph-words-inverse.tsx` |

## 文字与标题 / Text & headings（3）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `text-animate` | Animated text component with customizable reveal effects and timing | motion | — | `text-animate.tsx` |
| `text-gif` | Text component with GIF-like animation effects and customizable styling | class-variance-authority | — | `text-gif.tsx` |
| `typewriter` | Typewriter effect component with customizable typing speed and cursor animation | motion | — | `typewriter.tsx` |

## Texture 族（材质叠加）（3）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `texture-button` | Button component with texture overlay effects and customizable variants | @radix-ui/react-slot, class-variance-authority | — | `texture-button.tsx` |
| `texture-card` | Card component with texture background and customizable styling options | — | — | `texture-card.tsx` |
| `texture-overlay` | Texture overlay component with various CSS gradient patterns for adding visual texture t | — | — | `texture-overlay.tsx` |

## Border-beam 族（光束边框）（3）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `border-beam-button` | Shadcn Button wrapped in Border Beam: animated border glow with compact icon and text va | border-beam | button | `border-beam-button.tsx` |
| `border-beam-card` | border-beam around compound Card API with balanced title and description | border-beam | card | `border-beam-card.tsx` |
| `border-beam-input` | border-beam on Base UI input and input-group primitives with line or full border glow | @base-ui/react, border-beam | input-group | `border-beam-input.tsx` |

## Gateway 插画族（3）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `gateway-endpoint-illustration` | Illustration for gateway endpoint concepts | — | — | `gateway-endpoint-illustration.tsx` |
| `gateway-route-illustration` | Illustration for gateway routing | — | — | `gateway-route-illustration.tsx` |
| `gateway-svg-illustration` | SVG illustration for gateway overhead | — | — | `gateway-svg-illustration.tsx` |

## Organic 族（有机形态）（3）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `organic-button` | Anchor-based CTA with fixed SVG end caps, shared surface colors via CSS variables, and s | @radix-ui/react-slot, class-variance-authority, lucide-react | — | `organic-button.tsx` |
| `organic-card` | Composable marketing card with optional link root, image slot, eyebrow/title/body, accen | lucide-react | — | `organic-card.tsx` |
| `organic-card-small` | Compact card with SVG silhouette, category and date, motion morph on hover, and optional | lucide-react, motion | — | `organic-card-small.tsx` |

## Neumorphic 族（新拟物）（2）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `neumorph-button` | Neumorphic button component with soft shadows and tactile interaction effects | class-variance-authority, lucide-react, motion | — | `neumorph-button.tsx` |
| `neumorph-eyebrow` | Neumorphic eyebrow component with soft shadow effects and modern styling | class-variance-authority | — | `neumorph-eyebrow.tsx` |

## 其他 / Misc（2）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `marketing-feature-code` | Marketing section for code or network policy features | lucide-react | — | `marketing-feature-code.tsx` |
| `merging-bubbles` | Merging bubbles visualization | — | — | `merging-bubbles.tsx` |

## 协作 UI 族（2）

| 组件 Component | 说明 What it does | deps | regDeps | 源码 Source |
|---|---|---|---|---|
| `collab-avatar` | Collaboration avatar with initials and color | motion | — | `collab-avatar.tsx` |
| `collab-toolbar` | Toolbar component for collaborative editing UI | — | — | `collab-toolbar.tsx` |
