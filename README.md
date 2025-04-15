# Maple Neon: A Theme for Cherry Studio

<div style="text-align: center">
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/docs/README.zh.md">中文</a> |
<a href="https://github.com/BoningtonChen/CherryStudio_themes/blob/master/docs/README.fr.zh">Française</a>
</div>

## Introduction
This is a theme tailored for Cherry Studio.

## How to USE
1. (Recommended) Download [Maple Font](https://github.com/subframe7536/maple-font/releases).
2. Copy the context in [maple-neon.css](./maple-neon.css) file.
3. Paste it into Cherry Studio.
4. Here you go!

## What's special about the theme?
- It provides modernized and aesthetic UI for Cherry Studio.
- It mixes the Maple font with a neon-styled input-bar, creating a unique and visually appealing experience.

## Demonstration
Based on Cherry Studio v1.2.4
![Page Light](./images/main-page-light.png)

![Page Dark](./images/main-page-dark.png)

## Theme Content
```css
/* Maple Neon Theme */

/* 基础变量定义 */
:root {
  --chat-background-white: #fff;
  --color-border: rgba(120, 120, 120, 0.08) !important;
  --monospace-font: "Maple Mono NF CN", monospace !important;
  --content-font: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
    sans-serif !important;
  --input-gradient-opacity: 1;
  --box-shadow-message: 0 4px 16px -8px rgba(0, 0, 0, 0.04);
  --border-radius-message: 16px;
}

/* 消息容器样式 */
.message-content-container {
  background: var(--chat-background-white) !important;
  box-shadow: var(--box-shadow-message) !important;
  border: 1px solid var(--color-border) !important;
  border-radius: var(--border-radius-message) !important;
  margin: 8px 0 !important;
  padding: 12px 14px 2px 14px !important;
  transition: transform 0.22s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
}

.message-user .message-content-container {
  background: #fbfcfc !important;
  box-shadow: 0 8px 28px -12px rgba(0, 0, 0, 0.05) !important;
}

/* 输入框动画效果 */
@keyframes gradientFlow {
  0% {
    background-position: 0 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0 50%;
  }
}

@keyframes subtleBlinking {
  0% {
    filter: drop-shadow(rgba(33, 150, 243, 0.3) 0px 0px 2px);
  }
  50% {
    filter: drop-shadow(rgba(255, 165, 0, 0.3) 0px 0px 5px);
  }
  100% {
    filter: drop-shadow(rgba(33, 150, 243, 0.3) 0px 0px 2px);
  }
}

/* 输入框样式 */
[theme-mode="dark"] #inputbar:focus-within::before {
  opacity: 0.5 !important;
}

[theme-mode="dark"] #inputbar:focus-within::before {
  opacity: 0.5 !important;
}

#inputbar {
  z-index: 1;
  position: relative;
  box-shadow: 0 8px 24px -12px rgba(0, 0, 0, 0.06) !important;
  margin: 0 15px 15px 15px !important;
}

#inputbar::before {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  padding: 2px;
  background: linear-gradient(
    90deg,
    #d65f00,
    #ffb800,
    #8a2be2,
    #ffb800,
    #d45e00
  );
  background-size: 200% 200%;
  mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask-composite: exclude;
  animation: gradientFlow 4s linear infinite;
  opacity: 0;
  transition: all 0.4s ease-in-out;
  pointer-events: none;
}

#inputbar:focus-within {
  animation: blinking 4s linear infinite;
}

#inputbar:focus-within::before {
  opacity: 1;
}

/* 一般内容的字体设置 - 非等宽 */
body,
p,
div,
span,
h1,
h2,
h3,
h4,
h5,
h6,
li,
ul,
ol,
.message-content-container {
  font-family: var(--content-font), system-ui;
  line-height: 1.2 !important;
  letter-spacing: 0.018em !important;
}

/* 代码块和内联代码的特殊字体处理 */
pre,
pre *,
code,
.markdown-body pre,
.markdown-body pre *,
.markdown-body code {
  font-family: var(--monospace-font), monospace;
  -webkit-font-feature-settings: "liga" 1, "calt" 1, "ss01" 1, "ss02" 1,
    "ss03" 1, "zero" 1 !important;
  font-feature-settings: "liga" 1, "calt" 1, "ss01" 1, "ss02" 1, "ss03" 1,
    "zero" 1 !important;
  text-rendering: optimizeLegibility;
}

/* 确保代码输入区也使用等宽字体 */
textarea.form-control,
#inputbox {
  font-family: var(--content-font), system-ui;
}

/* 代码块样式优化 */
.markdown-body pre {
  border-radius: 8px;
  margin: 16px 0;
}

.markdown-body pre code {
  font-size: 0.92em;
  padding: 0.8em;
  line-height: 1.5 !important;
}

/* 内联代码样式 */
:not(pre) > code {
  padding: 0.1em 0.4em;
  border-radius: 3px;
  font-size: 0.9em;
  background: rgba(0, 0, 0, 0.04);
  font-family: var(--monospace-font), monospace !important;
}

/* 暗色模式设置 */
body[theme-mode="light"] {
  --color-primary: #3f6ec8;
  --color-primary-soft: #5b87df;
  --color-primary-mute: #2a4b87;
  --input-gradient-opacity: 0.3;
}

body[theme-mode="dark"] {
  --color-primary: #5b87df;
  --color-primary-soft: #3f6ec8;
  --color-primary-mute: #2a4b87;
  --color-border: rgba(255, 255, 255, 0.1);
  --chat-background-white: #1e1e24;
  --chat-text-user: #edeef0;
  --color-text: #edeef0;
  --box-shadow-message: 0 4px 16px -8px rgba(0, 0, 0, 0.3);
  --input-gradient-opacity: 0.6;
}

body[theme-mode="dark"] .message-content-container {
  background: var(--chat-background-white) !important;
  box-shadow: var(--box-shadow-message) !important;
  border: 1px solid var(--color-border) !important;
}

body[theme-mode="dark"] .message-user .message-content-container {
  background: #252530 !important;
  box-shadow: 0 8px 32px -12px rgba(0, 0, 0, 0.25) !important;
}

body[theme-mode="dark"] #inputbar {
  background: rgba(30, 30, 36, 0.96) !important;
  border: 1px solid var(--color-border) !important;
  box-shadow: 0 8px 32px -12px rgba(0, 0, 0, 0.25) !important;
}

body[theme-mode="dark"] :not(pre) > code {
  background: rgba(255, 255, 255, 0.1);
}

/* 确保语法高亮清晰可辨 */
body[theme-mode="dark"] .markdown-body pre {
  background-color: #262633 !important;
}

/* Bug fixes */
.bubble .message-user .message-action-button:hover {
  background-color: var(--color-background-mute);
}

/* 输入区域内的字体处理 */
.form-control {
  font-family: var(--content-font), system-ui;
}

```

## Customization
You can fork the project and modify your own theme for Cherry Studio, for exact instructions, check [Cherry Studio Docs](https://docs.cherry-ai.com/personalization-settings/css).

## Inspiration
### Themes
- Dracula Theme: https://cherrycss.com
- Neon Theme: https://cherry-ai.com/css

### Fonts
- Maple Font: https://github.com/subframe7536/maple-font

## LICENSE
The Project follows [MIT LICENSE](./LICENSE).
